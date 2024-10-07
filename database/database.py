import mysql.connector
from datetime import datetime
from mysql.connector import Error
import json
from decimal import Decimal


class MySQLDatabaseHandler:
    def __init__(self, host, user, password, database):
        """Initialize the MySQL database connection."""
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        """Connect to the MySQL database."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print(f"Connected to {self.database}")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    def create_table(self, table_name, columns):
        """
        Create a table in the database.

        :param table_name: Name of the table
        :param columns: List of tuples representing column definitions (name, type)
        """
        try:
            column_defs = ", ".join([f"{col} {dtype}" for col, dtype in columns])
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_defs})"
            self.cursor.execute(query)
            self.connection.commit()
            print(f"Table '{table_name}' created or already exists.")
        except Error as e:
            print(f"Error creating table: {e}")

    # def insert_data(self, table_name, data):
    #     """
    #     Insert data into a specified table.

    #     :param table_name: Name of the table
    #     :param data: Dictionary representing column names and values
    #     """
    #     try:
    #         columns = ", ".join(data.keys())
    #         placeholders = ", ".join(["%s" for _ in data])
    #         values = tuple(data.values())
    #         query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    #         self.cursor.execute(query, values)
    #         self.connection.commit()
    #         print("Data inserted successfully.")
    #     except Error as e:
    #         print(f"Error inserting data: {e}")

    # def clean_and_convert_to_int(self,value):
    #     """
    #     Cleans a string by removing spaces and commas, then converts it to an integer.

    #     :param value: The string to clean and convert.
    #     :return: The integer value or None if the conversion fails.
    #     """
    #     try:
    #         print(f"Value: {value}")
    #         # Remove spaces and commas from the string
    #         clean_value = value.replace(' ', '').replace(',', '')
    #         return int(clean_value)
    #     except ValueError:
    #         print(f"Error: Unable to convert '{value}' to an integer.")
    #         return None

    def insert_data(self, dataset_table, statistics_table, data):
        """
        Insert data into the dataset table and then insert views and reactions into the statistics table.
        If the post_id already exists in the dataset table, only insert the views and reactions.

        :param dataset_table: Name of the dataset table (main table).
        :param statistics_table: Name of the statistics table (foreign key relationship).
        :param data: Dictionary representing the data to be inserted. Views and reactions are stored separately.
        """
        try:
            # Step 1: Check if the post_id already exists in the `dataset` table
            check_query = (
                f"SELECT id FROM {dataset_table} WHERE post_id = %s AND brand = %s AND currency = %s"
            )
            self.cursor.execute(check_query, (data["post_id"], data["brand"], data["currency"]))
            result = self.cursor.fetchone()

            # print(f"result: {result}")
            if result:
                # Step 2a: If `post_id` exists, get the `dataset_id` and insert only views and reactions
                dataset_id = result[0]
                print(
                    f"Post ID {data['post_id']} already exists with dataset ID {dataset_id}. Inserting only views and reactions."
                )

                # Step 2b: Get the current views and reactions from the `statistics` table
                stats_query = f"SELECT views, reactions FROM {statistics_table} WHERE dataset_id = %s ORDER BY id DESC LIMIT 1"
                self.cursor.execute(stats_query, (dataset_id,))
                current_stats = self.cursor.fetchone()

                if current_stats:
                    current_views, current_reactions = current_stats

                    # Convert current views and reactions to integers
                    current_views = int(current_views)
                    current_reactions = int(current_reactions)

                    # Ensure the incoming data values are integers
                    new_views = data["views"]
                    new_reactions = data["reactions"]

                    print(f"New Views: {new_views}, New Reactions: {new_reactions}")
                    # Calculate the difference between the new and current values
                    views_diff = max(
                        0, new_views - current_views
                    )  # Ensure no negative values
                    reactions_diff = max(
                        0, new_reactions - current_reactions
                    )  # Ensure no negative values

                    print(
                        f"Current views: {current_views}, New views: {new_views}, Difference: {views_diff}"
                    )
                    print(
                        f"Current reactions: {current_reactions}, New reactions: {new_reactions}, Difference: {reactions_diff}"
                    )
                else:
                    # If no previous stats exist, use the new values as the difference
                    views_diff = int(data["views"])
                    reactions_diff = int(data["reactions"])
                    print(
                        "No existing statistics found for this dataset. Inserting initial values."
                    )

            else:
                # Step 3: If `post_id` does not exist, insert into `dataset` table and get the new `id`
                dataset_data = {
                    k: v for k, v in data.items() if k not in ["views", "reactions"]
                }
                dataset_columns = ", ".join(dataset_data.keys())
                dataset_placeholders = ", ".join(["%s" for _ in dataset_data])
                dataset_values = tuple(dataset_data.values())

                dataset_query = f"INSERT INTO {dataset_table} ({dataset_columns}) VALUES ({dataset_placeholders})"
                self.cursor.execute(dataset_query, dataset_values)

                # Get the last inserted ID from the `dataset` table
                dataset_id = self.cursor.lastrowid
                print(f"New post inserted with dataset ID {dataset_id}.")

                # Use the original values for views and reactions if the post is new
                views_diff = int(data["views"])
                reactions_diff = int(data["reactions"])

            # Step 4: Insert the calculated difference into the `statistics` table
            statistics_data = {
                "dataset_id": dataset_id,
                "views": views_diff,
                "reactions": reactions_diff,
            }
            statistics_columns = ", ".join(statistics_data.keys())
            statistics_placeholders = ", ".join(["%s" for _ in statistics_data])
            statistics_values = tuple(statistics_data.values())

            statistics_query = f"INSERT INTO {statistics_table} ({statistics_columns}) VALUES ({statistics_placeholders})"
            self.cursor.execute(statistics_query, statistics_values)

            # Commit the transaction
            self.connection.commit()
            print("Data inserted successfully into both tables.")

        except Error as e:
            self.connection.rollback()  # Rollback in case of error
            print(f"Error inserting data: {e}")


        # Function to convert datetime and Decimal objects to JSON serializable formats
    
    # Function to convert datetime and Decimal objects to JSON serializable formats
    def convert_record(self, record):
        def process_value(value):
            if isinstance(value, datetime):
                return value.isoformat()  # Convert datetime to ISO format string
            elif isinstance(value, Decimal):
                return float(value)  # Convert Decimal to float
            else:
                return value  # Leave other values unchanged (e.g., strings like 'viewsday1')

        return {key: process_value(value) for key, value in record.items()}

    
    def fetch_and_categorize_posts_by_date(self, dataset_table, statistics_table, brand, currency):
        """
        Fetch all posts, sum views and reactions for each post_id, calculate the number of days since each post was made,
        and categorize them if they are exactly 3 days, 7 days, or 30 days old.

        :param cursor: MySQL cursor to execute the queries.
        :param dataset_table: Name of the dataset table.
        :param statistics_table: Name of the statistics table (for relationships).
        :return: A dictionary with categorized records.
        """
        # Get the current date and time
        current_date = datetime.now()

        # Query to fetch all posts and sum views and reactions by post_id
        # query = f"""
        # SELECT d.post_id, d.date, SUM(s.views) as total_views, SUM(s.reactions) as total_reactions
        # FROM {dataset_table} d
        # JOIN {statistics_table} s ON d.id = s.dataset_id
        # GROUP BY d.post_id, d.date
        # """
        query = f"""
        SELECT d.post_id, d.date, d.brand, d.currency, SUM(s.views) AS total_views, SUM(s.reactions) AS total_reactions, DATEDIFF(CURRENT_DATE(), d.date) AS days_since_posted, CASE WHEN DATEDIFF(CURRENT_DATE(), d.date) = 3 THEN 'viewsday3' WHEN DATEDIFF(CURRENT_DATE(), d.date) = 7 THEN 'viewsday7' WHEN DATEDIFF(CURRENT_DATE(), d.date) = 30 THEN 'viewsday30' ELSE CONCAT('viewsday', DATEDIFF(CURRENT_DATE(), d.date)) END AS days_string FROM {dataset_table} d JOIN {statistics_table} s ON d.id = s.dataset_id WHERE d.brand = '{brand}' AND d.currency = '{currency}' GROUP BY d.post_id, d.date, d.brand, d.currency;
        """
        self.cursor.execute(query)
        records = self.cursor.fetchall()

        # # Initialize dictionaries to store categorized records
        # categorized_posts = {
        #     "viewsday3": [],
        #     "viewsday7": [],
        #     "viewsday30": [],
        # }

        # for record in records:
        #     post_id, post_date, total_views, total_reactions = (
        #         record  # 'post_date' is already a datetime object
        #     )
        #     # Convert Decimal to float if necessary
        #     total_views = (
        #         float(total_views) if isinstance(total_views, Decimal) else total_views
        #     )
        #     total_reactions = (
        #         int(total_reactions)
        #         if isinstance(total_reactions, Decimal)
        #         else total_reactions
        #     )

        #     # Calculate the number of days since the post was made
        #     days_since_posted = (current_date - post_date).days
        #     # Debugging prints
        #     print(f"Post ID: {post_id}")
        #     print(f"Current Date: {current_date}")
        #     print(f"Post Date: {post_date}")
        #     print(f"Days Since Posted: {days_since_posted}")

        #     # Categorize the post based on the number of days since it was posted
        #     if days_since_posted == 3:
        #         categorized_posts["viewsday3"].append(
        #             {
        #                 "post_id": post_id,
        #                 "date": post_date.strftime(
        #                     "%Y-%m-%d %H:%M:%S"
        #                 ),  # Format the datetime as a string for display
        #                 "views": total_views,
        #                 "reactions": total_reactions,
        #                 "days_since_posted": days_since_posted,
        #             }
        #         )
        #     elif days_since_posted == 7:
        #         categorized_posts["viewsday7"].append(
        #             {
        #                 "post_id": post_id,
        #                 "date": post_date.strftime("%Y-%m-%d %H:%M:%S"),
        #                 "views": total_views,
        #                 "reactions": total_reactions,
        #                 "days_since_posted": days_since_posted,
        #             }
        #         )
        #     elif days_since_posted == 30:
        #         categorized_posts["viewsday30"].append(
        #             {
        #                 "post_id": post_id,
        #                 "date": post_date.strftime("%Y-%m-%d %H:%M:%S"),
        #                 "views": total_views,
        #                 "reactions": total_reactions,
        #                 "days_since_posted": days_since_posted,
        #             }
        #         )

        
        
       # Define the column names for your records
        column_names = ['post_id', 'date', 'brand', 'currency', 'total_views', 'total_reactions', 'days_since_posted', 'days_string']

        # Convert the list of tuples into a list of dictionaries using the column names
        processed_records = [dict(zip(column_names, record)) for record in records]

        # Now apply the convert_record function to make sure datetime and Decimal values are JSON serializable
        processed_records = [self.convert_record(record) for record in processed_records]

        # Store categorized data in a JSON file
        with open("categorized_posts.json", "w") as json_file:
            json.dump(processed_records, json_file, indent=4)

        # print(f"Data: {categorized_posts}")
        # print(
        #     f"Current date: {current_date}, Post date: {records}, Days since posted: {days_since_posted}"
        # )
        return records

    def close(self):
        """Close the database connection."""
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection closed.")
