import requests
from bs4 import BeautifulSoup
from cryptography.fernet import Fernet


# Generate a key for encryption and decryption
# You must store this key securely. Anyone with this key can encrypt and decrypt your data.
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a message
def encrypt_message(message, key):
    """
    Encrypts a message using the provided key.
    
    :param message: The message to encrypt (string)
    :param key: The encryption key (bytes)
    :return: Encrypted message (bytes)
    """
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())  # Message must be encoded to bytes
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    """
    Decrypts a message using the provided key.
    
    :param encrypted_message: The encrypted message (bytes)
    :param key: The decryption key (bytes)
    :return: Decrypted message (string)
    """
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()  # Return the decoded string

# Example usage
if __name__ == "__main__":
    # Generate a key (this should be stored securely)
    key = generate_key()
    print(f"Encryption Key: {key}")

    # Original message
    message = "This is a secret message."
    
    # Encrypt the message
    encrypted_message = encrypt_message(message, key)
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, key)
    print(f"Decrypted Message: {decrypted_message}")
# Sample HTML content (for actual scraping, fetch the HTML using requests or another method)
# html_content = '''<!DOCTYPE html>
# <html lang="en" class="__className_7b175a" data-gtag="G-RQLZYC299K">
#     <head>
#         <meta charSet="utf-8"/>
#         <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"/>
#         <link rel="preload" href="/_next/static/media/035951aefad7b653-s.p.woff2" as="font" crossorigin="" type="font/woff2"/>
#         <link rel="preload" href="/_next/static/media/0d3d6de4d4f168ef-s.p.ttf" as="font" crossorigin="" type="font/ttf"/>
#         <link rel="preload" href="/_next/static/media/26a46d62cd723877-s.p.woff2" as="font" crossorigin="" type="font/woff2"/>
#         <link rel="preload" href="/_next/static/media/35b6be5591831960-s.p.ttf" as="font" crossorigin="" type="font/ttf"/>
#         <link rel="preload" href="/_next/static/media/4e81fe9cba68eadc-s.p.woff" as="font" crossorigin="" type="font/woff"/>
#         <link rel="preload" href="/_next/static/media/5f4839c814e9ec59-s.p.woff" as="font" crossorigin="" type="font/woff"/>
#         <link rel="preload" href="/_next/static/media/8acb5781ce311ba9-s.p.woff" as="font" crossorigin="" type="font/woff"/>
#         <link rel="preload" href="/_next/static/media/90b1a89cbb9b3d98-s.p.woff" as="font" crossorigin="" type="font/woff"/>
#         <link rel="preload" href="/_next/static/media/a34f9d1faa5f3315-s.p.woff2" as="font" crossorigin="" type="font/woff2"/>
#         <link rel="preload" href="/_next/static/media/be8c7f0c93c8bd5b-s.p.ttf" as="font" crossorigin="" type="font/ttf"/>
#         <link rel="preload" href="/_next/static/media/cddbbedcf75420b6-s.p.ttf" as="font" crossorigin="" type="font/ttf"/>
#         <link rel="preload" href="/_next/static/media/e7603192e130cb26-s.p.ttf" as="font" crossorigin="" type="font/ttf"/>
#         <link rel="preload" href="/_next/static/media/f869f1e338b9e6dc-s.p.woff" as="font" crossorigin="" type="font/woff"/>
#         <link rel="stylesheet" href="/_next/static/css/095e7f3527a345a7.css" data-precedence="next"/>
#         <link rel="stylesheet" href="/_next/static/css/90a14ad6b753303e.css" data-precedence="next"/>
#         <link rel="stylesheet" href="/_next/static/css/b72b5821f33bf271.css" data-precedence="next"/>
#         <link rel="stylesheet" href="/_next/static/css/a55981e9afb98fbc.css" data-precedence="next"/>
#         <link rel="preload" as="script" fetchPriority="low" href="/_next/static/chunks/webpack-35bb7d39aba18b7f.js"/>
#         <script src="/_next/static/chunks/fd9d1056-43c738669f0ccb09.js" async=""></script>
#         <script src="/_next/static/chunks/73618-ae265f0bcb1153c5.js" async=""></script>
#         <script src="/_next/static/chunks/main-app-e6edabb79ca831ee.js" async=""></script>
#         <script src="/_next/static/chunks/73220-3a1140fcb6d7d1ce.js" async=""></script>
#         <script src="/_next/static/chunks/8279-7d504843f5f4005d.js" async=""></script>
#         <script src="/_next/static/chunks/81495-383649326538acfd.js" async=""></script>
#         <script src="/_next/static/chunks/app/%5Blng%5D/layout-1e1244772c66069d.js" async=""></script>
#         <script src="/_next/static/chunks/43514-82bb92cc6c59dbee.js" async=""></script>
#         <script src="/_next/static/chunks/68326-28dd3db74d853a73.js" async=""></script>
#         <script src="/_next/static/chunks/app/%5Blng%5D/not-found-4649d50a4cf3c918.js" async=""></script>
#         <script async="" src="https://www.googletagmanager.com/gtag/js?id=G-RQLZYC299K"></script>
#         <script async="" src="/script/gtag.js"></script>
#         <script src="/_next/static/chunks/90413-e8900a879754adbf.js" async=""></script>
#         <script src="/_next/static/chunks/64876-41c2b8a9a6312500.js" async=""></script>
#         <script src="/_next/static/chunks/2330-f253ce8ad6ba3601.js" async=""></script>
#         <script src="/_next/static/chunks/77397-21c9436c20a4a9e1.js" async=""></script>
#         <script src="/_next/static/chunks/10391-ac4597646d3d667d.js" async=""></script>
#         <script src="/_next/static/chunks/98735-a897bd2a07df5b3f.js" async=""></script>
#         <script src="/_next/static/chunks/1448-ba568bcf236ccabb.js" async=""></script>
#         <script src="/_next/static/chunks/89980-1e653f4986615471.js" async=""></script>
#         <script src="/_next/static/chunks/4198-c5a33f0545079614.js" async=""></script>
#         <script src="/_next/static/chunks/78110-c9000034beae1679.js" async=""></script>
#         <script src="/_next/static/chunks/39577-6e0063d635209dcc.js" async=""></script>
#         <script src="/_next/static/chunks/85600-d838c560b6e3316b.js" async=""></script>
#         <script src="/_next/static/chunks/76958-91aef98d2406e983.js" async=""></script>
#         <script src="/_next/static/chunks/9751-dccd70e85b745aba.js" async=""></script>
#         <script src="/_next/static/chunks/714-602d8c7bb145d9fa.js" async=""></script>
#         <script src="/_next/static/chunks/60819-a2bc2b80dbdddd30.js" async=""></script>
#         <script src="/_next/static/chunks/92892-dd486ee805e7194e.js" async=""></script>
#         <script src="/_next/static/chunks/83286-7ca7aed2c53ce442.js" async=""></script>
#         <script src="/_next/static/chunks/50360-570f674fa7869486.js" async=""></script>
#         <script src="/_next/static/chunks/36269-379d608ce928088f.js" async=""></script>
#         <script src="/_next/static/chunks/38259-bceccd9489884b29.js" async=""></script>
#         <script src="/_next/static/chunks/45345-40abd9c1679bdc0c.js" async=""></script>
#         <script src="/_next/static/chunks/app/%5Blng%5D/(service)/layout-aa2e99dfe8f97961.js" async=""></script>
#         <script src="/_next/static/chunks/17434-0352ecce102e46f3.js" async=""></script>
#         <script src="/_next/static/chunks/31603-36ff12160e256f37.js" async=""></script>
#         <script src="/_next/static/chunks/app/%5Blng%5D/(service)/channels/%5Bid%5D/layout-c116489e26a8a7a2.js" async=""></script>
#         <script src="/_next/static/chunks/5135-6872f3ae6757f537.js" async=""></script>
#         <script src="/_next/static/chunks/1784-893e55e19169d325.js" async=""></script>
#         <script src="/_next/static/chunks/app/%5Blng%5D/(service)/channels/%5Bid%5D/publish/page-54e389d46a937312.js" async=""></script>
#         <link rel="preconnect dns-prefetch" href="https://img.telemetr.io/" crossorigin=""/>
#         <meta name="google-adsense-account" content="ca-pub-7504188967825231"/>
#         <title>baji 🇧🇩 - @baji_bgd - Telemetrio - Publications</title>
#         <meta name="description" content="baji 🇧🇩 - @baji_bgd in Telegram on Telemetrio - Publications in the Telegram channel"/>
#         <meta name="author" content="telemetr.io"/>
#         <link rel="manifest" href="/manifest.webmanifest"/>
#         <link rel="canonical" href="https://telemetr.io/en/channels/1829680439-baji_bgd/publish"/>
#         <link rel="alternate" hrefLang="x-default" href="https://telemetr.io/en/channels/1829680439-baji_bgd/publish"/>
#         <link rel="alternate" hrefLang="en" href="https://telemetr.io/en/channels/1829680439-baji_bgd/publish"/>
#         <link rel="alternate" hrefLang="ar" href="https://telemetr.io/ar/channels/1829680439-baji_bgd/publish"/>
#         <link rel="alternate" hrefLang="es" href="https://telemetr.io/es/channels/1829680439-baji_bgd/publish"/>
#         <link rel="alternate" hrefLang="fa" href="https://telemetr.io/fa/channels/1829680439-baji_bgd/publish"/>
#         <link rel="alternate" hrefLang="ru" href="https://telemetr.io/ru/channels/1829680439-baji_bgd/publish"/>
#         <link rel="alternate" hrefLang="uk" href="https://telemetr.io/uk/channels/1829680439-baji_bgd/publish"/>
#         <link rel="alternate" hrefLang="uz" href="https://telemetr.io/uz/channels/1829680439-baji_bgd/publish"/>
#         <meta property="og:title" content="baji 🇧🇩 - @baji_bgd"/>
#         <meta property="og:description" content="baji 🇧🇩 - @baji_bgd in Telegram on Telemetrio"/>
#         <meta name="twitter:card" content="summary"/>
#         <meta name="twitter:title" content="baji 🇧🇩 - @baji_bgd"/>
#         <meta name="twitter:description" content="baji 🇧🇩 - @baji_bgd in Telegram on Telemetrio"/>
#         <link rel="icon" href="/favicon.ico" type="image/x-icon" sizes="32x32"/>
#         <link rel="icon" href="/icon.svg?9e8ae486b6590917" type="image/svg+xml" sizes="any"/>
#         <link rel="icon" href="/icon1.ico?6bbf3a51efb3e540" type="image/x-icon" sizes="16x16"/>
#         <link rel="icon" href="/icon2.ico?4e3fe26fdc910605" type="image/x-icon" sizes="24x24"/>
#         <link rel="icon" href="/icon3.ico?13288ad692c389e6" type="image/x-icon" sizes="48x48"/>
#         <link rel="icon" href="/icon4.ico?802efc8d36f2fee9" type="image/x-icon" sizes="64x64"/>
#         <link rel="icon" href="/icon5.ico?f2d52d5dccdccc0b" type="image/x-icon" sizes="96x96"/>
#         <link rel="icon" href="/icon6.ico?2f133ca7e18ea7a3" type="image/x-icon" sizes="144x144"/>
#         <link rel="apple-touch-icon" href="/apple-icon.png?a9b2beb703eb6cf6" type="image/png" sizes="180x180"/>
#         <meta name="next-size-adjust"/>
#         <script src="/_next/static/chunks/polyfills-c67a75d1b6f99dc8.js" noModule=""></script>
#     </head>
#     <body class="flex min-h-screen flex-col justify-between">
#         <!--$-->
#         <div class="fixed bottom-12 left-[50%] z-40 w-full max-w-[1240px] -translate-x-1/2 px-4 transition-all duration-300 md:px-9 lg:px-[100px] pointer-events-none translate-y-[100px] opacity-0">
#             <div class="flex flex-col gap-6 px-4 py-5 bg-white border rounded-3xl border-border-base-secondary shadow-shadow-sm md:p-7 lg:flex-row">
#                 <div class="flex items-center gap-x-3 md:gap-x-4">
#                     <img alt="cookie" loading="lazy" width="94" height="94" decoding="async" data-nimg="1" class="h-[30px] w-[30px] md:h-[38px] md:w-[38px]" style="color:transparent" src="/_next/static/media/cookie.4819a8e1.png"/>
#                     <p class="text-base font-medium leading-[22px] text-text-base-primary">We use cookies to improve your browsing experience. By clicking «Accept all», you agree to the use of cookies.</p>
#                 </div>
#                 <div class="flex items-center gap-x-3 pl-[42px] md:gap-x-4 md:pl-[54px] lg:pl-0">
#                     <button class="button button-border whitespace-nowrap button_primary button_small z-10 w-fit">Accept all</button>
#                     <button class="button button-border whitespace-nowrap button_secondary button_small z-10 w-fit">Decline</button>
#                 </div>
#             </div>
#         </div>
#         <!--/$-->
#         <header class="main-header border-b border-border-base-secondary">
#             <nav class="container relative flex items-center justify-between py-4" aria-label="Global">
#                 <div class="-my-0.5 flex">
#                     <a class="-m-1.5 p-1.5" href="/en">
#                         <span class="sr-only">Telemetrio</span>
#                         <span class="group flex items-center gap-3" id="logo">
#                             <div class="main-logo__icon relative flex items-center justify-center">
#                                 <div class="hidden group-hover:flex">
#                                     <div class="absolute bottom-[20%] left-[17%] items-center justify-center Loader_loading-container__833ya">
#                                         <div class="mb-0 h-4.5 w-[20.8px] Loader_loading__MZ9UM">
#                                             <div class="flex rounded bg-[#F5C324] Loader_line-sm__dMvr1"></div>
#                                             <div class="flex rounded bg-[#2DB6F5] Loader_line-sm__dMvr1"></div>
#                                             <div class="flex rounded bg-[#006DDA] Loader_line-sm__dMvr1"></div>
#                                         </div>
#                                     </div>
#                                 </div>
#                                 <svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
#                                     <rect x="0.5" y="0.5" width="29" height="29" rx="5.5" fill="white"></rect>
#                                     <rect x="0.5" y="0.5" width="29" height="29" rx="5.5" stroke="#E7EAED"></rect>
#                                     <path class="group-hover:hidden" id="blueLine" d="M21.7339 10.1133C22.9787 10.1133 24.0001 11.2254 24.0001 12.5758V21.5361C24.0001 22.9023 22.9947 23.9985 21.7339 23.9985C20.4891 23.9985 19.4678 22.8864 19.4678 21.5361V12.5917C19.4678 11.2254 20.4732 10.1133 21.7339 10.1133Z" fill="#006DDA"></path>
#                                     <path class="group-hover:hidden" id="lightBlueLine" d="M14.9995 6C16.2443 6 17.2657 7.04854 17.2657 8.31951V21.6805C17.2657 22.9673 16.2603 24 14.9995 24C13.7548 24 12.7334 22.9515 12.7334 21.6805V8.33539C12.7334 7.04854 13.7548 6 14.9995 6Z" fill="#2DB6F5"></path>
#                                     <path class="group-hover:hidden" id="yellowLine" d="M8.26517 14.7539C9.50996 14.7539 10.5313 15.866 10.5313 17.2164V21.5377C10.5313 22.9039 9.52591 24.0001 8.26517 24.0001C7.02039 24.0001 5.99902 22.8881 5.99902 21.5377V17.2164C6.01498 15.866 7.02039 14.7539 8.26517 14.7539Z" fill="#F5C324"></path>
#                                 </svg>
#                             </div>
#                             <svg class="main-logo__text" xmlns="http://www.w3.org/2000/svg" width="123" height="18" viewBox="0 0 123 18" fill="none">
#                                 <path d="M11.9257 0.523385V3.0956H7.31912V17.3597H4.62999V3.0956H0V0.523385H11.9257Z" fill="#1C1E21"></path>
#                                 <path d="M14.8065 12.2854C14.9936 13.174 15.4223 13.8599 16.0926 14.3432C16.7629 14.8109 17.5814 15.0447 18.5479 15.0447C19.8886 15.0447 20.8941 14.5614 21.5644 13.5949L23.6456 14.8109C22.492 16.5101 20.7849 17.3597 18.5245 17.3597C16.6226 17.3597 15.0871 16.7829 13.9179 15.6293C12.7487 14.4601 12.1641 12.9869 12.1641 11.2098C12.1641 9.46378 12.7409 8.00619 13.8945 6.837C15.0481 5.65222 16.5291 5.05983 18.3374 5.05983C20.0523 5.05983 21.4553 5.66002 22.5465 6.86039C23.6534 8.06075 24.2068 9.51834 24.2068 11.2332C24.2068 11.4982 24.1756 11.8489 24.1132 12.2854H14.8065ZM14.7831 10.2276H21.6579C21.4865 9.27671 21.0889 8.55961 20.4654 8.07634C19.8574 7.59308 19.1403 7.35144 18.3141 7.35144C17.3787 7.35144 16.5992 7.60867 15.9757 8.12311C15.3521 8.63755 14.9546 9.33907 14.7831 10.2276Z" fill="#1C1E21"></path>
#                                 <path d="M27.5981 17.3597V1.45727L30.1236 0.521922V17.3597H27.5981Z" fill="#1C1E21"></path>
#                                 <path d="M36.2127 12.2854C36.3998 13.174 36.8285 13.8599 37.4988 14.3432C38.1691 14.8109 38.9876 15.0447 39.9541 15.0447C41.2948 15.0447 42.3003 14.5614 42.9706 13.5949L45.0518 14.8109C43.8982 16.5101 42.1911 17.3597 39.9307 17.3597C38.0288 17.3597 36.4933 16.7829 35.3241 15.6293C34.1549 14.4601 33.5703 12.9869 33.5703 11.2098C33.5703 9.46378 34.1471 8.00619 35.3007 6.837C36.4543 5.65222 37.9353 5.05983 39.7436 5.05983C41.4585 5.05983 42.8615 5.66002 43.9527 6.86039C45.0596 8.06075 45.613 9.51834 45.613 11.2332C45.613 11.4982 45.5818 11.8489 45.5194 12.2854H36.2127ZM36.1893 10.2276H43.0641C42.8927 9.27671 42.4951 8.55961 41.8716 8.07634C41.2636 7.59308 40.5465 7.35144 39.7203 7.35144C38.7849 7.35144 38.0054 7.60867 37.3819 8.12311C36.7583 8.63755 36.3608 9.33907 36.1893 10.2276Z" fill="#1C1E21"></path>
#                                 <path d="M61.7719 4.89615C63.097 4.89615 64.1648 5.32485 64.9755 6.18226C65.7861 7.03966 66.1914 8.19326 66.1914 9.64305V17.3597H63.666V9.80674C63.666 8.99611 63.4633 8.37254 63.058 7.93604C62.6527 7.48395 62.0993 7.25791 61.3977 7.25791C60.6183 7.25791 59.9947 7.51513 59.527 8.02957C59.075 8.54402 58.8489 9.31568 58.8489 10.3446V17.3597H56.3235V9.80674C56.3235 8.99611 56.1286 8.37254 55.7389 7.93604C55.3647 7.48395 54.8269 7.25791 54.1254 7.25791C53.3615 7.25791 52.7379 7.52293 52.2547 8.05296C51.7714 8.5674 51.5298 9.33127 51.5298 10.3446V17.3597H49.0043V5.20014H51.5298V6.60316C52.2781 5.46515 53.3927 4.89615 54.8737 4.89615C56.3702 4.89615 57.4771 5.51192 58.1942 6.74347C58.9736 5.51192 60.1662 4.89615 61.7719 4.89615Z" fill="#1C1E21"></path>
#                                 <path d="M72.0511 12.2854C72.2381 13.174 72.6668 13.8599 73.3372 14.3432C74.0075 14.8109 74.8259 15.0447 75.7925 15.0447C77.1331 15.0447 78.1386 14.5614 78.809 13.5949L80.8901 14.8109C79.7365 16.5101 78.0295 17.3597 75.7691 17.3597C73.8672 17.3597 72.3317 16.7829 71.1625 15.6293C69.9933 14.4601 69.4087 12.9869 69.4087 11.2098C69.4087 9.46378 69.9855 8.00619 71.1391 6.837C72.2927 5.65222 73.7737 5.05983 75.582 5.05983C77.2968 5.05983 78.6998 5.66002 79.7911 6.86039C80.8979 8.06075 81.4513 9.51834 81.4513 11.2332C81.4513 11.4982 81.4202 11.8489 81.3578 12.2854H72.0511ZM72.0277 10.2276H78.9025C78.731 9.27671 78.3335 8.55961 77.7099 8.07634C77.102 7.59308 76.3848 7.35144 75.5586 7.35144C74.6233 7.35144 73.8438 7.60867 73.2202 8.12311C72.5967 8.63755 72.1992 9.33907 72.0277 10.2276Z" fill="#1C1E21"></path>
#                                 <path d="M91.0014 7.63205H88.1018V13.7118C88.1018 14.1951 88.211 14.5459 88.4292 14.7641C88.6474 14.9668 88.967 15.0837 89.3879 15.1149C89.8244 15.1304 90.3623 15.1227 91.0014 15.0915V17.3597C89.0684 17.5935 87.6809 17.4298 86.8391 16.8686C85.9973 16.2918 85.5764 15.2396 85.5764 13.7118V7.63205H83.4251V5.20014H85.5764V1.27167L88.1018 0.523385V5.20014H91.0014V7.63205Z" fill="#1C1E21"></path>
#                                 <path d="M97.1007 7.16437C97.7399 5.71458 98.9403 4.98968 100.702 4.98968V7.72559C99.7353 7.66323 98.8935 7.89707 98.1764 8.4271C97.4593 8.94154 97.1007 9.79895 97.1007 10.9993V17.3597H94.5753V5.20014H97.1007V7.16437Z" fill="#1C1E21"></path>
#                                 <path d="M106.005 3.25929C105.693 3.57107 105.319 3.72696 104.883 3.72696C104.446 3.72696 104.064 3.57107 103.737 3.25929C103.425 2.93191 103.269 2.54998 103.269 2.11348C103.269 1.67698 103.425 1.30284 103.737 0.99106C104.049 0.663687 104.431 0.5 104.883 0.5C105.335 0.5 105.717 0.663687 106.029 0.99106C106.34 1.30284 106.496 1.67698 106.496 2.11348C106.496 2.54998 106.333 2.93191 106.005 3.25929ZM103.737 17.3597V6.13549L106.262 5.20014V17.3597H103.737Z" fill="#1C1E21"></path>
#                                 <path d="M116.007 17.5C114.292 17.5 112.834 16.9076 111.634 15.7228C110.434 14.5381 109.834 13.0805 109.834 11.3501C109.834 9.61967 110.434 8.16208 111.634 6.97731C112.834 5.79253 114.292 5.20014 116.007 5.20014C117.737 5.20014 119.195 5.79253 120.38 6.97731C121.58 8.16208 122.18 9.61967 122.18 11.3501C122.18 13.0805 121.58 14.5381 120.38 15.7228C119.195 16.9076 117.737 17.5 116.007 17.5ZM113.411 13.9924C114.113 14.6939 114.978 15.0447 116.007 15.0447C117.036 15.0447 117.901 14.6939 118.602 13.9924C119.304 13.2909 119.655 12.4101 119.655 11.3501C119.655 10.29 119.304 9.40922 118.602 8.70771C117.901 8.00619 117.036 7.65543 116.007 7.65543C114.978 7.65543 114.113 8.00619 113.411 8.70771C112.71 9.40922 112.359 10.29 112.359 11.3501C112.359 12.4101 112.71 13.2909 113.411 13.9924Z" fill="#1C1E21"></path>
#                             </svg>
#                         </span>
#                     </a>
#                 </div>
#                 <div class="md:-my-[2px] md:mx-5">
#                     <div class="absolute md:z-10 md:relative bottom-0 left-1/2 md:left-0 -translate-x-1/2 md:translate-x-0">
#                         <div id="R99f3tta" class="select">
#                             <button class="flex min-w-0 items-center gap-[6px] rounded-md bg-bg-base-secondary px-[10px] py-[6px] text-sm font-semibold invisible md:visible" id="headlessui-listbox-button-:R1j99f3tta:" type="button" aria-haspopup="listbox" aria-expanded="false" data-headlessui-state="">
#                                 <i class="icon-flag-line inline-flex leading-[0] h-3 w-3 text-[12px] text-gray-600"></i>
#                                 <div>Global</div>
#                             </button>
#                         </div>
#                     </div>
#                 </div>
#                 <div class="hidden xl:flex xl:flex-1 xl:gap-x-3">
#                     <div class="xl:flex xl:gap-x-6">
#                         <div class="relative" data-headlessui-state="">
#                             <div class="menu-item mt-0.5">
#                                 <button data-ref-id="ratings" class="menu-button -mx-2.5 -my-6 flex items-center gap-x-1 border-b-4 px-2.5 py-4 text-sm font-semibold leading-6 text-text-link-base outline-0 transition-all duration-200 hover:text-text-link-base-hover border-transparent focus:border-[#CBD5E1]" type="button" aria-expanded="false" data-headlessui-state="">
#                                     Ratings<i class="icon-chevron-down-line inline-flex leading-[0] flex-none text-xl leading-[0] text-inherit transition-transform duration-200 "></i>
#                                 </button>
#                             </div>
#                         </div>
#                         <div class="relative" data-headlessui-state="">
#                             <div class="menu-item mt-0.5">
#                                 <button data-ref-id="tools" class="menu-button -mx-2.5 -my-6 flex items-center gap-x-1 border-b-4 px-2.5 py-4 text-sm font-semibold leading-6 text-text-link-base outline-0 transition-all duration-200 hover:text-text-link-base-hover border-transparent focus:border-[#CBD5E1]" type="button" aria-expanded="false" data-headlessui-state="">
#                                     Tools<i class="icon-chevron-down-line inline-flex leading-[0] flex-none text-xl leading-[0] text-inherit transition-transform duration-200 "></i>
#                                 </button>
#                             </div>
#                         </div>
#                     </div>
#                     <div hidden="" style="position:fixed;top:1px;left:1px;width:1px;height:0;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);white-space:nowrap;border-width:0;display:none"></div>
#                     <a class="-my-6 flex items-center gap-x-1 border-b-4 px-2.5 py-4 text-sm font-semibold leading-6 text-text-link-base outline-0 transition-all duration-200 border-transparent hover:border-text-link-accent-hover hover:text-text-link-base-hover focus:border-[#CBD5E1] whitespace-nowrap" target="" href="/en/tg-ads/about">Telegram Ads</a>
#                     <a class="-my-6 flex items-center gap-x-1 border-b-4 px-2.5 py-4 text-sm font-semibold leading-6 text-text-link-base outline-0 transition-all duration-200 border-transparent hover:border-text-link-accent-hover hover:text-text-link-base-hover focus:border-[#CBD5E1] whitespace-nowrap mr-2" target="" href="/en/pricing">Prices</a>
#                 </div>
#                 <div class="-my-2 ml-auto w-full min-w-0 md:w-[234px]">
#                     <div id="R9h9f3tta" class="autocomplete">
#                         <div class="autocomplete__wrapper" id="headlessui-combobox-button-:Rd9h9f3tta:" tabindex="-1" aria-haspopup="listbox" aria-expanded="false" data-headlessui-state="">
#                             <i class="icon-search-line inline-flex leading-[0] autocomplete__icon mr-[6px]"></i>
#                             <input class="autocomplete__input" placeholder="Search (click &quot;/&quot;)" autoComplete="off" id="headlessui-combobox-input-:R5d9h9f3tta:" role="combobox" type="text" aria-expanded="false" aria-autocomplete="list" data-headlessui-state="" value=""/>
#                         </div>
#                     </div>
#                 </div>
#                 <div class="ml-6 hidden xl:flex xl:flex-none xl:justify-end xl:gap-x-6">
#                     <div class="relative" data-headlessui-state="">
#                         <div class="menu-item mt-1.5">
#                             <button data-ref-id="notification_menu" class="menu-button -mx-2.5 -my-6 flex items-center gap-x-1 border-b-4 px-2.5 py-4 text-base font-semibold leading-6 text-[#475569] outline-0 border-transparent focus:border-[#CBD5E1]" type="button" aria-expanded="false" data-headlessui-state="">
#                                 <i class="icon-bell-line inline-flex leading-[0] text-xl"></i>
#                             </button>
#                         </div>
#                     </div>
#                     <div class="relative" data-headlessui-state="">
#                         <div class="menu-item mt-1.5">
#                             <button data-ref-id="profile_menu" class="menu-button -mx-2.5 -my-6 flex h-14 items-center gap-x-1 border-b-4 px-2.5 py-4 text-base font-semibold leading-6 text-[#475569] outline-0 border-transparent focus:border-[#CBD5E1]" type="button" aria-expanded="false" data-headlessui-state="">
#                                 <img alt="avatar" loading="lazy" width="160" height="160" decoding="async" data-nimg="1" class="avatar -my-2.5  avatar__S" style="color:transparent" src="/_next/static/media/empty-profile.a21aa90d.svg"/>
#                                 <i class="icon-chevron-down-line inline-flex leading-[0] -mt-0.5 flex-none text-xl leading-[0] text-inherit transition-transform duration-200 "></i>
#                             </button>
#                         </div>
#                     </div>
#                 </div>
#                 <div hidden="" style="position:fixed;top:1px;left:1px;width:1px;height:0;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);white-space:nowrap;border-width:0;display:none"></div>
#                 <div class="ml-6 flex gap-6 xl:hidden">
#                     <button class="relative -m-2.5 inline-flex items-center gap-x-1 p-2.5 text-base font-semibold text-[#475569] outline-0">
#                         <i class="icon-bell-line inline-flex leading-[0] text-xl"></i>
#                     </button>
#                     <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-[#475569]">
#                         <span class="sr-only">Open main menu</span>
#                         <span class="inline-block h-5 w-5">
#                             <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
#                                 <path fill-rule="evenodd" clip-rule="evenodd" d="M1.28144 2H22.7186C23.4265 2 24 2.58162 24 3.29957C24 4.01751 23.4265 4.59913 22.7186 4.59913H1.28144C0.57352 4.59913 0 4.01751 0 3.29957C0 2.58162 0.57352 2 1.28144 2ZM22.7186 10.3004H1.28144C0.57352 10.3004 0 10.8821 0 11.6C0 12.3179 0.57352 12.8996 1.28144 12.8996H22.7186C23.4265 12.8996 24 12.3179 24 11.6C24 10.8821 23.4265 10.3004 22.7186 10.3004ZM22.7186 18.6009H1.28144C0.57352 18.6009 0 19.1825 0 19.9004C0 20.6184 0.57352 21.2 1.28144 21.2H22.7186C23.4265 21.2 24 20.6184 24 19.9004C24 19.1825 23.4265 18.6009 22.7186 18.6009Z"></path>
#                             </svg>
#                         </span>
#                     </button>
#                 </div>
#                 <div class="ml-6 hidden xl:flex xl:flex-none xl:justify-end xl:gap-x-6">
#                     <div class="relative" data-headlessui-state="">
#                         <div class="menu-item mt-1.5">
#                             <button data-ref-id="language_menu" class="menu-button -mx-2.5 -my-6 flex items-center gap-x-1 border-b-4 px-2.5 py-4 text-base font-semibold leading-6 text-[#475569] outline-0 border-transparent focus:border-[#CBD5E1]" type="button" aria-expanded="false" data-headlessui-state="">
#                                 <i class="icon-globe-line inline-flex leading-[0] text-xl"></i>
#                                 <span class="text-xs uppercase leading-5">en</span>
#                             </button>
#                         </div>
#                     </div>
#                 </div>
#                 <div hidden="" style="position:fixed;top:1px;left:1px;width:1px;height:0;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);white-space:nowrap;border-width:0;display:none"></div>
#             </nav>
#         </header>
#         <main class="flex flex-col items-start flex-1 py-4 sm:py-11">
#             <div class="banner left-0 right-0 top-0 z-20 w-full py-2.5 px-3 banner__accent mb-4 -mt-4 cursor-pointer sm:-mt-11 sm:mb-11">
#                 <div class="flex h-full items-center justify-center">
#                     <div class="banner__text flex items-center justify-center sm:mr-2">
#                         <h4 class="text-center text-sm font-medium leading-5 md:text-start">
#                             Don &#x27;t get caught by a cheater! Telemetrio finds and tags such channels 👉 <span class="underline underline-offset-4">If you want to see the tag, subscribe</span>
#                             👈
#                         </h4>
#                     </div>
#                     <div class="ml-auto flex h-6 w-6 items-center justify-center"></div>
#                 </div>
#             </div>
#             <div class="container flex flex-col justify-between w-full gap-6 lg:flex-row">
#                 <div class="flex flex-1 space-x-4 sm:space-x-6">
#                     <div class="relative flex items-start self-start">
#                         <img alt="avatar" loading="lazy" width="160" height="160" decoding="async" data-nimg="1" class="avatar h-11 w-11 sm:h-40 sm:w-40 avatar__circle avatar__L" style="color:transparent" src="https://img.telemetr.io/c/1ZP9sP/6187992883995458813?ty=l"/>
#                     </div>
#                     <div class="flex flex-col flex-1">
#                         <div class="inline-flex items-center gap-2 text-lg font-semibold sm:text-2xl">
#                             <div class="grid">
#                                 <h1 class="overflow-hidden text-ellipsis whitespace-nowrap">baji 🇧🇩</h1>
#                             </div>
#                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                 <span class="inline-block inline-flex w-5 h-5 sm:h-6 sm:w-6">
#                                     <img alt="black-icon" loading="lazy" width="14" height="14" decoding="async" data-nimg="1" style="color:transparent;width:100%;height:100%" src="/_next/static/media/black-label-blue.95fcfd40.svg"/>
#                                 </span>
#                             </button>
#                         </div>
#                         <div class="inline-flex items-center gap-2">
#                             <span data-state="closed">
#                                 <a href="https://t.me/baji_bgd" target="_blank" rel="nofollow noopener noreferrer" class="inline-flex items-center gap-1 text-sm font-semibold leading-4 rounded text-subtle sm:leading-6">@baji_bgd</a>
#                             </span>
#                         </div>
#                         <div class="-ml-[60px] mt-2 text-sm sm:ml-0">
#                             <p class="whitespace-pre-line text-text-secondary line-clamp-2"></p>
#                             <span class="flex items-center font-semibold cursor-pointer select-none w-fit text-text-dynamic">
#                                 Show more<i class="icon-chevron-down-line inline-flex leading-[0] flex-none text-lg transition-all duration-200 "></i>
#                             </span>
#                             <div class="flex flex-wrap items-end gap-3 mt-2">
#                                 <a data-state="closed" href="/en/catalog/bangladesh">
#                                     <span class="tag">
#                                         Bangladesh<span class="text-gray-600">144</span>
#                                     </span>
#                                 </a>
#                                 <span class="tag" data-state="closed">
#                                     Bengali<span class="text-gray-600">113</span>
#                                 </span>
#                                 <a data-state="closed" href="/en/catalog/bangladesh/bets-and-casino">
#                                     <span class="tag">
#                                         Betting and Casino<span class="text-gray-600">8 115</span>
#                                     </span>
#                                 </a>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#                 <div class="flex flex-col-reverse justify-between gap-x-6 gap-y-2 md:flex-row-reverse lg:flex-col">
#                     <div class="flex flex-1 flex-col-reverse items-end justify-between gap-x-2.5 sm:flex-row-reverse lg:flex-none lg:flex-col lg:items-end lg:gap-y-4">
#                         <div class="flex flex-col w-full mt-4 gap-x-3 gap-y-2 sm:w-auto md:flex-row lg:mt-0">
#                             <a class="button button-border whitespace-nowrap button_primary button_medium w-full md:w-auto" rel="nofollow" href="/en/ads-posts?destination=1ZP9sP-baji%20%F0%9F%87%A7%F0%9F%87%A9">
#                                 <i class="icon-announcement-03-line inline-flex leading-[0] button__icon"></i>
#                                 Advertising posts
#                             </a>
#                             <div class="flex w-full gap-x-3 sm:w-auto">
#                                 <button class="button button-border whitespace-nowrap button_secondary button_medium w-full md:w-auto">
#                                     <i class="icon-presentation-chart-line inline-flex leading-[0] button__icon"></i>
#                                     Statistics in a picture
#                                 </button>
#                                 <div class="md:relative" data-headlessui-state="">
#                                     <div aria-expanded="false" data-headlessui-state="">
#                                         <button class="button button-border whitespace-nowrap button_secondary button_medium button__icon-only">
#                                             <i class="icon-bookmark-line inline-flex leading-[0] button__icon button__icon-only"></i>
#                                         </button>
#                                     </div>
#                                 </div>
#                                 <div hidden="" style="position:fixed;top:1px;left:1px;width:1px;height:0;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);white-space:nowrap;border-width:0;display:none"></div>
#                                 <span class="relative" data-state="closed">
#                                     <button class="button button-border whitespace-nowrap button_secondary button_medium button__icon-only outline-none">
#                                         <i class="icon-link-line inline-flex leading-[0] button__icon button__icon-only"></i>
#                                     </button>
#                                 </span>
#                             </div>
#                         </div>
#                         <div class="flex flex-col items-start justify-end w-full gap-1 lg:flex-row lg:items-end"></div>
#                     </div>
#                 </div>
#             </div>
#             <div class="container flex flex-col justify-between w-full mt-6">
#                 <div class="grid flex-1 grid-cols-1 gap-y-4 sm:gap-5 md:grid-cols-2 xl:grid-cols-[3fr_2fr_2fr_2fr] xl:gap-y-0">
#                     <div class="w-full item">
#                         <div class="rounded-lg bg-gray-gradient shadow-border-custom-sm">
#                             <div class="flex justify-between border-b border-[#E7EAED] p-3 md:p-5">
#                                 <div class="flex items-center gap-3">
#                                     <span class="flex aspect-square rounded-full p-2.5 shadow-icon">
#                                         <i class="icon-two-users-line inline-flex leading-[0] text-xl text-text-dynamic"></i>
#                                     </span>
#                                     <div class="flex flex-col items-start">
#                                         <span class="flex items-center gap-3 text-2xl font-semibold text-text-primary">45 421</span>
#                                         <span class="inline-flex max-w-full items-center gap-1 truncate text-sm font-medium text-text-base-secondary gap-x-1 whitespace-nowrap flex-none">
#                                             <div class="grid flex-initial">
#                                                 <span class="truncate">Subscribers</span>
#                                             </div>
#                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                 <i class="icon-info-circle-line inline-flex leading-[0] text-neutral3 text-xl"></i>
#                                             </button>
#                                         </span>
#                                     </div>
#                                 </div>
#                             </div>
#                             <div class="flex justify-between text-center">
#                                 <div class="flex flex-1 flex-col items-center overflow-hidden border-r border-[#E7EAED] py-4 md:py-5">
#                                     <span class="mx-auto rounded bg-bg-danger px-2 py-1 text-base font-semibold leading-4 bg-bg-success text-text-success">+
#                                     <!-- -->
#                                     10</span>
#                                     <span class="text-sm font-medium lowercase text-text-secondary">24
#                                     <!-- -->
#                                     <!-- -->
#                                     hours</span>
#                                 </div>
#                                 <div class="flex flex-1 flex-col items-center overflow-hidden border-r border-[#E7EAED] py-4 md:py-5">
#                                     <span class="mx-auto rounded bg-bg-danger px-2 py-1 text-base font-semibold leading-4 bg-bg-success text-text-success">+
#                                     <!-- -->
#                                     249</span>
#                                     <span class="text-sm font-medium lowercase text-text-secondary">7
#                                     <!-- -->
#                                     <!-- -->
#                                     days</span>
#                                 </div>
#                                 <div class="flex flex-col items-center flex-1 py-4 overflow-hidden md:py-5">
#                                     <span class="mx-auto rounded bg-bg-danger px-2 py-1 text-base font-semibold leading-4 bg-bg-success text-text-success">+
#                                     <!-- -->
#                                     859</span>
#                                     <span class="text-sm font-medium lowercase text-text-secondary">30
#                                     <!-- -->
#                                     <!-- -->
#                                     days</span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="item w-full hidden md:block">
#                         <div class="rounded-lg bg-gray-gradient shadow-border-custom-sm">
#                             <div class="flex justify-between border-b border-[#E7EAED] p-3 md:p-5">
#                                 <div class="flex items-center gap-3">
#                                     <span class="flex aspect-square rounded-full p-2.5 shadow-icon">
#                                         <i class="icon-eye-line inline-flex leading-[0] text-xl text-text-dynamic"></i>
#                                     </span>
#                                     <div class="flex flex-col items-start">
#                                         <span class="flex items-center gap-3 text-2xl font-semibold text-text-primary">4 219</span>
#                                         <span class="inline-flex max-w-full items-center gap-1 truncate text-sm font-medium text-text-base-secondary gap-x-1 whitespace-nowrap flex-none">
#                                             <div class="grid flex-initial">
#                                                 <span class="truncate">Post views</span>
#                                             </div>
#                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                 <i class="icon-info-circle-line inline-flex leading-[0] text-neutral3 text-xl"></i>
#                                             </button>
#                                         </span>
#                                     </div>
#                                 </div>
#                             </div>
#                             <div class="flex justify-between text-center">
#                                 <div class="flex flex-1 flex-col border-r border-[#E7EAED] py-4 md:py-5">
#                                     <span class="text-base font-semibold text-text-primary">~
#                                     <!-- -->
#                                     <!-- -->
#                                     1 601</span>
#                                     <span class="text-sm font-medium text-text-secondary">24
#                                     <!-- -->
#                                     <!-- -->
#                                     hours</span>
#                                 </div>
#                                 <div class="flex flex-col items-center flex-1 py-4 md:py-5">
#                                     <span class="text-base font-semibold text-text-primary">~
#                                     <!-- -->
#                                     <!-- -->
#                                     2 067</span>
#                                     <span class="text-sm font-medium text-text-secondary">48
#                                     <!-- -->
#                                     <!-- -->
#                                     hours</span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="item w-full hidden md:block">
#                         <div class="rounded-lg bg-gray-gradient shadow-border-custom-sm">
#                             <div class="flex justify-between border-b border-[#E7EAED] p-3 md:p-5">
#                                 <div class="flex items-center gap-3">
#                                     <span class="flex aspect-square rounded-full p-2.5 shadow-icon">
#                                         <i class="icon-er-line inline-flex leading-[0] text-xl text-text-dynamic"></i>
#                                     </span>
#                                     <div class="flex flex-col items-start">
#                                         <span class="flex items-center gap-3 text-2xl font-semibold text-text-primary">9.29
#                                         <!-- -->
#                                         %</span>
#                                         <span class="inline-flex max-w-full items-center gap-1 truncate text-sm font-medium text-text-base-secondary gap-x-1 whitespace-nowrap flex-none">
#                                             <div class="grid flex-initial">
#                                                 <span class="truncate">Engagement rate</span>
#                                             </div>
#                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                 <i class="icon-info-circle-line inline-flex leading-[0] text-neutral3 text-xl"></i>
#                                             </button>
#                                         </span>
#                                     </div>
#                                 </div>
#                             </div>
#                             <div class="flex justify-between text-center">
#                                 <div class="flex flex-1 flex-col border-r border-[#E7EAED] py-4 md:py-5">
#                                     <span class="text-base font-semibold text-text-primary">3.5
#                                     <!-- -->
#                                     %</span>
#                                     <span class="text-sm font-medium text-text-secondary">24
#                                     <!-- -->
#                                     <!-- -->
#                                     hours</span>
#                                 </div>
#                                 <div class="flex flex-col items-center flex-1 py-4 md:py-5">
#                                     <span class="text-base font-semibold text-text-primary">4.6
#                                     <!-- -->
#                                     %</span>
#                                     <span class="text-sm font-medium text-text-secondary">48
#                                     <!-- -->
#                                     <!-- -->
#                                     hours</span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="item w-full hidden md:block">
#                         <div class="rounded-lg bg-gray-gradient shadow-border-custom-sm">
#                             <div class="flex justify-between border-b border-[#E7EAED] p-3 md:p-5">
#                                 <div class="flex items-center gap-3">
#                                     <span class="flex aspect-square rounded-full p-2.5 shadow-icon">
#                                         <i class="icon-symbol-at-line inline-flex leading-[0] text-xl text-text-dynamic"></i>
#                                     </span>
#                                     <div class="flex flex-col items-start">
#                                         <span class="flex items-center gap-3 text-2xl font-semibold text-text-primary">1</span>
#                                         <span class="inline-flex max-w-full items-center gap-1 truncate text-sm font-medium text-text-base-secondary gap-x-1 whitespace-nowrap flex-none">
#                                             <div class="grid flex-initial">
#                                                 <span class="truncate">Mentions</span>
#                                             </div>
#                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                 <i class="icon-info-circle-line inline-flex leading-[0] text-neutral3 text-xl"></i>
#                                             </button>
#                                         </span>
#                                     </div>
#                                 </div>
#                             </div>
#                             <div class="flex justify-between text-center">
#                                 <div class="flex flex-1 flex-col border-r border-[#E7EAED] py-4 md:py-5">
#                                     <span class="text-base font-semibold text-text-primary">
#                                         <span class="px-2 text-base font-medium rounded w-max bg-yang-gray-100 text-subtle">No data</span>
#                                     </span>
#                                     <span class="text-sm font-medium text-text-secondary">7
#                                     <!-- -->
#                                     <!-- -->
#                                     days
#                                     <!-- -->
#                                     </span>
#                                 </div>
#                                 <div class="flex flex-col items-center flex-1 py-4 md:py-5">
#                                     <span class="text-base font-semibold text-text-primary">
#                                         <span class="px-2 text-base font-medium rounded w-max bg-yang-gray-100 text-subtle">No data</span>
#                                     </span>
#                                     <span class="text-sm font-medium text-text-secondary">30
#                                     <!-- -->
#                                     <!-- -->
#                                     days</span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#             <div class="container">
#                 <div class="bg-gray-gradient container mt-4 grid w-full grid-cols-1 flex-wrap justify-between rounded-lg p-0 shadow-border-custom-sm sm:mt-6 sm:grid-cols-2 lg:grid-cols-4 lg:p-5 hidden md:grid">
#                     <div class="border-b border-[#E7EAED] p-3 sm:border-r lg:border-b-0 lg:py-0 lg:pl-0">
#                         <div class="flex items-center gap-3">
#                             <span class="flex aspect-square rounded-full p-2.5 shadow-icon">
#                                 <i class="icon-doc-line inline-flex leading-[0] text-xl text-text-dynamic"></i>
#                             </span>
#                             <div class="flex flex-col items-start">
#                                 <span class="flex items-center gap-3 text-base font-semibold">~
#                                 <!-- -->
#                                 <!-- -->
#                                 3</span>
#                                 <span class="inline-flex max-w-full items-center gap-1 truncate text-sm font-medium text-text-base-secondary gap-x-1 whitespace-nowrap flex-none">
#                                     <div class="grid flex-initial">
#                                         <span class="truncate">Posts per day</span>
#                                     </div>
#                                     <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                         <i class="icon-info-circle-line inline-flex leading-[0] text-neutral3 text-xl"></i>
#                                     </button>
#                                 </span>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="border-b border-[#E7EAED] p-3 lg:border-b-0 lg:border-r lg:py-0">
#                         <div class="flex items-center gap-3">
#                             <span class="flex aspect-square rounded-full p-2.5 shadow-icon">
#                                 <i class="icon-thumbs-up-line inline-flex leading-[0] text-xl text-text-dynamic"></i>
#                             </span>
#                             <div class="flex flex-col items-start">
#                                 <span class="flex items-center gap-3 text-base font-semibold">~
#                                 <!-- -->
#                                 <!-- -->
#                                 21</span>
#                                 <span class="inline-flex max-w-full items-center gap-1 truncate text-sm font-medium text-text-base-secondary gap-x-1 whitespace-nowrap flex-none">
#                                     <div class="grid flex-initial">
#                                         <span class="truncate">Reactions</span>
#                                     </div>
#                                     <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                         <i class="icon-info-circle-line inline-flex leading-[0] text-neutral3 text-xl"></i>
#                                     </button>
#                                 </span>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="border-b border-[#E7EAED] p-3 sm:border-b-0 sm:border-r lg:py-0">
#                         <div class="flex items-center gap-3">
#                             <span class="flex aspect-square rounded-full p-2.5 shadow-icon">
#                                 <i class="icon-message-square-line inline-flex leading-[0] text-xl text-text-dynamic"></i>
#                             </span>
#                             <div class="flex flex-col items-start">
#                                 <span class="flex items-center gap-3 text-base font-semibold">
#                                     <span class="px-2 text-base font-medium rounded w-max bg-yang-gray-100 text-subtle">No data</span>
#                                 </span>
#                                 <span class="inline-flex max-w-full items-center gap-1 truncate text-sm font-medium text-text-base-secondary gap-x-1 whitespace-nowrap flex-none">
#                                     <div class="grid flex-initial">
#                                         <span class="truncate">Comments</span>
#                                     </div>
#                                     <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                         <i class="icon-info-circle-line inline-flex leading-[0] text-neutral3 text-xl"></i>
#                                     </button>
#                                 </span>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="p-3 lg:py-0 lg:pr-0">
#                         <div class="flex items-center gap-3">
#                             <span class="flex aspect-square rounded-full p-2.5 shadow-icon">
#                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-xl text-text-dynamic"></i>
#                             </span>
#                             <div class="flex flex-col items-start">
#                                 <span class="flex items-center gap-3 text-base font-semibold">~
#                                 <!-- -->
#                                 <!-- -->
#                                 2</span>
#                                 <span class="inline-flex max-w-full items-center gap-1 truncate text-sm font-medium text-text-base-secondary gap-x-1 whitespace-nowrap flex-none">
#                                     <div class="grid flex-initial">
#                                         <span class="truncate">Reposts</span>
#                                     </div>
#                                     <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                         <i class="icon-info-circle-line inline-flex leading-[0] text-neutral3 text-xl"></i>
#                                     </button>
#                                 </span>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#                 <button class="block w-full px-4 py-2 mt-4 font-medium rounded-md bg-gray-gradient text-text-dynamic shadow-border-custom-sm hover:text-primary2 md:hidden">
#                     <span class="flex items-center justify-center gap-x-1.5 text-sm">
#                         <i class="icon-chevron-down-line inline-flex leading-[0] text-lg"></i>
#                         More stats
#                     </span>
#                 </button>
#             </div>
#             <div class="w-full scroll-mt-24 border-b border-border-base-secondary mt-11">
#                 <ul class="scrollbar-hide container -mb-[1px] flex gap-5 overflow-x-auto font-medium">
#                     <li class="tab-li">
#                         <a class="tab" href="/en/channels/1829680439-baji_bgd">Overview
#                         <!-- -->
#                         </a>
#                     </li>
#                     <li class="tab-li">
#                         <a class="tab" rel="nofollow" href="/en/channels/1829680439-baji_bgd/marketing">Advertising effectiveness
#                         <!-- -->
#                         </a>
#                     </li>
#                     <li class="tab-li">
#                         <a class="tab" href="/en/channels/1829680439-baji_bgd/quote">Quoting
#                         <!-- -->
#                         </a>
#                     </li>
#                     <li class="tab-li">
#                         <a class="tab tab_active" rel="nofollow" href="/en/channels/1829680439-baji_bgd/publish">Publications
#                         <!-- -->
#                         </a>
#                     </li>
#                     <li class="tab-li">
#                         <a class="tab" rel="nofollow" href="/en/channels/1829680439-baji_bgd/audience">Audience
#                         <!-- -->
#                         </a>
#                     </li>
#                     <li class="tab-li">
#                         <a class="tab" rel="nofollow" href="/en/channels/1829680439-baji_bgd/about">About the channel
#                         <!-- -->
#                         </a>
#                     </li>
#                     <li class="tab-li">
#                         <a class="tab" rel="nofollow" href="/en/channels/1829680439-baji_bgd/invite-links">Invite links
#                         <!-- -->
#                         </a>
#                     </li>
#                 </ul>
#             </div>
#             <div class="container relative my-16">
#                 <div class="flex flex-col gap-6 lg:flex-row lg:gap-10 xl:gap-16">
#                     <div class="flex w-full flex-1 flex-col lg:w-3/5">
#                         <div class="rounded-lg border border-border-base-secondary px-2.5 py-4 shadow-sm lg:px-7 lg:py-7">
#                             <!--$-->
#                             <div class="@container/chart-wrapper">
#                                 <div class="mb-4 flex w-full flex-col items-baseline justify-between gap-4 @3xl/chart-wrapper:flex-row">
#                                     <div class="flex w-full flex-1 flex-col text-center @3xl/chart-wrapper:mx-auto @3xl/chart-wrapper:text-left">
#                                         <div class="flex items-center justify-center @3xl/chart-wrapper:justify-start">
#                                             <span class="inline-flex max-w-full items-center gap-1 truncate font-semibold text-lg leading-[26px] lg:text-2xl @3xl/chart-wrapper:text-2xl gap-x-1.5 flex-none">
#                                                 <div class="grid flex-initial">
#                                                     <span class="truncate">Posting time distributions</span>
#                                                 </div>
#                                                 <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                     <i class="icon-info-circle-line inline-flex leading-[0] text-neutral3 text-[18px] lg:text-[24px]"></i>
#                                                 </button>
#                                             </span>
#                                         </div>
#                                     </div>
#                                 </div>
#                                 <div class="flex items-center justify-center overflow-auto h-[300px] sm:h-[400px]" id="chart_posting_time">
#                                     <div class="p-6 Loader_loading-container__833ya">
#                                         <div class="Loader_loading__MZ9UM Loader_loader__d53H6 ">
#                                             <div class="mx-0.5 bg-yellow Loader_line__3A5cM"></div>
#                                             <div class="bg-light-blue Loader_line__3A5cM"></div>
#                                             <div class="bg-primary Loader_line__3A5cM"></div>
#                                         </div>
#                                         <h4 class="text-2xl font-semibold">Data loading in progress...</h4>
#                                     </div>
#                                 </div>
#                             </div>
#                             <!--/$-->
#                         </div>
#                     </div>
#                     <div class="flex w-full flex-1 flex-col gap-6 lg:w-2/5 lg:max-w-[460px]">
#                         <div class="views-sources__bg flex h-full flex-col items-center justify-center rounded-[8px] p-4 text-center lg:rounded-[12px] lg:p-7">
#                             <div>
#                                 <h4 class="mb-2 text-xl font-semibold text-text-base-primary">Find out who reads your channel</h4>
#                                 <span class="text-sm font-medium text-text-base-secondary">This graph will show you who besides your subscribers reads your channel and learn about other sources of traffic.</span>
#                                 <button class="button button-border whitespace-nowrap button_primary button_small mb-6 mt-4 lg:mb-11">Find out sources views</button>
#                             </div>
#                             <div class="h-[244px] w-[300px] overflow-hidden md:h-[240px] md:w-[686px] lg:h-[265px] lg:w-[374px]">
#                                 <img alt="Views Sources" loading="lazy" width="296" height="241" decoding="async" data-nimg="1" class="h-full w-full object-cover" style="color:transparent" src="/_next/static/media/graph-mob.05527c4a.svg"/>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#                 <div class="mt-6 flex flex-col lg:mt-6 xl:mt-16">
#                     <div class="z-10 flex flex-col flex-wrap justify-between gap-2 bg-white pb-6 lg:sticky lg:top-[61px] lg:-mx-2 lg:flex-row lg:px-2 lg:pt-4">
#                         <div class="flex w-full flex-1">
#                             <span class="inline-flex max-w-full items-center gap-1 truncate font-semibold text-lg leading-[26px] lg:text-2xl w-full flex-1 justify-center whitespace-nowrap lg:justify-start gap-x-1.5 flex-none">
#                                 <div class="grid flex-initial">
#                                     <span class="truncate">Publication analysis</span>
#                                 </div>
#                                 <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                     <i class="icon-info-circle-line inline-flex leading-[0] text-neutral3 text-[18px] lg:text-[24px]"></i>
#                                 </button>
#                             </span>
#                         </div>
#                         <div class="flex w-full flex-1 flex-col gap-4 lg:flex-row">
#                             <div class="lg:w-52 xl:w-64">
#                                 <div id="R1jbrpiuubf3tta" is-expanded="false" class="select">
#                                     <button class="select__input" id="headlessui-listbox-button-:R2ljbrpiuubf3tta:" type="button" aria-haspopup="listbox" aria-expanded="false" data-headlessui-state="">
#                                         <i class="icon-type-figures-line inline-flex leading-[0] select__prepend-icon"></i>
#                                         <span class="flex-1 w-px min-w-0 truncate text-start">All posts</span>
#                                         <i class="icon-chevron-down-line inline-flex leading-[0] h-5 w-5 text-[20px] text-gray-600"></i>
#                                     </button>
#                                 </div>
#                             </div>
#                             <div class="lg:w-52 xl:w-64">
#                                 <div id="R2jbrpiuubf3tta" is-expanded="false" class="select">
#                                     <button class="select__input" id="headlessui-listbox-button-:R2mjbrpiuubf3tta:" type="button" aria-haspopup="listbox" aria-expanded="false" data-headlessui-state="">
#                                         <i class="icon-calendar-line inline-flex leading-[0] select__prepend-icon"></i>
#                                         <span class="flex-1 w-px min-w-0 truncate text-start">30 days</span>
#                                         <i class="icon-chevron-down-line inline-flex leading-[0] h-5 w-5 text-[20px] text-gray-600"></i>
#                                     </button>
#                                 </div>
#                             </div>
#                             <div class="lg:w-52 xl:w-64">
#                                 <div id="R3jbrpiuubf3tta" is-expanded="false" class="select">
#                                     <button class="select__input" id="headlessui-listbox-button-:R2njbrpiuubf3tta:" type="button" aria-haspopup="listbox" aria-expanded="false" data-headlessui-state="">
#                                         <i class="icon-filter-line inline-flex leading-[0] select__prepend-icon"></i>
#                                         <span class="flex-1 w-px min-w-0 truncate text-start">Latest posts</span>
#                                         <i class="icon-chevron-down-line inline-flex leading-[0] h-5 w-5 text-[20px] text-gray-600"></i>
#                                     </button>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="z-0 flex flex-col justify-between gap-6 sm:flex-row lg:gap-10 xl:gap-16">
#                         <div class="flex-1 overflow-auto lg:sticky lg:top-[calc(77px+66px)] lg:max-h-[calc(100vh-77px-66px)]">
#                             <table class="w-full whitespace-nowrap font-medium">
#                                 <thead class="sticky top-0 z-10 border-b border-neutral5 bg-white font-semibold">
#                                     <tr>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">Posts</td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">Views</td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="inline-flex max-w-full items-center gap-1 truncate flex-none">
#                                                 <div class="grid flex-initial">
#                                                     <span class="truncate">Shares</span>
#                                                 </div>
#                                                 <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                     <i class="icon-info-circle-line inline-flex leading-[0] text-neutral3 text-xl"></i>
#                                                 </button>
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="inline-flex max-w-full items-center gap-1 truncate flex-none">
#                                                 <div class="grid flex-initial">
#                                                     <span class="truncate">Views dynamics</span>
#                                                 </div>
#                                                 <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                     <i class="icon-info-circle-line inline-flex leading-[0] text-neutral3 text-xl"></i>
#                                                 </button>
#                                             </span>
#                                         </td>
#                                     </tr>
#                                 </thead>
#                                 <tbody>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">01</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">শোয়েব আখতার, যিনি &quot;রাওয়ালপিন্ডি এক্সপ্রেস &quot;নামে পরিচিত, এবং ব্রেট লি, অস্ট্রেলিয়ার কিংবদন্তি ফাস্ট বোলার, তাদের অসাধারণ গতির জন্য বিখ্যাত। আখতার ২০০৩ সালের বিশ্বকাপে ১৬১.৩ কিমি/ঘণ্টা বেগে বল করে নজর কেড়েছিলেন, তার ক্যারিয়ারে ৪৪৪ ওডিআই এবং ১৭৮ টেস্ট উইকেট নিয়েছিলেন। অন্যদিকে, লি ১৬১.১ কিমি/ঘণ্টা বেগে বল করেন, এবং ৭০০টিরও বেশি আন্তর্জাতিক উইকেট সংগ্রহ করেন, দুটি বিশ্বকাপ জয়ে অস্ট্রেলিয়ার গুরুত্বপূর্ণ ভূমিকা পালন করেন, তার আক্রমণাত্মক বোলিং স্টাইল এবং সুইংয়ের জন্য স্বীকৃত।</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1 216
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 3
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">02</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">সিএসকে এমএস ধোনিকে ৪ কোটি টাকায় আনক্যাপড খেলোয়াড় হিসেবে ধরে রাখতে পারবে, কারণ আইপিএলের একটি পুনর্জীবিত নিয়ম ভারতীয় খেলোয়াড়দের, যারা পাঁচ বছর ধরে আন্তর্জাতিক ক্রিকেট থেকে অবসর নিয়েছে, আনক্যাপড হিসেবে শ্রেণীবদ্ধ করার অনুমতি দেয়। ৪৩ বছর বয়সী ধোনি ২০২০ সালে অবসর নিয়েছিলেন এবং শুধুমাত্র আইপিএল খেলেন। তিনি ২০২৪ সালে সিএসকের অধিনায়কত্ব রুতুরাজ গায়কওয়াদের হাতে তুলে দেন।


# ❤️  Baji  সদস্য  হিসাবে সাইন-আপ করুন 🚀
#  🛡এখনই  Baji Appডাউনলোড  করুন!! ⬇️</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1 247
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">03</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">আপনি কি সেরা বেটিং অভিজ্ঞতা খুঁজছেন? আজই Baji-তে  যোগ দিন এবং নিজেকে স্পোর্টসের জগতে নিমজ্জিত করুন যা আগে কখনও হয়নি! লাইভ বেটিং অপশন এবং রিয়েল-টাইম আপডেট উপভোগ করুন যা আপনাকে খেলায় যুক্ত রাখবে। আমরা বিভিন্ন খেলা ও ইভেন্টে সর্বোত্তম অডস প্রদান করি, যা আপনার বেটের সর্বোচ্চ মূল্য নিশ্চিত করে। আজই সাইন আপ করুন এবং আপনার ভাগ্য আনলক করুন।</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1 295
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">04</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">ত্রিনবাগো নাইট রাইডার্স বনাম বার্বাডোজ রয়্যালস, ২৮তম ম্যাচের হাইলাইটস | ক্যারিবিয়ান প্রিমিয়ার লিগ ২০২৪

# ২০২৪ রিপাবলিক ব্যাংক ক্যারিবিয়ান প্রিমিয়ার লিগ (CPL) প্রতিযোগিতার শেষ সপ্তাহের দিকে বার্বাডোস রয়্যালসের জন্য আরেকটি হতাশাজনক রাত ছিল । যারা সহ শিরোপা প্রত্যাশী ত্রিনবাগো নাইট রাইডার্সের হাতে টানা চতুর্থ পরাজয়ের শিকার হয়েছিল। প্রতিযোগিতার শুরুতে পরাজিত দল হওয়া সত্ত্বেও রয়্যালস চূড়ান্ত বাছাইপর্বে চতুর্থ স্থানে ছিল।




# ❤️  Baji  সদস্য  হিসাবে সাইন-আপ করুন 🚀
#  🛡এখনই  Baji Appডাউনলোড  করুন!! ⬇️</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1 250
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">05</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">অবসর গ্রহণের পর, ব্রাভো আইপিএল ২০২৫-এর জন্য কেকেআরের মেন্টর হিসেবে দায়িত্ব নেবেন।

# ডোয়েন ব্রাভো অবসর নিয়েছেন এবং ২০২৫ সাল থেকে কলকাতা নাইট রাইডার্স (KKR)-এর মেন্টর হিসেবে যোগ দিয়েছেন, তিনি নাইট রাইডার্সের সব ফ্র্যাঞ্চাইজি পর্যবেক্ষণ করবেন। তিনি চেন্নাই সুপার কিংস (CSK) এর সাবেক কোচ এবং খেলোয়াড়। ব্রাভো পরামর্শক কোচ হিসাবে আফগানিস্তানকে ২০২৪ টি-টোয়েন্টি বিশ্বকাপের সেমিফাইনালে পৌঁছাতে সাহায্য করেছিলেন।</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1 787
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 4
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">06</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">গায়ানা আমাজন ওয়ারিয়র্স বনাম বার্বাডোজ রয়্যালস, ২৭ তম ম্যাচের হাইলাইটস | ক্যারিবিয়ান প্রিমিয়ার লিগ ২০২৪

# গায়ানা অ্যামাজন ওয়ারিয়র্স বার্বাডোজ রয়্যালসকে ৪৭ রানে পরাজিত করে। ফলে ২০২৪ রিপাবলিক ব্যাঙ্ক ক্যারিবিয়ান প্রিমিয়ার লিগের CPL পয়েন্ট টেবিলে শীর্ষ দুয়ে থাকার সম্ভাবনা রয়েছে। রয়্যালস, তাদের পূর্ববর্তী ফর্মের কারণে টেবিলের শীর্ষে উঠার আশায় ছিল, তবে সাম্প্রতিক ম্যাচে তৃতীয় পরাজয়ের ফলে তাদের তৃতীয় বা চতুর্থ স্থানে স্থির থাকতে হবে। ম্যাচের অধিনায়ক রোভম্যান পাওয়েল টসে জয়ী হয়ে প্রতিপক্ষকে ব্যাটিং করতে পাঠান। গুরবাজ দ্রুত আউট হলেও ওয়ারিয়র্স ২০ ওভারে ২১৯/৮ রান করতে সক্ষম হয়।</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1 642
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">07</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">🔒 baji  প্রিমিয়াম ডিপোজিট সিস্টেম উন্নত এনক্রিপশনের সাথে সর্বাধিক নিরাপত্তা, সহজ ব্যবহার এবং নিরাপদ লেনদেন নিশ্চিত করে 🔐

# 💵 সহজ ডিপোজিট  এবং দ্রুত উত্তোলন এবং চিন্তামুক্ত গেমিং অভিজ্ঞতার জন্য তৈরি করে।

# 🔒 baji তে অত্যাধুনিক ডিপোজিট সিস্টেম এনক্রিপশন প্রযুক্তি সহ শীর্ষ-স্তরের নিরাপত্তা প্রদান করে 🔐

# প্রতিটি লেনদেনে অতুলনীয় নিরাপত্তা এবং সুবিধার জন্য baji কে  বিশ্বাস করুন 🔓।

# স্ট্রেস-মুক্ত, নিরাপদ অ্যাডভেঞ্চারের জন্য এখনই baji তে যোগ দিন।</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1 578
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">08</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">🔒 baji  প্রিমিয়াম ডিপোজিট সিস্টেম উন্নত এনক্রিপশনের সাথে সর্বাধিক নিরাপত্তা, সহজ ব্যবহার এবং নিরাপদ লেনদেন নিশ্চিত করে 🔐...
# 💵 সহজ ডিপোজিট  এবং দ্রুত উত্তোলন এবং চিন্তামুক্ত গেমিং অভিজ্ঞতার জন্য তৈরি করে।

# 🔒 baji তে অত্যাধুনিক ডিপোজিট সিস্টেম এনক্রিপশন প্রযুক্তি সহ শীর্ষ-স্তরের নিরাপত্তা প্রদান করে 🔐

# প্রতিটি লেনদেনে অতুলনীয় নিরাপত্তা এবং সুবিধার জন্য baji কে  বিশ্বাস করুন 🔓।

# স্ট্রেস-মুক্ত, নিরাপদ অ্যাডভেঞ্চারের জন্য এখনই baji তে যোগ দিন।</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 3
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">09</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">🔒 baji  প্রিমিয়াম ডিপোজিট সিস্টেম উন্নত এনক্রিপশনের সাথে সর্বাধিক নিরাপত্তা, সহজ ব্যবহার এবং নিরাপদ লেনদেন নিশ্চিত করে 🔐

# 💵 সহজ ডিপোজিট  এবং দ্রুত উত্তোলন এবং চিন্তামুক্ত গেমিং অভিজ্ঞতার জন্য তৈরি করে।

# 🔒 baji তে অত্যাধুনিক ডিপোজিট সিস্টেম এনক্রিপশন প্রযুক্তি সহ শীর্ষ-স্তরের নিরাপত্তা প্রদান করে 🔐

# প্রতিটি লেনদেনে অতুলনীয় নিরাপত্তা এবং সুবিধার জন্য baji কে  বিশ্বাস করুন 🔓।

# স্ট্রেস-মুক্ত, নিরাপদ অ্যাডভেঞ্চারের জন্য এখনই baji তে যোগ দিন।


# ❤️  Baji  সদস্য  হিসাবে সাইন-আপ করুন 🚀
#  🛡এখনই  Baji Appডাউনলোড  করুন!! ⬇️
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">10</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">বিরতিহীন বিনোদন এবং বড় পুরস্কার খুঁজছেন? Jili Teen Patti আপনার জন্য! লক্ষ লক্ষ খেলোয়াড়ের সাথে যোগ দিন এবং রোমাঞ্চকর ম্যাচে আপনার কার্ডের দক্ষতা প্রদর্শন করুন। রিয়েল প্লেয়ারদের বিরুদ্ধে খেলুন, বিশেষ বৈশিষ্ট্যগুলি আনলক করুন এবং অত্যাশ্চর্য ভিজ্যুয়াল উপভোগ করুন। আজই শুরু করুন baji-র সাথে। 

# ❤️  Baji  সদস্য  হিসাবে সাইন-আপ করুন 🔼
#  🛡এখনই  Baji Appডাউনলোড  করুন!! ⬇️
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1 679
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">11</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">দ্বিতীয় টেস্টের প্রথম দিন ৩৫ ওভারের খেলা বৃষ্টির কারণে এবং খারাপ আলোতে বন্ধ হয়ে যায়। আর. অশ্বিন প্রথম উইকেট নেন, বাংলাদেশ অধিনায়ক নাজমুল হোসেন শান্তকে আউট করে। আকাশ দীপ দুই ওপেনারকে আউট করেন, জাকির হাসান শূন্য এবং সাদমান ইসলাম ২৪ রান করেন। টস জিতে ভারতীয় অধিনায়ক রোহিত শর্মা প্রথমে বোলিংয়ের সিদ্ধান্ত নেন।</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2 245
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">12</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">সেন্ট লুসিয়া কিংস বনাম ট্রিনবাগো নাইট রাইডার্স, ২৬ তম ম্যাচ হাইলাইটস | ক্যারিবিয়ান প্রিমিয়ার লিগ ২০২৪

# সেন্ট লুসিয়া কিংস ২০২৪ রিপাবলিক ব্যাংক ক্যারিবিয়ান প্রিমিয়ার লিগ (সিপিএল) প্লে-অফে অন্য তিনটি দলের জন্য একটি বিশাল সংকেত পাঠিয়েছে, তারা ২০ ওভারে ২১৮ রান সংগ্রহ করেছে এবং ট্রিনবাগো নাইট রাইডার্সকে ১৩৮/৯ রানে সীমাবদ্ধ করে ৮০ রানে বিজয়ী হয়েছে এবং পয়েন্ট টেবিলে সবার শীর্ষে আছে। কিংস ক্যাপ্টেন ফাফ ডু প্লেসিস এবং তার ওপেনিং পার্টনার জনসন চার্লস দুর্দান্ত ব্যাট করে। তাদের মধ্যে ১৪৫ রানের ওপেনিং পার্টনারশিপ হয় যেখানে তারা একাধিক বাউন্ডারি মেরেছিলেন, সেই কারনেই প্রথম ইনিংসটি শেষ হতে দুই ঘন্টার বেশি সময় লেগেছিল।


# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2 314
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">13</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">শুক্রবার বিশেষ প্রতিযোগিতা খুবই  কাছাকাছি!  ৪র্থ রাউন্ড  ২৭ সেপ্টেম্বর থেকে ৪ অক্টোবর পর্যন্ত অনুষ্ঠিত হবে, যা উত্তেজনাপূর্ণ গেম এবং চমত্কার পুরস্কার নিয়ে আসবে। প্রতিযোগিতায় যোগদান, স্পিন এবং বড় জয়ের সুযোগ মিস করবেন না! আপনার ক্যালেন্ডার চিহ্নিত করুন এবং  একশনের জন্য প্রস্তুত হন!</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2 082
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">14</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">🔥 চূড়ান্ত ক্রিকেট অভিজ্ঞতার জন্য প্রস্তুত হন! SKN Patriots-এর গর্বিত স্পন্সর হিসাবে,baji নিয়ে আসে সবচেয়ে রোমাঞ্চকর মুহূর্তগুলো– দারুণ ছক্কা, উইকেট, এবং বিদ্যুতের মতো খেলা। ⚡️

# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram             📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1 899
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">15</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">সময় প্রায় শেষ কিন্তু রোমাঞ্চ এখনো ফুরিয়ে যায়নি!

# আমাদের &#x27;ক্রিকেট ম্যারাথন লিডারবোর্ড &#x27;কনটেস্টে আপনার জন্য এখনও ৳১৫ কোটিরও বেশি একটি শট অপেক্ষা করছে। আপনার বোনাসের অংশ বাড়িতে নিতে ডিপোজিট করুন, স্পোর্টস মার্কেটে বেট রাখুন, পয়েন্ট সংগ্রহ করুন এবং শীর্ষ ৫০০-এ উঠুন। শেষ বাঁশি বাজার আগে এখনই অ্যাকশন নিন!

# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram             📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1 925
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">16</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">সেন্ট কিটস এবং নেভিস প্যাট্রিয়টস বনাম ট্রিনবাগো নাইট রাইডার্স, ২৫ তম ম্যাচ হাইলাইটস | ক্যারিবিয়ান প্রিমিয়ার লিগ ২০২৪

# ২০২৪ সালের রিপাবলিক ব্যাংক CPL-এর দ্বিতীয় ম্যাচে উচ্চ স্কোরিং প্রতিযোগিতায় ত্রিনবাগো নাইট রাইডার্স সেন্ট কিটস অ্যান্ড নেভিস প্যাট্রিয়টসকে সাত উইকেটে হারিয়ে তাদের মৌসুমের ইতি টানে। প্রতিযোগিতায় তাদের প্রথম ম্যাচ জেতার পর থেকে প্যাট্রিয়টস প্রতিটি খেলায় হেরেছে, তবে তারা টস হেরে ব্যাট করতে নেমে ১৯৩/৪ রান করার পরও তারৌবায় এই হারটি বিশেষভাবে নিষ্ঠুর মনে হয়েছে। অধিনায়ক আন্দ্রে ফ্লেচার সামনে থেকে নেতৃত্ব দিয়ে ৬১ বলে ৯৩ রানের অসাধারণ ইনিংস খেলেন, যেখানে চারদিকেই শট মারেন এবং বিশাল ছয়টি ছক্কা মেরেছিলেন। ফ্লেচার তাঁর শতক থেকে মাত্র সাত রান দূরে ছিলেন, যখন ক্রিস জর্ডান তাকে লং অফ বাউন্ডারিতে কায়রন পোলার্ডের &quot;বাকেট হাতে &quot;ক্যাচ আউট করান।</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2 413
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 5
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">17</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">চ্যালেঞ্জ টাইম 
# এই ধাঁধা দিয়ে আপনার মস্তিষ্ক পরীক্ষা করুন এবং দেখুন কত দ্রুত আপনি এটি সমাধান করতে পারেন! ⏳
# আপনার বন্ধুদেরও চ্যালেঞ্জ করুন — কে সবচেয়ে দ্রুত ধাঁধা সমাধান করতে পারে? 🚀</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2 370
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">18</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">লাগামহীন রোমাঞ্চ উপভোগ করুন! 

# আমাদের সীমিত সময়ের &#x27;ওয়েলকাম অফার &#x27;-এর মাধ্যমে আপনার মোট উইনিং এর উপর ৳১,০০০ পর্যন্ত একটি ডাবল বোনাস আনলক করুন! শুধু আপনার ফার্স্ট ডিপোজিট করুন, Yellow Bat-এর Diva &#x27;s Ace গেমে বেট রাখুন, আপনার উইনিং এর স্ক্রিনশট Facebook-এ শেয়ার করুন এবং একটি এক্সট্রা ফ্রি বোনাস লুফে নেওয়ার সহজ রিকোয়ারমেন্টগুলো সম্পূর্ণ করুন! তাড়াতাড়ি করুন, যদিও—এটি &#x27;আগে আসলে আগে পাবেন &#x27;ভিত্তিতে পাওয়া যায়। এক্সাইটমেন্ট মিস করবেন না!</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2 504
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">19</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">ভারত বনাম বাংলাদেশ ম্যাচ মানে হাইভোল্টেজের খেলা! টেস্ট ক্রিকেটে এই দ্বন্দ্বে প্রতিটি বল এবং প্রতিটি ইনিংসে থাকে চরম উত্তেজনা। দুই দলের জন্যই গর্ব এবং ইতিহাসের চ্যালেঞ্জ—দর্শকরা প্রত্যাশা করেন অবিশ্বাস্য নাটকীয়তা, দুর্দান্ত বোলিং এবং অসাধারণ ব্যাটিং! তাই, ভারত-বাংলাদেশের খেলা সবসময়ই বিশেষ কিছু! 🏏🔥

# আপনার মতামত জানাতে কমেন্ট করুন! ক্রিকেটের এই মহাযুদ্ধ সম্পর্কে আপনার ভাবনা কী? 🏏✨</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2 433
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">20</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">আপনার পছন্দের স্লট খেলা খুঁজছেন? JILI Slot Fortune Gem 2 খেলুন!আপনার বাজির ১০০০ গুণ পর্যন্ত অসাধারণ পুরস্কার জিততে পারবেন! বিশেষ ৪র্থ রিলে কেবল মাল্টিপ্লায়ার সিম্বল রয়েছে, যা উত্তেজনা এবং সম্ভাবনাকে বাড়িয়ে তোলে। সর্বোচ্চ ৭৫,১২৫,০০০ টাকার বিশাল পুরস্কার জিততে এখনই যোগ দিন এবং ভাগ্যকে পরীক্ষা করুন!

# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2 899
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">21</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">বাংলাদেশের বিপক্ষে দ্বিতীয় টেস্টে ছয় রেকর্ডের কাছাকাছি পৌঁছে গেছেন আর অশ্বিন। চতুর্থ ইনিংসে 100 ছুঁতে তার একটি উইকেট  প্রয়োজন।


# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2 751
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">22</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">২০২৪ রিপাবলিক ব্যাংক ক্যারিবিয়ান প্রিমিয়ার লিগ (CPL) এর প্লে-অফ করার জন্য চারটি দল কোয়ালিফাই করেছে   কিন্তু এটি বার্বাডোস রয়্যালস এবং সেন্ট লুসিয়া কিংসকে প্রভিডেন্সে স্তম্ভিত করেছে । ক্রিজে জেসন হোল্ডার এবং মহেশ থেকশানার সাথে শেষ ওভারে রয়্যালসকে ২১ রানের প্রয়োজন ছিল বলে শেষের পর্যায়ে পড়েছিলেন অ্যালিক আথানাজে এবং নাইম ইয়ং।

# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 3 067
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">23</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">হুররে! আমাদের &#x27;আল্টিমেট ফিয়েস্তা স্পিন &#x27;ক্যাম্পেইন এখন বিজয়ীদের উদযাপন করার সময়! ১০০ জন ভাগ্যবান প্লেয়ারদের অভিনন্দন যারা প্রত্যেকে একটি দুর্দান্ত ৳৫৭৭ বোনাস পেয়েছে। আপনার অবিশ্বাস্য সাপোর্ট এর জন্য এই ক্যাম্পেইনটি একটি বিশাল সফলতা পেয়েছে! আমরা সত্যিই এই আনন্দে আপনার যোগদানকে প্রশংসা করি।

# &#x27;আল্টিমেট ফিয়েস্তা স্পিন &#x27;অ্যাডভেঞ্চারে অংশগ্রহণ করার জন্য আপনাকে ধন্যবাদ। আরও রোমাঞ্চকর ক্যাম্পেইন এবং বেশি বেশি জেতার সুযোগ পেতে Baji-এর সাথেই সাথেই থাকুন!



# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2 605
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">24</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">গতকালের ম্যাচটি ছিল এককথায় অবিস্মরণীয়! আল নাসের আল হামজকে পরাজিত করে মাঠে দারুণ উল্লাস ছড়িয়েছে, যেখানে প্রতিটি মুহূর্ত ছিল চরম উত্তেজনার! দুর্দান্ত গোল, চোখধাঁধানো দক্ষতা এবং তীব্র প্রতিদ্বন্দ্বিতা – ভক্তদের জন্য এটি ছিল সত্যিই স্মরণীয় একটি রাত। আপনার প্রিয় মুহূর্তটি কোনটি ছিল? ⚽️

# আল হামজ (1) - (2) আল নাসের

# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2 985
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 4
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">25</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">গতকালের ম্যাচটি ছিল এককথায় অবিস্মরণীয়! আল নাসের আল হামজকে পরাজিত করে মাঠে দারুণ উল্লাস ছড়িয়েছে, যেখানে প্রতিটি মুহূর্ত ছিল চরম উত্তেজনার! দুর্দান্ত গোল, চোখধাঁধানো দক্ষতা এবং তীব্র প্রতিদ্বন্দ্বিতা – ভক্তদের জন্য এটি ছিল সত্যিই স্মরণীয় একটি রাত। আপনার প্রিয় মুহূর্তটি কোনটি ছিল? ⚽️

# আল হামজ (1) - (2) আল নাসের

# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">26</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">২৪ সেপ্টেম্বর থেকে ১ অক্টোবর পর্যন্ত চলমান JILI ফিশ টুর্নামেন্টের রাউন্ড ৪-এর উত্তেজনায় ডুবে যান! সমস্ত মুদ্রার জন্য উন্মুক্ত, এটি আপনার খেলার, জেতার এবং রোমাঞ্চকর  ফিশ-থিমযুক্ত গেম উপভোগ করার সুযোগ। মিস করবেন না—মজায় যোগ দিন এবং বড় পুরস্কারের জন্য প্রতিযোগিতা করুন !</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2 853
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">27</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">২৪ সেপ্টেম্বর থেকে ১ অক্টোবর পর্যন্ত JILI সুপার টুর্নামেন্টের রাউন্ড ৪ এর জন্য প্রস্তুত হন! উত্তেজনাপূর্ণ গেমগুলিতে প্রতিদ্বন্দ্বিতা করার এবং অবিশ্বাস্য পুরস্কার জেতার সুযোগটি মিস করবেন না। অ্যাকশনে যোগ দিন এবং টুর্নামেন্টের রোমাঞ্চের অভিজ্ঞতা নিন!</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2 952
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">28</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">গয়ানা আমাজন ওয়ারিয়র্স বনাম অ্যান্টিগুয়া ও বারবুডা ফ্যালকনস, ২৩তম ম্যাচের হাইলাইটস | CPL২০২৪

# বর্তমান চ্যাম্পিয়ন গয়ানা আমাজন ওয়ারিয়র্স অ্যান্টিগুয়া ও বারবুডা ফ্যালকনসকে ২৭ রানে হারিয়ে ২০২৪ সালের রিপাবলিক ব্যাংক ক্যারিবিয়ান প্রিমিয়ার লিগ (CPL)-এর শেষ পর্যায়ে জায়গা করে নিয়েছে। ফ্যালকনসের পরাজয়ের ফলে তারা এখন টুর্নামেন্ট থেকে বাদ পড়েছে এবং এই বছরের ইভেন্টের শেষ চারটি দল নিশ্চিত হয়েছে। ফ্যালকনস টস জিতে প্রথমে ফিল্ডিং করার সিদ্ধান্ত নেয় এবং ওয়ারিয়র্সকে ১৩৫/৭-এ সীমাবদ্ধ করে।


# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2 916
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">29</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">USD $3,500,000 এর বিশাল প্রাইজ পুলের সাথে PP ডেইলি স্লট টুর্নামেন্টের জন্য প্রস্তুত হোন! ২৩শে সেপ্টেম্বর ২০২৪ ) থেকে ৩০শে সেপ্টেম্বর, ২০২৪ পর্যন্ত, আপনার প্রিয় প্রাগম্যাটিক প্লে গেমগুলি খেলুন (নির্দিষ্ট শিরোনাম ব্যতীত) এবং আপনার জেতার সুযোগ নিন! দৈনিক  র‍যান্ডম পুরস্কার পাওয়ার এই অবিশ্বাস্য সুযোগটি মিস করবেন না!</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 3 446
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 7
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">30</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">টনি পপোভিক নতুন প্রধান কোচ হিসেবে অস্ট্রেলিয়ার দায়িত্ব গ্রহণ করেছেন, গ্রাহাম আর্নল্ডের পদত্যাগের পর, যিনি ২০২৬ বিশ্বকাপের এশিয়ান কোয়ালিফাইয়ে খারাপ শুরু করার কারণে চলে যান। অস্ট্রেলিয়ার &#x27;সোনালী প্রজন্মের &#x27;একজন সদস্য হিসেবে, পপোভিক ১০ অক্টোবর চীনের বিরুদ্ধে একটি গুরুত্বপূর্ণ জয় পেতে সোকারুদের নেতৃত্ব দিতে প্রস্তুত, কারণ তারা বর্তমানে জাপানের পিছনে পাঁচ পয়েন্টে রয়েছে।

# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 3 219
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">31</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">আপনি কোন প্লেয়ারের  এবং কত নাম্বার জার্সি পেতে চান?</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 3 532
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">32</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">বার্বাডোস রয়্যালস বনাম সেন্ট লুসিয়া কিংস, ২২তম ম্যাচের হাইলাইটস | ক্যারিবিয়ান প্রিমিয়ার লিগ ২০২৪

# শীর্ষে থাকা বার্বাডোস রয়্যালস প্রভিডেন্সে একটি ম্যাচ খেলেছিল, যেখানে তারা ৯৬/৯ স্কোর করেছিল এবং ৭ উইকেটে পরাজিত হয়েছিল। সেন্ট লুসিয়া কিংস অসাধারণ একটি পারফরম্যান্স প্রদর্শন করে ২০২৪ সালের রিপাবলিক ব্যাংক ক্যারিবিয়ান প্রিমিয়ার লিগ (সিপিএল) প্লে-অফের একটি স্থান নিশ্চিত করেছে। রয়্যালস টস জিতে ব্যাট করার সিদ্ধান্ত নেয়। উইকেটগুলো নিয়মিতভাবে পড়তে থাকে, কারণ জোসেফ এবং রোস্টন চেজ দুর্দান্ত বল করেন কিংসের হয়ে, তারা মিলে সাতটি উইকেট নেন। রয়্যালস কোনোমতে তাদের ২০ ওভার পূর্ণ করতে সক্ষম হয়েছিল, মূলত নীচের সারির কেশব মহারাজ এবং মাহীশ থিকশানার প্রতিরোধের জন্য।</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 3 109
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">33</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">উত্তেজনাপূর্ণ সাক্ষাৎ: বর্নমাউথ লিভারপুলের বিরুদ্ধে শ্বাসরুদ্ধকর লড়াই

# গতকাল বর্নমাউথ একটি কঠিন চ্যালেঞ্জের সম্মুখীন হয়েছিল, যেহেতু তারা লিভারপুলের কাছে ৩-০ গোলে পরাজিত হয়। লিভারপুল ম্যাচের শুরুতেই শক্তিশালীভাবে আক্রমণ শুরু করে এবং দ্রুত একটি গোল করে এগিয়ে যায়। তারা পরবর্তীতে আরও দুটি গোল যোগ করে। চেরিরা কিছু প্রাণবন্ত প্রচেষ্টা চালালেও, লিভারপুলের দৃঢ় প্রতিরক্ষা ভাঙতে তারা ব্যর্থ হয়। এটি ছিল একটি হতাশাজনক ফলাফল, কিন্তু দলটি আবারও শক্তি নিয়ে ফিরে আসার জন্য প্রস্তুতি নেবে! 💪⚽️

# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 3 148
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">34</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">গায়ানা অ্যামাজন ওয়ারিয়র্স বনাম সেন্ট কিটস অ্যান্ড নেভিস প্যাট্রিয়টস, ২১তম ম্যাচ হাইলাইটস | সিপিএল ২০২৪

# গায়ানা অ্যামাজন ওয়ারিয়র্স টানা দুটি হারের পর শেষ ম্যাচে জয় তুলে নিয়েছে। তারা সেন্ট কিটস অ্যান্ড নেভিস প্যাট্রিয়টসকে ৩০ রানে পরাজিত করেছে। শিমরন হেটমায়ার আবারও ওয়ারিয়র্সের হয়ে নায়ক হয়ে ওঠেন, ধীরগতির পিচে মাত্র ৩৩ বলে ৬৩ রানের বিধ্বংসী ইনিংস খেলেন। তিনি এখন দলের হয়ে সর্বোচ্চ রান সংগ্রাহক, ৬ ইনিংসে ২১৬ রান করেছেন প্রায় ১৯০ স্ট্রাইক রেটে। তবে, অলরাউন্ডার রোমারিও শেফার্ড শেষ দুই ম্যাচে নিচের দিকে নেমে গুরুত্বপূর্ণ ক্যামিও ইনিংস খেলেছেন। বোলিংয়ে, তাদের বেশ কিছু শক্তিশালী বিকল্প রয়েছে। গুডাকেশ মোটি ৬ ইনিংসে ১০ উইকেট নিয়ে শীর্ষস্থানে রয়েছেন এবং তার ইকোনমি রেট ৬.৮০। ওয়ারিয়র্সরা তাদের জয়ের ধারা অব্যাহত রাখবে।</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 3 176
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">35</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">আপনি কি চিনতে পেরেছেন 
# কে এই প্লেয়ার? 
# কমেন্ট করে আপনার উত্তর জানান।</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2 943
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">36</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">বর্নমাউথ চেলসির বিরুদ্ধে সাহসিকতার সাথে লড়াই করেছে! ⚽️💙

# এই উত্তেজনাপূর্ণ ম্যাচে আমাদের দল অসাধারণ দক্ষতা ও সংকল্প প্রদর্শন করেছে। যদিও চেলসি শেষ পর্যন্ত জয়লাভ করেছে, কিন্তু আমাদের খেলোয়াড়রা প্রতিটি মুহূর্তে প্রাণবন্ত ফুটবল খেলেছে। এবং এর চমৎকার পারফরম্যান্স আমাদের আশা জাগিয়েছে। গোল এবং রক্ষণাত্মক খেলা—প্রত্যেকটি পাল্টা আক্রমণ ছিল দারুণ!

# আপনাদের মতে ম্যাচের কোন মুহূর্তগুলো সবচেয়ে স্মরণীয় ছিল? মন্তব্যে জানাতে ভুলবেন না!


# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 3 080
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">37</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">বর্নমাউথ চেলসির বিরুদ্ধে সাহসিকতার সাথে লড়াই করেছে! ⚽️💙

# এই উত্তেজনাপূর্ণ ম্যাচে আমাদের দল অসাধারণ দক্ষতা ও সংকল্প প্রদর্শন করেছে। যদিও চেলসি শেষ পর্যন্ত জয়লাভ করেছে, কিন্তু আমাদের খেলোয়াড়রা প্রতিটি মুহূর্তে প্রাণবন্ত ফুটবল খেলেছে। এবং এর চমৎকার পারফরম্যান্স আমাদের আশা জাগিয়েছে। গোল এবং রক্ষণাত্মক খেলা—প্রত্যেকটি পাল্টা আক্রমণ ছিল দারুণ!

# আপনাদের মতে ম্যাচের কোন মুহূর্তগুলো সবচেয়ে স্মরণীয় ছিল? মন্তব্যে জানাতে ভুলবেন না!

# #Bj #Baji #Sports #BJSports #AFCBournemouth #MatchDay #Football #PremierLeague #Excitement

# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 12
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1 opacity-40">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 0
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">38</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">Place Baji-তে KM Power Ball-এর উত্তেজনা অনুভব করতে প্রস্তুত হোন, যেখানে প্রতিটি কার্ড আপনাকে বিশাল জয়ের কাছাকাছি নিয়ে আসে! আপনার বিঙ্গো কার্ডের উপরের প্যাটার্ন বা লাইনগুলিকে মেলাতে লক্ষ্য করুন এবং প্রতিটি বেটিং রাউন্ডের পরে সেগুলিকে বিশেষ সোনা, হীরা বা রেইনবো বোনাস কার্ডে রূপান্তরিত হতে দেখুন। আপনি যত বেশি খেলবেন, বিশাল পুরস্কার জেতার সম্ভাবনা তত বেশি হবে! মিস করবেন না।</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 3 248
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 2
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">39</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">আপনি কি চিনতে পেরেছেন
# কে এই প্লেয়ার?🤔
# কমেন্ট করে আপনার উত্তর জানান।


# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 1 950
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 9
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                     <tr class="border-b border-neutral5 last:border-b-0">
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <div class="flex items-center gap-4">
#                                                 <span class="text-xs font-medium text-neutral3">40</span>
#                                                 <div class="flex flex-col">
#                                                     <span class="short-text max-w-[210px] font-medium hover:cursor-pointer hover:text-text-accent">ত্রিনবাগো নাইট রাইডার্স বনাম অ্যান্টিগা ও বারবুডা ফ্যালকন্স, ২০তম ম্যাচের হাইলাইটস | CPL ২০২৪

# পোর্ট অফ স্পেনের একটি রোমাঞ্চকর ম্যাচে ত্রিনবাগো নাইট রাইডার্স অ্যান্টিগা ও বারবুডা ফ্যালকন্সের কাছে ছয় উইকেটে হেরে যায়, ফ্যালকন্স এক ওভার বাকি থাকতে টার্গেট তাড়া করে। এই জয়ে ফ্যালকন্সের অগ্রগতির আশা বেঁচে রইল এবং এ বছরের রিপাবলিক ব্যাংক CPL-এ নাইট রাইডার্সের বিরুদ্ধে তাদের দ্বিতীয় জয় নিশ্চিত হলো।


# 🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑
#  🛡এখনই Baji App ডাউনলোড  করুন!! ✅
  
# 📱 Facebook               📱 Twitter
# 📱 Instagram              📱 Threads
# 📱 Tiktok                     📱 Pinterest</span>
#                                                     <span class="min-h-[16px] text-xs font-medium text-neutral3"></span>
#                                                 </div>
#                                             </div>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-eye-line inline-flex leading-[0] text-neutral3"></i>
#                                                 4 075
#                                             </span>
#                                         </td>
#                                         <td class="px-4 py-4 first:pl-6 last:pr-6">
#                                             <span class="flex items-center gap-1">
#                                                 <i class="icon-arrow-repost-line inline-flex leading-[0] text-neutral3"></i>
#                                                 4
#                                             </span>
#                                         </td>
#                                         <td class="w-[237px] p-2 first:pl-6 last:pr-3">
#                                             <span class="w-max rounded bg-yang-gray-100 px-2 text-sm font-medium text-subtle">Loading...</span>
#                                         </td>
#                                     </tr>
#                                 </tbody>
#                             </table>
#                         </div>
#                         <div class="flex flex-1 flex-col gap-6">
#                             <div class="flex w-full flex-1 gap-6 flex-col">
#                                 <div class="w-full max-w-4xl @container/post">
#                                     <div class="rounded-lg space-y-4 border border-border-base-secondary p-6 shadow-sm">
#                                         <div class="flex items-center gap-2 border-b border-border-base-secondary pb-4">
#                                             <div class="grid flex-1">
#                                                 <div class="channel-name flex items-center channel-name_M ">
#                                                     <div class="channel-name__content">
#                                                         <div class="flex items-center channel-name__header">
#                                                             <span class="grid">
#                                                                 <a target="_blank" class="font-semibold cursor-pointer channel-name__title short-text text-text-base-primary first-letter:uppercase hover:text-text-accent" href="/en/channels/1829680439-baji_bgd">baji 🇧🇩</a>
#                                                             </span>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <div></div>
#                                                             </button>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <span class="inline-block flex-none channel-name__verified">
#                                                                     <img alt="black-icon" loading="lazy" width="14" height="14" decoding="async" data-nimg="1" style="color:transparent;width:100%;height:100%" src="/_next/static/media/black-label-blue.95fcfd40.svg"/>
#                                                                 </span>
#                                                             </button>
#                                                         </div>
#                                                         <div class="flex items-center channel-name__attributes"></div>
#                                                     </div>
#                                                 </div>
#                                             </div>
#                                             <span class="relative" data-state="closed">
#                                                 <button class="button button-border whitespace-nowrap button_secondary button_small button__icon-only outline-none h-9 w-9">
#                                                     <i class="icon-link-line inline-flex leading-[0] button__icon button__icon-only"></i>
#                                                 </button>
#                                             </span>
#                                         </div>
#                                         <div style="background:url(data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwC9KmYyOR06HFNtl8vcFzs7Driq0FxLPcojt8hzkAe1PuZZLaUBTlCMkGsuVl8yLo4qhfI886wnG08g+nrV0lAiOThTyDn2p21SuSq8dOKqKZLMK6jSIlPLCt2IYkH6UVo3UUcy7OAAPlx2orS5JWsmzcI45A60t66u55O4HH4VRgkMcinBIz09asGUi5WXGMntSa1KT0L6fPpkYccg8ZoGpQkhCD9aZcTl0x1wc1lkc5OetCEX3lCFmPc0VV3F8KO1FBLkkyASMFAB6e9L5rYPv7miinYLgbthkDIPqCajTfMQuScevaiikOTsi6ihFwKKKKZyNn//2Q==);background-size:cover;background-position:center;background-repeat:no-repeat" class="post-image relative flex aspect-square h-full max-w-[410px] items-center justify-center overflow-hidden rounded-lg bg-bg-base-tertiary bg-opacity-90">
#                                             <div class="absolute bottom-0 left-0 right-0 top-0 bg-[#F6F7F8] bg-opacity-80"></div>
#                                             <div class="z-[1] flex flex-col items-center gap-3">
#                                                 <i class="icon-image-line inline-flex leading-[0] text-6xl text-icon-base-secondary"></i>
#                                                 <span class="font-semibold text-text-base-tertiary">Photo unavailable</span>
#                                                 <a href="https://t.me/baji_bgd/1639" target="_blank" class="link inline-flex items-center text-sm font-medium" rel="nofollow noopener noreferrer">
#                                                     Show in Telegram<i class="icon-chevron-right-line inline-flex leading-[0] text-lg"></i>
#                                                 </a>
#                                             </div>
#                                         </div>
#                                         <div class="whitespace-pre-line break-words py-px text-sm text-text-base-primary line-clamp-5">
#                                             <div>শোয়েব আখতার, যিনি "রাওয়ালপিন্ডি এক্সপ্রেস" নামে পরিচিত, এবং ব্রেট লি, অস্ট্রেলিয়ার কিংবদন্তি ফাস্ট বোলার, তাদের অসাধারণ গতির জন্য বিখ্যাত। আখতার ২০০৩ সালের বিশ্বকাপে ১৬১.৩ কিমি/ঘণ্টা বেগে বল করে নজর কেড়েছিলেন, তার ক্যারিয়ারে ৪৪৪ ওডিআই এবং ১৭৮ টেস্ট উইকেট নিয়েছিলেন। অন্যদিকে, লি ১৬১.১ কিমি/ঘণ্টা বেগে বল করেন, এবং ৭০০টিরও বেশি আন্তর্জাতিক উইকেট সংগ্রহ করেন, দুটি বিশ্বকাপ জয়ে অস্ট্রেলিয়ার গুরুত্বপূর্ণ ভূমিকা পালন করেন, তার আক্রমণাত্মক বোলিং স্টাইল এবং সুইংয়ের জন্য স্বীকৃত।</div>
#                                         </div>
#                                         <span class="block w-full cursor-pointer text-center font-medium text-text-link-accent hover:text-text-link-accent-hover">Show all...</span>
#                                         <div class="flex flex-wrap gap-2"></div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="flex items-center gap-1 rounded-[14px] bg-bg-base-tertiary px-2 py-1 text-xs font-medium text-yang-gray-700">
#                                                 <span class="text-sm leading-none">👍</span>
#                                                 <!-- -->
#                                                 16
#                                             </span>
#                                             <span class="flex items-center gap-1 rounded-[14px] bg-bg-base-tertiary px-2 py-1 text-xs font-medium text-yang-gray-700">
#                                                 <span class="text-sm leading-none">❤</span>
#                                                 <!-- -->
#                                                 1
#                                             </span>
#                                             <span class="flex items-center gap-1 rounded-[14px] bg-bg-base-tertiary px-2 py-1 text-xs font-medium text-yang-gray-700">
#                                                 <span class="text-sm leading-none">😁</span>
#                                                 <!-- -->
#                                                 1
#                                             </span>
#                                         </div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="w-full gap-2 rounded border border-border-base-secondary px-3 py-1.5 text-center text-sm font-medium text-text-base-secondary">ব্রেট লি</span>
#                                         </div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="w-full gap-2 rounded border border-border-base-secondary px-3 py-1.5 text-center text-sm font-medium text-text-base-secondary">শোয়েব আখতার</span>
#                                         </div>
#                                         <div class="flex flex-col gap-1 border-t border-border-base-secondary pt-4">
#                                             <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-4">
#                                                 <a href="https://t.me/baji_bgd/1639" target="_blank" class="text-xs font-medium text-text-base-secondary" rel="nofollow noopener noreferrer"></a>
#                                                 <div class="hidden flex-1 items-baseline justify-end whitespace-nowrap @sm/post:flex">
#                                                     <p class="flex items-center gap-x-2 divide-x divide-border-base-secondary text-xs font-medium text-text-base-secondary">
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-eye-line inline-flex leading-[0] text-base"></i>
#                                                             1 216
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-arrow-repost-line inline-flex leading-[0] text-base"></i>
#                                                             3
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-message-square-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                     </p>
#                                                 </div>
#                                                 <button class="link-button link-button_secondary link-button_small">
#                                                     <span data-state="closed">Analytics</span>
#                                                     <i class="icon-chevron-right-line inline-flex leading-[0] link-button__icon"></i>
#                                                 </button>
#                                             </div>
#                                         </div>
#                                     </div>
#                                 </div>
#                                 <div class="w-full max-w-4xl @container/post">
#                                     <div class="rounded-lg space-y-4 border border-border-base-secondary p-6 shadow-sm">
#                                         <div class="flex items-center gap-2 border-b border-border-base-secondary pb-4">
#                                             <div class="grid flex-1">
#                                                 <div class="channel-name flex items-center channel-name_M ">
#                                                     <div class="channel-name__content">
#                                                         <div class="flex items-center channel-name__header">
#                                                             <span class="grid">
#                                                                 <a target="_blank" class="font-semibold cursor-pointer channel-name__title short-text text-text-base-primary first-letter:uppercase hover:text-text-accent" href="/en/channels/1829680439-baji_bgd">baji 🇧🇩</a>
#                                                             </span>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <div></div>
#                                                             </button>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <span class="inline-block flex-none channel-name__verified">
#                                                                     <img alt="black-icon" loading="lazy" width="14" height="14" decoding="async" data-nimg="1" style="color:transparent;width:100%;height:100%" src="/_next/static/media/black-label-blue.95fcfd40.svg"/>
#                                                                 </span>
#                                                             </button>
#                                                         </div>
#                                                         <div class="flex items-center channel-name__attributes"></div>
#                                                     </div>
#                                                 </div>
#                                             </div>
#                                             <span class="relative" data-state="closed">
#                                                 <button class="button button-border whitespace-nowrap button_secondary button_small button__icon-only outline-none h-9 w-9">
#                                                     <i class="icon-link-line inline-flex leading-[0] button__icon button__icon-only"></i>
#                                                 </button>
#                                             </span>
#                                         </div>
#                                         <div style="background:url(data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCoyED3oCkckZ9qe2SeDSkEDI60xDBuIOUGMdQMYqN0yPepVLs+0DBPWkcEHBGD3qUxtEcjRFDiPY31Joodc/WirJuSKQcEVZKDaD3NUI32sM52960N6tjZj1Gazm7FIECDk8NSHZuKkbiTzSPuzuIHHp3p4OMElQCKysU9SkeGIopDmSQ9RzmiuhGTaRGJHAwHIHpmnxTskgLEkd+aKKGroaZe8wFNyMdv1qLedw5P0oorKBUnaNwGQPvE/jRRRWpx8zP/2Q==);background-size:cover;background-position:center;background-repeat:no-repeat" class="post-image relative flex aspect-square h-full max-w-[410px] items-center justify-center overflow-hidden rounded-lg bg-bg-base-tertiary bg-opacity-90">
#                                             <div class="absolute bottom-0 left-0 right-0 top-0 bg-[#F6F7F8] bg-opacity-80"></div>
#                                             <div class="z-[1] flex flex-col items-center gap-3">
#                                                 <i class="icon-image-line inline-flex leading-[0] text-6xl text-icon-base-secondary"></i>
#                                                 <span class="font-semibold text-text-base-tertiary">Photo unavailable</span>
#                                                 <a href="https://t.me/baji_bgd/1638" target="_blank" class="link inline-flex items-center text-sm font-medium" rel="nofollow noopener noreferrer">
#                                                     Show in Telegram<i class="icon-chevron-right-line inline-flex leading-[0] text-lg"></i>
#                                                 </a>
#                                             </div>
#                                         </div>
#                                         <div class="whitespace-pre-line break-words py-px text-sm text-text-base-primary line-clamp-5">
#                                             <div>
#                                                 সিএসকে এমএস ধোনিকে ৪ কোটি টাকায় আনক্যাপড খেলোয়াড় হিসেবে ধরে রাখতে পারবে, কারণ আইপিএলের একটি পুনর্জীবিত নিয়ম ভারতীয় খেলোয়াড়দের, যারা পাঁচ বছর ধরে আন্তর্জাতিক ক্রিকেট থেকে অবসর নিয়েছে, আনক্যাপড হিসেবে শ্রেণীবদ্ধ করার অনুমতি দেয়। ৪৩ বছর বয়সী ধোনি ২০২০ সালে অবসর নিয়েছিলেন এবং শুধুমাত্র আইপিএল খেলেন। তিনি ২০২৪ সালে সিএসকের অধিনায়কত্ব রুতুরাজ গায়কওয়াদের হাতে তুলে দেন।


# ❤️
#                                                 <b>
#                                                     &nbsp;<i></i>
#                                                 </b>
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://baji.social/bj/tgndt" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Baji</i>
#                                                     </b>
#                                                 </a>
#                                                 <b>
#                                                     <i>সদস্য  </i>
#                                                 </b>
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://baji.social/bj/tgndt" class="text-primary break-all">
#                                                     <b>
#                                                         <i>হিসাবে সাইন-আপ</i>
#                                                     </b>
#                                                 </a>
#                                                 <b>
#                                                     <i>&nbsp;করুন </i>
#                                                 </b>
#                                                 <b>
#                                                     <i>🚀</i>
#                                                 </b>
#                                                 <b>
#                                                     <i></i>
#                                                 </b>
#                                                 <b>
#                                                     <i>🛡</i>
#                                                 </b>
#                                                 <b>
#                                                     <i>এখনই </i>
#                                                 </b>
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://bjbaji5.com/page/guest/appDownload.jsp" class="text-primary break-all">
#                                                     <i>Baji App</i>
#                                                 </a>
#                                                 <i>ডাউনলোড  করুন!!</i>
#                                                 ⬇️
#                                             </div>
#                                         </div>
#                                         <span class="block w-full cursor-pointer text-center font-medium text-text-link-accent hover:text-text-link-accent-hover">Show all...</span>
#                                         <div class="flex flex-wrap gap-2"></div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="flex items-center gap-1 rounded-[14px] bg-bg-base-tertiary px-2 py-1 text-xs font-medium text-yang-gray-700">
#                                                 <span class="text-sm leading-none">👍</span>
#                                                 <!-- -->
#                                                 11
#                                             </span>
#                                         </div>
#                                         <div class="flex flex-col gap-1 border-t border-border-base-secondary pt-4">
#                                             <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-4">
#                                                 <a href="https://t.me/baji_bgd/1638" target="_blank" class="text-xs font-medium text-text-base-secondary" rel="nofollow noopener noreferrer"></a>
#                                                 <div class="hidden flex-1 items-baseline justify-end whitespace-nowrap @sm/post:flex">
#                                                     <p class="flex items-center gap-x-2 divide-x divide-border-base-secondary text-xs font-medium text-text-base-secondary">
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-eye-line inline-flex leading-[0] text-base"></i>
#                                                             1 247
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-arrow-repost-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-message-square-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                     </p>
#                                                 </div>
#                                                 <button class="link-button link-button_secondary link-button_small">
#                                                     <span data-state="closed">Analytics</span>
#                                                     <i class="icon-chevron-right-line inline-flex leading-[0] link-button__icon"></i>
#                                                 </button>
#                                             </div>
#                                         </div>
#                                     </div>
#                                 </div>
#                                 <div class="w-full max-w-4xl @container/post">
#                                     <div class="rounded-lg space-y-4 border border-border-base-secondary p-6 shadow-sm">
#                                         <div class="flex items-center gap-2 border-b border-border-base-secondary pb-4">
#                                             <div class="grid flex-1">
#                                                 <div class="channel-name flex items-center channel-name_M ">
#                                                     <div class="channel-name__content">
#                                                         <div class="flex items-center channel-name__header">
#                                                             <span class="grid">
#                                                                 <a target="_blank" class="font-semibold cursor-pointer channel-name__title short-text text-text-base-primary first-letter:uppercase hover:text-text-accent" href="/en/channels/1829680439-baji_bgd">baji 🇧🇩</a>
#                                                             </span>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <div></div>
#                                                             </button>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <span class="inline-block flex-none channel-name__verified">
#                                                                     <img alt="black-icon" loading="lazy" width="14" height="14" decoding="async" data-nimg="1" style="color:transparent;width:100%;height:100%" src="/_next/static/media/black-label-blue.95fcfd40.svg"/>
#                                                                 </span>
#                                                             </button>
#                                                         </div>
#                                                         <div class="flex items-center channel-name__attributes"></div>
#                                                     </div>
#                                                 </div>
#                                             </div>
#                                             <span class="relative" data-state="closed">
#                                                 <button class="button button-border whitespace-nowrap button_secondary button_small button__icon-only outline-none h-9 w-9">
#                                                     <i class="icon-link-line inline-flex leading-[0] button__icon button__icon-only"></i>
#                                                 </button>
#                                             </span>
#                                         </div>
#                                         <div style="background:url(data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDLA54qUOFBHbNTeRs+fovrTP3YRl+X5Tw2OtS9TRaDQx2kdj3pskezGGB44xUjSAxFRimSSbolDMTyTj0pIbsDmPywAhV+Op60U2V97Z9qK0TuZNWFmuHkjVDwoqMMVBGeKKYwINKwXLOSLcAZAJ5BHQ0jqvkgj7wqAMdu3Jp3GBU2NFqh6oSPQGinvKuAq0UydBI5FRCCGOT2I/wp/nqcEhyR05H+FFFXZGdxjTL3EhB4PzD/AAqPdEVICPuPT5v/AK1FFTYq5Ygh2AM33v5UUUUjllJtn//Z);background-size:cover;background-position:center;background-repeat:no-repeat" class="post-image relative flex aspect-square h-full max-w-[410px] items-center justify-center overflow-hidden rounded-lg bg-bg-base-tertiary bg-opacity-90">
#                                             <div class="absolute bottom-0 left-0 right-0 top-0 bg-[#F6F7F8] bg-opacity-80"></div>
#                                             <div class="z-[1] flex flex-col items-center gap-3">
#                                                 <i class="icon-image-line inline-flex leading-[0] text-6xl text-icon-base-secondary"></i>
#                                                 <span class="font-semibold text-text-base-tertiary">Photo unavailable</span>
#                                                 <a href="https://t.me/baji_bgd/1637" target="_blank" class="link inline-flex items-center text-sm font-medium" rel="nofollow noopener noreferrer">
#                                                     Show in Telegram<i class="icon-chevron-right-line inline-flex leading-[0] text-lg"></i>
#                                                 </a>
#                                             </div>
#                                         </div>
#                                         <div class="whitespace-pre-line break-words py-px text-sm text-text-base-primary line-clamp-5">
#                                             <div>আপনি কি সেরা বেটিং অভিজ্ঞতা খুঁজছেন? আজই Baji-তে  যোগ দিন এবং নিজেকে স্পোর্টসের জগতে নিমজ্জিত করুন যা আগে কখনও হয়নি! লাইভ বেটিং অপশন এবং রিয়েল-টাইম আপডেট উপভোগ করুন যা আপনাকে খেলায় যুক্ত রাখবে। আমরা বিভিন্ন খেলা ও ইভেন্টে সর্বোত্তম অডস প্রদান করি, যা আপনার বেটের সর্বোচ্চ মূল্য নিশ্চিত করে। আজই সাইন আপ করুন এবং আপনার ভাগ্য আনলক করুন।</div>
#                                         </div>
#                                         <span class="block w-full cursor-pointer text-center font-medium text-text-link-accent hover:text-text-link-accent-hover">Show all...</span>
#                                         <div class="flex flex-wrap gap-2"></div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="flex items-center gap-1 rounded-[14px] bg-bg-base-tertiary px-2 py-1 text-xs font-medium text-yang-gray-700">
#                                                 <span class="text-sm leading-none">👍</span>
#                                                 <!-- -->
#                                                 1
#                                             </span>
#                                         </div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="w-full gap-2 rounded border border-border-base-secondary px-3 py-1.5 text-center text-sm font-medium text-text-base-secondary">❤️</span>
#                                         </div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="w-full gap-2 rounded border border-border-base-secondary px-3 py-1.5 text-center text-sm font-medium text-text-base-secondary">🔥</span>
#                                         </div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="w-full gap-2 rounded border border-border-base-secondary px-3 py-1.5 text-center text-sm font-medium text-text-base-secondary">এখনই আনলক করুন 🔒</span>
#                                         </div>
#                                         <div class="flex flex-col gap-1 border-t border-border-base-secondary pt-4">
#                                             <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-4">
#                                                 <a href="https://t.me/baji_bgd/1637" target="_blank" class="text-xs font-medium text-text-base-secondary" rel="nofollow noopener noreferrer"></a>
#                                                 <div class="hidden flex-1 items-baseline justify-end whitespace-nowrap @sm/post:flex">
#                                                     <p class="flex items-center gap-x-2 divide-x divide-border-base-secondary text-xs font-medium text-text-base-secondary">
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-eye-line inline-flex leading-[0] text-base"></i>
#                                                             1 295
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-arrow-repost-line inline-flex leading-[0] text-base"></i>
#                                                             1
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-message-square-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                     </p>
#                                                 </div>
#                                                 <button class="link-button link-button_secondary link-button_small">
#                                                     <span data-state="closed">Analytics</span>
#                                                     <i class="icon-chevron-right-line inline-flex leading-[0] link-button__icon"></i>
#                                                 </button>
#                                             </div>
#                                         </div>
#                                     </div>
#                                 </div>
#                                 <div class="w-full max-w-4xl @container/post">
#                                     <div class="rounded-lg space-y-4 border border-border-base-secondary p-6 shadow-sm">
#                                         <div class="flex items-center gap-2 border-b border-border-base-secondary pb-4">
#                                             <div class="grid flex-1">
#                                                 <div class="channel-name flex items-center channel-name_M ">
#                                                     <div class="channel-name__content">
#                                                         <div class="flex items-center channel-name__header">
#                                                             <span class="grid">
#                                                                 <a target="_blank" class="font-semibold cursor-pointer channel-name__title short-text text-text-base-primary first-letter:uppercase hover:text-text-accent" href="/en/channels/1829680439-baji_bgd">baji 🇧🇩</a>
#                                                             </span>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <div></div>
#                                                             </button>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <span class="inline-block flex-none channel-name__verified">
#                                                                     <img alt="black-icon" loading="lazy" width="14" height="14" decoding="async" data-nimg="1" style="color:transparent;width:100%;height:100%" src="/_next/static/media/black-label-blue.95fcfd40.svg"/>
#                                                                 </span>
#                                                             </button>
#                                                         </div>
#                                                         <div class="flex items-center channel-name__attributes"></div>
#                                                     </div>
#                                                 </div>
#                                             </div>
#                                             <span class="relative" data-state="closed">
#                                                 <button class="button button-border whitespace-nowrap button_secondary button_small button__icon-only outline-none h-9 w-9">
#                                                     <i class="icon-link-line inline-flex leading-[0] button__icon button__icon-only"></i>
#                                                 </button>
#                                             </span>
#                                         </div>
#                                         <div style="background:url(data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoABYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDNjAYgDrUs0S+WG2FexOaBabed9OaEEdh7jP8AjSuSU2AzxRVkWuRnePxFFF0M0AE9qaNhDYChvrVGIyNgi4VT6HOR+lSouyNiro2OpC1LVhq1y3+79RRQiRvCrbFyevy0VOgm4p2ZkLI2QAxH44qeOUrneQcjH3hRRWlkFiRL5I0AVST3NFFFLlQ3Hmd2f//Z);background-size:cover;background-position:center;background-repeat:no-repeat" class="post-image relative flex aspect-square h-full max-w-[410px] items-center justify-center overflow-hidden rounded-lg bg-bg-base-tertiary bg-opacity-90">
#                                             <div class="absolute bottom-0 left-0 right-0 top-0 bg-[#F6F7F8] bg-opacity-80"></div>
#                                             <div class="absolute right-2.5 top-2.5 rounded bg-[#F6F7F8] px-1.5 py-1 text-xs text-text-base-secondary">02:59</div>
#                                             <div class="z-[1] flex flex-col items-center gap-3">
#                                                 <i class="icon-play-line inline-flex leading-[0] text-6xl text-icon-base-secondary"></i>
#                                                 <span class="font-semibold text-text-base-tertiary">Video unavailable</span>
#                                                 <a href="https://t.me/baji_bgd/1636" target="_blank" class="link inline-flex items-center text-sm font-medium" rel="nofollow noopener noreferrer">
#                                                     Show in Telegram<i class="icon-chevron-right-line inline-flex leading-[0] text-lg"></i>
#                                                 </a>
#                                             </div>
#                                         </div>
#                                         <div class="whitespace-pre-line break-words py-px text-sm text-text-base-primary line-clamp-5">
#                                             <div>
#                                                 ত্রিনবাগো নাইট রাইডার্স বনাম বার্বাডোজ রয়্যালস, ২৮তম ম্যাচের হাইলাইটস | ক্যারিবিয়ান প্রিমিয়ার লিগ ২০২৪

# ২০২৪ রিপাবলিক ব্যাংক ক্যারিবিয়ান প্রিমিয়ার লিগ (CPL) প্রতিযোগিতার শেষ সপ্তাহের দিকে বার্বাডোস রয়্যালসের জন্য আরেকটি হতাশাজনক রাত ছিল । যারা সহ শিরোপা প্রত্যাশী ত্রিনবাগো নাইট রাইডার্সের হাতে টানা চতুর্থ পরাজয়ের শিকার হয়েছিল। প্রতিযোগিতার শুরুতে পরাজিত দল হওয়া সত্ত্বেও রয়্যালস চূড়ান্ত বাছাইপর্বে চতুর্থ স্থানে ছিল।


# <b></b>
#                                                 <b>❤️</b>
#                                                 <b>
#                                                     &nbsp;<i></i>
#                                                 </b>
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://baji.social/bj/tgndt" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Baji</i>
#                                                     </b>
#                                                 </a>
#                                                 <b>
#                                                     <i>সদস্য  </i>
#                                                 </b>
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://baji.social/bj/tgndt" class="text-primary break-all">
#                                                     <b>
#                                                         <i>হিসাবে সাইন-আপ</i>
#                                                     </b>
#                                                 </a>
#                                                 <b>
#                                                     <i>&nbsp;করুন </i>
#                                                 </b>
#                                                 <b>
#                                                     <i>🚀</i>
#                                                 </b>
#                                                 <b>
#                                                     <i></i>
#                                                 </b>
#                                                 <b>
#                                                     <i>🛡</i>
#                                                 </b>
#                                                 <b>
#                                                     <i>এখনই </i>
#                                                 </b>
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://bjbaji5.com/page/guest/appDownload.jsp" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Baji App</i>
#                                                     </b>
#                                                 </a>
#                                                 <b>
#                                                     <i>ডাউনলোড  করুন!!</i>
#                                                 </b>
#                                                 <b>⬇️</b>
#                                             </div>
#                                         </div>
#                                         <span class="block w-full cursor-pointer text-center font-medium text-text-link-accent hover:text-text-link-accent-hover">Show all...</span>
#                                         <div class="flex flex-wrap gap-2">
#                                             <div class="flex w-full gap-x-2">
#                                                 <div class="flex min-h-[50px] min-w-[50px] items-center justify-center rounded-full bg-bg-base-secondary text-icon-base-primary-disabled">
#                                                     <i class="icon-file-line inline-flex leading-[0] text-3xl"></i>
#                                                 </div>
#                                                 <div class="flex w-[calc(100%-58px)] flex-1 flex-col justify-center">
#                                                     <span class="truncate break-all text-sm font-medium text-text-base-secondary">Video290924 (BJbdt).mp4</span>
#                                                     <span class="text-xs font-medium text-text-base-primary-disabled">128.55 MB</span>
#                                                 </div>
#                                             </div>
#                                         </div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="flex items-center gap-1 rounded-[14px] bg-bg-base-tertiary px-2 py-1 text-xs font-medium text-yang-gray-700">
#                                                 <span class="text-sm leading-none">❤</span>
#                                                 <!-- -->
#                                                 6
#                                             </span>
#                                         </div>
#                                         <div class="flex flex-col gap-1 border-t border-border-base-secondary pt-4">
#                                             <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-4">
#                                                 <a href="https://t.me/baji_bgd/1636" target="_blank" class="text-xs font-medium text-text-base-secondary" rel="nofollow noopener noreferrer"></a>
#                                                 <div class="hidden flex-1 items-baseline justify-end whitespace-nowrap @sm/post:flex">
#                                                     <p class="flex items-center gap-x-2 divide-x divide-border-base-secondary text-xs font-medium text-text-base-secondary">
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-eye-line inline-flex leading-[0] text-base"></i>
#                                                             1 250
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-arrow-repost-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-message-square-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                     </p>
#                                                 </div>
#                                                 <button class="link-button link-button_secondary link-button_small">
#                                                     <span data-state="closed">Analytics</span>
#                                                     <i class="icon-chevron-right-line inline-flex leading-[0] link-button__icon"></i>
#                                                 </button>
#                                             </div>
#                                         </div>
#                                     </div>
#                                 </div>
#                                 <div class="w-full max-w-4xl @container/post">
#                                     <div class="rounded-lg space-y-4 border border-border-base-secondary p-6 shadow-sm">
#                                         <div class="flex items-center gap-2 border-b border-border-base-secondary pb-4">
#                                             <div class="grid flex-1">
#                                                 <div class="channel-name flex items-center channel-name_M ">
#                                                     <div class="channel-name__content">
#                                                         <div class="flex items-center channel-name__header">
#                                                             <span class="grid">
#                                                                 <a target="_blank" class="font-semibold cursor-pointer channel-name__title short-text text-text-base-primary first-letter:uppercase hover:text-text-accent" href="/en/channels/1829680439-baji_bgd">baji 🇧🇩</a>
#                                                             </span>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <div></div>
#                                                             </button>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <span class="inline-block flex-none channel-name__verified">
#                                                                     <img alt="black-icon" loading="lazy" width="14" height="14" decoding="async" data-nimg="1" style="color:transparent;width:100%;height:100%" src="/_next/static/media/black-label-blue.95fcfd40.svg"/>
#                                                                 </span>
#                                                             </button>
#                                                         </div>
#                                                         <div class="flex items-center channel-name__attributes"></div>
#                                                     </div>
#                                                 </div>
#                                             </div>
#                                             <span class="relative" data-state="closed">
#                                                 <button class="button button-border whitespace-nowrap button_secondary button_small button__icon-only outline-none h-9 w-9">
#                                                     <i class="icon-link-line inline-flex leading-[0] button__icon button__icon-only"></i>
#                                                 </button>
#                                             </span>
#                                         </div>
#                                         <div style="background:url(data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCrLLn5V6etRgEkAck0lSW5AnQtwM1025VoVGKirIVoXhYGZMKfQ80TxL1QHHT6VPdnPljMjBh8ufXNKYn5Xbzjk9q51N31Gyk/l7MBCHGM89aKkmiwSO9FXyX1RDRCGqaIoHUuT16VAFJGRj86kJIHzqDj3p87sNMuXEYeQSq4AH6UgugR0LY5PbiqTTFhgcD0zS+dtXAHb161Cih3J5H82Qv2NFQedk5wB7Cit4ySVhphG6BCHBznsB/WntNGcDDY9Nq/4UUVgZjGkiHIVs/Rf8Ka8kLbRhwAOwAoopDInK7vkzj3oooouB//2Q==);background-size:cover;background-position:center;background-repeat:no-repeat" class="post-image relative flex aspect-square h-full max-w-[410px] items-center justify-center overflow-hidden rounded-lg bg-bg-base-tertiary bg-opacity-90">
#                                             <div class="absolute bottom-0 left-0 right-0 top-0 bg-[#F6F7F8] bg-opacity-80"></div>
#                                             <div class="z-[1] flex flex-col items-center gap-3">
#                                                 <i class="icon-image-line inline-flex leading-[0] text-6xl text-icon-base-secondary"></i>
#                                                 <span class="font-semibold text-text-base-tertiary">Photo unavailable</span>
#                                                 <a href="https://t.me/baji_bgd/1635" target="_blank" class="link inline-flex items-center text-sm font-medium" rel="nofollow noopener noreferrer">
#                                                     Show in Telegram<i class="icon-chevron-right-line inline-flex leading-[0] text-lg"></i>
#                                                 </a>
#                                             </div>
#                                         </div>
#                                         <div class="whitespace-pre-line break-words py-px text-sm text-text-base-primary line-clamp-5">
#                                             <div>অবসর গ্রহণের পর, ব্রাভো আইপিএল ২০২৫-এর জন্য কেকেআরের মেন্টর হিসেবে দায়িত্ব নেবেন।

# ডোয়েন ব্রাভো অবসর নিয়েছেন এবং ২০২৫ সাল থেকে কলকাতা নাইট রাইডার্স (KKR)-এর মেন্টর হিসেবে যোগ দিয়েছেন, তিনি নাইট রাইডার্সের সব ফ্র্যাঞ্চাইজি পর্যবেক্ষণ করবেন। তিনি চেন্নাই সুপার কিংস (CSK) এর সাবেক কোচ এবং খেলোয়াড়। ব্রাভো পরামর্শক কোচ হিসাবে আফগানিস্তানকে ২০২৪ টি-টোয়েন্টি বিশ্বকাপের সেমিফাইনালে পৌঁছাতে সাহায্য করেছিলেন।</div>
#                                         </div>
#                                         <span class="block w-full cursor-pointer text-center font-medium text-text-link-accent hover:text-text-link-accent-hover">Show all...</span>
#                                         <div class="flex flex-wrap gap-2"></div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="flex items-center gap-1 rounded-[14px] bg-bg-base-tertiary px-2 py-1 text-xs font-medium text-yang-gray-700">
#                                                 <span class="text-sm leading-none">👍</span>
#                                                 <!-- -->
#                                                 17
#                                             </span>
#                                             <span class="flex items-center gap-1 rounded-[14px] bg-bg-base-tertiary px-2 py-1 text-xs font-medium text-yang-gray-700">
#                                                 <span class="text-sm leading-none">🔥</span>
#                                                 <!-- -->
#                                                 1
#                                             </span>
#                                         </div>
#                                         <div class="flex flex-col gap-1 border-t border-border-base-secondary pt-4">
#                                             <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-4">
#                                                 <a href="https://t.me/baji_bgd/1635" target="_blank" class="text-xs font-medium text-text-base-secondary" rel="nofollow noopener noreferrer"></a>
#                                                 <div class="hidden flex-1 items-baseline justify-end whitespace-nowrap @sm/post:flex">
#                                                     <p class="flex items-center gap-x-2 divide-x divide-border-base-secondary text-xs font-medium text-text-base-secondary">
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-eye-line inline-flex leading-[0] text-base"></i>
#                                                             1 787
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-arrow-repost-line inline-flex leading-[0] text-base"></i>
#                                                             4
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-message-square-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                     </p>
#                                                 </div>
#                                                 <button class="link-button link-button_secondary link-button_small">
#                                                     <span data-state="closed">Analytics</span>
#                                                     <i class="icon-chevron-right-line inline-flex leading-[0] link-button__icon"></i>
#                                                 </button>
#                                             </div>
#                                         </div>
#                                     </div>
#                                 </div>
#                                 <div class="w-full max-w-4xl @container/post">
#                                     <div class="rounded-lg space-y-4 border border-border-base-secondary p-6 shadow-sm">
#                                         <div class="flex items-center gap-2 border-b border-border-base-secondary pb-4">
#                                             <div class="grid flex-1">
#                                                 <div class="channel-name flex items-center channel-name_M ">
#                                                     <div class="channel-name__content">
#                                                         <div class="flex items-center channel-name__header">
#                                                             <span class="grid">
#                                                                 <a target="_blank" class="font-semibold cursor-pointer channel-name__title short-text text-text-base-primary first-letter:uppercase hover:text-text-accent" href="/en/channels/1829680439-baji_bgd">baji 🇧🇩</a>
#                                                             </span>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <div></div>
#                                                             </button>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <span class="inline-block flex-none channel-name__verified">
#                                                                     <img alt="black-icon" loading="lazy" width="14" height="14" decoding="async" data-nimg="1" style="color:transparent;width:100%;height:100%" src="/_next/static/media/black-label-blue.95fcfd40.svg"/>
#                                                                 </span>
#                                                             </button>
#                                                         </div>
#                                                         <div class="flex items-center channel-name__attributes"></div>
#                                                     </div>
#                                                 </div>
#                                             </div>
#                                             <span class="relative" data-state="closed">
#                                                 <button class="button button-border whitespace-nowrap button_secondary button_small button__icon-only outline-none h-9 w-9">
#                                                     <i class="icon-link-line inline-flex leading-[0] button__icon button__icon-only"></i>
#                                                 </button>
#                                             </span>
#                                         </div>
#                                         <div style="background:url(data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoABYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDNjAYgDrUs0S+WG2FexOaUWZBzupzQDb2Hvz/jSuKxSYDNFWhZn+9+lFF0M0CeO/5U3zFI7CqUTzMMi52nuCT/AIVLDGCDgrIfUdvzpbbhcsblI60UqRo0KkhWJ/iA60VDkDaW7MhZGyAGI/HFWIZjGSWIJxj7wNFFaWQnFMdHfiNQAKKKKOVC5Ef/2Q==);background-size:cover;background-position:center;background-repeat:no-repeat" class="post-image relative flex aspect-square h-full max-w-[410px] items-center justify-center overflow-hidden rounded-lg bg-bg-base-tertiary bg-opacity-90">
#                                             <div class="absolute bottom-0 left-0 right-0 top-0 bg-[#F6F7F8] bg-opacity-80"></div>
#                                             <div class="absolute right-2.5 top-2.5 rounded bg-[#F6F7F8] px-1.5 py-1 text-xs text-text-base-secondary">02:57</div>
#                                             <div class="z-[1] flex flex-col items-center gap-3">
#                                                 <i class="icon-play-line inline-flex leading-[0] text-6xl text-icon-base-secondary"></i>
#                                                 <span class="font-semibold text-text-base-tertiary">Video unavailable</span>
#                                                 <a href="https://t.me/baji_bgd/1634" target="_blank" class="link inline-flex items-center text-sm font-medium" rel="nofollow noopener noreferrer">
#                                                     Show in Telegram<i class="icon-chevron-right-line inline-flex leading-[0] text-lg"></i>
#                                                 </a>
#                                             </div>
#                                         </div>
#                                         <div class="whitespace-pre-line break-words py-px text-sm text-text-base-primary line-clamp-5">
#                                             <div>গায়ানা আমাজন ওয়ারিয়র্স বনাম বার্বাডোজ রয়্যালস, ২৭ তম ম্যাচের হাইলাইটস | ক্যারিবিয়ান প্রিমিয়ার লিগ ২০২৪

# গায়ানা অ্যামাজন ওয়ারিয়র্স বার্বাডোজ রয়্যালসকে ৪৭ রানে পরাজিত করে। ফলে ২০২৪ রিপাবলিক ব্যাঙ্ক ক্যারিবিয়ান প্রিমিয়ার লিগের CPL পয়েন্ট টেবিলে শীর্ষ দুয়ে থাকার সম্ভাবনা রয়েছে। রয়্যালস, তাদের পূর্ববর্তী ফর্মের কারণে টেবিলের শীর্ষে উঠার আশায় ছিল, তবে সাম্প্রতিক ম্যাচে তৃতীয় পরাজয়ের ফলে তাদের তৃতীয় বা চতুর্থ স্থানে স্থির থাকতে হবে। ম্যাচের অধিনায়ক রোভম্যান পাওয়েল টসে জয়ী হয়ে প্রতিপক্ষকে ব্যাটিং করতে পাঠান। গুরবাজ দ্রুত আউট হলেও ওয়ারিয়র্স ২০ ওভারে ২১৯/৮ রান করতে সক্ষম হয়।</div>
#                                         </div>
#                                         <span class="block w-full cursor-pointer text-center font-medium text-text-link-accent hover:text-text-link-accent-hover">Show all...</span>
#                                         <div class="flex flex-wrap gap-2">
#                                             <div class="flex w-full gap-x-2">
#                                                 <div class="flex min-h-[50px] min-w-[50px] items-center justify-center rounded-full bg-bg-base-secondary text-icon-base-primary-disabled">
#                                                     <i class="icon-file-line inline-flex leading-[0] text-3xl"></i>
#                                                 </div>
#                                                 <div class="flex w-[calc(100%-58px)] flex-1 flex-col justify-center">
#                                                     <span class="truncate break-all text-sm font-medium text-text-base-secondary">Video280924 (BJbdt).mp4</span>
#                                                     <span class="text-xs font-medium text-text-base-primary-disabled">128.33 MB</span>
#                                                 </div>
#                                             </div>
#                                         </div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="flex items-center gap-1 rounded-[14px] bg-bg-base-tertiary px-2 py-1 text-xs font-medium text-yang-gray-700">
#                                                 <span class="text-sm leading-none">👍</span>
#                                                 <!-- -->
#                                                 10
#                                             </span>
#                                             <span class="flex items-center gap-1 rounded-[14px] bg-bg-base-tertiary px-2 py-1 text-xs font-medium text-yang-gray-700">
#                                                 <span class="text-sm leading-none">❤</span>
#                                                 <!-- -->
#                                                 1
#                                             </span>
#                                         </div>
#                                         <div class="flex flex-col gap-1 border-t border-border-base-secondary pt-4">
#                                             <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-4">
#                                                 <a href="https://t.me/baji_bgd/1634" target="_blank" class="text-xs font-medium text-text-base-secondary" rel="nofollow noopener noreferrer"></a>
#                                                 <div class="hidden flex-1 items-baseline justify-end whitespace-nowrap @sm/post:flex">
#                                                     <p class="flex items-center gap-x-2 divide-x divide-border-base-secondary text-xs font-medium text-text-base-secondary">
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-eye-line inline-flex leading-[0] text-base"></i>
#                                                             1 642
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-arrow-repost-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-message-square-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                     </p>
#                                                 </div>
#                                                 <button class="link-button link-button_secondary link-button_small">
#                                                     <span data-state="closed">Analytics</span>
#                                                     <i class="icon-chevron-right-line inline-flex leading-[0] link-button__icon"></i>
#                                                 </button>
#                                             </div>
#                                         </div>
#                                     </div>
#                                 </div>
#                                 <div class="w-full max-w-4xl @container/post">
#                                     <div class="rounded-lg space-y-4 border border-border-base-secondary p-6 shadow-sm">
#                                         <div class="flex items-center gap-2 border-b border-border-base-secondary pb-4">
#                                             <div class="grid flex-1">
#                                                 <div class="channel-name flex items-center channel-name_M ">
#                                                     <div class="channel-name__content">
#                                                         <div class="flex items-center channel-name__header">
#                                                             <span class="grid">
#                                                                 <a target="_blank" class="font-semibold cursor-pointer channel-name__title short-text text-text-base-primary first-letter:uppercase hover:text-text-accent" href="/en/channels/1829680439-baji_bgd">baji 🇧🇩</a>
#                                                             </span>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <div></div>
#                                                             </button>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <span class="inline-block flex-none channel-name__verified">
#                                                                     <img alt="black-icon" loading="lazy" width="14" height="14" decoding="async" data-nimg="1" style="color:transparent;width:100%;height:100%" src="/_next/static/media/black-label-blue.95fcfd40.svg"/>
#                                                                 </span>
#                                                             </button>
#                                                         </div>
#                                                         <div class="flex items-center channel-name__attributes"></div>
#                                                     </div>
#                                                 </div>
#                                             </div>
#                                             <span class="relative" data-state="closed">
#                                                 <button class="button button-border whitespace-nowrap button_secondary button_small button__icon-only outline-none h-9 w-9">
#                                                     <i class="icon-link-line inline-flex leading-[0] button__icon button__icon-only"></i>
#                                                 </button>
#                                             </span>
#                                         </div>
#                                         <div style="background:url(data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwClM5f5V+7/ADpsduzkYHWpkjyQK0II8EKnQfePrW/KkrmHNbRGYbNx2/UVE0TIcEEGti6CEEd6qzlEULK3UcHrinZPcpNlNjGYxhSH4zz1opGCkZU5FFZNWLuWIpBkHNW4LlVzz2rLVXxuUHHrin7JQfuPz/smtFJNambgXXuVbI5yeMVXuZwRs25wBzUBEyrlgQBxkqaTeP73Si6Y+UQHCYxjmimM2TRWbaLsTxMgUh2Iz225/rSkxHHznPQ/Kf8AGiipaGMdkEZw+T/dIP8AjUDNuPQD6UUUhjaKKKAP/9k=);background-size:cover;background-position:center;background-repeat:no-repeat" class="post-image relative flex aspect-square h-full max-w-[410px] items-center justify-center overflow-hidden rounded-lg bg-bg-base-tertiary bg-opacity-90">
#                                             <div class="absolute bottom-0 left-0 right-0 top-0 bg-[#F6F7F8] bg-opacity-80"></div>
#                                             <div class="z-[1] flex flex-col items-center gap-3">
#                                                 <i class="icon-image-line inline-flex leading-[0] text-6xl text-icon-base-secondary"></i>
#                                                 <span class="font-semibold text-text-base-tertiary">Photo unavailable</span>
#                                                 <a href="https://t.me/baji_bgd/1633" target="_blank" class="link inline-flex items-center text-sm font-medium" rel="nofollow noopener noreferrer">
#                                                     Show in Telegram<i class="icon-chevron-right-line inline-flex leading-[0] text-lg"></i>
#                                                 </a>
#                                             </div>
#                                         </div>
#                                         <div class="whitespace-pre-line break-words py-px text-sm text-text-base-primary line-clamp-5">
#                                             <div>🔒 baji  প্রিমিয়াম ডিপোজিট সিস্টেম উন্নত এনক্রিপশনের সাথে সর্বাধিক নিরাপত্তা, সহজ ব্যবহার এবং নিরাপদ লেনদেন নিশ্চিত করে 🔐

# 💵 সহজ ডিপোজিট  এবং দ্রুত উত্তোলন এবং চিন্তামুক্ত গেমিং অভিজ্ঞতার জন্য তৈরি করে।

# 🔒 baji তে অত্যাধুনিক ডিপোজিট সিস্টেম এনক্রিপশন প্রযুক্তি সহ শীর্ষ-স্তরের নিরাপত্তা প্রদান করে 🔐

# প্রতিটি লেনদেনে অতুলনীয় নিরাপত্তা এবং সুবিধার জন্য baji কে  বিশ্বাস করুন 🔓।

# স্ট্রেস-মুক্ত, নিরাপদ অ্যাডভেঞ্চারের জন্য এখনই baji তে যোগ দিন।</div>
#                                         </div>
#                                         <span class="block w-full cursor-pointer text-center font-medium text-text-link-accent hover:text-text-link-accent-hover">Show all...</span>
#                                         <div class="flex flex-wrap gap-2"></div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="flex items-center gap-1 rounded-[14px] bg-bg-base-tertiary px-2 py-1 text-xs font-medium text-yang-gray-700">
#                                                 <span class="text-sm leading-none">👍</span>
#                                                 <!-- -->
#                                                 8
#                                             </span>
#                                             <span class="flex items-center gap-1 rounded-[14px] bg-bg-base-tertiary px-2 py-1 text-xs font-medium text-yang-gray-700">
#                                                 <span class="text-sm leading-none">❤</span>
#                                                 <!-- -->
#                                                 3
#                                             </span>
#                                         </div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="w-full gap-2 rounded border border-border-base-secondary px-3 py-1.5 text-center text-sm font-medium text-text-base-secondary">❤️</span>
#                                         </div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="w-full gap-2 rounded border border-border-base-secondary px-3 py-1.5 text-center text-sm font-medium text-text-base-secondary">🔥</span>
#                                         </div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="w-full gap-2 rounded border border-border-base-secondary px-3 py-1.5 text-center text-sm font-medium text-text-base-secondary">🤩</span>
#                                         </div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="w-full gap-2 rounded border border-border-base-secondary px-3 py-1.5 text-center text-sm font-medium text-text-base-secondary">এখনি যোগ দিন</span>
#                                         </div>
#                                         <div class="flex flex-col gap-1 border-t border-border-base-secondary pt-4">
#                                             <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-4">
#                                                 <a href="https://t.me/baji_bgd/1633" target="_blank" class="text-xs font-medium text-text-base-secondary" rel="nofollow noopener noreferrer"></a>
#                                                 <div class="hidden flex-1 items-baseline justify-end whitespace-nowrap @sm/post:flex">
#                                                     <p class="flex items-center gap-x-2 divide-x divide-border-base-secondary text-xs font-medium text-text-base-secondary">
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-eye-line inline-flex leading-[0] text-base"></i>
#                                                             1 578
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-arrow-repost-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-message-square-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                     </p>
#                                                 </div>
#                                                 <button class="link-button link-button_secondary link-button_small">
#                                                     <span data-state="closed">Analytics</span>
#                                                     <i class="icon-chevron-right-line inline-flex leading-[0] link-button__icon"></i>
#                                                 </button>
#                                             </div>
#                                         </div>
#                                     </div>
#                                 </div>
#                                 <div class="w-full max-w-4xl @container/post">
#                                     <div class="rounded-lg space-y-4 border border-border-base-secondary p-6 shadow-sm">
#                                         <div class="flex items-center gap-2 border-b border-border-base-secondary pb-4">
#                                             <div class="grid flex-1">
#                                                 <div class="channel-name flex items-center channel-name_M ">
#                                                     <div class="channel-name__content">
#                                                         <div class="flex items-center channel-name__header">
#                                                             <span class="grid">
#                                                                 <a target="_blank" class="font-semibold cursor-pointer channel-name__title short-text text-text-base-primary first-letter:uppercase hover:text-text-accent" href="/en/channels/1829680439-baji_bgd">baji 🇧🇩</a>
#                                                             </span>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <div></div>
#                                                             </button>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <span class="inline-block flex-none channel-name__verified">
#                                                                     <img alt="black-icon" loading="lazy" width="14" height="14" decoding="async" data-nimg="1" style="color:transparent;width:100%;height:100%" src="/_next/static/media/black-label-blue.95fcfd40.svg"/>
#                                                                 </span>
#                                                             </button>
#                                                         </div>
#                                                         <div class="flex items-center channel-name__attributes"></div>
#                                                     </div>
#                                                 </div>
#                                             </div>
#                                             <span class="relative" data-state="closed">
#                                                 <button class="button button-border whitespace-nowrap button_secondary button_small button__icon-only outline-none h-9 w-9">
#                                                     <i class="icon-link-line inline-flex leading-[0] button__icon button__icon-only"></i>
#                                                 </button>
#                                             </span>
#                                         </div>
#                                         <div style="background:url(data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwClM5f5V+7/ADpsduzkYHWpkjyQK0II8EKnQfePrW/KkrmHNbRGYbNx2/UVE0TIcEEGti6CEEd6qzlEULK3UcHrinZPcpNlNjGYxhSH4zz1opGCkZU5FFZNWLuWIpBkHNW4LlVzz2rLVXxuUHHrin7JQfuPz/smtFJNambgXXuVbI5yeMVXuZwRs25wBzUBEyrlgQBxkqaTeP73Si6Y+UQHCYxjmimM2TRWbaLsTxMgUh2Iz225/rSkxHHznPQ/Kf8AGiipaGMdkEZw+T/dIP8AjUDNuPQD6UUUhjaKKKAP/9k=);background-size:cover;background-position:center;background-repeat:no-repeat" class="post-image relative flex aspect-square h-full max-w-[410px] items-center justify-center overflow-hidden rounded-lg bg-bg-base-tertiary bg-opacity-90">
#                                             <div class="absolute bottom-0 left-0 right-0 top-0 bg-[#F6F7F8] bg-opacity-80"></div>
#                                             <div class="z-[1] flex flex-col items-center gap-3">
#                                                 <i class="icon-image-line inline-flex leading-[0] text-6xl text-icon-base-secondary"></i>
#                                                 <span class="font-semibold text-text-base-tertiary">Photo unavailable</span>
#                                                 <a href="https://t.me/baji_bgd/1632" target="_blank" class="link inline-flex items-center text-sm font-medium" rel="nofollow noopener noreferrer">
#                                                     Show in Telegram<i class="icon-chevron-right-line inline-flex leading-[0] text-lg"></i>
#                                                 </a>
#                                             </div>
#                                         </div>
#                                         <div class="whitespace-pre-line break-words py-px text-sm text-text-base-primary line-clamp-5">
#                                             <div>🔒 baji  প্রিমিয়াম ডিপোজিট সিস্টেম উন্নত এনক্রিপশনের সাথে সর্বাধিক নিরাপত্তা, সহজ ব্যবহার এবং নিরাপদ লেনদেন নিশ্চিত করে 🔐...
# 💵 সহজ ডিপোজিট  এবং দ্রুত উত্তোলন এবং চিন্তামুক্ত গেমিং অভিজ্ঞতার জন্য তৈরি করে।

# 🔒 baji তে অত্যাধুনিক ডিপোজিট সিস্টেম এনক্রিপশন প্রযুক্তি সহ শীর্ষ-স্তরের নিরাপত্তা প্রদান করে 🔐

# প্রতিটি লেনদেনে অতুলনীয় নিরাপত্তা এবং সুবিধার জন্য baji কে  বিশ্বাস করুন 🔓।

# স্ট্রেস-মুক্ত, নিরাপদ অ্যাডভেঞ্চারের জন্য এখনই baji তে যোগ দিন।</div>
#                                         </div>
#                                         <span class="block w-full cursor-pointer text-center font-medium text-text-link-accent hover:text-text-link-accent-hover">Show all...</span>
#                                         <div class="flex flex-wrap gap-2"></div>
#                                         <div class="flex flex-wrap gap-2"></div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="w-full gap-2 rounded border border-border-base-secondary px-3 py-1.5 text-center text-sm font-medium text-text-base-secondary">Join Now</span>
#                                         </div>
#                                         <div class="flex flex-col gap-1 border-t border-border-base-secondary pt-4">
#                                             <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-4">
#                                                 <a href="https://t.me/baji_bgd/1632" target="_blank" class="text-xs font-medium text-text-base-secondary" rel="nofollow noopener noreferrer"></a>
#                                                 <div class="hidden flex-1 items-baseline justify-end whitespace-nowrap @sm/post:flex">
#                                                     <p class="flex items-center gap-x-2 divide-x divide-border-base-secondary text-xs font-medium text-text-base-secondary">
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-eye-line inline-flex leading-[0] text-base"></i>
#                                                             3
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-arrow-repost-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-message-square-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                     </p>
#                                                 </div>
#                                                 <button class="link-button link-button_secondary link-button_small">
#                                                     <span data-state="closed">Analytics</span>
#                                                     <i class="icon-chevron-right-line inline-flex leading-[0] link-button__icon"></i>
#                                                 </button>
#                                             </div>
#                                         </div>
#                                     </div>
#                                 </div>
#                                 <div class="w-full max-w-4xl @container/post">
#                                     <div class="rounded-lg space-y-4 border border-border-base-secondary p-6 shadow-sm">
#                                         <div class="flex items-center gap-2 border-b border-border-base-secondary pb-4">
#                                             <div class="grid flex-1">
#                                                 <div class="channel-name flex items-center channel-name_M ">
#                                                     <div class="channel-name__content">
#                                                         <div class="flex items-center channel-name__header">
#                                                             <span class="grid">
#                                                                 <a target="_blank" class="font-semibold cursor-pointer channel-name__title short-text text-text-base-primary first-letter:uppercase hover:text-text-accent" href="/en/channels/1829680439-baji_bgd">baji 🇧🇩</a>
#                                                             </span>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <div></div>
#                                                             </button>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <span class="inline-block flex-none channel-name__verified">
#                                                                     <img alt="black-icon" loading="lazy" width="14" height="14" decoding="async" data-nimg="1" style="color:transparent;width:100%;height:100%" src="/_next/static/media/black-label-blue.95fcfd40.svg"/>
#                                                                 </span>
#                                                             </button>
#                                                         </div>
#                                                         <div class="flex items-center channel-name__attributes"></div>
#                                                     </div>
#                                                 </div>
#                                             </div>
#                                             <span class="relative" data-state="closed">
#                                                 <button class="button button-border whitespace-nowrap button_secondary button_small button__icon-only outline-none h-9 w-9">
#                                                     <i class="icon-link-line inline-flex leading-[0] button__icon button__icon-only"></i>
#                                                 </button>
#                                             </span>
#                                         </div>
#                                         <div style="background:url(data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwClM5f5V+7/ADpsduzkYHWpkjyQK0II8EKnQfePrW/KkrmHNbRGYbNx2/UVE0TIcEEGti6CEEd6qzlEULK3UcHrinZPcpNlNjGYxhSH4zz1opGCkZU5FFZNWLuWIpBkHNW4LlVzz2rLVXxuUHHrin7JQfuPz/smtFJNambgXXuVbI5yeMVXuZwRs25wBzUBEyrlgQBxkqaTeP73Si6Y+UQHCYxjmimM2TRWbaLsTxMgUh2Iz225/rSkxHHznPQ/Kf8AGiipaGMdkEZw+T/dIP8AjUDNuPQD6UUUhjaKKKAP/9k=);background-size:cover;background-position:center;background-repeat:no-repeat" class="post-image relative flex aspect-square h-full max-w-[410px] items-center justify-center overflow-hidden rounded-lg bg-bg-base-tertiary bg-opacity-90">
#                                             <div class="absolute bottom-0 left-0 right-0 top-0 bg-[#F6F7F8] bg-opacity-80"></div>
#                                             <div class="z-[1] flex flex-col items-center gap-3">
#                                                 <i class="icon-image-line inline-flex leading-[0] text-6xl text-icon-base-secondary"></i>
#                                                 <span class="font-semibold text-text-base-tertiary">Photo unavailable</span>
#                                                 <a href="https://t.me/baji_bgd/1631" target="_blank" class="link inline-flex items-center text-sm font-medium" rel="nofollow noopener noreferrer">
#                                                     Show in Telegram<i class="icon-chevron-right-line inline-flex leading-[0] text-lg"></i>
#                                                 </a>
#                                             </div>
#                                         </div>
#                                         <div class="whitespace-pre-line break-words py-px text-sm text-text-base-primary line-clamp-5">
#                                             <div>
#                                                 🔒 baji  প্রিমিয়াম ডিপোজিট সিস্টেম উন্নত এনক্রিপশনের সাথে সর্বাধিক নিরাপত্তা, সহজ ব্যবহার এবং নিরাপদ লেনদেন নিশ্চিত করে 🔐

# 💵 সহজ ডিপোজিট  এবং দ্রুত উত্তোলন এবং চিন্তামুক্ত গেমিং অভিজ্ঞতার জন্য তৈরি করে।

# 🔒 baji তে অত্যাধুনিক ডিপোজিট সিস্টেম এনক্রিপশন প্রযুক্তি সহ শীর্ষ-স্তরের নিরাপত্তা প্রদান করে 🔐

# প্রতিটি লেনদেনে অতুলনীয় নিরাপত্তা এবং সুবিধার জন্য baji কে  বিশ্বাস করুন 🔓।

# স্ট্রেস-মুক্ত, নিরাপদ অ্যাডভেঞ্চারের জন্য এখনই baji তে যোগ দিন।


# ❤️
#                                                 <b>
#                                                     &nbsp;<i></i>
#                                                 </b>
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://baji.social/bj/tgndt" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Baji</i>
#                                                     </b>
#                                                 </a>
#                                                 <b>
#                                                     <i>সদস্য  </i>
#                                                 </b>
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://baji.social/bj/tgndt" class="text-primary break-all">
#                                                     <b>
#                                                         <i>হিসাবে সাইন-আপ</i>
#                                                     </b>
#                                                 </a>
#                                                 <b>
#                                                     <i>&nbsp;করুন </i>
#                                                 </b>
#                                                 <b>
#                                                     <i>🚀</i>
#                                                 </b>
#                                                 <b>
#                                                     <i></i>
#                                                 </b>
#                                                 <b>
#                                                     <i>🛡</i>
#                                                 </b>
#                                                 <b>
#                                                     <i>এখনই </i>
#                                                 </b>
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://bjbaji5.com/page/guest/appDownload.jsp" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Baji App</i>
#                                                     </b>
#                                                 </a>
#                                                 <b>
#                                                     <i>ডাউনলোড  করুন!!</i>
#                                                 </b>
#                                                 <b>⬇️</b>
#                                                 <b></b>
#                                                 📱 
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://www.facebook.com/baji.bgd/" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Facebook</i>
#                                                     </b>
#                                                 </a>
#                                                 <b></b>
#                                                 📱 
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://x.com/baji_bgd" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Twitter</i>
#                                                     </b>
#                                                 </a>
#                                                 📱 
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://www.instagram.com/baji.bgd/" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Instagram</i>
#                                                     </b>
#                                                 </a>
#                                                 <b>
#                                                     <i></i>
#                                                 </b>
#                                                 📱 
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://www.threads.net/@baji.bgd" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Threads</i>
#                                                     </b>
#                                                 </a>
#                                                 📱 
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://www.tiktok.com/@bj.live88" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Tiktok</i>
#                                                     </b>
#                                                 </a>
#                                                 <b>
#                                                     <i></i>
#                                                 </b>
#                                                 📱 
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://www.pinterest.com/baji_bgd/" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Pinterest</i>
#                                                     </b>
#                                                 </a>
#                                             </div>
#                                         </div>
#                                         <span class="block w-full cursor-pointer text-center font-medium text-text-link-accent hover:text-text-link-accent-hover">Show all...</span>
#                                         <div class="flex flex-wrap gap-2"></div>
#                                         <div class="flex flex-wrap gap-2"></div>
#                                         <div class="flex flex-col gap-1 border-t border-border-base-secondary pt-4">
#                                             <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-4">
#                                                 <a href="https://t.me/baji_bgd/1631" target="_blank" class="text-xs font-medium text-text-base-secondary" rel="nofollow noopener noreferrer"></a>
#                                                 <div class="hidden flex-1 items-baseline justify-end whitespace-nowrap @sm/post:flex">
#                                                     <p class="flex items-center gap-x-2 divide-x divide-border-base-secondary text-xs font-medium text-text-base-secondary">
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-eye-line inline-flex leading-[0] text-base"></i>
#                                                             1
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-arrow-repost-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-message-square-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                     </p>
#                                                 </div>
#                                                 <button class="link-button link-button_secondary link-button_small">
#                                                     <span data-state="closed">Analytics</span>
#                                                     <i class="icon-chevron-right-line inline-flex leading-[0] link-button__icon"></i>
#                                                 </button>
#                                             </div>
#                                         </div>
#                                     </div>
#                                 </div>
#                                 <div class="w-full max-w-4xl @container/post">
#                                     <div class="rounded-lg space-y-4 border border-border-base-secondary p-6 shadow-sm">
#                                         <div class="flex items-center gap-2 border-b border-border-base-secondary pb-4">
#                                             <div class="grid flex-1">
#                                                 <div class="channel-name flex items-center channel-name_M ">
#                                                     <div class="channel-name__content">
#                                                         <div class="flex items-center channel-name__header">
#                                                             <span class="grid">
#                                                                 <a target="_blank" class="font-semibold cursor-pointer channel-name__title short-text text-text-base-primary first-letter:uppercase hover:text-text-accent" href="/en/channels/1829680439-baji_bgd">baji 🇧🇩</a>
#                                                             </span>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <div></div>
#                                                             </button>
#                                                             <button type="button" data-state="closed" class="inline-flex" aria-label="Popover Button" aria-expanded="false" aria-haspopup="dialog">
#                                                                 <span class="inline-block flex-none channel-name__verified">
#                                                                     <img alt="black-icon" loading="lazy" width="14" height="14" decoding="async" data-nimg="1" style="color:transparent;width:100%;height:100%" src="/_next/static/media/black-label-blue.95fcfd40.svg"/>
#                                                                 </span>
#                                                             </button>
#                                                         </div>
#                                                         <div class="flex items-center channel-name__attributes"></div>
#                                                     </div>
#                                                 </div>
#                                             </div>
#                                             <span class="relative" data-state="closed">
#                                                 <button class="button button-border whitespace-nowrap button_secondary button_small button__icon-only outline-none h-9 w-9">
#                                                     <i class="icon-link-line inline-flex leading-[0] button__icon button__icon-only"></i>
#                                                 </button>
#                                             </span>
#                                         </div>
#                                         <div style="background:url(data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDPGScCrKgRJuPJpIo9gyfvUkgeRxGi5x17VpOp0Rn8crIkVycblxu6Go7hAw+UZYelTXTMqRqi8r1PpTrNI9xlDbiB0PY1nF6XZbpJS0KLGPZgIVcYzk0VYvpYZHYeVscdCO9FVZg1YfHhyAD+NNmmUyrHEAAO/eqqvIi5XOOxxVkSo+CyPlT1wBzUS8x0lyao0H2RQFnbc5HTFZ74WCZo8jJHTtTjdZJ4PtUbzwrvUo3zc+3tSWj0NL6alVpGb7xzRUeaK6LmZaidBGQz456YP+NPMiZP7zIPXIP+NFFZNCRE7pj5MZz6H/GoXOQKKKnYpvQZRRRVXEf/2Q==);background-size:cover;background-position:center;background-repeat:no-repeat" class="post-image relative flex aspect-square h-full max-w-[410px] items-center justify-center overflow-hidden rounded-lg bg-bg-base-tertiary bg-opacity-90">
#                                             <div class="absolute bottom-0 left-0 right-0 top-0 bg-[#F6F7F8] bg-opacity-80"></div>
#                                             <div class="z-[1] flex flex-col items-center gap-3">
#                                                 <i class="icon-image-line inline-flex leading-[0] text-6xl text-icon-base-secondary"></i>
#                                                 <span class="font-semibold text-text-base-tertiary">Photo unavailable</span>
#                                                 <a href="https://t.me/baji_bgd/1630" target="_blank" class="link inline-flex items-center text-sm font-medium" rel="nofollow noopener noreferrer">
#                                                     Show in Telegram<i class="icon-chevron-right-line inline-flex leading-[0] text-lg"></i>
#                                                 </a>
#                                             </div>
#                                         </div>
#                                         <div class="whitespace-pre-line break-words py-px text-sm text-text-base-primary line-clamp-5">
#                                             <div>
#                                                 বিরতিহীন বিনোদন এবং বড় পুরস্কার খুঁজছেন? Jili Teen Patti আপনার জন্য! লক্ষ লক্ষ খেলোয়াড়ের সাথে যোগ দিন এবং রোমাঞ্চকর ম্যাচে আপনার কার্ডের দক্ষতা প্রদর্শন করুন। রিয়েল প্লেয়ারদের বিরুদ্ধে খেলুন, বিশেষ বৈশিষ্ট্যগুলি আনলক করুন এবং অত্যাশ্চর্য ভিজ্যুয়াল উপভোগ করুন। আজই শুরু করুন baji-র সাথে। 

# ❤️
#                                                 <b>
#                                                     &nbsp;<i></i>
#                                                 </b>
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://baji.social/bj/tgndt" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Baji</i>
#                                                     </b>
#                                                 </a>
#                                                 <b>
#                                                     <i>সদস্য  </i>
#                                                 </b>
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://baji.social/bj/tgndt" class="text-primary break-all">
#                                                     <b>
#                                                         <i>হিসাবে সাইন-আপ</i>
#                                                     </b>
#                                                 </a>
#                                                 <b>
#                                                     <i>&nbsp;করুন </i>
#                                                 </b>
#                                                 <b>
#                                                     <i>🔼</i>
#                                                 </b>
#                                                 <b>
#                                                     <i></i>
#                                                 </b>
#                                                 <b>
#                                                     <i>🛡</i>
#                                                 </b>
#                                                 <b>
#                                                     <i>এখনই </i>
#                                                 </b>
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://bjbaji5.com/page/guest/appDownload.jsp" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Baji App</i>
#                                                     </b>
#                                                 </a>
#                                                 <b>
#                                                     <i>ডাউনলোড  করুন!!</i>
#                                                 </b>
#                                                 <b>⬇️</b>
#                                                 <b></b>
#                                                 📱 
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://www.facebook.com/baji.bgd/" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Facebook</i>
#                                                     </b>
#                                                 </a>
#                                                 <b></b>
#                                                 📱 
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://x.com/baji_bgd" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Twitter</i>
#                                                     </b>
#                                                 </a>
#                                                 📱 
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://www.instagram.com/baji.bgd/" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Instagram</i>
#                                                     </b>
#                                                 </a>
#                                                 <b>
#                                                     <i></i>
#                                                 </b>
#                                                 📱 
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://www.threads.net/@baji.bgd" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Threads</i>
#                                                     </b>
#                                                 </a>
#                                                 📱 
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://www.tiktok.com/@bj.live88" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Tiktok</i>
#                                                     </b>
#                                                 </a>
#                                                 <b>
#                                                     <i></i>
#                                                 </b>
#                                                 📱 
#                                                 <a aria-label="link to url" target="_blank" rel="noopener noreferrer nofollow" href="https://www.pinterest.com/baji_bgd/" class="text-primary break-all">
#                                                     <b>
#                                                         <i>Pinterest</i>
#                                                     </b>
#                                                 </a>
#                                             </div>
#                                         </div>
#                                         <span class="block w-full cursor-pointer text-center font-medium text-text-link-accent hover:text-text-link-accent-hover">Show all...</span>
#                                         <div class="flex flex-wrap gap-2"></div>
#                                         <div class="flex flex-wrap gap-2">
#                                             <span class="flex items-center gap-1 rounded-[14px] bg-bg-base-tertiary px-2 py-1 text-xs font-medium text-yang-gray-700">
#                                                 <span class="text-sm leading-none">👍</span>
#                                                 <!-- -->
#                                                 11
#                                             </span>
#                                         </div>
#                                         <div class="flex flex-col gap-1 border-t border-border-base-secondary pt-4">
#                                             <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-4">
#                                                 <a href="https://t.me/baji_bgd/1630" target="_blank" class="text-xs font-medium text-text-base-secondary" rel="nofollow noopener noreferrer"></a>
#                                                 <div class="hidden flex-1 items-baseline justify-end whitespace-nowrap @sm/post:flex">
#                                                     <p class="flex items-center gap-x-2 divide-x divide-border-base-secondary text-xs font-medium text-text-base-secondary">
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-eye-line inline-flex leading-[0] text-base"></i>
#                                                             1 679
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-arrow-repost-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                         <span class="inline-flex items-center gap-1 pl-2 first:pl-0">
#                                                             <i class="icon-message-square-line inline-flex leading-[0] text-base"></i>
#                                                             0
#                                                         </span>
#                                                     </p>
#                                                 </div>
#                                                 <button class="link-button link-button_secondary link-button_small">
#                                                     <span data-state="closed">Analytics</span>
#                                                     <i class="icon-chevron-right-line inline-flex leading-[0] link-button__icon"></i>
#                                                 </button>
#                                             </div>
#                                         </div>
#                                     </div>
#                                 </div>
#                                 <button class="button button-border whitespace-nowrap button_secondary button_medium w-full">
#                                     <i class="icon-chevron-down-line inline-flex leading-[0] button__icon"></i>
#                                     Show more
#                                 </button>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#             <nav aria-label="Breadcrumb" class="hidden">
#                 <ol class="breadcrumb">
#                     <li>
#                         <a href="/enhttps://telemetr.io/en">Home</a>
#                     </li>
#                     <li>
#                         <a href="/enhttps://telemetr.io/en/catalog/bangladesh">Bangladesh</a>
#                     </li>
#                     <li>
#                         <a href="/enhttps://telemetr.io/en/catalog/bangladesh/bets-and-casino">Betting and Casino</a>
#                     </li>
#                     <li>
#                         <a href="/enhttps://telemetr.io/en/channels/1829680439-baji_bgd">baji 🇧🇩</a>
#                     </li>
#                 </ol>
#                 <script type="application/ld+json">
#                     {
#                         "@context": "https://schema.org",
#                         "@type": "BreadcrumbList",
#                         "itemListElement": [
#                             {
#                                 "@type": "ListItem",
#                                 "position": 1,
#                                 "name": "Home",
#                                 "item": "https://telemetr.io/en"
#                             },
#                             {
#                                 "@type": "ListItem",
#                                 "position": 2,
#                                 "name": "Bangladesh",
#                                 "item": "https://telemetr.io/en/catalog/bangladesh"
#                             },
#                             {
#                                 "@type": "ListItem",
#                                 "position": 3,
#                                 "name": "Betting and Casino",
#                                 "item": "https://telemetr.io/en/catalog/bangladesh/bets-and-casino"
#                             },
#                             {
#                                 "@type": "ListItem",
#                                 "position": 4,
#                                 "name": "baji 🇧🇩",
#                                 "item": "https://telemetr.io/en/channels/1829680439-baji_bgd"
#                             }
#                         ]
#                     }</script>
#             </nav>
#         </main>
#         <footer class="container space-y-10 border-t border-border-base-secondary bg-bg-base-primary px-6 pb-5 pt-7 text-sm text-text-link-base min-[414px]:space-y-11 md:space-y-12 xl:px-11 xl:pt-10">
#             <div class="flex flex-col justify-between gap-x-9 gap-y-9 md:gap-y-10 lg:gap-y-9 xl:flex-row ">
#                 <div class="flex flex-1 flex-wrap items-center justify-between gap-y-2 min-[1070px]:gap-x-10 xl:flex-col xl:items-start xl:justify-normal">
#                     <div class="-my-0.5 flex min-[414px]:basis-[44%] min-[1070px]:basis-0 xl:mb-4">
#                         <a class="-m-1.5 p-1.5" href="">
#                             <p class="sr-only">Telemetrio</p>
#                             <span class="group flex items-center gap-3" id="logo">
#                                 <div class="main-logo__icon relative flex items-center justify-center">
#                                     <div class="hidden group-hover:flex">
#                                         <div class="absolute bottom-[20%] left-[17%] items-center justify-center Loader_loading-container__833ya">
#                                             <div class="mb-0 h-4.5 w-[20.8px] Loader_loading__MZ9UM">
#                                                 <div class="flex rounded bg-[#F5C324] Loader_line-sm__dMvr1"></div>
#                                                 <div class="flex rounded bg-[#2DB6F5] Loader_line-sm__dMvr1"></div>
#                                                 <div class="flex rounded bg-[#006DDA] Loader_line-sm__dMvr1"></div>
#                                             </div>
#                                         </div>
#                                     </div>
#                                     <svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
#                                         <rect x="0.5" y="0.5" width="29" height="29" rx="5.5" fill="white"></rect>
#                                         <rect x="0.5" y="0.5" width="29" height="29" rx="5.5" stroke="#E7EAED"></rect>
#                                         <path class="group-hover:hidden" id="blueLine" d="M21.7339 10.1133C22.9787 10.1133 24.0001 11.2254 24.0001 12.5758V21.5361C24.0001 22.9023 22.9947 23.9985 21.7339 23.9985C20.4891 23.9985 19.4678 22.8864 19.4678 21.5361V12.5917C19.4678 11.2254 20.4732 10.1133 21.7339 10.1133Z" fill="#006DDA"></path>
#                                         <path class="group-hover:hidden" id="lightBlueLine" d="M14.9995 6C16.2443 6 17.2657 7.04854 17.2657 8.31951V21.6805C17.2657 22.9673 16.2603 24 14.9995 24C13.7548 24 12.7334 22.9515 12.7334 21.6805V8.33539C12.7334 7.04854 13.7548 6 14.9995 6Z" fill="#2DB6F5"></path>
#                                         <path class="group-hover:hidden" id="yellowLine" d="M8.26517 14.7539C9.50996 14.7539 10.5313 15.866 10.5313 17.2164V21.5377C10.5313 22.9039 9.52591 24.0001 8.26517 24.0001C7.02039 24.0001 5.99902 22.8881 5.99902 21.5377V17.2164C6.01498 15.866 7.02039 14.7539 8.26517 14.7539Z" fill="#F5C324"></path>
#                                     </svg>
#                                 </div>
#                                 <svg class="main-logo__text" xmlns="http://www.w3.org/2000/svg" width="123" height="18" viewBox="0 0 123 18" fill="none">
#                                     <path d="M11.9257 0.523385V3.0956H7.31912V17.3597H4.62999V3.0956H0V0.523385H11.9257Z" fill="#1C1E21"></path>
#                                     <path d="M14.8065 12.2854C14.9936 13.174 15.4223 13.8599 16.0926 14.3432C16.7629 14.8109 17.5814 15.0447 18.5479 15.0447C19.8886 15.0447 20.8941 14.5614 21.5644 13.5949L23.6456 14.8109C22.492 16.5101 20.7849 17.3597 18.5245 17.3597C16.6226 17.3597 15.0871 16.7829 13.9179 15.6293C12.7487 14.4601 12.1641 12.9869 12.1641 11.2098C12.1641 9.46378 12.7409 8.00619 13.8945 6.837C15.0481 5.65222 16.5291 5.05983 18.3374 5.05983C20.0523 5.05983 21.4553 5.66002 22.5465 6.86039C23.6534 8.06075 24.2068 9.51834 24.2068 11.2332C24.2068 11.4982 24.1756 11.8489 24.1132 12.2854H14.8065ZM14.7831 10.2276H21.6579C21.4865 9.27671 21.0889 8.55961 20.4654 8.07634C19.8574 7.59308 19.1403 7.35144 18.3141 7.35144C17.3787 7.35144 16.5992 7.60867 15.9757 8.12311C15.3521 8.63755 14.9546 9.33907 14.7831 10.2276Z" fill="#1C1E21"></path>
#                                     <path d="M27.5981 17.3597V1.45727L30.1236 0.521922V17.3597H27.5981Z" fill="#1C1E21"></path>
#                                     <path d="M36.2127 12.2854C36.3998 13.174 36.8285 13.8599 37.4988 14.3432C38.1691 14.8109 38.9876 15.0447 39.9541 15.0447C41.2948 15.0447 42.3003 14.5614 42.9706 13.5949L45.0518 14.8109C43.8982 16.5101 42.1911 17.3597 39.9307 17.3597C38.0288 17.3597 36.4933 16.7829 35.3241 15.6293C34.1549 14.4601 33.5703 12.9869 33.5703 11.2098C33.5703 9.46378 34.1471 8.00619 35.3007 6.837C36.4543 5.65222 37.9353 5.05983 39.7436 5.05983C41.4585 5.05983 42.8615 5.66002 43.9527 6.86039C45.0596 8.06075 45.613 9.51834 45.613 11.2332C45.613 11.4982 45.5818 11.8489 45.5194 12.2854H36.2127ZM36.1893 10.2276H43.0641C42.8927 9.27671 42.4951 8.55961 41.8716 8.07634C41.2636 7.59308 40.5465 7.35144 39.7203 7.35144C38.7849 7.35144 38.0054 7.60867 37.3819 8.12311C36.7583 8.63755 36.3608 9.33907 36.1893 10.2276Z" fill="#1C1E21"></path>
#                                     <path d="M61.7719 4.89615C63.097 4.89615 64.1648 5.32485 64.9755 6.18226C65.7861 7.03966 66.1914 8.19326 66.1914 9.64305V17.3597H63.666V9.80674C63.666 8.99611 63.4633 8.37254 63.058 7.93604C62.6527 7.48395 62.0993 7.25791 61.3977 7.25791C60.6183 7.25791 59.9947 7.51513 59.527 8.02957C59.075 8.54402 58.8489 9.31568 58.8489 10.3446V17.3597H56.3235V9.80674C56.3235 8.99611 56.1286 8.37254 55.7389 7.93604C55.3647 7.48395 54.8269 7.25791 54.1254 7.25791C53.3615 7.25791 52.7379 7.52293 52.2547 8.05296C51.7714 8.5674 51.5298 9.33127 51.5298 10.3446V17.3597H49.0043V5.20014H51.5298V6.60316C52.2781 5.46515 53.3927 4.89615 54.8737 4.89615C56.3702 4.89615 57.4771 5.51192 58.1942 6.74347C58.9736 5.51192 60.1662 4.89615 61.7719 4.89615Z" fill="#1C1E21"></path>
#                                     <path d="M72.0511 12.2854C72.2381 13.174 72.6668 13.8599 73.3372 14.3432C74.0075 14.8109 74.8259 15.0447 75.7925 15.0447C77.1331 15.0447 78.1386 14.5614 78.809 13.5949L80.8901 14.8109C79.7365 16.5101 78.0295 17.3597 75.7691 17.3597C73.8672 17.3597 72.3317 16.7829 71.1625 15.6293C69.9933 14.4601 69.4087 12.9869 69.4087 11.2098C69.4087 9.46378 69.9855 8.00619 71.1391 6.837C72.2927 5.65222 73.7737 5.05983 75.582 5.05983C77.2968 5.05983 78.6998 5.66002 79.7911 6.86039C80.8979 8.06075 81.4513 9.51834 81.4513 11.2332C81.4513 11.4982 81.4202 11.8489 81.3578 12.2854H72.0511ZM72.0277 10.2276H78.9025C78.731 9.27671 78.3335 8.55961 77.7099 8.07634C77.102 7.59308 76.3848 7.35144 75.5586 7.35144C74.6233 7.35144 73.8438 7.60867 73.2202 8.12311C72.5967 8.63755 72.1992 9.33907 72.0277 10.2276Z" fill="#1C1E21"></path>
#                                     <path d="M91.0014 7.63205H88.1018V13.7118C88.1018 14.1951 88.211 14.5459 88.4292 14.7641C88.6474 14.9668 88.967 15.0837 89.3879 15.1149C89.8244 15.1304 90.3623 15.1227 91.0014 15.0915V17.3597C89.0684 17.5935 87.6809 17.4298 86.8391 16.8686C85.9973 16.2918 85.5764 15.2396 85.5764 13.7118V7.63205H83.4251V5.20014H85.5764V1.27167L88.1018 0.523385V5.20014H91.0014V7.63205Z" fill="#1C1E21"></path>
#                                     <path d="M97.1007 7.16437C97.7399 5.71458 98.9403 4.98968 100.702 4.98968V7.72559C99.7353 7.66323 98.8935 7.89707 98.1764 8.4271C97.4593 8.94154 97.1007 9.79895 97.1007 10.9993V17.3597H94.5753V5.20014H97.1007V7.16437Z" fill="#1C1E21"></path>
#                                     <path d="M106.005 3.25929C105.693 3.57107 105.319 3.72696 104.883 3.72696C104.446 3.72696 104.064 3.57107 103.737 3.25929C103.425 2.93191 103.269 2.54998 103.269 2.11348C103.269 1.67698 103.425 1.30284 103.737 0.99106C104.049 0.663687 104.431 0.5 104.883 0.5C105.335 0.5 105.717 0.663687 106.029 0.99106C106.34 1.30284 106.496 1.67698 106.496 2.11348C106.496 2.54998 106.333 2.93191 106.005 3.25929ZM103.737 17.3597V6.13549L106.262 5.20014V17.3597H103.737Z" fill="#1C1E21"></path>
#                                     <path d="M116.007 17.5C114.292 17.5 112.834 16.9076 111.634 15.7228C110.434 14.5381 109.834 13.0805 109.834 11.3501C109.834 9.61967 110.434 8.16208 111.634 6.97731C112.834 5.79253 114.292 5.20014 116.007 5.20014C117.737 5.20014 119.195 5.79253 120.38 6.97731C121.58 8.16208 122.18 9.61967 122.18 11.3501C122.18 13.0805 121.58 14.5381 120.38 15.7228C119.195 16.9076 117.737 17.5 116.007 17.5ZM113.411 13.9924C114.113 14.6939 114.978 15.0447 116.007 15.0447C117.036 15.0447 117.901 14.6939 118.602 13.9924C119.304 13.2909 119.655 12.4101 119.655 11.3501C119.655 10.29 119.304 9.40922 118.602 8.70771C117.901 8.00619 117.036 7.65543 116.007 7.65543C114.978 7.65543 114.113 8.00619 113.411 8.70771C112.71 9.40922 112.359 10.29 112.359 11.3501C112.359 12.4101 112.71 13.2909 113.411 13.9924Z" fill="#1C1E21"></path>
#                                 </svg>
#                             </span>
#                         </a>
#                     </div>
#                     <div class="mb-1 flex basis-full flex-col gap-x-10 gap-y-2 min-[414px]:order-1 min-[414px]:mb-0 min-[414px]:gap-y-3 md:basis-auto md:items-start md:gap-y-2 min-[1070px]:order-none min-[1070px]:flex-row min-[1070px]:items-center xl:mb-8 xl:flex-col xl:items-start xl:gap-y-4">
#                         <p class="text-sm text-text-base-secondary">Search and analysis of Telegram channels in one place</p>
#                     </div>
#                     <div class="min-[414px]:basis-[52%] min-[1070px]:flex-1 "></div>
#                 </div>
#                 <div class="grid grid-cols-1 gap-x-9 gap-y-7 min-[508px]:grid-cols-2 md:grid-cols-3 md:gap-y-9 lg:gap-x-11 min-[1070px]:flex min-[1070px]:justify-start xl:gap-x-9 min-[1680px]:gap-x-[68px]">
#                     <div class="">
#                         <span class="block mb-4 text-sm font-semibold text-text-base-primary">Ratings</span>
#                         <ul class="flex flex-col gap-4 list-none">
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="">Primary Catalog</a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="">
#                                     Market overview<span class="bg-bg-label-primary-10 mx-1 rounded bg-bg-label-primary-01 px-1.5 py-px text-xs font-medium capitalize text-text-base-quaternary">BETA</span>
#                                 </a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="/en/top-country">Country ranking</a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="/en/category">Ratings by category</a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="">
#                                     Rating of channel networks<span class="mx-1 rounded bg-bg-label-primary-01 px-1.5 py-px text-xs font-medium capitalize text-text-base-quaternary">NEW</span>
#                                 </a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="/en/collections/public">Recommended collections</a>
#                             </li>
#                         </ul>
#                     </div>
#                     <div class="">
#                         <span class="block mb-4 text-sm font-semibold text-text-base-primary">Tools</span>
#                         <ul class="flex flex-col gap-4 list-none">
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="/en/tracking/about">Event tracking</a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="/en/ads-posts/about">Advertising posts</a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="">
#                                     Advertiser rankings<span class="bg-bg-label-primary-10 mx-1 rounded bg-bg-label-primary-01 px-1.5 py-px text-xs font-medium capitalize text-text-base-quaternary">BETA</span>
#                                 </a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="/en/posts-search/about">
#                                     Posts search<span class="mx-1 rounded bg-bg-label-primary-01 px-1.5 py-px text-xs font-medium capitalize text-text-base-quaternary">NEW</span>
#                                 </a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="/en/tg-cleaner/deleting">
#                                     TgCleaner<span class="bg-bg-label-primary-10 mx-1 rounded bg-bg-label-primary-01 px-1.5 py-px text-xs font-medium capitalize text-text-base-quaternary">BETA</span>
#                                 </a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_blank" href="https://joinio.pro/">Joinio</a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="/en/tg-ads/about">
#                                     Telegram Ads<span class="bg-bg-label-primary-10 mx-1 rounded bg-bg-label-primary-01 px-1.5 py-px text-xs font-medium capitalize text-text-base-quaternary">BETA</span>
#                                 </a>
#                             </li>
#                         </ul>
#                     </div>
#                     <div class="">
#                         <span class="block mb-4 text-sm font-semibold text-text-base-primary">Resources</span>
#                         <ul class="flex flex-col gap-4 list-none">
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_blank" href="https://medium.com/@telemetrio">Instruction</a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="https://t.me/+5YM9Haq7C71iZjFi">English language chat support</a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="https://t.me/telemetrio_news">Telemetrio News</a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="https://eratelegram.com/en">Conference</a>
#                             </li>
#                         </ul>
#                     </div>
#                     <div class="">
#                         <span class="block mb-4 text-sm font-semibold text-text-base-primary">API</span>
#                         <ul class="flex flex-col gap-4 list-none">
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_blank" href="https://api.telemetr.io/docs/intro/overview">API documentation</a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_blank" href="https://t.me/telemetrio_api_bot">
#                                     API bot<span class="mx-1 rounded bg-bg-label-primary-01 px-1.5 py-px text-xs font-medium capitalize text-text-base-quaternary">NEW</span>
#                                 </a>
#                             </li>
#                         </ul>
#                     </div>
#                     <div class="">
#                         <span class="block mb-4 text-sm font-semibold text-text-base-primary">Our bots</span>
#                         <ul class="flex flex-col gap-4 list-none">
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="https://t.me/telemetr_io_bot">@telemetr_io_bot</a>
#                             </li>
#                             <li>
#                                 <a class="flex items-center font-medium text-text-link-base hover:text-text-link-base-hover" target="_self" href="https://t.me/TelemetrioSupport_bot">@TelemetrioSupport_bot</a>
#                             </li>
#                         </ul>
#                     </div>
#                 </div>
#             </div>
#             <div class="flex flex-col items-center justify-between pt-5 text-xs border-t gap-y-3 min-[1070px]:flex-row">
#                 <div class="flex items-center gap-1 text-text-base-tertiary order-1 min-[1070px]:order-none">
#                     <i class="icon-copywriting-line inline-flex leading-[0]"></i>
#                     2024
#                     <!-- -->
#                     <!-- -->
#                     Telemetr.io All Right Reserved
#                 </div>
#                 <div class="flex flex-wrap items-center justify-center gap-3 sm:flex-row min-[1070px]:gap-6">
#                     <a href="/en/dmca" class="text-sm font-medium text-text-base-secondary">DMCA</a>
#                     <a href="/en/terms-of-use" class="text-sm font-medium text-text-base-secondary">Terms of Use</a>
#                     <a href="/en/privacy-policy" class="text-sm font-medium text-text-base-secondary">Telemetrio Privacy Policy</a>
#                 </div>
#             </div>
#         </footer>
#         <button class="button button-border whitespace-nowrap button_secondary button_medium button__icon-only fixed bottom-6 right-24 z-30 transition-opacity duration-300 sm:h-10 sm:w-10 opacity-0 pointer-events-none" aria-label="Scroll to top">
#             <i class="icon-arrow-up-line inline-flex leading-[0] button__icon button__icon-only"></i>
#         </button>
#         <noscript>
#             <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PCM9CD4W" height="0" width="0" style="display:none;visibility:hidden"></iframe>
#         </noscript>
#         <script src="/_next/static/chunks/webpack-35bb7d39aba18b7f.js" async=""></script>
#         <script>
#             (self.__next_f = self.__next_f || []).push([0]);
#             self.__next_f.push([2, null])
#         </script>
#         <script>
#             self.__next_f.push([1, "0:\"$L1\"\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "2:HL[\"/_next/static/media/035951aefad7b653-s.p.woff2\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/woff2\"}]\n3:HL[\"/_next/static/media/0d3d6de4d4f168ef-s.p.ttf\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/ttf\"}]\n4:HL[\"/_next/static/media/26a46d62cd723877-s.p.woff2\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/woff2\"}]\n5:HL[\"/_next/static/media/35b6be5591831960-s.p.ttf\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/ttf\"}]\n6:HL[\"/_next/static/media/4e81fe9cba68eadc-s.p.woff\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/woff\"}]\n7:HL[\"/_next/stat"])
#         </script>
#         <script>
#             self.__next_f.push([1, "ic/media/5f4839c814e9ec59-s.p.woff\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/woff\"}]\n8:HL[\"/_next/static/media/8acb5781ce311ba9-s.p.woff\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/woff\"}]\n9:HL[\"/_next/static/media/90b1a89cbb9b3d98-s.p.woff\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/woff\"}]\na:HL[\"/_next/static/media/a34f9d1faa5f3315-s.p.woff2\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/woff2\"}]\nb:HL[\"/_next/static/media/be8c7f0c93c8bd5b-s.p.ttf\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/ttf\"}]\nc:HL[\"/_next/static/media/cddbbedc"])
#         </script>
#         <script>
#             self.__next_f.push([1, "f75420b6-s.p.ttf\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/ttf\"}]\nd:HL[\"/_next/static/media/e7603192e130cb26-s.p.ttf\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/ttf\"}]\ne:HL[\"/_next/static/media/f869f1e338b9e6dc-s.p.woff\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/woff\"}]\nf:HL[\"/_next/static/css/095e7f3527a345a7.css\",\"style\"]\n10:HL[\"/_next/static/css/90a14ad6b753303e.css\",\"style\"]\n11:HL[\"/_next/static/css/b72b5821f33bf271.css\",\"style\"]\n12:HL[\"/_next/static/css/a55981e9afb98fbc.css\",\"style\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "13:I[33728,[],\"\"]\n16:I[56954,[],\"\"]\n19:I[7264,[],\"\"]\n1e:I[29928,[],\"\"]\n17:[\"lng\",\"en\",\"d\"]\n18:[\"id\",\"1829680439-baji_bgd\",\"d\"]\n1f:[]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "1:[null,[\"$\",\"$L13\",null,{\"buildId\":\"93IHyY7pJzQBxzFbqZ9Lb\",\"assetPrefix\":\"\",\"initialCanonicalUrl\":\"/en/channels/1829680439-baji_bgd/publish\",\"initialTree\":[\"\",{\"children\":[[\"lng\",\"en\",\"d\"],{\"children\":[\"(service)\",{\"children\":[\"channels\",{\"children\":[[\"id\",\"1829680439-baji_bgd\",\"d\"],{\"children\":[\"publish\",{\"children\":[\"__PAGE__\",{}]}]}]}]}]},\"$undefined\",\"$undefined\",true]}],\"initialSeedData\":[\"\",{\"children\":[[\"lng\",\"en\",\"d\"],{\"children\":[\"(service)\",{\"children\":[\"channels\",{\"children\":[[\"id\",\"1829680439-baji_bgd\",\"d\"],{\"children\":[\"publish\",{\"children\":[\"__PAGE__\",{},[\"$L14\",\"$L15\",null]]},[\"$\",\"$L16\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\",\"$17\",\"children\",\"(service)\",\"children\",\"channels\",\"children\",\"$18\",\"children\",\"publish\",\"children\"],\"loading\":\"$undefined\",\"loadingStyles\":\"$undefined\",\"loadingScripts\":\"$undefined\",\"hasLoading\":false,\"error\":\"$undefined\",\"errorStyles\":\"$undefined\",\"errorScripts\":\"$undefined\",\"template\":[\"$\",\"$L19\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":\"$undefined\",\"notFoundStyles\":\"$undefined\",\"styles\":null}]]},[null,\"$L1a\",null]]},[\"$\",\"$L16\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\",\"$17\",\"children\",\"(service)\",\"children\",\"channels\",\"children\"],\"loading\":\"$undefined\",\"loadingStyles\":\"$undefined\",\"loadingScripts\":\"$undefined\",\"hasLoading\":false,\"error\":\"$undefined\",\"errorStyles\":\"$undefined\",\"errorScripts\":\"$undefined\",\"template\":[\"$\",\"$L19\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":\"$undefined\",\"notFoundStyles\":\"$undefined\",\"styles\":[[\"$\",\"link\",\"0\",{\"rel\":\"stylesheet\",\"href\":\"/_next/static/css/a55981e9afb98fbc.css\",\"precedence\":\"next\",\"crossOrigin\":\"$undefined\"}]]}]]},[null,\"$L1b\",null]]},[null,\"$L1c\",null]]},[\"$\",\"$L16\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\"],\"loading\":\"$undefined\",\"loadingStyles\":\"$undefined\",\"loadingScripts\":\"$undefined\",\"hasLoading\":false,\"error\":\"$undefined\",\"errorStyles\":\"$undefined\",\"errorScripts\":\"$undefined\",\"template\":[\"$\",\"$L19\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":[[\"$\",\"title\",null,{\"children\":\"404: This page could not be found.\"}],[\"$\",\"div\",null,{\"style\":{\"fontFamily\":\"system-ui,\\\"Segoe UI\\\",Roboto,Helvetica,Arial,sans-serif,\\\"Apple Color Emoji\\\",\\\"Segoe UI Emoji\\\"\",\"height\":\"100vh\",\"textAlign\":\"center\",\"display\":\"flex\",\"flexDirection\":\"column\",\"alignItems\":\"center\",\"justifyContent\":\"center\"},\"children\":[\"$\",\"div\",null,{\"children\":[[\"$\",\"style\",null,{\"dangerouslySetInnerHTML\":{\"__html\":\"body{color:#000;background:#fff;margin:0}.next-error-h1{border-right:1px solid rgba(0,0,0,.3)}@media (prefers-color-scheme:dark){body{color:#fff;background:#000}.next-error-h1{border-right:1px solid rgba(255,255,255,.3)}}\"}}],[\"$\",\"h1\",null,{\"className\":\"next-error-h1\",\"style\":{\"display\":\"inline-block\",\"margin\":\"0 20px 0 0\",\"padding\":\"0 23px 0 0\",\"fontSize\":24,\"fontWeight\":500,\"verticalAlign\":\"top\",\"lineHeight\":\"49px\"},\"children\":\"404\"}],[\"$\",\"div\",null,{\"style\":{\"display\":\"inline-block\"},\"children\":[\"$\",\"h2\",null,{\"style\":{\"fontSize\":14,\"fontWeight\":400,\"lineHeight\":\"49px\",\"margin\":0},\"children\":\"This page could not be found.\"}]}]]}]}]],\"notFoundStyles\":[],\"styles\":[[\"$\",\"link\",\"0\",{\"rel\":\"stylesheet\",\"href\":\"/_next/static/css/095e7f3527a345a7.css\",\"precedence\":\"next\",\"crossOrigin\":\"$undefined\"}]]}]],\"initialHead\":[false,\"$L1d\"],\"globalErrorComponent\":\"$1e\",\"missingSlots\":\"$W1f\"}]]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "20:I[73994,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"69695\",\"static/chunks/app/%5Blng%5D/layout-1e1244772c66069d.js\"],\"\"]\n21:I[72326,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"69695\",\"static/chunks/app/%5Blng%5D/layout-1e1244772c66069d.js\"],\"\"]\n22:I[79669,[\"73220\",\"static/chunks/73220-3a1140fcb6d"])
#         </script>
#         <script>
#             self.__next_f.push([1, "7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"99600\",\"static/chunks/app/%5Blng%5D/not-found-4649d50a4cf3c918.js\"],\"\"]\n23:I[92064,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"69695\",\"static/chunks/app/%5Blng%5D/layout-1e1244772c66069d.js\"],\"\"]\n2"])
#         </script>
#         <script>
#             self.__next_f.push([1, "4:I[58178,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"69695\",\"static/chunks/app/%5Blng%5D/layout-1e1244772c66069d.js\"],\"\"]\n25:I[68493,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"69695\",\"static/chunks/app/%5Blng%5D/layout-1e1244772c66069d.js\"],\"LiveChat\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "1c:[\"$\",\"html\",null,{\"lang\":\"en\",\"className\":\"__className_7b175a\",\"data-gtag\":\"G-RQLZYC299K\",\"children\":[[\"$\",\"link\",null,{\"rel\":\"preconnect dns-prefetch\",\"href\":\"https://img.telemetr.io/\",\"crossOrigin\":\"\"}],[\"$\",\"meta\",null,{\"name\":\"google-adsense-account\",\"content\":\"ca-pub-7504188967825231\"}],[\"$\",\"script\",null,{\"async\":true,\"src\":\"https://www.googletagmanager.com/gtag/js?id=G-RQLZYC299K\"}],[\"$\",\"script\",null,{\"async\":true,\"src\":\"/script/gtag.js\"}],[\"$\",\"$L20\",null,{\"id\":\"google-tag-manager\",\"strategy\":\"afterInteractive\",\"children\":\"\\n        (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':\\n        new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],\\n        j=d.createElement(s),dl=l!='dataLayer'?'\u0026l='+l:'';j.async=true;j.src=\\n        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);\\n        })(window,document,'script','dataLayer','GTM-PCM9CD4W');\\n        \"}],[\"$\",\"$L21\",null,{}],[\"$\",\"body\",null,{\"suppressHydrationWarning\":true,\"className\":\"flex min-h-screen flex-col justify-between\",\"children\":[[\"$\",\"$L16\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\",\"$17\",\"children\"],\"loading\":\"$undefined\",\"loadingStyles\":\"$undefined\",\"loadingScripts\":\"$undefined\",\"hasLoading\":false,\"error\":\"$undefined\",\"errorStyles\":\"$undefined\",\"errorScripts\":\"$undefined\",\"template\":[\"$\",\"$L19\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":[\"$\",\"$L22\",null,{}],\"notFoundStyles\":[],\"styles\":[[\"$\",\"link\",\"0\",{\"rel\":\"stylesheet\",\"href\":\"/_next/static/css/90a14ad6b753303e.css\",\"precedence\":\"next\",\"crossOrigin\":\"$undefined\"}],[\"$\",\"link\",\"1\",{\"rel\":\"stylesheet\",\"href\":\"/_next/static/css/b72b5821f33bf271.css\",\"precedence\":\"next\",\"crossOrigin\":\"$undefined\"}]]}],[\"$\",\"$L23\",null,{}],[\"$\",\"$L24\",null,{\"gtmId\":\"GTM-PCM9CD4W\"}],[\"$\",\"$L25\",null,{}]]}]]}]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "26:I[27654,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"1448\",\"static/chunks/1448-ba568bcf236ccabb.js\",\"89980\",\"static/chunks/89980-1e653f4986615471.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"78110\",\"static/chunks/78110-c9000034beae1679.js\",\"39577\",\"static/chunks/39577-6e0063d635209dcc.js\",\"85600\",\"static/chunks/85600-d838c560b6e3316b.js\",\"76958\",\"static/chunks/76958-91aef98d2406e983.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"83286\",\"static/chunks/83286-7ca7aed2c53ce442.js\",\"50360\",\"static/chunks/50360-570f674fa7869486.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"38259\",\"static/chunks/38259-bceccd9489884b29.js\",\"45345\",\"static/chunks/45345-40abd9c1679bdc0c.js\",\"5994\",\"static/chunks/app/%5Blng%5D/(service)/layout-aa2e99dfe8f97961.js\"],\"Providers\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "27:\"$Sreact.suspense\"\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "28:I[80160,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"1448\",\"static/chunks/1448-ba568bcf236ccabb.js\",\"89980\",\"static/chunks/89980-1e653f4986615471.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"78110\",\"static/chunks/78110-c9000034beae1679.js\",\"39577\",\"static/chunks/39577-6e0063d635209dcc.js\",\"85600\",\"static/chunks/85600-d838c560b6e3316b.js\",\"76958\",\"static/chunks/76958-91aef98d2406e983.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"83286\",\"static/chunks/83286-7ca7aed2c53ce442.js\",\"50360\",\"static/chunks/50360-570f674fa7869486.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"38259\",\"static/chunks/38259-bceccd9489884b29.js\",\"45345\",\"static/chunks/45345-40abd9c1679bdc0c.js\",\"5994\",\"static/chunks/app/%5Blng%5D/(service)/layout-aa2e99dfe8f97961.js\"],\"\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "29:I[15643,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"1448\",\"static/chunks/1448-ba568bcf236ccabb.js\",\"89980\",\"static/chunks/89980-1e653f4986615471.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"78110\",\"static/chunks/78110-c9000034beae1679.js\",\"39577\",\"static/chunks/39577-6e0063d635209dcc.js\",\"85600\",\"static/chunks/85600-d838c560b6e3316b.js\",\"76958\",\"static/chunks/76958-91aef98d2406e983.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"83286\",\"static/chunks/83286-7ca7aed2c53ce442.js\",\"50360\",\"static/chunks/50360-570f674fa7869486.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"38259\",\"static/chunks/38259-bceccd9489884b29.js\",\"45345\",\"static/chunks/45345-40abd9c1679bdc0c.js\",\"5994\",\"static/chunks/app/%5Blng%5D/(service)/layout-aa2e99dfe8f97961.js\"],\"DefaultPlanTokenCheck\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "2a:I[51328,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"1448\",\"static/chunks/1448-ba568bcf236ccabb.js\",\"89980\",\"static/chunks/89980-1e653f4986615471.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"78110\",\"static/chunks/78110-c9000034beae1679.js\",\"39577\",\"static/chunks/39577-6e0063d635209dcc.js\",\"85600\",\"static/chunks/85600-d838c560b6e3316b.js\",\"76958\",\"static/chunks/76958-91aef98d2406e983.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"83286\",\"static/chunks/83286-7ca7aed2c53ce442.js\",\"50360\",\"static/chunks/50360-570f674fa7869486.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"38259\",\"static/chunks/38259-bceccd9489884b29.js\",\"45345\",\"static/chunks/45345-40abd9c1679bdc0c.js\",\"5994\",\"static/chunks/app/%5Blng%5D/(service)/layout-aa2e99dfe8f97961.js\"],\"\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "2b:I[46024,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"1448\",\"static/chunks/1448-ba568bcf236ccabb.js\",\"89980\",\"static/chunks/89980-1e653f4986615471.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"78110\",\"static/chunks/78110-c9000034beae1679.js\",\"39577\",\"static/chunks/39577-6e0063d635209dcc.js\",\"85600\",\"static/chunks/85600-d838c560b6e3316b.js\",\"76958\",\"static/chunks/76958-91aef98d2406e983.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"83286\",\"static/chunks/83286-7ca7aed2c53ce442.js\",\"50360\",\"static/chunks/50360-570f674fa7869486.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"38259\",\"static/chunks/38259-bceccd9489884b29.js\",\"45345\",\"static/chunks/45345-40abd9c1679bdc0c.js\",\"5994\",\"static/chunks/app/%5Blng%5D/(service)/layout-aa2e99dfe8f97961.js\"],\"\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "2c:I[63823,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"1448\",\"static/chunks/1448-ba568bcf236ccabb.js\",\"89980\",\"static/chunks/89980-1e653f4986615471.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"78110\",\"static/chunks/78110-c9000034beae1679.js\",\"39577\",\"static/chunks/39577-6e0063d635209dcc.js\",\"85600\",\"static/chunks/85600-d838c560b6e3316b.js\",\"76958\",\"static/chunks/76958-91aef98d2406e983.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"83286\",\"static/chunks/83286-7ca7aed2c53ce442.js\",\"50360\",\"static/chunks/50360-570f674fa7869486.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"38259\",\"static/chunks/38259-bceccd9489884b29.js\",\"45345\",\"static/chunks/45345-40abd9c1679bdc0c.js\",\"5994\",\"static/chunks/app/%5Blng%5D/(service)/layout-aa2e99dfe8f97961.js\"],\"\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "2d:I[42532,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"1448\",\"static/chunks/1448-ba568bcf236ccabb.js\",\"89980\",\"static/chunks/89980-1e653f4986615471.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"78110\",\"static/chunks/78110-c9000034beae1679.js\",\"39577\",\"static/chunks/39577-6e0063d635209dcc.js\",\"85600\",\"static/chunks/85600-d838c560b6e3316b.js\",\"76958\",\"static/chunks/76958-91aef98d2406e983.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"83286\",\"static/chunks/83286-7ca7aed2c53ce442.js\",\"50360\",\"static/chunks/50360-570f674fa7869486.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"38259\",\"static/chunks/38259-bceccd9489884b29.js\",\"45345\",\"static/chunks/45345-40abd9c1679bdc0c.js\",\"5994\",\"static/chunks/app/%5Blng%5D/(service)/layout-aa2e99dfe8f97961.js\"],\"GlobalDialogs\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "2e:I[71452,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"1448\",\"static/chunks/1448-ba568bcf236ccabb.js\",\"89980\",\"static/chunks/89980-1e653f4986615471.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"78110\",\"static/chunks/78110-c9000034beae1679.js\",\"39577\",\"static/chunks/39577-6e0063d635209dcc.js\",\"85600\",\"static/chunks/85600-d838c560b6e3316b.js\",\"76958\",\"static/chunks/76958-91aef98d2406e983.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"83286\",\"static/chunks/83286-7ca7aed2c53ce442.js\",\"50360\",\"static/chunks/50360-570f674fa7869486.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"38259\",\"static/chunks/38259-bceccd9489884b29.js\",\"45345\",\"static/chunks/45345-40abd9c1679bdc0c.js\",\"5994\",\"static/chunks/app/%5Blng%5D/(service)/layout-aa2e99dfe8f97961.js\"],\"SuperOfferDialogWrapper\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "2f:I[68514,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"1448\",\"static/chunks/1448-ba568bcf236ccabb.js\",\"89980\",\"static/chunks/89980-1e653f4986615471.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"78110\",\"static/chunks/78110-c9000034beae1679.js\",\"39577\",\"static/chunks/39577-6e0063d635209dcc.js\",\"85600\",\"static/chunks/85600-d838c560b6e3316b.js\",\"76958\",\"static/chunks/76958-91aef98d2406e983.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"83286\",\"static/chunks/83286-7ca7aed2c53ce442.js\",\"50360\",\"static/chunks/50360-570f674fa7869486.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"38259\",\"static/chunks/38259-bceccd9489884b29.js\",\"45345\",\"static/chunks/45345-40abd9c1679bdc0c.js\",\"5994\",\"static/chunks/app/%5Blng%5D/(service)/layout-aa2e99dfe8f97961.js\"],\"\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "1b:[\"$\",\"$L26\",null,{\"lng\":\"en\",\"auth\":true,\"plan\":\"$undefined\",\"permissions\":{\"viewChannel\":false,\"viewCheatersTags\":false,\"export\":false,\"useTracking\":true,\"viewAllChatNets\":false,\"viewAllTopBuyers\":false,\"searchAdsPostsDays90\":false,\"searchAdsPostsAllTime\":false,\"hideCheaters\":false,\"searchAdsPostsDays180\":false,\"viewFirstAdsPosts\":true,\"viewAllAdsPosts\":false,\"viewFirstTgAdsAdvertisers\":true,\"viewAllTgAdsAdvertisers\":false,\"viewFirstTgAdsCreatives\":true,\"viewAllTgAdsCreatives\":false,\"viewFirstTopBuyers\":true},\"moderatorPermissions\":\"$undefined\",\"categories\":{\"count\":41,\"items\":[{\"id\":{\"categoryId\":\"1Y5Zq3WYB\",\"slug\":\"technology-and-applications\"},\"name\":\"technology \u0026 applications\",\"membersCount\":\"629045633\",\"channelsCount\":54654,\"blocked\":false,\"slug\":\"technology-and-applications\"},{\"id\":{\"categoryId\":\"2MoXrBvGQ\",\"slug\":\"facts\"},\"name\":\"facts\",\"membersCount\":\"84956242\",\"channelsCount\":7465,\"blocked\":false,\"slug\":\"facts\"},{\"id\":{\"categoryId\":\"5wq9Rv4UQ\",\"slug\":\"social-network\"},\"name\":\"social network\",\"membersCount\":\"85615182\",\"channelsCount\":13144,\"blocked\":false,\"slug\":\"social-network\"},{\"id\":{\"categoryId\":\"6TVkBZBWA\",\"slug\":\"nature-and-animals\"},\"name\":\"nature and animals\",\"membersCount\":\"92858336\",\"channelsCount\":16150,\"blocked\":false,\"slug\":\"nature-and-animals\"},{\"id\":{\"categoryId\":\"6rjzTbQIJ\",\"slug\":\"travel\"},\"name\":\"travel\",\"membersCount\":\"110315175\",\"channelsCount\":19179,\"blocked\":false,\"slug\":\"travel\"},{\"id\":{\"categoryId\":\"6ygb4JDbz\",\"slug\":\"music\"},\"name\":\"music\",\"membersCount\":\"390091978\",\"channelsCount\":78308,\"blocked\":false,\"slug\":\"music\"},{\"id\":{\"categoryId\":\"73wy3h7Ga\",\"slug\":\"business\"},\"name\":\"business\",\"membersCount\":\"586938673\",\"channelsCount\":100882,\"blocked\":false,\"slug\":\"business\"},{\"id\":{\"categoryId\":\"7JeRWunw9\",\"slug\":\"cryptocurrencies\"},\"name\":\"cryptocurrencies\",\"membersCount\":\"1923542547\",\"channelsCount\":79429,\"blocked\":false,\"slug\":\"cryptocurrencies\"},{\"id\":{\"categoryId\":\"8k9uJJDqc\",\"slug\":\"games\"},\"name\":\"games\",\"membersCount\":\"701350096\",\"channelsCount\":81877,\"blocked\":false,\"slug\":\"games\"},{\"id\":{\"categoryId\":\"9bO2OWL7y\",\"slug\":\"picture\"},\"name\":\"picture\",\"membersCount\":\"62529435\",\"channelsCount\":11243,\"blocked\":false,\"slug\":\"picture\"},{\"id\":{\"categoryId\":\"A3kRuH61H\",\"slug\":\"art-and-design\"},\"name\":\"art \u0026 design\",\"membersCount\":\"140945607\",\"channelsCount\":39982,\"blocked\":false,\"slug\":\"art-and-design\"},{\"id\":{\"categoryId\":\"CJWBagYw7\",\"slug\":\"books\"},\"name\":\"books\",\"membersCount\":\"143074187\",\"channelsCount\":27208,\"blocked\":false,\"slug\":\"books\"},{\"id\":{\"categoryId\":\"F3fhmhPAw\",\"slug\":\"linguistics\"},\"name\":\"linguistics\",\"membersCount\":\"36618819\",\"channelsCount\":6787,\"blocked\":false,\"slug\":\"linguistics\"},{\"id\":{\"categoryId\":\"GrV1hfO57\",\"slug\":\"bets-and-casino\"},\"name\":\"bets \u0026 casino\",\"membersCount\":\"1722311983\",\"channelsCount\":133787,\"blocked\":false,\"slug\":\"bets-and-casino\"},{\"id\":{\"categoryId\":\"HoTaQVEux\",\"slug\":\"motivation-and-quotes\"},\"name\":\"motivation and quotes\",\"membersCount\":\"181717890\",\"channelsCount\":29552,\"blocked\":false,\"slug\":\"motivation-and-quotes\"},{\"id\":{\"categoryId\":\"Hrq5MdJLi\",\"slug\":\"humor-and-entertainment\"},\"name\":\"humor \u0026 entertainment\",\"membersCount\":\"290119811\",\"channelsCount\":45288,\"blocked\":false,\"slug\":\"humor-and-entertainment\"},{\"id\":{\"categoryId\":\"OBfd25y9m\",\"slug\":\"religion-and-spirituality\"},\"name\":\"religion \u0026 spirituality\",\"membersCount\":\"527963774\",\"channelsCount\":143622,\"blocked\":false,\"slug\":\"religion-and-spirituality\"},{\"id\":{\"categoryId\":\"RGAfBUAl1\",\"slug\":\"telegram\"},\"name\":\"telegram\",\"membersCount\":\"134164431\",\"channelsCount\":5437,\"blocked\":false,\"slug\":\"telegram\"},{\"id\":{\"categoryId\":\"SMb7kkI4F\",\"slug\":\"transport\"},\"name\":\"transport\",\"membersCount\":\"95060622\",\"channelsCount\":18519,\"blocked\":false,\"slug\":\"transport\"},{\"id\":{\"categoryId\":\"V4xyI404d\",\"slug\":\"other\"},\"name\":\"other\",\"membersCount\":\"94891\",\"channelsCount\":17,\"blocked\":false,\"slug\":\"other\"},{\"id\":{\"categoryId\":\"WeTBPd0s1\",\"slug\":\"food-and-drink\"},\"name\":\"food \u0026 drink\",\"membersCount\":\"134362863\",\"channelsCount\":21014,\"blocked\":false,\"slug\":\"food-and-drink\"},{\"id\":{\"categoryId\":\"XBhA1tiMq\",\"slug\":\"sports\"},\"name\":\"sports\",\"membersCount\":\"315287959\",\"channelsCount\":35850,\"blocked\":false,\"slug\":\"sports\"},{\"id\":{\"categoryId\":\"XtJVweWxm\",\"slug\":\"blogs\"},\"name\":\"blogs\",\"membersCount\":\"228088727\",\"channelsCount\":89585,\"blocked\":false,\"slug\":\"blogs\"},{\"id\":{\"categoryId\":\"bjEbAZd4y\",\"slug\":\"sales\"},\"name\":\"sales\",\"membersCount\":\"330657187\",\"channelsCount\":43256,\"blocked\":false,\"slug\":\"sales\"},{\"id\":{\"categoryId\":\"dSaWDWWIX\",\"slug\":\"beauty\"},\"name\":\"beauty\",\"membersCount\":\"213962077\",\"channelsCount\":49601,\"blocked\":false,\"slug\":\"beauty\"},{\"id\":{\"categoryId\":\"gTxJVfQzs\",\"slug\":\"movies\"},\"name\":\"movies\",\"membersCount\":\"1356663051\",\"channelsCount\":118061,\"blocked\":false,\"slug\":\"movies\"},{\"id\":{\"categoryId\":\"he9Ly6T6O\",\"slug\":\"family-and-children\"},\"name\":\"family \u0026 children\",\"membersCount\":\"78258713\",\"channelsCount\":12861,\"blocked\":false,\"slug\":\"family-and-children\"},{\"id\":{\"categoryId\":\"kwuS97PYT\",\"slug\":\"education\"},\"name\":\"education\",\"membersCount\":\"920642757\",\"channelsCount\":130851,\"blocked\":false,\"slug\":\"education\"},{\"id\":{\"categoryId\":\"m6yGG2Ye@\",\"slug\":\"medicine\"},\"name\":\"medicine\",\"membersCount\":\"118554027\",\"channelsCount\":24013,\"blocked\":false,\"slug\":\"medicine\"},{\"id\":{\"categoryId\":\"mf2MkrwoE\",\"slug\":\"politics\"},\"name\":\"politics\",\"membersCount\":\"323359351\",\"channelsCount\":34536,\"blocked\":false,\"slug\":\"politics\"},{\"id\":{\"categoryId\":\"mxorZRxAA\",\"slug\":\"erotic\"},\"name\":\"erotic\",\"membersCount\":\"2034849698\",\"channelsCount\":206190,\"blocked\":false,\"slug\":\"erotic\"},{\"id\":{\"categoryId\":\"rW6jiogfG\",\"slug\":\"marketing-and-pr\"},\"name\":\"marketing \u0026 pr\",\"membersCount\":\"50373577\",\"channelsCount\":7226,\"blocked\":false,\"slug\":\"marketing-and-pr\"},{\"id\":{\"categoryId\":\"t3YiaQgvx\",\"slug\":\"psychology\"},\"name\":\"psychology\",\"membersCount\":\"112685792\",\"channelsCount\":25742,\"blocked\":false,\"slug\":\"psychology\"},{\"id\":{\"categoryId\":\"tyQki9nXm\",\"slug\":\"career\"},\"name\":\"career\",\"membersCount\":\"178468932\",\"channelsCount\":17555,\"blocked\":false,\"slug\":\"career\"},{\"id\":{\"categoryId\":\"yqivk2Kx\",\"slug\":\"legal\"},\"name\":\"legal\",\"membersCount\":\"43193798\",\"channelsCount\":6936,\"blocked\":false,\"slug\":\"legal\"},{\"id\":{\"categoryId\":\"yurVgU76a\",\"slug\":\"economy-and-finance\"},\"name\":\"economy \u0026 finance\",\"membersCount\":\"887891214\",\"channelsCount\":82014,\"blocked\":false,\"slug\":\"economy-and-finance\"},{\"id\":{\"categoryId\":\"zBMeATYGE\",\"slug\":\"healthy-lifestyle\"},\"name\":\"healthy lifestyle\",\"membersCount\":\"114485748\",\"channelsCount\":20542,\"blocked\":false,\"slug\":\"healthy-lifestyle\"},{\"id\":{\"categoryId\":\"MqpAf@IsD\",\"slug\":\"real-estate\"},\"name\":\"real estate\",\"membersCount\":\"65090835\",\"channelsCount\":16170,\"blocked\":false,\"slug\":\"real-estate\"},{\"id\":{\"categoryId\":\"GGBK0Mbm$\",\"slug\":\"home-and-architecture\"},\"name\":\"home \u0026 architecture\",\"membersCount\":\"55133453\",\"channelsCount\":10226,\"blocked\":false,\"slug\":\"home-and-architecture\"},{\"id\":{\"categoryId\":\"wE1@n4moe\",\"slug\":\"prohibited-content\"},\"name\":\"prohibited content\",\"membersCount\":\"234790564\",\"channelsCount\":26022,\"blocked\":true,\"slug\":\"prohibited-content\"},{\"id\":{\"categoryId\":\"1IKDv6$co\",\"slug\":\"news-and-media\"},\"name\":\"news \u0026 media\",\"membersCount\":\"1027013394\",\"channelsCount\":68136,\"blocked\":false,\"slug\":\"news-and-media\"}]},\"countries\":{\"count\":85,\"items\":[{\"id\":{\"countryId\":\"india\"},\"name\":\"india\",\"channelsCount\":266105,\"membersCount\":\"2712946810\"},{\"id\":{\"countryId\":\"pakistan\"},\"name\":\"pakistan\",\"channelsCount\":16,\"membersCount\":\"380349\"},{\"id\":{\"countryId\":\"israel\"},\"name\":\"israel\",\"channelsCount\":4218,\"membersCount\":\"30732307\"},{\"id\":{\"countryId\":\"greece\"},\"name\":\"greece\",\"channelsCount\":369,\"membersCount\":\"1128600\"},{\"id\":{\"countryId\":\"france\"},\"name\":\"france\",\"channelsCount\":25663,\"membersCount\":\"231547864\"},{\"id\":{\"countryId\":\"korea\"},\"name\":\"korea\",\"channelsCount\":6119,\"membersCount\":\"23527219\"},{\"id\":{\"countryId\":\"saudi_arabia\"},\"name\":\"saudi_arabia\",\"channelsCount\":64064,\"membersCount\":\"312342541\"},{\"id\":{\"countryId\":\"russia\"},\"name\":\"russia\",\"channelsCount\":574651,\"membersCount\":\"3813803239\"},{\"id\":{\"countryId\":\"oman\"},\"name\":\"oman\",\"channelsCount\":2,\"membersCount\":\"23194\"},{\"id\":{\"countryId\":\"serbia\"},\"name\":\"serbia\",\"channelsCount\":1079,\"membersCount\":\"3616297\"},{\"id\":{\"countryId\":\"somalia\"},\"name\":\"somalia\",\"channelsCount\":5,\"membersCount\":\"154776\"},{\"id\":{\"countryId\":\"syria\"},\"name\":\"syria\",\"channelsCount\":24,\"membersCount\":\"690492\"},{\"id\":{\"countryId\":\"ukraine\"},\"name\":\"ukraine\",\"channelsCount\":52691,\"membersCount\":\"372538569\"},{\"id\":{\"countryId\":\"estonia\"},\"name\":\"estonia\",\"channelsCount\":2,\"membersCount\":\"36590\"},{\"id\":{\"countryId\":\"romania\"},\"name\":\"romania\",\"channelsCount\":691,\"membersCount\":\"2874060\"},{\"id\":{\"countryId\":\"lebanon\"},\"name\":\"lebanon\",\"channelsCount\":2,\"membersCount\":\"41234\"},{\"id\":{\"countryId\":\"armenia\"},\"name\":\"armenia\",\"channelsCount\":3665,\"membersCount\":\"10248265\"},{\"id\":{\"countryId\":\"croatia\"},\"name\":\"croatia\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"countryId\":\"brazil\"},\"name\":\"brazil\",\"channelsCount\":28924,\"membersCount\":\"252162848\"},{\"id\":{\"countryId\":\"bahrain\"},\"name\":\"bahrain\",\"channelsCount\":1,\"membersCount\":\"10540\"},{\"id\":{\"countryId\":\"taiwan\"},\"name\":\"taiwan\",\"channelsCount\":2,\"membersCount\":\"6745\"},{\"id\":{\"countryId\":\"belarus\"},\"name\":\"belarus\",\"channelsCount\":5551,\"membersCount\":\"20346124\"},{\"id\":{\"countryId\":\"indonesia\"},\"name\":\"indonesia\",\"channelsCount\":51848,\"membersCount\":\"509013746\"},{\"id\":{\"countryId\":\"moldova\"},\"name\":\"moldova\",\"channelsCount\":832,\"membersCount\":\"3254301\"},{\"id\":{\"countryId\":\"turkmenistan\"},\"name\":\"turkmenistan\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"countryId\":\"portugal\"},\"name\":\"portugal\",\"channelsCount\":1730,\"membersCount\":\"9767990\"},{\"id\":{\"countryId\":\"jordan\"},\"name\":\"jordan\",\"channelsCount\":3,\"membersCount\":\"41330\"},{\"id\":{\"countryId\":\"norway\"},\"name\":\"norway\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"countryId\":\"libya\"},\"name\":\"libya\",\"channelsCount\":5,\"membersCount\":\"83889\"},{\"id\":{\"countryId\":\"malaysia\"},\"name\":\"malaysia\",\"channelsCount\":50518,\"membersCount\":\"695714526\"},{\"id\":{\"countryId\":\"palestine\"},\"name\":\"palestine\",\"channelsCount\":7,\"membersCount\":\"118836\"},{\"id\":{\"countryId\":\"bulgaria\"},\"name\":\"bulgaria\",\"channelsCount\":27,\"membersCount\":\"166141\"},{\"id\":{\"countryId\":\"uae\"},\"name\":\"uae\",\"channelsCount\":4885,\"membersCount\":\"28825412\"},{\"id\":{\"countryId\":\"yemen\"},\"name\":\"yemen\",\"channelsCount\":22,\"membersCount\":\"636632\"},{\"id\":{\"countryId\":\"tunisia\"},\"name\":\"tunisia\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"countryId\":\"united_kingdom\"},\"name\":\"united_kingdom\",\"channelsCount\":10301,\"membersCount\":\"58934501\"},{\"id\":{\"countryId\":\"uzbekistan\"},\"name\":\"uzbekistan\",\"channelsCount\":64187,\"membersCount\":\"455178694\"},{\"id\":{\"countryId\":\"kenya\"},\"name\":\"kenya\",\"channelsCount\":14,\"membersCount\":\"148504\"},{\"id\":{\"countryId\":\"sudan\"},\"name\":\"sudan\",\"channelsCount\":3,\"membersCount\":\"43485\"},{\"id\":{\"countryId\":\"nigeria\"},\"name\":\"nigeria\",\"channelsCount\":7660,\"membersCount\":\"88370696\"},{\"id\":{\"countryId\":\"bosnia_and_herzegovina\"},\"name\":\"bosnia_and_herzegovina\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"countryId\":\"canada\"},\"name\":\"canada\",\"channelsCount\":7,\"membersCount\":\"61712\"},{\"id\":{\"countryId\":\"iraq\"},\"name\":\"iraq\",\"channelsCount\":132144,\"membersCount\":\"815596957\"},{\"id\":{\"countryId\":\"finland\"},\"name\":\"finland\",\"channelsCount\":4128,\"membersCount\":\"46390034\"},{\"id\":{\"countryId\":\"azerbaijan\"},\"name\":\"azerbaijan\",\"channelsCount\":4107,\"membersCount\":\"25896245\"},{\"id\":{\"countryId\":\"slovakia\"},\"name\":\"slovakia\",\"channelsCount\":4,\"membersCount\":\"7536\"},{\"id\":{\"countryId\":\"kazakhstan\"},\"name\":\"kazakhstan\",\"channelsCount\":8803,\"membersCount\":\"42192418\"},{\"id\":{\"countryId\":\"mongolia\"},\"name\":\"mongolia\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"countryId\":\"algeria\"},\"name\":\"algeria\",\"channelsCount\":6,\"membersCount\":\"107200\"},{\"id\":{\"countryId\":\"japan\"},\"name\":\"japan\",\"channelsCount\":4960,\"membersCount\":\"33244205\"},{\"id\":{\"countryId\":\"qatar\"},\"name\":\"qatar\",\"channelsCount\":1,\"membersCount\":\"4354\"},{\"id\":{\"countryId\":\"czech_republic\"},\"name\":\"czech_republic\",\"channelsCount\":751,\"membersCount\":\"2470337\"},{\"id\":{\"countryId\":\"georgia\"},\"name\":\"georgia\",\"channelsCount\":1281,\"membersCount\":\"3780214\"},{\"id\":{\"countryId\":\"kyrgyzstan\"},\"name\":\"kyrgyzstan\",\"channelsCount\":2635,\"membersCount\":\"9034199\"},{\"id\":{\"countryId\":\"morocco\"},\"name\":\"morocco\",\"channelsCount\":4,\"membersCount\":\"65360\"},{\"id\":{\"countryId\":\"iran\"},\"name\":\"iran\",\"channelsCount\":233475,\"membersCount\":\"1713629436\"},{\"id\":{\"countryId\":\"ethiopia\"},\"name\":\"ethiopia\",\"channelsCount\":16450,\"membersCount\":\"133256672\"},{\"id\":{\"countryId\":\"germany\"},\"name\":\"germany\",\"channelsCount\":11173,\"membersCount\":\"64766819\"},{\"id\":{\"countryId\":\"china\"},\"name\":\"china\",\"channelsCount\":112646,\"membersCount\":\"981566530\"},{\"id\":{\"countryId\":\"tajikistan\"},\"name\":\"tajikistan\",\"channelsCount\":4165,\"membersCount\":\"14065921\"},{\"id\":{\"countryId\":\"afghanistan\"},\"name\":\"afghanistan\",\"channelsCount\":13,\"membersCount\":\"158930\"},{\"id\":{\"countryId\":\"egypt\"},\"name\":\"egypt\",\"channelsCount\":19354,\"membersCount\":\"96702440\"},{\"id\":{\"countryId\":\"sweden\"},\"name\":\"sweden\",\"channelsCount\":12,\"membersCount\":\"28664\"},{\"id\":{\"countryId\":\"turkey\"},\"name\":\"turkey\",\"channelsCount\":18918,\"membersCount\":\"128267731\"},{\"id\":{\"countryId\":\"singapore\"},\"name\":\"singapore\",\"channelsCount\":4029,\"membersCount\":\"26894855\"},{\"id\":{\"countryId\":\"australia\"},\"name\":\"australia\",\"channelsCount\":1,\"membersCount\":\"1202\"},{\"id\":{\"countryId\":\"slovenia\"},\"name\":\"slovenia\",\"channelsCount\":1,\"membersCount\":\"2311\"},{\"id\":{\"countryId\":\"poland\"},\"name\":\"poland\",\"channelsCount\":2705,\"membersCount\":\"8496681\"},{\"id\":{\"countryId\":\"netherlands\"},\"name\":\"netherlands\",\"channelsCount\":1273,\"membersCount\":\"6297293\"},{\"id\":{\"countryId\":\"vietnam\"},\"name\":\"vietnam\",\"channelsCount\":9503,\"membersCount\":\"104689278\"},{\"id\":{\"countryId\":\"italy\"},\"name\":\"italy\",\"channelsCount\":18029,\"membersCount\":\"151223885\"},{\"id\":{\"countryId\":\"spain\"},\"name\":\"spain\",\"channelsCount\":57413,\"membersCount\":\"666697958\"},{\"id\":{\"countryId\":\"thailand\"},\"name\":\"thailand\",\"channelsCount\":3087,\"membersCount\":\"31434043\"},{\"id\":{\"countryId\":\"sri_lanka\"},\"name\":\"sri_lanka\",\"channelsCount\":3117,\"membersCount\":\"16225175\"},{\"id\":{\"countryId\":\"austria\"},\"name\":\"austria\",\"channelsCount\":201,\"membersCount\":\"1099857\"},{\"id\":{\"countryId\":\"cambodia\"},\"name\":\"cambodia\",\"channelsCount\":5548,\"membersCount\":\"19793496\"},{\"id\":{\"countryId\":\"usa\"},\"name\":\"usa\",\"channelsCount\":36933,\"membersCount\":\"223941779\"},{\"id\":{\"countryId\":\"bangladesh\"},\"name\":\"bangladesh\",\"channelsCount\":15492,\"membersCount\":\"64579495\"},{\"id\":{\"countryId\":\"myanmar\"},\"name\":\"myanmar\",\"channelsCount\":26803,\"membersCount\":\"391944457\"},{\"id\":{\"countryId\":\"latvia\"},\"name\":\"latvia\",\"channelsCount\":380,\"membersCount\":\"778280\"},{\"id\":{\"countryId\":\"lithuania\"},\"name\":\"lithuania\",\"channelsCount\":295,\"membersCount\":\"746868\"},{\"id\":{\"countryId\":\"colombia\"},\"name\":\"colombia\",\"channelsCount\":224,\"membersCount\":\"2616973\"},{\"id\":{\"countryId\":\"chile\"},\"name\":\"chile\",\"channelsCount\":111,\"membersCount\":\"803570\"},{\"id\":{\"countryId\":\"philippines\"},\"name\":\"philippines\",\"channelsCount\":182,\"membersCount\":\"1848265\"},{\"id\":{\"countryId\":\"international\"},\"name\":\"international\",\"channelsCount\":513,\"membersCount\":\"1206157660\"}]},\"languages\":{\"count\":114,\"items\":[{\"id\":{\"languageId\":\"am\"},\"name\":\"am\",\"channelsCount\":11379,\"membersCount\":\"105433871\"},{\"id\":{\"languageId\":\"ve\"},\"name\":\"ve\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"ha\"},\"name\":\"ha\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"tl\"},\"name\":\"tl\",\"channelsCount\":509,\"membersCount\":\"4258563\"},{\"id\":{\"languageId\":\"he\"},\"name\":\"he\",\"channelsCount\":2980,\"membersCount\":\"20129255\"},{\"id\":{\"languageId\":\"eo\"},\"name\":\"eo\",\"channelsCount\":116,\"membersCount\":\"700017\"},{\"id\":{\"languageId\":\"ka\"},\"name\":\"ka\",\"channelsCount\":189,\"membersCount\":\"455623\"},{\"id\":{\"languageId\":\"gl\"},\"name\":\"gl\",\"channelsCount\":54,\"membersCount\":\"310080\"},{\"id\":{\"languageId\":\"da\"},\"name\":\"da\",\"channelsCount\":56,\"membersCount\":\"66820\"},{\"id\":{\"languageId\":\"cs\"},\"name\":\"cs\",\"channelsCount\":338,\"membersCount\":\"831223\"},{\"id\":{\"languageId\":\"ug\"},\"name\":\"ug\",\"channelsCount\":62,\"membersCount\":\"59654\"},{\"id\":{\"languageId\":\"pl\"},\"name\":\"pl\",\"channelsCount\":1868,\"membersCount\":\"5569418\"},{\"id\":{\"languageId\":\"hr\"},\"name\":\"hr\",\"channelsCount\":10,\"membersCount\":\"13831\"},{\"id\":{\"languageId\":\"uz\"},\"name\":\"uz\",\"channelsCount\":46730,\"membersCount\":\"379443506\"},{\"id\":{\"languageId\":\"sa\"},\"name\":\"sa\",\"channelsCount\":1,\"membersCount\":\"2306\"},{\"id\":{\"languageId\":\"jv\"},\"name\":\"jv\",\"channelsCount\":2108,\"membersCount\":\"23453860\"},{\"id\":{\"languageId\":\"fr\"},\"name\":\"fr\",\"channelsCount\":21605,\"membersCount\":\"204778487\"},{\"id\":{\"languageId\":\"bo\"},\"name\":\"bo\",\"channelsCount\":9,\"membersCount\":\"14900\"},{\"id\":{\"languageId\":\"mr\"},\"name\":\"mr\",\"channelsCount\":2171,\"membersCount\":\"28525912\"},{\"id\":{\"languageId\":\"ig\"},\"name\":\"ig\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"bs\"},\"name\":\"bs\",\"channelsCount\":161,\"membersCount\":\"891283\"},{\"id\":{\"languageId\":\"ee\"},\"name\":\"ee\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"ht\"},\"name\":\"ht\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"ja\"},\"name\":\"ja\",\"channelsCount\":943,\"membersCount\":\"7074224\"},{\"id\":{\"languageId\":\"sl\"},\"name\":\"sl\",\"channelsCount\":20,\"membersCount\":\"65119\"},{\"id\":{\"languageId\":\"fa\"},\"name\":\"fa\",\"channelsCount\":214804,\"membersCount\":\"1634093528\"},{\"id\":{\"languageId\":\"ms\"},\"name\":\"ms\",\"channelsCount\":3820,\"membersCount\":\"26748490\"},{\"id\":{\"languageId\":\"sw\"},\"name\":\"sw\",\"channelsCount\":2,\"membersCount\":\"9141\"},{\"id\":{\"languageId\":\"th\"},\"name\":\"th\",\"channelsCount\":2436,\"membersCount\":\"29352764\"},{\"id\":{\"languageId\":\"vi\"},\"name\":\"vi\",\"channelsCount\":8315,\"membersCount\":\"97400684\"},{\"id\":{\"languageId\":\"tr\"},\"name\":\"tr\",\"channelsCount\":12421,\"membersCount\":\"102886130\"},{\"id\":{\"languageId\":\"ln\"},\"name\":\"ln\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"zh\"},\"name\":\"zh\",\"channelsCount\":109386,\"membersCount\":\"965172671\"},{\"id\":{\"languageId\":\"kk\"},\"name\":\"kk\",\"channelsCount\":3190,\"membersCount\":\"21218246\"},{\"id\":{\"languageId\":\"it\"},\"name\":\"it\",\"channelsCount\":14710,\"membersCount\":\"131504471\"},{\"id\":{\"languageId\":\"te\"},\"name\":\"te\",\"channelsCount\":477,\"membersCount\":\"4145395\"},{\"id\":{\"languageId\":\"ng\"},\"name\":\"ng\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"de\"},\"name\":\"de\",\"channelsCount\":9216,\"membersCount\":\"55750381\"},{\"id\":{\"languageId\":\"tt\"},\"name\":\"tt\",\"channelsCount\":253,\"membersCount\":\"920034\"},{\"id\":{\"languageId\":\"st\"},\"name\":\"st\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"nn\"},\"name\":\"nn\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"es\"},\"name\":\"es\",\"channelsCount\":47345,\"membersCount\":\"566956971\"},{\"id\":{\"languageId\":\"tg\"},\"name\":\"tg\",\"channelsCount\":860,\"membersCount\":\"3590662\"},{\"id\":{\"languageId\":\"sd\"},\"name\":\"sd\",\"channelsCount\":1,\"membersCount\":\"1180\"},{\"id\":{\"languageId\":\"qu\"},\"name\":\"qu\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"tn\"},\"name\":\"tn\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"ne\"},\"name\":\"ne\",\"channelsCount\":45,\"membersCount\":\"129688\"},{\"id\":{\"languageId\":\"xh\"},\"name\":\"xh\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"fi\"},\"name\":\"fi\",\"channelsCount\":79,\"membersCount\":\"157577\"},{\"id\":{\"languageId\":\"bg\"},\"name\":\"bg\",\"channelsCount\":309,\"membersCount\":\"700332\"},{\"id\":{\"languageId\":\"tk\"},\"name\":\"tk\",\"channelsCount\":198,\"membersCount\":\"1721672\"},{\"id\":{\"languageId\":\"sg\"},\"name\":\"sg\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"se\"},\"name\":\"se\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"su\"},\"name\":\"su\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"sn\"},\"name\":\"sn\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"gu\"},\"name\":\"gu\",\"channelsCount\":972,\"membersCount\":\"6970901\"},{\"id\":{\"languageId\":\"ak\"},\"name\":\"ak\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"so\"},\"name\":\"so\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"ca\"},\"name\":\"ca\",\"channelsCount\":366,\"membersCount\":\"852367\"},{\"id\":{\"languageId\":\"mn\"},\"name\":\"mn\",\"channelsCount\":137,\"membersCount\":\"665680\"},{\"id\":{\"languageId\":\"kn\"},\"name\":\"kn\",\"channelsCount\":2235,\"membersCount\":\"12459669\"},{\"id\":{\"languageId\":\"en\"},\"name\":\"en\",\"channelsCount\":297101,\"membersCount\":\"4496838139\"},{\"id\":{\"languageId\":\"mt\"},\"name\":\"mt\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"ko\"},\"name\":\"ko\",\"channelsCount\":3286,\"membersCount\":\"12192825\"},{\"id\":{\"languageId\":\"bn\"},\"name\":\"bn\",\"channelsCount\":10715,\"membersCount\":\"48850880\"},{\"id\":{\"languageId\":\"et\"},\"name\":\"et\",\"channelsCount\":98,\"membersCount\":\"227682\"},{\"id\":{\"languageId\":\"hy\"},\"name\":\"hy\",\"channelsCount\":1430,\"membersCount\":\"4789340\"},{\"id\":{\"languageId\":\"ss\"},\"name\":\"ss\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"wo\"},\"name\":\"wo\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"zu\"},\"name\":\"zu\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"fo\"},\"name\":\"fo\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"ku\"},\"name\":\"ku\",\"channelsCount\":50,\"membersCount\":\"236169\"},{\"id\":{\"languageId\":\"cy\"},\"name\":\"cy\",\"channelsCount\":1,\"membersCount\":\"2350\"},{\"id\":{\"languageId\":\"an\"},\"name\":\"an\",\"channelsCount\":1,\"membersCount\":\"2348\"},{\"id\":{\"languageId\":\"el\"},\"name\":\"el\",\"channelsCount\":263,\"membersCount\":\"897786\"},{\"id\":{\"languageId\":\"rn\"},\"name\":\"rn\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"ky\"},\"name\":\"ky\",\"channelsCount\":538,\"membersCount\":\"1817591\"},{\"id\":{\"languageId\":\"nl\"},\"name\":\"nl\",\"channelsCount\":608,\"membersCount\":\"2889787\"},{\"id\":{\"languageId\":\"hu\"},\"name\":\"hu\",\"channelsCount\":172,\"membersCount\":\"367904\"},{\"id\":{\"languageId\":\"ts\"},\"name\":\"ts\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"ur\"},\"name\":\"ur\",\"channelsCount\":497,\"membersCount\":\"1466437\"},{\"id\":{\"languageId\":\"hi\"},\"name\":\"hi\",\"channelsCount\":19628,\"membersCount\":\"241160607\"},{\"id\":{\"languageId\":\"sr\"},\"name\":\"sr\",\"channelsCount\":179,\"membersCount\":\"1115122\"},{\"id\":{\"languageId\":\"ar\"},\"name\":\"ar\",\"channelsCount\":218251,\"membersCount\":\"1249276394\"},{\"id\":{\"languageId\":\"sv\"},\"name\":\"sv\",\"channelsCount\":88,\"membersCount\":\"125402\"},{\"id\":{\"languageId\":\"af\"},\"name\":\"af\",\"channelsCount\":42,\"membersCount\":\"247335\"},{\"id\":{\"languageId\":\"lg\"},\"name\":\"lg\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"ny\"},\"name\":\"ny\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"be\"},\"name\":\"be\",\"channelsCount\":278,\"membersCount\":\"521302\"},{\"id\":{\"languageId\":\"ps\"},\"name\":\"ps\",\"channelsCount\":1369,\"membersCount\":\"4228194\"},{\"id\":{\"languageId\":\"id\"},\"name\":\"id\",\"channelsCount\":13316,\"membersCount\":\"159066832\"},{\"id\":{\"languageId\":\"ta\"},\"name\":\"ta\",\"channelsCount\":1248,\"membersCount\":\"7240433\"},{\"id\":{\"languageId\":\"ml\"},\"name\":\"ml\",\"channelsCount\":2398,\"membersCount\":\"36509512\"},{\"id\":{\"languageId\":\"la\"},\"name\":\"la\",\"channelsCount\":1,\"membersCount\":\"2074\"},{\"id\":{\"languageId\":\"ru\"},\"name\":\"ru\",\"channelsCount\":568636,\"membersCount\":\"3718427704\"},{\"id\":{\"languageId\":\"az\"},\"name\":\"az\",\"channelsCount\":3325,\"membersCount\":\"23032676\"},{\"id\":{\"languageId\":\"ro\"},\"name\":\"ro\",\"channelsCount\":836,\"membersCount\":\"2924995\"},{\"id\":{\"languageId\":\"sk\"},\"name\":\"sk\",\"channelsCount\":274,\"membersCount\":\"1124614\"},{\"id\":{\"languageId\":\"pt\"},\"name\":\"pt\",\"channelsCount\":26690,\"membersCount\":\"234496868\"},{\"id\":{\"languageId\":\"bm\"},\"name\":\"bm\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"uk\"},\"name\":\"uk\",\"channelsCount\":40302,\"membersCount\":\"299642955\"},{\"id\":{\"languageId\":\"rw\"},\"name\":\"rw\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"ti\"},\"name\":\"ti\",\"channelsCount\":0,\"membersCount\":\"0\"},{\"id\":{\"languageId\":\"km\"},\"name\":\"km\",\"channelsCount\":4618,\"membersCount\":\"17041688\"},{\"id\":{\"languageId\":\"pa\"},\"name\":\"pa\",\"channelsCount\":564,\"membersCount\":\"1924728\"},{\"id\":{\"languageId\":\"no\"},\"name\":\"no\",\"channelsCount\":264,\"membersCount\":\"999919\"},{\"id\":{\"languageId\":\"arz\"},\"name\":\"arz\",\"channelsCount\":19,\"membersCount\":\"69237\"},{\"id\":{\"languageId\":\"si\"},\"name\":\"si\",\"channelsCount\":2119,\"membersCount\":\"10745049\"},{\"id\":{\"languageId\":\"my\"},\"name\":\"my\",\"channelsCount\":23263,\"membersCount\":\"365798618\"},{\"id\":{\"languageId\":\"ba\"},\"name\":\"ba\",\"channelsCount\":40,\"membersCount\":\"56839\"},{\"id\":{\"languageId\":\"yi\"},\"name\":\"yi\",\"channelsCount\":73,\"membersCount\":\"331000\"},{\"id\":{\"languageId\":\"ce\"},\"name\":\"ce\",\"channelsCount\":131,\"membersCount\":\"273659\"},{\"id\":{\"languageId\":\"mk\"},\"name\":\"mk\",\"channelsCount\":22,\"membersCount\":\"81777\"},{\"id\":{\"languageId\":\"eu\"},\"name\":\"eu\",\"channelsCount\":32,\"membersCount\":\"53494\"}]},\"features\":{\"showDiscountBanner\":false,\"openChannelInNewTab\":true,\"showImages\":true,\"showAdsIndex\":false,\"ambassadorAds\":\"\"},\"fingerprint\":\"4c9967c9-107c-5522-bb9d-4df8d9821b3d\",\"ipCountry\":\"$undefined\",\"children\":[[\"$\",\"$27\",null,{\"children\":[\"$\",\"$L28\",null,{}]}],[\"$\",\"$L29\",null,{}],[\"$\",\"$L2a\",null,{}],[\"$\",\"$L2b\",null,{\"features\":{}}],[\"$\",\"main\",null,{\"className\":\"flex flex-col items-start flex-1 py-4 sm:py-11\",\"children\":[\"$\",\"$L16\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\",\"$17\",\"children\",\"(service)\",\"children\"],\"loading\":\"$undefined\",\"loadingStyles\":\"$undefined\",\"loadingScripts\":\"$undefined\",\"hasLoading\":false,\"error\":\"$undefined\",\"errorStyles\":\"$undefined\",\"errorScripts\":\"$undefined\",\"template\":[\"$\",\"$L19\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":\"$undefined\",\"notFoundStyles\":\"$undefined\",\"styles\":null}]}],[\"$\",\"$L2c\",null,{\"features\":{}}],[\"$\",\"$L2d\",null,{}],[\"$\",\"$L2e\",null,{}],[\"$\",\"$L2f\",null,{}]]}]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "1d:[[\"$\",\"meta\",\"0\",{\"name\":\"viewport\",\"content\":\"width=device-width, initial-scale=1, maximum-scale=1\"}],[\"$\",\"meta\",\"1\",{\"charSet\":\"utf-8\"}],[\"$\",\"title\",\"2\",{\"children\":\"baji 🇧🇩 - @baji_bgd - Telemetrio - Publications\"}],[\"$\",\"meta\",\"3\",{\"name\":\"description\",\"content\":\"baji 🇧🇩 - @baji_bgd in Telegram on Telemetrio - Publications in the Telegram channel\"}],[\"$\",\"meta\",\"4\",{\"name\":\"author\",\"content\":\"telemetr.io\"}],[\"$\",\"link\",\"5\",{\"rel\":\"manifest\",\"href\":\"/manifest.webmanifest\"}],[\"$\",\"link\",\"6\",{\"rel\":\"canonical\",\"href\":\"https://telemetr.io/en/channels/1829680439-baji_bgd/publish\"}],[\"$\",\"link\",\"7\",{\"rel\":\"alternate\",\"hrefLang\":\"x-default\",\"href\":\"https://telemetr.io/en/channels/1829680439-baji_bgd/publish\"}],[\"$\",\"link\",\"8\",{\"rel\":\"alternate\",\"hrefLang\":\"en\",\"href\":\"https://telemetr.io/en/channels/1829680439-baji_bgd/publish\"}],[\"$\",\"link\",\"9\",{\"rel\":\"alternate\",\"hrefLang\":\"ar\",\"href\":\"https://telemetr.io/ar/channels/1829680439-baji_bgd/publish\"}],[\"$\",\"link\",\"10\",{\"rel\":\"alternate\",\"hrefLang\":\"es\",\"href\":\"https://telemetr.io/es/channels/1829680439-baji_bgd/publish\"}],[\"$\",\"link\",\"11\",{\"rel\":\"alternate\",\"hrefLang\":\"fa\",\"href\":\"https://telemetr.io/fa/channels/1829680439-baji_bgd/publish\"}],[\"$\",\"link\",\"12\",{\"rel\":\"alternate\",\"hrefLang\":\"ru\",\"href\":\"https://telemetr.io/ru/channels/1829680439-baji_bgd/publish\"}],[\"$\",\"link\",\"13\",{\"rel\":\"alternate\",\"hrefLang\":\"uk\",\"href\":\"https://telemetr.io/uk/channels/1829680439-baji_bgd/publish\"}],[\"$\",\"link\",\"14\",{\"rel\":\"alternate\",\"hrefLang\":\"uz\",\"href\":\"https://telemetr.io/uz/channels/1829680439-baji_bgd/publish\"}],[\"$\",\"meta\",\"15\",{\"property\":\"og:title\",\"content\":\"baji 🇧🇩 - @baji_bgd\"}],[\"$\",\"meta\",\"16\",{\"property\":\"og:description\",\"content\":\"baji 🇧🇩 - @baji_bgd in Telegram on Telemetrio\"}],[\"$\",\"meta\",\"17\",{\"name\":\"twitter:card\",\"content\":\"summary\"}],[\"$\",\"meta\",\"18\",{\"name\":\"twitter:title\",\"content\":\"baji 🇧🇩 - @baji_bgd\"}],[\"$\",\"meta\",\"19\",{\"name\":\"twitter:description\",\"content\":\"baji 🇧🇩 - @baji_bgd in Telegram on Telemetrio\"}],[\"$\",\"link\",\"20\",{\"rel\":\"icon\",\"href\":\"/favicon.ico\",\"type\":\"image/x-icon\",\"sizes\":\"32x32\"}],[\"$\",\"link\",\"21\",{\"rel\":\"icon\",\"href\":\"/icon.svg?9e8ae486b6590917\",\"type\":\"image/svg+xml\",\"sizes\":\"any\"}],[\"$\",\"link\",\"22\",{\"rel\":\"icon\",\"href\":\"/icon1.ico?6bbf3a51efb3e540\",\"type\":\"image/x-icon\",\"sizes\":\"16x16\"}],[\"$\",\"link\",\"23\",{\"rel\":\"icon\",\"href\":\"/icon2.ico?4e3fe26fdc910605\",\"type\":\"image/x-icon\",\"sizes\":\"24x24\"}],[\"$\",\"link\",\"24\",{\"rel\":\"icon\",\"href\":\"/icon3.ico?13288ad692c389e6\",\"type\":\"image/x-icon\",\"sizes\":\"48x48\"}],[\"$\",\"link\",\"25\",{\"rel\":\"icon\",\"href\":\"/icon4.ico?802efc8d36f2fee9\",\"type\":\"image/x-icon\",\"sizes\":\"64x64\"}],[\"$\",\"link\",\"26\",{\"rel\":\"icon\",\"href\":\"/icon5.ico?f2d52d5dccdccc0b\",\"type\":\"image/x-icon\",\"sizes\":\"96x96\"}],[\"$\",\"link\",\"27\",{\"rel\":\"icon\",\"href\":\"/icon6.ico?2f133ca7e18ea7a3\",\"type\":\"image/x-icon\",\"sizes\":\"144x144\"}],[\"$\",\"link\",\"28\",{\"rel\":\"apple-touch-icon\",\"href\":\"/apple-icon.png?a9b2beb703eb6cf6\",\"type\":\"image/png\",\"sizes\":\"180x180\"}],[\"$\",\"meta\",\"29\",{\"name\":\"next-size-adjust\"}]]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "14:null\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "30:I[89169,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"1448\",\"static/chunks/1448-ba568bcf236ccabb.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"85600\",\"static/chunks/85600-d838c560b6e3316b.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"50360\",\"static/chunks/50360-570f674fa7869486.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"17434\",\"static/chunks/17434-0352ecce102e46f3.js\",\"31603\",\"static/chunks/31603-36ff12160e256f37.js\",\"92072\",\"static/chunks/app/%5Blng%5D/(service)/channels/%5Bid%5D/layout-c116489e26a8a7a2.js\"],\"\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "31:I[83044,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"1448\",\"static/chunks/1448-ba568bcf236ccabb.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"85600\",\"static/chunks/85600-d838c560b6e3316b.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"50360\",\"static/chunks/50360-570f674fa7869486.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"17434\",\"static/chunks/17434-0352ecce102e46f3.js\",\"31603\",\"static/chunks/31603-36ff12160e256f37.js\",\"92072\",\"static/chunks/app/%5Blng%5D/(service)/channels/%5Bid%5D/layout-c116489e26a8a7a2.js\"],\"\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "32:I[51455,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"1448\",\"static/chunks/1448-ba568bcf236ccabb.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"85600\",\"static/chunks/85600-d838c560b6e3316b.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"50360\",\"static/chunks/50360-570f674fa7869486.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"17434\",\"static/chunks/17434-0352ecce102e46f3.js\",\"31603\",\"static/chunks/31603-36ff12160e256f37.js\",\"92072\",\"static/chunks/app/%5Blng%5D/(service)/channels/%5Bid%5D/layout-c116489e26a8a7a2.js\"],\"\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "33:I[64412,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"1448\",\"static/chunks/1448-ba568bcf236ccabb.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"85600\",\"static/chunks/85600-d838c560b6e3316b.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"50360\",\"static/chunks/50360-570f674fa7869486.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"17434\",\"static/chunks/17434-0352ecce102e46f3.js\",\"31603\",\"static/chunks/31603-36ff12160e256f37.js\",\"92072\",\"static/chunks/app/%5Blng%5D/(service)/channels/%5Bid%5D/layout-c116489e26a8a7a2.js\"],\"\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "34:I[67473,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"1448\",\"static/chunks/1448-ba568bcf236ccabb.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"85600\",\"static/chunks/85600-d838c560b6e3316b.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"50360\",\"static/chunks/50360-570f674fa7869486.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"17434\",\"static/chunks/17434-0352ecce102e46f3.js\",\"31603\",\"static/chunks/31603-36ff12160e256f37.js\",\"92072\",\"static/chunks/app/%5Blng%5D/(service)/channels/%5Bid%5D/layout-c116489e26a8a7a2.js\"],\"\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "42:I[68326,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"1448\",\"static/chunks/1448-ba568bcf236ccabb.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"85600\",\"static/chunks/85600-d838c560b6e3316b.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"50360\",\"static/chunks/50360-570f674fa7869486.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"17434\",\"static/chunks/17434-0352ecce102e46f3.js\",\"31603\",\"static/chunks/31603-36ff12160e256f37.js\",\"92072\",\"static/chunks/app/%5Blng%5D/(service)/channels/%5Bid%5D/layout-c116489e26a8a7a2.js\"],\"\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "36:{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"}\n37:{\"verified\":false,\"scam\":false,\"fake\":false,\"restricted\":false}\n39:{\"participants\":0.20746865757233585,\"views\":0.4530670859847248,\"appeal\":false}\n38:{\"verified\":false,\"cheater\":false,\"blocked\":false,\"onlyForOwners\":false,\"cheaterInfo\":\"$39\"}\n3b:{\"languageId\":\"bn\"}\n3a:{\"id\":\"$3b\",\"name\":\"bn\",\"position\":113}\n3d:{\"countryId\":\"bangladesh\"}\n3c:{\"id\":\"$3d\",\"name\":\"bangladesh\",\"position\":144}\n40:{\"categoryId\":\"GrV1hfO57\",\"slug\":\"bets-and-casino\"}\n3f:{\"id\":\"$4"])
#         </script>
#         <script>
#             self.__next_f.push([1, "0\",\"name\":\"bets \u0026 casino\",\"blocked\":false,\"position\":8115}\n3e:[\"$3f\"]\n41:{\"title\":\"bj | baji (Bangladesh)\",\"date\":\"2023-02-14T04:06:41Z\"}\n35:{\"id\":\"$36\",\"title\":\"baji 🇧🇩\",\"about\":\"\",\"membersCount\":45421,\"peer\":\"PEER_TYPE_CHANNEL\",\"privacy\":\"CHAT_PRIVACY_PUBLIC\",\"username\":\"baji_bgd\",\"photoId\":\"6187992883995458813\",\"photoUrl\":\"https://img.telemetr.io/c/1ZP9sP/6187992883995458813?ty=l\",\"telegramFlags\":\"$37\",\"collectorFlags\":\"$38\",\"language\":\"$3a\",\"country\":\"$3c\",\"category\":\"$3e\",\"updatedAt\":\"2024-09-30T"])
#         </script>
#         <script>
#             self.__next_f.push([1, "04:15:01Z\",\"channelCreation\":\"$41\",\"channelNet\":null,\"adsIndex\":46.13527}\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "1a:[[\"$\",\"$L30\",null,{}],[\"$\",\"$L31\",null,{\"channelInfo\":{\"id\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"title\":\"baji 🇧🇩\",\"about\":\"\",\"membersCount\":45421,\"peer\":\"PEER_TYPE_CHANNEL\",\"privacy\":\"CHAT_PRIVACY_PUBLIC\",\"username\":\"baji_bgd\",\"photoId\":\"6187992883995458813\",\"photoUrl\":\"https://img.telemetr.io/c/1ZP9sP/6187992883995458813?ty=l\",\"telegramFlags\":{\"verified\":false,\"scam\":false,\"fake\":false,\"restricted\":false},\"collectorFlags\":{\"verified\":false,\"cheater\":false,\"blocked\":false,\"onlyForOwners\":false,\"cheaterInfo\":{\"participants\":0.20746865757233585,\"views\":0.4530670859847248,\"appeal\":false}},\"language\":{\"id\":{\"languageId\":\"bn\"},\"name\":\"bn\",\"position\":113},\"country\":{\"id\":{\"countryId\":\"bangladesh\"},\"name\":\"bangladesh\",\"position\":144},\"category\":[{\"id\":{\"categoryId\":\"GrV1hfO57\",\"slug\":\"bets-and-casino\"},\"name\":\"bets \u0026 casino\",\"blocked\":false,\"position\":8115}],\"updatedAt\":\"2024-09-30T04:15:01Z\",\"channelCreation\":{\"title\":\"bj | baji (Bangladesh)\",\"date\":\"2023-02-14T04:06:41Z\"},\"channelNet\":null,\"adsIndex\":46.13527},\"channelStatistics\":{\"id\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"title\":\"baji 🇧🇩\",\"username\":\"baji_bgd\",\"membersCount\":45421,\"peer\":\"PEER_TYPE_CHANNEL\",\"channelStats\":{\"updatedAt\":\"2024-09-29T00:00:00Z\",\"membersCount\":45421,\"membersChange\":{\"tomorrow\":10,\"last7Days\":249,\"last30Days\":859},\"messagesCount\":{\"tomorrow\":4,\"last7Days\":32,\"last30Days\":115},\"mentions\":{\"allTime\":1},\"forwards\":{\"allTime\":2},\"engagementRate\":{\"avgPercent\":9.288655,\"after24HourPercent\":3.5248013,\"after48HourPercent\":4.5507584},\"postViews\":{\"after24Hour\":1601,\"after48Hour\":2067},\"postsPerDayAvg\":3,\"engagementShallow\":{\"byMessagesCount\":48,\"viewsAvg\":4219,\"reactionsAvg\":21,\"commentsAvg\":0,\"forwardsAvg\":2},\"engagementDeep\":{\"byMessagesCount\":224,\"viewsAvg\":4432,\"reactionsAvg\":25,\"commentsAvg\":0,\"forwardsAvg\":2},\"tgRecommendations\":{\"recommendations\":32,\"membersCount\":297074}},\"telegramStats\":null},\"currentPage\":\"$undefined\"}],[\"$\",\"$L32\",null,{}],[\"$\",\"$L33\",null,{\"channelId\":\"1829680439\",\"hasServerAccess\":true,\"children\":[\"$\",\"$L16\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\",\"$17\",\"children\",\"(service)\",\"children\",\"channels\",\"children\",\"$18\",\"children\"],\"loading\":\"$undefined\",\"loadingStyles\":\"$undefined\",\"loadingScripts\":\"$undefined\",\"hasLoading\":false,\"error\":\"$undefined\",\"errorStyles\":\"$undefined\",\"errorScripts\":\"$undefined\",\"template\":[\"$\",\"$L19\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":\"$undefined\",\"notFoundStyles\":\"$undefined\",\"styles\":null}]}],[\"$\",\"$L34\",null,{\"channelInfo\":\"$35\"}],[\"$\",\"nav\",null,{\"aria-label\":\"Breadcrumb\",\"className\":\"hidden\",\"children\":[[\"$\",\"ol\",null,{\"className\":\"breadcrumb\",\"children\":[[\"$\",\"li\",\"1\",{\"children\":[\"$\",\"$L42\",null,{\"href\":\"/enhttps://telemetr.io/en\",\"children\":\"Home\"}]}],[\"$\",\"li\",\"2\",{\"children\":[\"$\",\"$L42\",null,{\"href\":\"/enhttps://telemetr.io/en/catalog/bangladesh\",\"children\":\"Bangladesh\"}]}],[\"$\",\"li\",\"3\",{\"children\":[\"$\",\"$L42\",null,{\"href\":\"/enhttps://telemetr.io/en/catalog/bangladesh/bets-and-casino\",\"children\":\"Betting and Casino\"}]}],[\"$\",\"li\",\"4\",{\"children\":[\"$\",\"$L42\",null,{\"href\":\"/enhttps://telemetr.io/en/channels/1829680439-baji_bgd\",\"children\":\"baji 🇧🇩\"}]}]]}],[\"$\",\"script\",null,{\"type\":\"application/ld+json\",\"dangerouslySetInnerHTML\":{\"__html\":\"{\\\"@context\\\":\\\"https://schema.org\\\",\\\"@type\\\":\\\"BreadcrumbList\\\",\\\"itemListElement\\\":[{\\\"@type\\\":\\\"ListItem\\\",\\\"position\\\":1,\\\"name\\\":\\\"Home\\\",\\\"item\\\":\\\"https://telemetr.io/en\\\"},{\\\"@type\\\":\\\"ListItem\\\",\\\"position\\\":2,\\\"name\\\":\\\"Bangladesh\\\",\\\"item\\\":\\\"https://telemetr.io/en/catalog/bangladesh\\\"},{\\\"@type\\\":\\\"ListItem\\\",\\\"position\\\":3,\\\"name\\\":\\\"Betting and Casino\\\",\\\"item\\\":\\\"https://telemetr.io/en/catalog/bangladesh/bets-and-casino\\\"},{\\\"@type\\\":\\\"ListItem\\\",\\\"position\\\":4,\\\"name\\\":\\\"baji 🇧🇩\\\",\\\"item\\\":\\\"https://telemetr.io/en/channels/1829680439-baji_bgd\\\"}]}\"}}]]}]]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "43:I[91780,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"89980\",\"static/chunks/89980-1e653f4986615471.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"5135\",\"static/chunks/5135-6872f3ae6757f537.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"83286\",\"static/chunks/83286-7ca7aed2c53ce442.js\",\"1784\",\"static/chunks/1784-893e55e19169d325.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"38259\",\"static/chunks/38259-bceccd9489884b29.js\",\"88776\",\"static/chunks/app/%5Blng%5D/(service)/channels/%5Bid%5D/publish/page-54e389d46a937312.js\"],\"\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "44:I[42529,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"89980\",\"static/chunks/89980-1e653f4986615471.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"5135\",\"static/chunks/5135-6872f3ae6757f537.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"83286\",\"static/chunks/83286-7ca7aed2c53ce442.js\",\"1784\",\"static/chunks/1784-893e55e19169d325.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"38259\",\"static/chunks/38259-bceccd9489884b29.js\",\"88776\",\"static/chunks/app/%5Blng%5D/(service)/channels/%5Bid%5D/publish/page-54e389d46a937312.js\"],\"\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "45:I[98372,[\"73220\",\"static/chunks/73220-3a1140fcb6d7d1ce.js\",\"8279\",\"static/chunks/8279-7d504843f5f4005d.js\",\"81495\",\"static/chunks/81495-383649326538acfd.js\",\"43514\",\"static/chunks/43514-82bb92cc6c59dbee.js\",\"68326\",\"static/chunks/68326-28dd3db74d853a73.js\",\"90413\",\"static/chunks/90413-e8900a879754adbf.js\",\"64876\",\"static/chunks/64876-41c2b8a9a6312500.js\",\"2330\",\"static/chunks/2330-f253ce8ad6ba3601.js\",\"77397\",\"static/chunks/77397-21c9436c20a4a9e1.js\",\"10391\",\"static/chunks/10391-ac4597646d3d667d.js\",\"98735\",\"static/chunks/98735-a897bd2a07df5b3f.js\",\"89980\",\"static/chunks/89980-1e653f4986615471.js\",\"4198\",\"static/chunks/4198-c5a33f0545079614.js\",\"5135\",\"static/chunks/5135-6872f3ae6757f537.js\",\"9751\",\"static/chunks/9751-dccd70e85b745aba.js\",\"714\",\"static/chunks/714-602d8c7bb145d9fa.js\",\"60819\",\"static/chunks/60819-a2bc2b80dbdddd30.js\",\"92892\",\"static/chunks/92892-dd486ee805e7194e.js\",\"83286\",\"static/chunks/83286-7ca7aed2c53ce442.js\",\"1784\",\"static/chunks/1784-893e55e19169d325.js\",\"36269\",\"static/chunks/36269-379d608ce928088f.js\",\"38259\",\"static/chunks/38259-bceccd9489884b29.js\",\"88776\",\"static/chunks/app/%5Blng%5D/(service)/channels/%5Bid%5D/publish/page-54e389d46a937312.js\"],\"\"]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, "46:T4a3,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwC9KmYyOR06HFNtl8vcFzs7Driq0FxLPcojt8hzkAe1PuZZLaUBTlCMkGsuVl8yLo4qhfI886wnG08g+nrV0lAiOThTyDn2p21SuSq8dOKqKZLMK6jSIlPLCt2IYkH6UVo3UUcy7OAAPlx2orS5JWsmzcI45A60t66u55O4HH4VRgkMcinBIz09asGUi5WXGMntSa1KT0L6fPpkYccg8ZoGpQkhCD9aZcTl0x1wc1lkc5OetCEX3lCFmPc0VV3F8KO1FBLkkyASMFAB6e9L5rYPv7miinYLgbthkDIPqCajTfMQuScevaiikOTsi6ihFwKKKKZyNn//2Q=="])
#         </script>
#         <script>
#             self.__next_f.push([1, "47:T45f,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCoyED3oCkckZ9qe2SeDSkEDI60xDBuIOUGMdQMYqN0yPepVLs+0DBPWkcEHBGD3qUxtEcjRFDiPY31Joodc/WirJuSKQcEVZKDaD3NUI32sM52960N6tjZj1Gazm7FIECDk8NSHZuKkbiTzSPuzuIHHp3p4OMElQCKysU9SkeGIopDmSQ9RzmiuhGTaRGJHAwHIHpmnxTskgLEkd+aKKGroaZe8wFNyMdv1qLedw5P0oorKBUnaNwGQPvE/jRRRWpx8zP/2Q=="])
#         </script>
#         <script>
#             self.__next_f.push([1, "48:T477,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDLA54qUOFBHbNTeRs+fovrTP3YRl+X5Tw2OtS9TRaDQx2kdj3pskezGGB44xUjSAxFRimSSbolDMTyTj0pIbsDmPywAhV+Op60U2V97Z9qK0TuZNWFmuHkjVDwoqMMVBGeKKYwINKwXLOSLcAZAJ5BHQ0jqvkgj7wqAMdu3Jp3GBU2NFqh6oSPQGinvKuAq0UydBI5FRCCGOT2I/wp/nqcEhyR05H+FFFXZGdxjTL3EhB4PzD/AAqPdEVICPuPT5v/AK1FFTYq5Ygh2AM33v5UUUUjllJtn//Z"])
#         </script>
#         <script>
#             self.__next_f.push([1, "49:T417,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoABYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDNjAYgDrUs0S+WG2FexOaBabed9OaEEdh7jP8AjSuSU2AzxRVkWuRnePxFFF0M0AE9qaNhDYChvrVGIyNgi4VT6HOR+lSouyNiro2OpC1LVhq1y3+79RRQiRvCrbFyevy0VOgm4p2ZkLI2QAxH44qeOUrneQcjH3hRRWlkFiRL5I0AVST3NFFFLlQ3Hmd2f//Z"])
#         </script>
#         <script>
#             self.__next_f.push([1, "4a:T493,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCrLLn5V6etRgEkAck0lSW5AnQtwM1025VoVGKirIVoXhYGZMKfQ80TxL1QHHT6VPdnPljMjBh8ufXNKYn5Xbzjk9q51N31Gyk/l7MBCHGM89aKkmiwSO9FXyX1RDRCGqaIoHUuT16VAFJGRj86kJIHzqDj3p87sNMuXEYeQSq4AH6UgugR0LY5PbiqTTFhgcD0zS+dtXAHb161Cih3J5H82Qv2NFQedk5wB7Cit4ySVhphG6BCHBznsB/WntNGcDDY9Nq/4UUVgZjGkiHIVs/Rf8Ka8kLbRhwAOwAoopDInK7vkzj3oooouB//2Q=="])
#         </script>
#         <script>
#             self.__next_f.push([1, "4b:T413,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoABYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDNjAYgDrUs0S+WG2FexOaUWZBzupzQDb2Hvz/jSuKxSYDNFWhZn+9+lFF0M0CeO/5U3zFI7CqUTzMMi52nuCT/AIVLDGCDgrIfUdvzpbbhcsblI60UqRo0KkhWJ/iA60VDkDaW7MhZGyAGI/HFWIZjGSWIJxj7wNFFaWQnFMdHfiNQAKKKKOVC5Ef/2Q=="])
#         </script>
#         <script>
#             self.__next_f.push([1, "4c:T483,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwClM5f5V+7/ADpsduzkYHWpkjyQK0II8EKnQfePrW/KkrmHNbRGYbNx2/UVE0TIcEEGti6CEEd6qzlEULK3UcHrinZPcpNlNjGYxhSH4zz1opGCkZU5FFZNWLuWIpBkHNW4LlVzz2rLVXxuUHHrin7JQfuPz/smtFJNambgXXuVbI5yeMVXuZwRs25wBzUBEyrlgQBxkqaTeP73Si6Y+UQHCYxjmimM2TRWbaLsTxMgUh2Iz225/rSkxHHznPQ/Kf8AGiipaGMdkEZw+T/dIP8AjUDNuPQD6UUUhjaKKKAP/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "4d:T483,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwClM5f5V+7/ADpsduzkYHWpkjyQK0II8EKnQfePrW/KkrmHNbRGYbNx2/UVE0TIcEEGti6CEEd6qzlEULK3UcHrinZPcpNlNjGYxhSH4zz1opGCkZU5FFZNWLuWIpBkHNW4LlVzz2rLVXxuUHHrin7JQfuPz/smtFJNambgXXuVbI5yeMVXuZwRs25wBzUBEyrlgQBxkqaTeP73Si6Y+UQHCYxjmimM2TRWbaLsTxMgUh2Iz225/rSkxHHznPQ/Kf8AGiipaGMdkEZw+T/dIP8AjUDNuPQD6UUUhjaKKKAP/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "4e:T483,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwClM5f5V+7/ADpsduzkYHWpkjyQK0II8EKnQfePrW/KkrmHNbRGYbNx2/UVE0TIcEEGti6CEEd6qzlEULK3UcHrinZPcpNlNjGYxhSH4zz1opGCkZU5FFZNWLuWIpBkHNW4LlVzz2rLVXxuUHHrin7JQfuPz/smtFJNambgXXuVbI5yeMVXuZwRs25wBzUBEyrlgQBxkqaTeP73Si6Y+UQHCYxjmimM2TRWbaLsTxMgUh2Iz225/rSkxHHznPQ/Kf8AGiipaGMdkEZw+T/dIP8AjUDNuPQD6UUUhjaKKKAP/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "4f:T4a7,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDPGScCrKgRJuPJpIo9gyfvUkgeRxGi5x17VpOp0Rn8crIkVycblxu6Go7hAw+UZYelTXTMqRqi8r1PpTrNI9xlDbiB0PY1nF6XZbpJS0KLGPZgIVcYzk0VYvpYZHYeVscdCO9FVZg1YfHhyAD+NNmmUyrHEAAO/eqqvIi5XOOxxVkSo+CyPlT1wBzUS8x0lyao0H2RQFnbc5HTFZ74WCZo8jJHTtTjdZJ4PtUbzwrvUo3zc+3tSWj0NL6alVpGb7xzRUeaK6LmZaidBGQz456YP+NPMiZP7zIPXIP+NFFZNCRE7pj5MZz6H/GoXOQKKKnYpvQZRRRVXEf/2Q=="])
#         </script>
#         <script>
#             self.__next_f.push([1, "50:T463,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDZorGkjZpD+9lOO5ambJQOJpf++qANys/UreGZNxZVlA4OevtVMrNjmaX/AL6qIhR/y2bNAEUpjwQI9jj3Jop7W+8bg5JxxkUUxGnE6OgZDuU9M087MYIFYtvO8Ldyp6ir6ThhnPXpWfI7juWMIQRzQLePYV52nmofNXrTxOg71pZIRIsEajHOPeiojcIQeenpRUuN+ouZIyllIUDHT3NL5x9P1NFFW0guBn7EfqaespkO1VHvyaKKiw5OyJgAOgx6miiimcjZ/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "51:T423,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoABYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDNjAYgDrU00S+WG2FexOaUWRB+/wDpTmt8g9Pwz/jSuTYosBniirItOfvfpRRdFGmAuOnP0pF2F24XPr61nRvK/IuQp9CTn+VTQxZB2uGYDqopWFzW3LY2jO7Gc8fSioozvLRyEMyHrRUy912Y7xMtZG4CsR+OKtQXDRA5wWPGdwOKKKuwmrkcV0sTs+CWbrRRRRYOVH//2Q=="])
#         </script>
#         <script>
#             self.__next_f.push([1, "52:T4c3,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCKOaBI1+6D/u1AYHf540JQnimxwlwCO9Tqki4RASfrWduxtoiMW0hyNhFJJbOgyQB26irUcbs/lSIqg8k5J/rTpbdfK3RsWbOABRqgumUHMezAQq4xnmirM1uoi3fxDvkYoq1NMzcH0G2x+RQoYsM9BT1JMvyg+mPeoredI0w2Oue9TRuNxYuV3dMCiK97XYu6sPWORpGyQvHOewp4Ro9pDKR7fQ1EJAruc/KeOooklDZxnJ9x0rOfxabAou1x0g/dtjGBg9MdaKbL5hDBlwTjOW6UVNi0U08vaN2M9+DTsw8fd/I/40UV0HMIxQn74Az0ANJuC4KOcj2oorNo2jJtF2AyN88mOegxRRRQc8pNs//Z"])
#         </script>
#         <script>
#             self.__next_f.push([1, "53:T4c7,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCii1fijwisDkntikWJTGGXYQffmm+eq3IjVBjOAQenvWTVyE2WTeLHOI2Vh2BI4NJeW3nrk4B7GoRC81+quuFj5Y57dql+VySDnngk8Y7UcttUWzMkEart2FXGM89aKuXECuD9wEdwelFaqRHMRW8qYGd2e4psgkM/lhTgnIAqKJY9u5pirZ6BM1PIylh/pTj0HlUrajirMnuJGgtvLTHmyH5yPSqYyNoJIDNU0jLhQHDk8klNuKrq4Rsqp4OevFNMosu4xgnNFRAtO/v3NFTYwdkxkLoIyrMB+f8AQ1I0qH+P/wBC/wAaKKto2uMmkRzgSlVx0wSP51FEjStgfifSiik1YmTsrl9EEa4FFFFBzM//2Q=="])
#         </script>
#         <script>
#             self.__next_f.push([1, "54:T423,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoABYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDNjAYgDrUs0S+WG2FexOaUWRB+/wDpTng+U/0z/jSuSUmAzxRVkWhz1P8A3zRRdDNIgbfkxmkUoZGGAMY59az43lYZFyFPcEn/AAqVBsjZg6sR1IWptYatexe/d+o/OimoEeFG2jJ68UVOgm4p2ZjLI2QAxH44qeOUqDvIORj7woorSwWJEvkjQBVYnuaKKKXKhuKk7s//2Q=="])
#         </script>
#         <script>
#             self.__next_f.push([1, "55:T463,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDNGM+1TrACM7uO1RxxOxIXselSyeZGVQdMUmNPoVmB37T2NWooo5oCmQrqchj3pPIEiAg4k7g01kWMYbJouDGOYtmFUhx1Ocg0VHgbvl6UVVxWZd3pEfkI+Y81NKY5FGAeKzQx4BPAp5uX/vfpSZHKtyV+CFX5fc0jwhjy/wAx9v8A69QeYzMMmpXLBeN3PsDSsWtBqwkDcfw5oqNpWPGePpRTASmsO4ooqmIarYOak89/X9TRRUjJbaAudzD5P50UUUGEptM//9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "56:T4a7,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDLjRmyVUmrEYcMAVIA9RVcO6L8rEfSp4mkO1m3MM55qWaLlsSi+kEpAHydDUd2mH8xeVbmp4rTZlyA4P8ADT1tvNtAGYLjOM/WlzJCaKJaIxjapDcc560VF91iKK0uZ2FPIxWrC5e3UO54GNmKpQeYIyU568bSanzNtJVhnthTz+lTJXKRYZDgsrU0glBEh5Pc+9VAsxHLn64b/CnpK6RruBVx2I6ioasXe5Fe2bWxB3bg3eipJWkuCAcdMAZoqk9NSXZFZHAGDn8Kd5nu3+fxooq2iBrOQPlJ+mT/AI1EGdyACSegoopNBcv28XljLcv/ACooopHK5Ns//9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "57:T4b3,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCk9g6JuIOPahLF5BleR7Vdvrzny42K7TyauWjqtuAWzjv60WYzH/s2X+6aQ2bxgkggCt4yJjdvwF6iq11cJgQj7xI5z0pAZD+XsACFX46nrRVm8+VjBJhiuMP3HeirRLsU2kLuXbkk5NaVhfRRxeXIxXnjuKzQhYcY/OpocIjLIqkZyORSYGoyqUZw3DZP1x0/pVK4Vpd9wOI1wF96Tz4i2Sx+nanXNwJYQi9Mj8qkbIr52M788Ng9Pain3IWcx7Oo4OKKoRXilVEIO7OcjGP6in+fH/00/T/Ciim0hXGSTL5ZCl8n1x/hVdS7EKuSTRRU2sO5owRmJcnlu9FFFByuTZ//2Q=="])
#         </script>
#         <script>
#             self.__next_f.push([1, "58:T4b3,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCgkBNTC0wMuQv1NXFjVIy/THOO1VgzSNvJyPT0rNXlqi5NRFFrHnbkYxnOPxqNrTK7o2BHtVnI8k8n0/z+FQglGLDgelDutg0K0nlhNuwq4xnJoq9dQJJEHQfMRkGiqjUTWpLi+ghuN8TDrkYAqIMvptHv2qtFK0Thh2qX7QxH+rQ++OanlcdiuZPcsi4Ux+WF569KiYgjpuPsaYLtgPuJzwRjrS+cSDmNAPXGDTjdCaT3JA7LEq88DkUVXMhY0VDjd3LWmiGo8YTDg59gKf5kWR978FWiiui1zFDTPHg43buxKiozMzHnaf8AgIooqLDuSQxmdtxACjqQMUUUUWMZTaZ//9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "59:T4af,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwC6dsgAA3Lnio1CAtGIwD1xiifcY8Q8HPQVZRPkBON54JpgZiyTyTEHaFLYC4qWazWRAGXbIR97PepUtnS6Zt2EHK/WpGdZE54NQ7lKxizIseUKFZBjPOc0VfuoUm6HPGFY9jRVKSE4sqQXcoflqvw3ZJ8sryO+ax1DdVB47ip43c8jKsOpxQxJms87RR7yQRn7oHWl8yBjxwaz97lCHG49QMYqRTJ5YAAz/KluPbYuM6SfuR19cUVXjDfalc9AP1oosguzMjm8tNu3POepFONxxjZjP+2aKKuyIuKLsj+H8dxqRbsE/d7/AN40UUrIdy1C/m/ORgeuTzRRRU2MpSdz/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "5a:T413,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoABYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDNjAYgDrU00S+WG2FexOaQWeDnfT3hG3kge/P+NIVikwGaKsi0yMhx+VFFwNAA5o3KTgAA9z61RjeZxkXIU+hJz/KpYogythw5A/hFAXtuWOPUUUyIKxeNwpZT1A60VMnyuzQXRmLI2QFYj8cVaguWiBzgse+4HFFFVYGrkcV0InZ8Es3WiiinYOVH/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "5b:T483,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwBtKud4A61FlpSVjGQOpqVUfYUyCOxx71nJ9ERSp9WSPJMW8pG2YGScZqCYedHiT/WLxmnmIxzx/MAG9RTXieOVvMJ2sSQ3rUqNlodGjKjmMJt8va47560U6VRuI/U0VqpXMmh1nP5bFCcBuM1fCiOQAHKkdKyki3rnP6VYVpUTbknHTionHW6Ki7F6Qh3jVgOTyfbFOv3jIjG7gZ4rO86QSA7ScUyWd3f5xjHaqSC5Yl8ncS5OaKpmQk9aKSjYOYE8vb82M/Q/40rGPbwBnHof8aKK05dSCKloopgFFFFAH//Z"])
#         </script>
#         <script>
#             self.__next_f.push([1, "5c:T4a7,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCGIOVVgcAnnjkVJ5a7Mu5Izyc8GkukkTMYIAYDn2pbNAAUIHqe+aQxBEqZKqfw6ikkjWaAlsiQcgmp5QiQHD9O7j3qoZxJEA+cn+IeuaaDQhlVEGwoVkGM89aKviJLu2wRhk4D0U7klLzmnwJCMqMAgYp/mtFGhG0Egjiq6RSOMojEDuBT3jmePBif5TxwaBoUz70wPu+n86hmbcAATgUAhEdWGH6fTmmAjnNPQC3DNsi2SD5DzkdaKqrlm2qCc8AUUmwvYnjkVYyDnOc9Kd5sfPX6bRRRRbURCwh3ZJfB9AKiVSzYXknpRRSC5ft4BEuTy3c0UUUHK22z/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "5d:T4b7,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwB5jh5XYuRyaqGDI46+mKsOQYyMHcDycfepxaJY22k7sevFClYJRK5tQCPn/SmtZsykx5Yj2qbcjfKT69DnvTlnIBAVs5zkDvScpDUY9yjIEVduwq4xnJoq5LZNNH5ijBxnB60Vat1M2+xFDKXhIPX1qWRj8pUnI+8Aaoxy+XxjIzzzipftC5OIyAf9qi5SSNDKgH1465/HrVdY4WjHmDn+L1qOJiwB2j/GntIpHBAPutZuLsUmrk8RkhjDL90YFFVfMbhWkJXqVoqXG5WvYhjm2Rhctx7Cni4TJPzj0xj/AAoorVxMxPOjJOfM/MVEzLn5M496KKFuBZt4jw7/AICiiig5pSdz/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "5e:T4b7,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwB5jh5XYuRyaqGDI46+mKsOQYyMHcDycfepxaJY22k7sevFClYJRK5tQCPn/SmtZsykx5Yj2qbcjfKT69DnvTlnIBAVs5zkDvScpDUY9yjIEVduwq4xnJoq5LZNNH5ijBxnB60Vat1M2+xFDKXhIPX1qWRj8pUnI+8Aaoxy+XxjIzzzipftC5OIyAf9qi5SSNDKgH1465/HrVdY4WjHmDn+L1qOJiwB2j/GntIpHBAPutZuLsUmrk8RkhjDL90YFFVfMbhWkJXqVoqXG5WvYhjm2Rhctx7Cni4TJPzj0xj/AAoorVxMxPOjJOfM/MVEzLn5M496KKFuBZt4jw7/AICiiig5pSdz/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "5f:T4a3,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDOyDUiwSsoZVyD3zTUtpZM7FyB71KlvMpO5Ayr1G6hm3qAhkVgHZVz3zTZY1Ck+YhI9DU2yQx7/LiXnPTmo3iMjEuPn9BxSu+rH8SImMRjG1SG4zz1op8lv5abs/n60Va1MXFoltZ2YeWo+b+dTgSksmVCnvWfFK0Tbk61Mlw5AG8KfpUSg29ClJvS5YIZdoDsV4IFKrBWbjd74xVVjN13k1GZJM8s1J031LWhLKHkJBbK54FFR7z60VsuVFaCIYwnOd30/wDr04PFxzjH+x/9eiioscw8Op4RyT7jFHOfmSiitFsdFNtrUkRAfmK0UUVk2efUqScj/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "60:T413,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoABYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDNjAYgDrU00S+WG2FexOaBZMCPmpzW5IIx+Iz/AI0risUmAzRVr7Gw7/pRRdDLgOPWl87IAJ6VSjeZhkXO09wSf8KmhQbTgiQ+q9v0pbAmTF19aKdHGPLBcKxP8QHUUVDkDcVuZKyNkAMR+OKswzGNsswPH94GiitLITimLHfLEpVVOM5oooo5ULlR/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "61:T4b3,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCpHCrRg5O7PTFSLbe5P4U9SVVU2YYnFWE+Q8gk+h71vKvFPlNEis8IEfA5qBoie1XW5OVb5eynGP8AGpkjQ/MQRx93rSVeDVmDT6mTJ5YTAQq4xnnrRV24tjIpOMYGc4oqeS+qM2gcAxjOS56H0pn+kbwMHOcDK9aN5STlyFHIIpvnzkgl8YPGcf4VzNXdza66lgo69Yh9dn/1qafta8KhAB7Jimec5XDTHrnGAeaVbmdzgy89e1FhXLD+YsI55P3uKKpEuxJZ898DvmirUraD23KqyDIyTj2qVZ4wOrE/QUUUzO477TH3xk/7AppnjJHJH0UUUUCuMM2D8pyPeiiiiwXP/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "62:T453,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCIWooeBUQn0FPSYOmabIw28mqJGQW4kGXYqc9MVJLZhk+Ujd2qOOYjJ6g9fap0mBzUrzKkUZAirt2FZBjOTRU90EkAIHzetFUIiD8YXgUzcc800OQhU8j+VNJGeKAHN8pyKlBw4waY8cgQkrx1qLeQVPoKAL6FcjdyaKhgmiJG/Oe2KKAI43RUw2ev90GniWIMD83HT5FoopWFcR7scFR82ehQYqsWJOePwoopFEsEJlbJGF7miiigwnN3P//Z"])
#         </script>
#         <script>
#             self.__next_f.push([1, "63:T40f,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoABcDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCsBShcvtHWnFMxHnHeljIIGSQMZzTlJoxcGtxHT5PuYI75oqWHCQjJ3Ak5orSMbq4mmmUhISu3IHuakB/0cMMZXtmokRGj3MHz7YpNo3fKsmO3FZPXc2v3JXmBiVQeepoqs2QehH1oqribbY5ZSqgYB/AUvnn0H5D/AAooqRkbuXPOPwGKKKKYH//Z"])
#         </script>
#         <script>
#             self.__next_f.push([1, "64:T40f,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoABYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDNjAYgDrU00S+WG2FexOaiEGD96nsoIxjHvk/40hWKzAZ4oqYQDGd4/GigCyqc1Im3gcfWqsQdsMJ1Vh65yP0qeGIEEq4ZgOqigLpEuzOcD9KKdC5JaNmyyHqKKmT5XZiuZSyNkAMR+OKtQXDRA5wWPGdwOKKKqw2rkcV0sTs+CWbrRRRTsHKj/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "65:T403,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoABYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDMiTzGCdzwDSqm87dwGPXvU32RccOfyoNsMDDfpUmqZWcYYj0oqc2uf46KZL1LxNJnPSqaylkdjIwI+6AetNLuu05II+8R1qeUjlL2RRVWR5I2OGYoehzRRyisQRkMhXI45yTUsmXAGYx6ncOaKKou7I/PaIgLg8fWiiimJs//2Q=="])
#         </script>
#         <script>
#             self.__next_f.push([1, "66:T40f,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoABYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDNjAYgDrU00S+WG2FexOaUWBB+/TjalgQMZ9cn/GlcViiwGaKuCwbGdwFFF0MujpS+ZkFRjcD+lUInmcZFyFPcEn/CpoE7qwdh6cVOwrosk88UURZMQO7ccn5hRUOTG2luY6yNkAMR+OKsQzmMkswJx/eFFFatITSY6O+EYwAeeTiiiijlQuRH/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "67:T45f,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDPDo8fzj5gODQYJBzjimW4JkHGcVbMijOV4pNsaSKlJUihcnJB9OcUMUB+7n8adybAXQx42AN6560VGSM8DAopgX4YkjgViOWHJp3lLLHlSarR3BERjfkY4PpVmA7UwOMVsrPQxd1qUAME7sgj2zUm+P0/8dFByJ3JOOTTZe3OT/n3rE2GNjsc/hiinQxGV8du5opCckhlWIJtoKP0Pf0ooq07MTV0RS5M7gf3jQiGRwq9aKKljbsi/GgjUKKKKKRytn//2Q=="])
#         </script>
#         <script>
#             self.__next_f.push([1, "68:T403,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoABYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDMiTzGCdzwDTlTedu5Rj1704QHHRx+FBh4wA35VJqpIhcYYj0oqTyC3/6qKZL1NIvSbqorKWR2MjAj7oB60hdxtOSCPvEdaz5CLF/INFVJHkjY4Zyh6HNFPkCxBGQyFcjjnJOKlky4AzGPU7hzRRVlXZF57REBcHA+tFFFMV2f/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "69:T493,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDPlTEYOME02FN749anu/L8tcHLClt4Zoo47lMYJ/Kk2VYW7szCmRnHQk+tUxxWvMxuogmcMOSPSq8MCwy4nj3MeVB6EUIGVmMRjG1SH4zz1oqzqYTzU2IqkjnFFWQZ5Ga2IA7WcKR9cZOayatJOy7VU8AYFQ0UmXGyZCOM9CRROMtExcHy/TvTIp4GRlncBuxxUctyuDtff3+7gelJ36DjYXYrSy+aQzZ7UVBv3kksQT6CimnYlrUiVwqYxz7qDS+bg5GP++BRRVsQGfPYE+6ijzfZf++RRRU2uO5LEDMRwAg7gAZooooMZTdz/9k="])
#         </script>
#         <script>
#             self.__next_f.push([1, "6a:T45f,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDPDo8fzj5gODQYJBzjimW4JkHGcVbMijOV4pNsaSKlJUihcnJB9OcUMUB+7n8adybAXQx42AN6560VGSM8DAopgX4YkjgViOWHJp3lLLHlSarR3BERjfkY4PpVmA7UwOMVsrPQxd1qUAME7sgj2zUm+P0/8dFByJ3JOOTTZe3OT/n3rE2GNjsc/hiinQxGV8du5opCckhlWIJtoKP0Pf0ooq07MTV0RS5M7gf3jQiGRwq9aKKljbsi/GgjUKKKKKRytn//2Q=="])
#         </script>
#         <script>
#             self.__next_f.push([1, "6b:T40f,"])
#         </script>
#         <script>
#             self.__next_f.push([1, "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAoABYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDNjAYgDrU00S+WG2FexOaQWhB+9Tmi46AZ78/40risU2AzxRVkWhK5DCii6GaBIJGDR5ik44x/Os+IyMARcKp9Dnj9KkC7YmYOHI9BSsF0Wyy56iiljjBhXeg8zucUVD0BuJkLI2QAxH44qZZWVWDEHIx94GiitLCsOivmQsWJYt1NFFFFkJxTP//Z"])
#         </script>
#         <script>
#             self.__next_f.push([1, "15:[[\"$\",\"div\",null,{\"className\":\"flex flex-col gap-6 lg:flex-row lg:gap-10 xl:gap-16\",\"children\":[[\"$\",\"div\",null,{\"className\":\"flex w-full flex-1 flex-col lg:w-3/5\",\"children\":[\"$\",\"div\",null,{\"className\":\"rounded-lg border border-border-base-secondary px-2.5 py-4 shadow-sm lg:px-7 lg:py-7\",\"children\":[\"$\",\"$L43\",null,{\"id\":\"posting_time\",\"channelId\":\"1829680439\"}]}]}],[\"$\",\"div\",null,{\"className\":\"flex w-full flex-1 flex-col gap-6 lg:w-2/5 lg:max-w-[460px]\",\"children\":[\"$\",\"$L44\",null,{\"data\":\"$undefined\"}]}]]}],[\"$\",\"div\",null,{\"className\":\"mt-6 flex flex-col lg:mt-6 xl:mt-16\",\"children\":[\"$\",\"$L45\",null,{\"channelId\":\"1829680439\",\"preloadedPublicationAnalytics\":{\"messages\":[{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1639,\"publishDate\":\"2024-09-29T08:28:40Z\",\"message\":\"শোয়েব আখতার, যিনি \\\"রাওয়ালপিন্ডি এক্সপ্রেস\\\" নামে পরিচিত, এবং ব্রেট লি, অস্ট্রেলিয়ার কিংবদন্তি ফাস্ট বোলার, তাদের অসাধারণ গতির জন্য বিখ্যাত। আখতার ২০০৩ সালের বিশ্বকাপে ১৬১.৩ কিমি/ঘণ্টা বেগে বল করে নজর কেড়েছিলেন, তার ক্যারিয়ারে ৪৪৪ ওডিআই এবং ১৭৮ টেস্ট উইকেট নিয়েছিলেন। অন্যদিকে, লি ১৬১.১ কিমি/ঘণ্টা বেগে বল করেন, এবং ৭০০টিরও বেশি আন্তর্জাতিক উইকেট সংগ্রহ করেন, দুটি বিশ্বকাপ জয়ে অস্ট্রেলিয়ার গুরুত্বপূর্ণ ভূমিকা পালন করেন, তার আক্রমণাত্মক বোলিং স্টাইল এবং সুইংয়ের জন্য স্বীকৃত।\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6325766917930991358, \\\"date\\\": \\\"2024-09-29T08:24:26+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgovSpmMjkdOhxTbZfL3Bc7Ow64qtBcSz3KI7fIc5AHtT7mWS2lAU5QjJBrLlZfMi6OKoXyPPOsJxtPIPp61dJQIjk4U8g59qdtUrkqvHTiqimSzCuo0iJTywrdiGJB+lFaN1FHMuzgAD5cdqK0uSVrJs3COOQOtLeurueTuBx+FUYJDHIpwSM9PWrBlIuVlxjJ7UmtSk9C+nz6ZGHHIPGaBqUJIQg/WmXE5dMdcHNZZHOTnrQhF95QhZj3NFVdxfCjtRQS5JMgEjBQAenvS+a2D7+5oop2C4G7YZAyD6gmo03zELknHr2oopDk7IuooRcCiiimcjZ/\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [20874, 49079, 77600, 113277, 175565]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"replyMarkup\":{\"rows\":[{\"buttons\":[{\"kind\":\"KeyboardButtonCallback\",\"text\":\"ব্রেট লি\"},{\"kind\":\"KeyboardButtonCallback\",\"text\":\"শোয়েব আখতার\"}]}]},\"meta\":{\"views\":1216,\"forwardsCount\":3,\"commentsCount\":0,\"reactionsCount\":18,\"publishDate\":\"2024-09-29T08:28:40Z\",\"deletedAt\":null,\"reactions\":[{\"count\":16,\"emoticon\":\"👍\"},{\"count\":1,\"emoticon\":\"❤\"},{\"count\":1,\"emoticon\":\"😁\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":175565,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$46\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1638,\"publishDate\":\"2024-09-29T06:53:10Z\",\"message\":\"সিএসকে এমএস ধোনিকে ৪ কোটি টাকায় আনক্যাপড খেলোয়াড় হিসেবে ধরে রাখতে পারবে, কারণ আইপিএলের একটি পুনর্জীবিত নিয়ম ভারতীয় খেলোয়াড়দের, যারা পাঁচ বছর ধরে আন্তর্জাতিক ক্রিকেট থেকে অবসর নিয়েছে, আনক্যাপড হিসেবে শ্রেণীবদ্ধ করার অনুমতি দেয়। ৪৩ বছর বয়সী ধোনি ২০২০ সালে অবসর নিয়েছিলেন এবং শুধুমাত্র আইপিএল খেলেন। তিনি ২০২৪ সালে সিএসকের অধিনায়কত্ব রুতুরাজ গায়কওয়াদের হাতে তুলে দেন।\\n\\n\\n❤️  Baji  সদস্য  হিসাবে সাইন-আপ করুন 🚀\\n 🛡এখনই  Baji Appডাউনলোড  করুন!! ⬇️\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6325584283036663749, \\\"date\\\": \\\"2024-09-29T06:53:10+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgoqMhA96ApHJGfantkng0pBAyOtMQwbiDlBjHUDGKjdMj3qVS7PtAwT1pHBBwRg96lMbRHI0RQ4j2N9SaKHXP1oqybkikHBFWSg2g9zVCN9rDOdvetDerY2Y9Rms5uxSBAg5PDUh2bipG4k80j7s7iBx6d6eDjBJUAisrFPUpHhiKKQ5kkPUc5oroRk2kRiRwMByB6Zp8U7JICxJHfmiihq6GmXvMBTcjHb9ai3ncOT9KKKygVJ2jcBkD7xP40UUVqcfMz\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [20585, 49165, 80913, 141157, 270550]}], \\\"has_stickers\\\": false}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":381,\"length\":2,\"documentId\":\"6301075047410829543\"},{\"kind\":\"MessageEntityBold\",\"offset\":383,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":384,\"length\":1},{\"kind\":\"MessageEntityTextUrl\",\"offset\":385,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":385,\"length\":4},{\"kind\":\"MessageEntityItalic\",\"offset\":385,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":389,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":389,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":398,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":398,\"length\":14},{\"kind\":\"MessageEntityItalic\",\"offset\":398,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":412,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":412,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":418,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":418,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":418,\"length\":2,\"documentId\":\"5217880283860194582\"},{\"kind\":\"MessageEntityBold\",\"offset\":420,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":420,\"length\":2},{\"kind\":\"MessageEntityBold\",\"offset\":422,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":422,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":422,\"length\":2,\"documentId\":\"5251203410396458957\"},{\"kind\":\"MessageEntityBold\",\"offset\":424,\"length\":5},{\"kind\":\"MessageEntityItalic\",\"offset\":424,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":430,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityItalic\",\"offset\":430,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":438,\"length\":15},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":454,\"length\":2,\"documentId\":\"5406745015365943482\"}],\"meta\":{\"views\":1247,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":11,\"publishDate\":\"2024-09-29T06:53:10Z\",\"deletedAt\":null,\"reactions\":[{\"count\":11,\"emoticon\":\"👍\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":270550,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$47\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1637,\"publishDate\":\"2024-09-29T03:53:53Z\",\"message\":\"আপনি কি সেরা বেটিং অভিজ্ঞতা খুঁজছেন? আজই Baji-তে  যোগ দিন এবং নিজেকে স্পোর্টসের জগতে নিমজ্জিত করুন যা আগে কখনও হয়নি! লাইভ বেটিং অপশন এবং রিয়েল-টাইম আপডেট উপভোগ করুন যা আপনাকে খেলায় যুক্ত রাখবে। আমরা বিভিন্ন খেলা ও ইভেন্টে সর্বোত্তম অডস প্রদান করি, যা আপনার বেটের সর্বোচ্চ মূল্য নিশ্চিত করে। আজই সাইন আপ করুন এবং আপনার ভাগ্য আনলক করুন।\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6325766917930991224, \\\"date\\\": \\\"2024-09-29T03:51:20+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgoywOeKlDhQR2zU3kbPn6L60z92EZfl+U8NjrUvU0Wg0MdpHY96bJHsxhgeOMVI0gMRUYpkkm6JQzE8k49KSG7A5j8sAIVfjqetFNlfe2faitE7mTVhZrh5I1Q8KKjDFQRniimMCDSsFyzki3AGQCeQR0NI6r5II+8KgDHbtyadxgVNjRaoeqEj0Bop7yrgKtFMnQSORUQghjk9iP8Kf56nBIckdOR/hRRV2RncY0y9xIQeD8w/wAKj3RFSAj7j0+b/wCtRRU2KuWIIdgDN97+VFFFI5ZSbZ8=\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [20936, 47222, 69905, 96234, 148446]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"replyMarkup\":{\"rows\":[{\"buttons\":[{\"kind\":\"KeyboardButtonCallback\",\"text\":\"❤️\"},{\"kind\":\"KeyboardButtonCallback\",\"text\":\"🔥\"}]},{\"buttons\":[{\"kind\":\"KeyboardButtonUrl\",\"text\":\"এখনই আনলক করুন 🔒\",\"url\":\"https://baji.social/bj/tgndt\"}]}]},\"meta\":{\"views\":1295,\"forwardsCount\":1,\"commentsCount\":0,\"reactionsCount\":1,\"publishDate\":\"2024-09-29T03:53:53Z\",\"deletedAt\":null,\"reactions\":[{\"count\":1,\"emoticon\":\"👍\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":148446,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$48\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1636,\"publishDate\":\"2024-09-29T03:19:31Z\",\"message\":\"ত্রিনবাগো নাইট রাইডার্স বনাম বার্বাডোজ রয়্যালস, ২৮তম ম্যাচের হাইলাইটস | ক্যারিবিয়ান প্রিমিয়ার লিগ ২০২৪\\n\\n২০২৪ রিপাবলিক ব্যাংক ক্যারিবিয়ান প্রিমিয়ার লিগ (CPL) প্রতিযোগিতার শেষ সপ্তাহের দিকে বার্বাডোস রয়্যালসের জন্য আরেকটি হতাশাজনক রাত ছিল । যারা সহ শিরোপা প্রত্যাশী ত্রিনবাগো নাইট রাইডার্সের হাতে টানা চতুর্থ পরাজয়ের শিকার হয়েছিল। প্রতিযোগিতার শুরুতে পরাজিত দল হওয়া সত্ত্বেও রয়্যালস চূড়ান্ত বাছাইপর্বে চতুর্থ স্থানে ছিল।\\n\\n\\n\\n\\n❤️  Baji  সদস্য  হিসাবে সাইন-আপ করুন 🚀\\n 🛡এখনই  Baji Appডাউনলোড  করুন!! ⬇️\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaDocument\\\", \\\"nopremium\\\": false, \\\"spoiler\\\": false, \\\"video\\\": true, \\\"round\\\": false, \\\"voice\\\": false, \\\"document\\\": {\\\"_\\\": \\\"Document\\\", \\\"id\\\": 6325584282580422866, \\\"date\\\": \\\"2024-09-29T03:19:31+00:00\\\", \\\"mime_type\\\": \\\"video/mp4\\\", \\\"size\\\": 134795323, \\\"attributes\\\": [{\\\"_\\\": \\\"DocumentAttributeVideo\\\", \\\"duration\\\": 178.077, \\\"w\\\": 1080, \\\"h\\\": 1920, \\\"round_message\\\": false, \\\"supports_streaming\\\": true, \\\"nosound\\\": false}, {\\\"_\\\": \\\"DocumentAttributeFilename\\\", \\\"file_name\\\": \\\"Video290924 (BJbdt).mp4\\\"}], \\\"thumbs\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgWzYwGIA61LNEvlhthXsTmgWm3nfTmhBHYe4z/AI0rklNgM8UVZFrkZ3j8RRRdDNABPamjYQ2Aob61RiMjYIuFU+hzkfpUqLsjYq6NjqQtS1Yatct/u/UUUIkbwq2xcnr8tFToJuKdmZCyNkAMR+OKnjlK53kHIx94UUVpZBYkS+SNAFUk9zRRRS5UNx5ndn8=\\\"}]}}\",\"entities\":[{\"kind\":\"MessageEntityBold\",\"offset\":432,\"length\":2},{\"kind\":\"MessageEntityBold\",\"offset\":434,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":434,\"length\":2,\"documentId\":\"6301075047410829543\"},{\"kind\":\"MessageEntityBold\",\"offset\":436,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":437,\"length\":1},{\"kind\":\"MessageEntityTextUrl\",\"offset\":438,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":438,\"length\":4},{\"kind\":\"MessageEntityItalic\",\"offset\":438,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":442,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":442,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":451,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":451,\"length\":14},{\"kind\":\"MessageEntityItalic\",\"offset\":451,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":465,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":465,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":471,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":471,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":471,\"length\":2,\"documentId\":\"5217880283860194582\"},{\"kind\":\"MessageEntityBold\",\"offset\":473,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":473,\"length\":2},{\"kind\":\"MessageEntityBold\",\"offset\":475,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":475,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":475,\"length\":2,\"documentId\":\"5251203410396458957\"},{\"kind\":\"MessageEntityBold\",\"offset\":477,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":477,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":483,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":483,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":483,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":491,\"length\":16},{\"kind\":\"MessageEntityItalic\",\"offset\":491,\"length\":15},{\"kind\":\"MessageEntityBold\",\"offset\":507,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":507,\"length\":2,\"documentId\":\"5406745015365943482\"}],\"meta\":{\"views\":1250,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":6,\"publishDate\":\"2024-09-29T03:19:31Z\",\"deletedAt\":null,\"reactions\":[{\"count\":6,\"emoticon\":\"❤\"}],\"isAd\":false},\"album\":[],\"photo\":null,\"video\":{\"width\":1080,\"height\":1920,\"size\":134795323,\"durationSeconds\":178.077,\"url\":\"\",\"thumbUrl\":\"\",\"filename\":\"Video290924 (BJbdt).mp4\",\"thumbBase64\":\"$49\"}},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1635,\"publishDate\":\"2024-09-28T10:20:10Z\",\"message\":\"অবসর গ্রহণের পর, ব্রাভো আইপিএল ২০২৫-এর জন্য কেকেআরের মেন্টর হিসেবে দায়িত্ব নেবেন।\\n\\nডোয়েন ব্রাভো অবসর নিয়েছেন এবং ২০২৫ সাল থেকে কলকাতা নাইট রাইডার্স (KKR)-এর মেন্টর হিসেবে যোগ দিয়েছেন, তিনি নাইট রাইডার্সের সব ফ্র্যাঞ্চাইজি পর্যবেক্ষণ করবেন। তিনি চেন্নাই সুপার কিংস (CSK) এর সাবেক কোচ এবং খেলোয়াড়। ব্রাভো পরামর্শক কোচ হিসাবে আফগানিস্তানকে ২০২৪ টি-টোয়েন্টি বিশ্বকাপের সেমিফাইনালে পৌঁছাতে সাহায্য করেছিলেন।\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6323332483222978158, \\\"date\\\": \\\"2024-09-28T10:20:10+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgoqyy5+VenrUYBJAHJNJUluQJ0LcDNdNuVaFRioqyFaF4WBmTCn0PNE8S9UBx0+lT3Zz5YzIwYfLn1zSmJ+V2845PaudTd9RspP5ezAQhxjPPWipJosEjvRV8l9UQ0QhqmiKB1Lk9elQBSRkY/OpCSB86g496fO7DTLlxGHkEquAB+lILoEdC2OT24qk0xYYHA9M0vnbVwB29etQoodyeR/NkL9jRUHnZOcAeworeMklYaYRugQhwc57Af1p7TRnAw2PTav+FFFYGYxpIhyFbP0X/CmvJC20YcADsAKKKQyJyu75M496KKKLgf\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [16794, 45910, 85818, 132926, 213538]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"meta\":{\"views\":1787,\"forwardsCount\":4,\"commentsCount\":0,\"reactionsCount\":18,\"publishDate\":\"2024-09-28T10:20:10Z\",\"deletedAt\":null,\"reactions\":[{\"count\":17,\"emoticon\":\"👍\"},{\"count\":1,\"emoticon\":\"🔥\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":213538,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$4a\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1634,\"publishDate\":\"2024-09-28T09:40:42Z\",\"message\":\"গায়ানা আমাজন ওয়ারিয়র্স বনাম বার্বাডোজ রয়্যালস, ২৭ তম ম্যাচের হাইলাইটস | ক্যারিবিয়ান প্রিমিয়ার লিগ ২০২৪\\n\\nগায়ানা অ্যামাজন ওয়ারিয়র্স বার্বাডোজ রয়্যালসকে ৪৭ রানে পরাজিত করে। ফলে ২০২৪ রিপাবলিক ব্যাঙ্ক ক্যারিবিয়ান প্রিমিয়ার লিগের CPL পয়েন্ট টেবিলে শীর্ষ দুয়ে থাকার সম্ভাবনা রয়েছে। রয়্যালস, তাদের পূর্ববর্তী ফর্মের কারণে টেবিলের শীর্ষে উঠার আশায় ছিল, তবে সাম্প্রতিক ম্যাচে তৃতীয় পরাজয়ের ফলে তাদের তৃতীয় বা চতুর্থ স্থানে স্থির থাকতে হবে। ম্যাচের অধিনায়ক রোভম্যান পাওয়েল টসে জয়ী হয়ে প্রতিপক্ষকে ব্যাটিং করতে পাঠান। গুরবাজ দ্রুত আউট হলেও ওয়ারিয়র্স ২০ ওভারে ২১৯/৮ রান করতে সক্ষম হয়।\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaDocument\\\", \\\"nopremium\\\": false, \\\"spoiler\\\": false, \\\"video\\\": true, \\\"round\\\": false, \\\"voice\\\": false, \\\"document\\\": {\\\"_\\\": \\\"Document\\\", \\\"id\\\": 6323332482766737666, \\\"date\\\": \\\"2024-09-28T09:40:42+00:00\\\", \\\"mime_type\\\": \\\"video/mp4\\\", \\\"size\\\": 134562703, \\\"attributes\\\": [{\\\"_\\\": \\\"DocumentAttributeVideo\\\", \\\"duration\\\": 176.109, \\\"w\\\": 1080, \\\"h\\\": 1920, \\\"round_message\\\": false, \\\"supports_streaming\\\": true, \\\"nosound\\\": false}, {\\\"_\\\": \\\"DocumentAttributeFilename\\\", \\\"file_name\\\": \\\"Video280924 (BJbdt).mp4\\\"}], \\\"thumbs\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgWzYwGIA61LNEvlhthXsTmlFmQc7qc0A29h78/40risUmAzRVoWZ/vfpRRdDNAnjv+VN8xSOwqlE8zDIudp7gk/wCFSwxgg4KyH1Hb86W24XLG5SOtFKkaNCpIVif4gOtFQ5A2luzIWRsgBiPxxViGYxkliCcY+8DRRWlkJxTHR34jUACiiijlQuRH\\\"}]}}\",\"entities\":[],\"meta\":{\"views\":1642,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":11,\"publishDate\":\"2024-09-28T09:40:42Z\",\"deletedAt\":null,\"reactions\":[{\"count\":10,\"emoticon\":\"👍\"},{\"count\":1,\"emoticon\":\"❤\"}],\"isAd\":false},\"album\":[],\"photo\":null,\"video\":{\"width\":1080,\"height\":1920,\"size\":134562703,\"durationSeconds\":176.109,\"url\":\"\",\"thumbUrl\":\"\",\"filename\":\"Video280924 (BJbdt).mp4\",\"thumbBase64\":\"$4b\"}},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1633,\"publishDate\":\"2024-09-28T08:35:01Z\",\"message\":\"🔒 baji  প্রিমিয়াম ডিপোজিট সিস্টেম উন্নত এনক্রিপশনের সাথে সর্বাধিক নিরাপত্তা, সহজ ব্যবহার এবং নিরাপদ লেনদেন নিশ্চিত করে 🔐\\n\\n💵 সহজ ডিপোজিট  এবং দ্রুত উত্তোলন এবং চিন্তামুক্ত গেমিং অভিজ্ঞতার জন্য তৈরি করে।\\n\\n🔒 baji তে অত্যাধুনিক ডিপোজিট সিস্টেম এনক্রিপশন প্রযুক্তি সহ শীর্ষ-স্তরের নিরাপত্তা প্রদান করে 🔐\\n\\nপ্রতিটি লেনদেনে অতুলনীয় নিরাপত্তা এবং সুবিধার জন্য baji কে  বিশ্বাস করুন 🔓।\\n\\nস্ট্রেস-মুক্ত, নিরাপদ অ্যাডভেঞ্চারের জন্য এখনই baji তে যোগ দিন।\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6323332483222978123, \\\"date\\\": \\\"2024-09-28T08:23:07+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgopTOX+Vfu/wA6bHbs5GB1qZI8kCtCCPBCp0H3j61vypK5hzW0RmGzcdv1FRNEyHBBBrYughBHeqs5RFCyt1HB64p2T3KTZTYxmMYUh+M89aKRgpGVORRWTVi7liKQZBzVuC5Vc89qy1V8blBx64p+yUH7j8/7JrRSTWpm4F17lWyOcnjFV7mcEbNucAc1ARMq5YEAcZKmk3j+90oumPlEBwmMY5opjNk0Vm2i7E8TIFIdiM9tuf60pMRx85z0Pyn/ABooqWhjHZBGcPk/3SD/AI1Azbj0A+lFFIY2iiigDw==\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [19439, 40778, 64695, 89189, 138102]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"replyMarkup\":{\"rows\":[{\"buttons\":[{\"kind\":\"KeyboardButtonCallback\",\"text\":\"❤️\"},{\"kind\":\"KeyboardButtonCallback\",\"text\":\"🔥\"},{\"kind\":\"KeyboardButtonCallback\",\"text\":\"🤩\"}]},{\"buttons\":[{\"kind\":\"KeyboardButtonUrl\",\"text\":\"এখনি যোগ দিন\",\"url\":\"https://baji.social/bj/tgndt\"}]}]},\"meta\":{\"views\":1578,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":11,\"publishDate\":\"2024-09-28T08:35:01Z\",\"deletedAt\":null,\"reactions\":[{\"count\":8,\"emoticon\":\"👍\"},{\"count\":3,\"emoticon\":\"❤\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":138102,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$4c\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1632,\"publishDate\":\"2024-09-28T08:27:59Z\",\"message\":\"🔒 baji  প্রিমিয়াম ডিপোজিট সিস্টেম উন্নত এনক্রিপশনের সাথে সর্বাধিক নিরাপত্তা, সহজ ব্যবহার এবং নিরাপদ লেনদেন নিশ্চিত করে 🔐...\\n💵 সহজ ডিপোজিট  এবং দ্রুত উত্তোলন এবং চিন্তামুক্ত গেমিং অভিজ্ঞতার জন্য তৈরি করে।\\n\\n🔒 baji তে অত্যাধুনিক ডিপোজিট সিস্টেম এনক্রিপশন প্রযুক্তি সহ শীর্ষ-স্তরের নিরাপত্তা প্রদান করে 🔐\\n\\nপ্রতিটি লেনদেনে অতুলনীয় নিরাপত্তা এবং সুবিধার জন্য baji কে  বিশ্বাস করুন 🔓।\\n\\nস্ট্রেস-মুক্ত, নিরাপদ অ্যাডভেঞ্চারের জন্য এখনই baji তে যোগ দিন।\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6323332483222978123, \\\"date\\\": \\\"2024-09-28T08:23:07+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgopTOX+Vfu/wA6bHbs5GB1qZI8kCtCCPBCp0H3j61vypK5hzW0RmGzcdv1FRNEyHBBBrYughBHeqs5RFCyt1HB64p2T3KTZTYxmMYUh+M89aKRgpGVORRWTVi7liKQZBzVuC5Vc89qy1V8blBx64p+yUH7j8/7JrRSTWpm4F17lWyOcnjFV7mcEbNucAc1ARMq5YEAcZKmk3j+90oumPlEBwmMY5opjNk0Vm2i7E8TIFIdiM9tuf60pMRx85z0Pyn/ABooqWhjHZBGcPk/3SD/AI1Azbj0A+lFFIY2iiigDw==\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [19439, 40778, 64695, 89189, 138102]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"replyMarkup\":{\"rows\":[{\"buttons\":[{\"kind\":\"KeyboardButtonUrl\",\"text\":\"Join Now\",\"url\":\"https://baji.social/bj/tgndt\"}]}]},\"meta\":{\"views\":3,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":0,\"publishDate\":\"2024-09-28T08:27:59Z\",\"deletedAt\":\"2024-09-28T08:30:31Z\",\"reactions\":[],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":138102,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$4d\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1631,\"publishDate\":\"2024-09-28T08:23:07Z\",\"message\":\"🔒 baji  প্রিমিয়াম ডিপোজিট সিস্টেম উন্নত এনক্রিপশনের সাথে সর্বাধিক নিরাপত্তা, সহজ ব্যবহার এবং নিরাপদ লেনদেন নিশ্চিত করে 🔐\\n\\n💵 সহজ ডিপোজিট  এবং দ্রুত উত্তোলন এবং চিন্তামুক্ত গেমিং অভিজ্ঞতার জন্য তৈরি করে।\\n\\n🔒 baji তে অত্যাধুনিক ডিপোজিট সিস্টেম এনক্রিপশন প্রযুক্তি সহ শীর্ষ-স্তরের নিরাপত্তা প্রদান করে 🔐\\n\\nপ্রতিটি লেনদেনে অতুলনীয় নিরাপত্তা এবং সুবিধার জন্য baji কে  বিশ্বাস করুন 🔓।\\n\\nস্ট্রেস-মুক্ত, নিরাপদ অ্যাডভেঞ্চারের জন্য এখনই baji তে যোগ দিন।\\n\\n\\n❤️  Baji  সদস্য  হিসাবে সাইন-আপ করুন 🚀\\n 🛡এখনই  Baji Appডাউনলোড  করুন!! ⬇️\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6323332483222978123, \\\"date\\\": \\\"2024-09-28T08:23:07+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgopTOX+Vfu/wA6bHbs5GB1qZI8kCtCCPBCp0H3j61vypK5hzW0RmGzcdv1FRNEyHBBBrYughBHeqs5RFCyt1HB64p2T3KTZTYxmMYUh+M89aKRgpGVORRWTVi7liKQZBzVuC5Vc89qy1V8blBx64p+yUH7j8/7JrRSTWpm4F17lWyOcnjFV7mcEbNucAc1ARMq5YEAcZKmk3j+90oumPlEBwmMY5opjNk0Vm2i7E8TIFIdiM9tuf60pMRx85z0Pyn/ABooqWhjHZBGcPk/3SD/AI1Azbj0A+lFFIY2iiigDw==\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [19439, 40778, 64695, 89189, 138102]}], \\\"has_stickers\\\": false}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":451,\"length\":2,\"documentId\":\"6301075047410829543\"},{\"kind\":\"MessageEntityBold\",\"offset\":453,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":454,\"length\":1},{\"kind\":\"MessageEntityTextUrl\",\"offset\":455,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":455,\"length\":4},{\"kind\":\"MessageEntityItalic\",\"offset\":455,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":459,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":459,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":468,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":468,\"length\":14},{\"kind\":\"MessageEntityItalic\",\"offset\":468,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":482,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":482,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":488,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":488,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":488,\"length\":2,\"documentId\":\"5217880283860194582\"},{\"kind\":\"MessageEntityBold\",\"offset\":490,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":490,\"length\":2},{\"kind\":\"MessageEntityBold\",\"offset\":492,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":492,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":492,\"length\":2,\"documentId\":\"5251203410396458957\"},{\"kind\":\"MessageEntityBold\",\"offset\":494,\"length\":5},{\"kind\":\"MessageEntityItalic\",\"offset\":494,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":500,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":500,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":500,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":508,\"length\":16},{\"kind\":\"MessageEntityItalic\",\"offset\":508,\"length\":15},{\"kind\":\"MessageEntityBold\",\"offset\":524,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":524,\"length\":2,\"documentId\":\"5406745015365943482\"},{\"kind\":\"MessageEntityBold\",\"offset\":526,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":530,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":533,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":533,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":533,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":541,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":556,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":559,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":559,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":559,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":567,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":570,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":570,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":570,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":579,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":579,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":593,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":596,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":596,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":596,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":604,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":607,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":607,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":607,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":613,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":613,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":634,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":637,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":637,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":637,\"length\":9}],\"meta\":{\"views\":1,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":0,\"publishDate\":\"2024-09-28T08:23:07Z\",\"deletedAt\":\"2024-09-28T08:24:53Z\",\"reactions\":[],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":138102,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$4e\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1630,\"publishDate\":\"2024-09-28T06:25:46Z\",\"message\":\"বিরতিহীন বিনোদন এবং বড় পুরস্কার খুঁজছেন? Jili Teen Patti আপনার জন্য! লক্ষ লক্ষ খেলোয়াড়ের সাথে যোগ দিন এবং রোমাঞ্চকর ম্যাচে আপনার কার্ডের দক্ষতা প্রদর্শন করুন। রিয়েল প্লেয়ারদের বিরুদ্ধে খেলুন, বিশেষ বৈশিষ্ট্যগুলি আনলক করুন এবং অত্যাশ্চর্য ভিজ্যুয়াল উপভোগ করুন। আজই শুরু করুন baji-র সাথে। \\n\\n❤️  Baji  সদস্য  হিসাবে সাইন-আপ করুন 🔼\\n 🛡এখনই  Baji Appডাউনলোড  করুন!! ⬇️\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6321259092055801904, \\\"date\\\": \\\"2024-09-28T06:25:46+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgozxknAqyoESbjyaSKPYMn71JIHkcRoucde1aTqdEZ/HKyJFcnG5cbuhqO4QMPlGWHpU10zKkaovK9T6U6zSPcZQ24gdD2NZxel2W6SUtCixj2YCFXGM5NFWL6WGR2HlbHHQjvRVWYNWHx4cgA/jTZplMqxxAADv3qqryIuVzjscVZEqPgsj5U9cAc1EvMdJcmqNB9kUBZ23OR0xWe+FgmaPIyR07U43WSeD7VG88K71KN83Pt7Ulo9DS+mpVaRm+8c0VHmiui5mWonQRkM+OemD/jTzImT+8yD1yD/jRRWTQkRO6Y+TGc+h/xqFzkCiip2Kb0GUUUVVxH\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [20540, 50778, 83776, 112348, 171875]}], \\\"has_stickers\\\": false}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":293,\"length\":2,\"documentId\":\"6301075047410829543\"},{\"kind\":\"MessageEntityBold\",\"offset\":295,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":296,\"length\":1},{\"kind\":\"MessageEntityTextUrl\",\"offset\":297,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":297,\"length\":4},{\"kind\":\"MessageEntityItalic\",\"offset\":297,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":301,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":301,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":310,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":310,\"length\":14},{\"kind\":\"MessageEntityItalic\",\"offset\":310,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":324,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":324,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":330,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":330,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":330,\"length\":2,\"documentId\":\"5449683594425410231\"},{\"kind\":\"MessageEntityBold\",\"offset\":332,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":332,\"length\":2},{\"kind\":\"MessageEntityBold\",\"offset\":334,\"length\":2},{\"kind\":\"MessageEntityItalic\",\"offset\":334,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":334,\"length\":2,\"documentId\":\"5251203410396458957\"},{\"kind\":\"MessageEntityBold\",\"offset\":336,\"length\":5},{\"kind\":\"MessageEntityItalic\",\"offset\":336,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":342,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":342,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":342,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":350,\"length\":16},{\"kind\":\"MessageEntityItalic\",\"offset\":350,\"length\":15},{\"kind\":\"MessageEntityBold\",\"offset\":366,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":366,\"length\":2,\"documentId\":\"5406745015365943482\"},{\"kind\":\"MessageEntityBold\",\"offset\":368,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":372,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":375,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":375,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":375,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":383,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":398,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":401,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":401,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":401,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":409,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":412,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":412,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":412,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":421,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":421,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":435,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":438,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":438,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":438,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":446,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":449,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":449,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":449,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":455,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":455,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":476,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":479,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":479,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":479,\"length\":9}],\"meta\":{\"views\":1679,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":11,\"publishDate\":\"2024-09-28T06:25:46Z\",\"deletedAt\":null,\"reactions\":[{\"count\":11,\"emoticon\":\"👍\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":171875,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$4f\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1629,\"publishDate\":\"2024-09-27T11:07:11Z\",\"message\":\"দ্বিতীয় টেস্টের প্রথম দিন ৩৫ ওভারের খেলা বৃষ্টির কারণে এবং খারাপ আলোতে বন্ধ হয়ে যায়। আর. অশ্বিন প্রথম উইকেট নেন, বাংলাদেশ অধিনায়ক নাজমুল হোসেন শান্তকে আউট করে। আকাশ দীপ দুই ওপেনারকে আউট করেন, জাকির হাসান শূন্য এবং সাদমান ইসলাম ২৪ রান করেন। টস জিতে ভারতীয় অধিনায়ক রোহিত শর্মা প্রথমে বোলিংয়ের সিদ্ধান্ত নেন।\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6321256278852222858, \\\"date\\\": \\\"2024-09-27T11:06:16+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgo2aKxpI2aQ/vZTjuWpmyUDiaX/vqgDcrP1K3hmTcWVZQODnr7VTKzY5ml/wC+qiIUf8tmzQBFKY8ECPY49yaKe1vvG4OSccZFFMRpxOjoGQ7lPTNPOzGCBWLbzvC3cqeoq+k4YZz16VnyO47ljCEEc0C3j2Fedp5qHzV608ToO9aWSESLBGoxzj3oqI3CEHnp6UVLjfqLmSMpZSFAx09zS+cfT9TRRVtILgZ+xH6mnrKZDtVR78miiosOTsiYADoMepooopnI2Q==\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [20067, 54495, 100186, 140399, 207303]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"replyMarkup\":{\"rows\":[{\"buttons\":[{\"kind\":\"KeyboardButtonUrl\",\"text\":\"এখনই যোগ দিন\",\"url\":\"https://baji.social/bj/tgndt\"}]}]},\"meta\":{\"views\":2245,\"forwardsCount\":1,\"commentsCount\":0,\"reactionsCount\":13,\"publishDate\":\"2024-09-27T11:07:11Z\",\"deletedAt\":null,\"reactions\":[{\"count\":13,\"emoticon\":\"👍\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":207303,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$50\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1627,\"publishDate\":\"2024-09-27T05:30:51Z\",\"message\":\"সেন্ট লুসিয়া কিংস বনাম ট্রিনবাগো নাইট রাইডার্স, ২৬ তম ম্যাচ হাইলাইটস | ক্যারিবিয়ান প্রিমিয়ার লিগ ২০২৪\\n\\nসেন্ট লুসিয়া কিংস ২০২৪ রিপাবলিক ব্যাংক ক্যারিবিয়ান প্রিমিয়ার লিগ (সিপিএল) প্লে-অফে অন্য তিনটি দলের জন্য একটি বিশাল সংকেত পাঠিয়েছে, তারা ২০ ওভারে ২১৮ রান সংগ্রহ করেছে এবং ট্রিনবাগো নাইট রাইডার্সকে ১৩৮/৯ রানে সীমাবদ্ধ করে ৮০ রানে বিজয়ী হয়েছে এবং পয়েন্ট টেবিলে সবার শীর্ষে আছে। কিংস ক্যাপ্টেন ফাফ ডু প্লেসিস এবং তার ওপেনিং পার্টনার জনসন চার্লস দুর্দান্ত ব্যাট করে। তাদের মধ্যে ১৪৫ রানের ওপেনিং পার্টনারশিপ হয় যেখানে তারা একাধিক বাউন্ডারি মেরেছিলেন, সেই কারনেই প্রথম ইনিংসটি শেষ হতে দুই ঘন্টার বেশি সময় লেগেছিল।\\n\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaDocument\\\", \\\"nopremium\\\": false, \\\"spoiler\\\": false, \\\"video\\\": true, \\\"round\\\": false, \\\"voice\\\": false, \\\"document\\\": {\\\"_\\\": \\\"Document\\\", \\\"id\\\": 6318711158085783761, \\\"date\\\": \\\"2024-09-27T05:30:51+00:00\\\", \\\"mime_type\\\": \\\"video/mp4\\\", \\\"size\\\": 128533942, \\\"attributes\\\": [{\\\"_\\\": \\\"DocumentAttributeVideo\\\", \\\"duration\\\": 169.035, \\\"w\\\": 1080, \\\"h\\\": 1920, \\\"round_message\\\": false, \\\"supports_streaming\\\": true, \\\"nosound\\\": false}, {\\\"_\\\": \\\"DocumentAttributeFilename\\\", \\\"file_name\\\": \\\"Video270924 (BJbdt).mp4\\\"}], \\\"thumbs\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgWzYwGIA61NNEvlhthXsTmlFkQfv8A6U5rfIPT8M/40rk2KLAZ4oqyLTn736UUXRRpgLjpz9KRdhduFz6+tZ0byvyLkKfQk5/lU0MWQdrhmA6qKVhc1ty2NozuxnPH0oqKM7y0chDMh60VMvddmO8TLWRuArEfjirUFw0QOcFjxncDiiirsJq5HFdLE7Pglm60UUUWDlR/\\\"}]}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":623,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":625,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":627,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":627,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":631,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":640,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":640,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":654,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":661,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":661,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":663,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":665,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":667,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":672,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":672,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":680,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":697,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":697,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":698,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":702,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":705,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":705,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":705,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":713,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":728,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":731,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":731,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":731,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":739,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":742,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":742,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":742,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":751,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":751,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":765,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":768,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":768,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":768,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":776,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":779,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":779,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":779,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":785,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":785,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":806,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":809,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":809,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":809,\"length\":9}],\"meta\":{\"views\":2314,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":11,\"publishDate\":\"2024-09-27T05:30:51Z\",\"deletedAt\":null,\"reactions\":[{\"count\":11,\"emoticon\":\"👍\"}],\"isAd\":false},\"album\":[],\"photo\":null,\"video\":{\"width\":1080,\"height\":1920,\"size\":128533942,\"durationSeconds\":169.035,\"url\":\"\",\"thumbUrl\":\"\",\"filename\":\"Video270924 (BJbdt).mp4\",\"thumbBase64\":\"$51\"}},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1626,\"publishDate\":\"2024-09-27T04:18:05Z\",\"message\":\"শুক্রবার বিশেষ প্রতিযোগিতা খুবই  কাছাকাছি!  ৪র্থ রাউন্ড  ২৭ সেপ্টেম্বর থেকে ৪ অক্টোবর পর্যন্ত অনুষ্ঠিত হবে, যা উত্তেজনাপূর্ণ গেম এবং চমত্কার পুরস্কার নিয়ে আসবে। প্রতিযোগিতায় যোগদান, স্পিন এবং বড় জয়ের সুযোগ মিস করবেন না! আপনার ক্যালেন্ডার চিহ্নিত করুন এবং  একশনের জন্য প্রস্তুত হন!\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6321157142417096443, \\\"date\\\": \\\"2024-09-27T04:17:02+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgoijmgSNfug/7tQGB3+eNCUJ4pscJcAjvU6pIuEQEn61nbsbaIjFtIcjYRSSWzoMkAduoq1HG7P5UiKoPJOSf606W3Xyt0bFmzgAUaoLplBzHswEKuMZ5oqzNbqIt38Q75GKKtTTM3B9BtsfkUKGLDPQU9STL8oPpj3qK3nSNMNjrnvU0bjcWLld3TAoive12LurD1jkaRskLxznsKeEaPaQyke30NRCQK7nPynjqKJJQ2cZyfcdKzn8WmwKLtcdIP3bYxgYPTHWimy+YQwZcE4zlulFTYtFNPL2jdjPfg07MPH3fyP+NFFdBzCMUJ++AM9ADSbguCjnI9qKKzaNoybRdgMjfPJjnoMUUUUHPKTbM=\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [24997, 78801, 152582, 203708, 311527]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"replyMarkup\":{\"rows\":[{\"buttons\":[{\"kind\":\"KeyboardButtonUrl\",\"text\":\"আরো বিস্তারিত জানার জন্য\",\"url\":\"https://bit.ly/3ZdCTXT\"}]}]},\"meta\":{\"views\":2082,\"forwardsCount\":1,\"commentsCount\":0,\"reactionsCount\":13,\"publishDate\":\"2024-09-27T04:18:05Z\",\"deletedAt\":null,\"reactions\":[{\"count\":9,\"emoticon\":\"👍\"},{\"count\":3,\"emoticon\":\"🔥\"},{\"count\":1,\"emoticon\":\"🫡\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":311527,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$52\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1625,\"publishDate\":\"2024-09-27T03:23:46Z\",\"message\":\"🔥 চূড়ান্ত ক্রিকেট অভিজ্ঞতার জন্য প্রস্তুত হন! SKN Patriots-এর গর্বিত স্পন্সর হিসাবে,baji নিয়ে আসে সবচেয়ে রোমাঞ্চকর মুহূর্তগুলো– দারুণ ছক্কা, উইকেট, এবং বিদ্যুতের মতো খেলা। ⚡️\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram             📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaDocument\\\", \\\"nopremium\\\": false, \\\"spoiler\\\": false, \\\"video\\\": true, \\\"round\\\": false, \\\"voice\\\": false, \\\"document\\\": {\\\"_\\\": \\\"Document\\\", \\\"id\\\": 6318711158085783679, \\\"date\\\": \\\"2024-09-27T03:23:45+00:00\\\", \\\"mime_type\\\": \\\"video/mp4\\\", \\\"size\\\": 44873015, \\\"attributes\\\": [{\\\"_\\\": \\\"DocumentAttributeVideo\\\", \\\"duration\\\": 24.0, \\\"w\\\": 1920, \\\"h\\\": 1080, \\\"round_message\\\": false, \\\"supports_streaming\\\": true, \\\"nosound\\\": false}, {\\\"_\\\": \\\"DocumentAttributeFilename\\\", \\\"file_name\\\": \\\"Baji SKN Patriots promo video.mp4\\\"}], \\\"thumbs\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ARYoxaKKKACiiigAooooAKKKKACiiigAooooAw==\\\"}]}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":180,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":182,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":184,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":184,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":188,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":197,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":197,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":211,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":218,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":218,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":220,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":222,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":224,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":229,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":229,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":237,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":254,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":254,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":255,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":259,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":262,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":262,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":262,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":270,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":285,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":288,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":288,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":288,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":296,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":299,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":299,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":299,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":308,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":308,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":321,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":324,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":324,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":324,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":332,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":335,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":335,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":335,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":341,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":341,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":362,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":365,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":365,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":365,\"length\":9}],\"meta\":{\"views\":1899,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":11,\"publishDate\":\"2024-09-27T03:23:46Z\",\"deletedAt\":null,\"reactions\":[{\"count\":9,\"emoticon\":\"🔥\"},{\"count\":2,\"emoticon\":\"👍\"}],\"isAd\":false},\"album\":[],\"photo\":null,\"video\":{\"width\":1920,\"height\":1080,\"size\":44873015,\"durationSeconds\":24,\"url\":\"\",\"thumbUrl\":\"\",\"filename\":\"Baji SKN Patriots promo video.mp4\",\"thumbBase64\":\"data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAWACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDFooooAKKKKACiiigAooooAKKKKACiiigD/9k=\"}},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1624,\"publishDate\":\"2024-09-27T03:05:45Z\",\"message\":\"সময় প্রায় শেষ কিন্তু রোমাঞ্চ এখনো ফুরিয়ে যায়নি!\\n\\nআমাদের 'ক্রিকেট ম্যারাথন লিডারবোর্ড' কনটেস্টে আপনার জন্য এখনও ৳১৫ কোটিরও বেশি একটি শট অপেক্ষা করছে। আপনার বোনাসের অংশ বাড়িতে নিতে ডিপোজিট করুন, স্পোর্টস মার্কেটে বেট রাখুন, পয়েন্ট সংগ্রহ করুন এবং শীর্ষ ৫০০-এ উঠুন। শেষ বাঁশি বাজার আগে এখনই অ্যাকশন নিন!\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram             📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6318711158542024147, \\\"date\\\": \\\"2024-09-27T03:05:45+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgoootX4o8IrA5J7YpFiUxhl2EH35pvnqtyI1QYzgEHp71k1chNlk3ixziNlYdgSODSXlt565OAexqEQvNfqrrhY+WOe3apflckg554JPGO1HLbVFszJBGq7dhVxjPPWirlxArg/cBHcHpRWqkRzEVvKmBndnuKbIJDP5YU4JyAKiiWPbuaYq2egTNTyMpYf6U49B5VK2o4qzJ7iRoLby0x5sh+cj0qmMjaCSAzVNIy4UBw5PJJTbiq6uEbKqeDnrxTTKLLuMYJzRUQLTv79zRU2MHZMZC6CMqzAfn/AENSNKh/j/8AQv8AGiiraNrjJpEc4EpVcdMEj+dRRI0rYH4n0oopNWJk7K5fRBGuBRRRQczP\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [22726, 59597, 108882, 158399, 250035]}], \\\"has_stickers\\\": false}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":306,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":308,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":310,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":310,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":314,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":323,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":323,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":337,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":344,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":344,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":346,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":348,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":350,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":355,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":355,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":363,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":380,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":380,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":381,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":385,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":388,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":388,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":388,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":396,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":411,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":414,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":414,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":414,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":422,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":425,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":425,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":425,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":434,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":434,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":447,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":450,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":450,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":450,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":458,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":461,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":461,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":461,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":467,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":467,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":488,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":491,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":491,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":491,\"length\":9}],\"meta\":{\"views\":1925,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":6,\"publishDate\":\"2024-09-27T03:05:45Z\",\"deletedAt\":null,\"reactions\":[{\"count\":5,\"emoticon\":\"🔥\"},{\"count\":1,\"emoticon\":\"👍\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":250035,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$53\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1623,\"publishDate\":\"2024-09-26T09:09:59Z\",\"message\":\"সেন্ট কিটস এবং নেভিস প্যাট্রিয়টস বনাম ট্রিনবাগো নাইট রাইডার্স, ২৫ তম ম্যাচ হাইলাইটস | ক্যারিবিয়ান প্রিমিয়ার লিগ ২০২৪\\n\\n২০২৪ সালের রিপাবলিক ব্যাংক CPL-এর দ্বিতীয় ম্যাচে উচ্চ স্কোরিং প্রতিযোগিতায় ত্রিনবাগো নাইট রাইডার্স সেন্ট কিটস অ্যান্ড নেভিস প্যাট্রিয়টসকে সাত উইকেটে হারিয়ে তাদের মৌসুমের ইতি টানে। প্রতিযোগিতায় তাদের প্রথম ম্যাচ জেতার পর থেকে প্যাট্রিয়টস প্রতিটি খেলায় হেরেছে, তবে তারা টস হেরে ব্যাট করতে নেমে ১৯৩/৪ রান করার পরও তারৌবায় এই হারটি বিশেষভাবে নিষ্ঠুর মনে হয়েছে। অধিনায়ক আন্দ্রে ফ্লেচার সামনে থেকে নেতৃত্ব দিয়ে ৬১ বলে ৯৩ রানের অসাধারণ ইনিংস খেলেন, যেখানে চারদিকেই শট মারেন এবং বিশাল ছয়টি ছক্কা মেরেছিলেন। ফ্লেচার তাঁর শতক থেকে মাত্র সাত রান দূরে ছিলেন, যখন ক্রিস জর্ডান তাকে লং অফ বাউন্ডারিতে কায়রন পোলার্ডের \\\"বাকেট হাতে\\\" ক্যাচ আউট করান।\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaDocument\\\", \\\"nopremium\\\": false, \\\"spoiler\\\": false, \\\"video\\\": true, \\\"round\\\": false, \\\"voice\\\": false, \\\"document\\\": {\\\"_\\\": \\\"Document\\\", \\\"id\\\": 6316459358272099353, \\\"date\\\": \\\"2024-09-26T09:09:59+00:00\\\", \\\"mime_type\\\": \\\"video/mp4\\\", \\\"size\\\": 130276776, \\\"attributes\\\": [{\\\"_\\\": \\\"DocumentAttributeVideo\\\", \\\"duration\\\": 169.369, \\\"w\\\": 1080, \\\"h\\\": 1920, \\\"round_message\\\": false, \\\"supports_streaming\\\": true, \\\"nosound\\\": false}, {\\\"_\\\": \\\"DocumentAttributeFilename\\\", \\\"file_name\\\": \\\"Video260924 (BJbdt).mp4\\\"}], \\\"thumbs\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgWzYwGIA61LNEvlhthXsTmlFkQfv8A6U54PlP9M/40rklJgM8UVZFoc9T/AN80UXQzSIG35MZpFKGRhgDGOfWs+N5WGRchT3BJ/wAKlQbI2YOrEdSFqbWGrXsXv3fqPzopqBHhRtoyevFFToJuKdmYyyNkAMR+OKnjlKg7yDkY+8KKK0sFiRL5I0AVWJ7miiilyobipO7P\\\"}]}}\",\"entities\":[],\"meta\":{\"views\":2413,\"forwardsCount\":5,\"commentsCount\":0,\"reactionsCount\":18,\"publishDate\":\"2024-09-26T09:09:59Z\",\"deletedAt\":null,\"reactions\":[{\"count\":10,\"emoticon\":\"👍\"},{\"count\":8,\"emoticon\":\"🔥\"}],\"isAd\":false},\"album\":[],\"photo\":null,\"video\":{\"width\":1080,\"height\":1920,\"size\":130276776,\"durationSeconds\":169.369,\"url\":\"\",\"thumbUrl\":\"\",\"filename\":\"Video260924 (BJbdt).mp4\",\"thumbBase64\":\"$54\"}},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1622,\"publishDate\":\"2024-09-26T08:19:21Z\",\"message\":\"চ্যালেঞ্জ টাইম \\nএই ধাঁধা দিয়ে আপনার মস্তিষ্ক পরীক্ষা করুন এবং দেখুন কত দ্রুত আপনি এটি সমাধান করতে পারেন! ⏳\\nআপনার বন্ধুদেরও চ্যালেঞ্জ করুন — কে সবচেয়ে দ্রুত ধাঁধা সমাধান করতে পারে? 🚀\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6316653542789726264, \\\"date\\\": \\\"2024-09-26T08:13:57+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgozRjPtU6wAjO7jtUccTsSF7HpUsnmRlUHTFJjT6FZgd+09jVqKKOaApkK6nIY96TyBIgIOJO4NNZFjGGyaLgxjmLZhVIcdTnINFR4G75elFVcVmXd6RH5CPmPNTSmORRgHis0MeATwKebl/736UmRyrclfghV+X3NI8IY8v8AMfb/AOvUHmMzDJqVywXjdz7A0rFrQasJA3H8OaKjaVjxnj6UUwEprDuKKKpiGq2DmpPPf1/U0UVIyW2gLncw+T+dFFFBhKbTPw==\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [19690, 41563, 61967, 85643, 127385]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"replyMarkup\":{\"rows\":[{\"buttons\":[{\"kind\":\"KeyboardButtonCallback\",\"text\":\"A . তামিম ইকবাল\"},{\"kind\":\"KeyboardButtonCallback\",\"text\":\"B . মাহমুদুল্লাহ\"}]},{\"buttons\":[{\"kind\":\"KeyboardButtonCallback\",\"text\":\"C . মাশরাফি মুর্তজা\"},{\"kind\":\"KeyboardButtonCallback\",\"text\":\"D . সাকিব আল হাসান\"}]},{\"buttons\":[{\"kind\":\"KeyboardButtonUrl\",\"text\":\"এখনই যোগ দিন\",\"url\":\"https://baji.social/bj/tgndt\"}]}]},\"meta\":{\"views\":2370,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":7,\"publishDate\":\"2024-09-26T08:19:21Z\",\"deletedAt\":null,\"reactions\":[{\"count\":3,\"emoticon\":\"👏\"},{\"count\":2,\"emoticon\":\"👍\"},{\"count\":2,\"emoticon\":\"❤\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":127385,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$55\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1621,\"publishDate\":\"2024-09-26T04:41:38Z\",\"message\":\"লাগামহীন রোমাঞ্চ উপভোগ করুন! \\n\\nআমাদের সীমিত সময়ের 'ওয়েলকাম অফার'-এর মাধ্যমে আপনার মোট উইনিং এর উপর ৳১,০০০ পর্যন্ত একটি ডাবল বোনাস আনলক করুন! শুধু আপনার ফার্স্ট ডিপোজিট করুন, Yellow Bat-এর Diva's Ace গেমে বেট রাখুন, আপনার উইনিং এর স্ক্রিনশট Facebook-এ শেয়ার করুন এবং একটি এক্সট্রা ফ্রি বোনাস লুফে নেওয়ার সহজ রিকোয়ারমেন্টগুলো সম্পূর্ণ করুন! তাড়াতাড়ি করুন, যদিও—এটি 'আগে আসলে আগে পাবেন' ভিত্তিতে পাওয়া যায়। এক্সাইটমেন্ট মিস করবেন না!\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6316653542789726109, \\\"date\\\": \\\"2024-09-26T04:39:15+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgoy40ZslVJqxGHDAFSAPUVXDui/KxH0qeJpDtZtzDOealmi5bEovpBKQB8nQ1Hdph/MXlW5qeK02ZcgOD/AA09bbzbQBmC4zjP1pcyQmiiWiMY2qQ3HOetFRfdYiitLmdhTyMVqwuXt1DueBjZiqUHmCMlOevG0mp8zbSVYZ7YU8/pUyVykWGQ4LK1NIJQRIeT3PvVQLMRy5+uG/wp6Suka7gVcdiOoqGrF3uRXtm1sQd24N3oqSVpLggHHTAGaKpPTUl2RWRwBg5/CneZ7t/n8aKKtogazkD5Sfpk/wCNRBncgAknoKKKTQXL9vF5Yy3L/wAqKKKRyuTbPw==\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [22699, 58951, 99648, 139803, 213019]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"replyMarkup\":{\"rows\":[{\"buttons\":[{\"kind\":\"KeyboardButtonUrl\",\"text\":\"আরো বিস্তারিত জানার জানতে\",\"url\":\"https://bit.ly/3BsfXdA\"}]}]},\"meta\":{\"views\":2504,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":22,\"publishDate\":\"2024-09-26T04:41:38Z\",\"deletedAt\":null,\"reactions\":[{\"count\":9,\"emoticon\":\"❤\"},{\"count\":7,\"emoticon\":\"👍\"},{\"count\":6,\"emoticon\":\"🔥\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":213019,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$56\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1620,\"publishDate\":\"2024-09-26T03:15:14Z\",\"message\":\"ভারত বনাম বাংলাদেশ ম্যাচ মানে হাইভোল্টেজের খেলা! টেস্ট ক্রিকেটে এই দ্বন্দ্বে প্রতিটি বল এবং প্রতিটি ইনিংসে থাকে চরম উত্তেজনা। দুই দলের জন্যই গর্ব এবং ইতিহাসের চ্যালেঞ্জ—দর্শকরা প্রত্যাশা করেন অবিশ্বাস্য নাটকীয়তা, দুর্দান্ত বোলিং এবং অসাধারণ ব্যাটিং! তাই, ভারত-বাংলাদেশের খেলা সবসময়ই বিশেষ কিছু! 🏏🔥\\n\\nআপনার মতামত জানাতে কমেন্ট করুন! ক্রিকেটের এই মহাযুদ্ধ সম্পর্কে আপনার ভাবনা কী? 🏏✨\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6316653542789726069, \\\"date\\\": \\\"2024-09-26T03:07:51+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgopPYOibiDj2oSxeQZXke1Xb6858uNiu08mrlo6rbgFs47+tFmMx/7Nl/umkNm8YJIIAreMiY3b8BeoqtdXCYEI+8SOc9KQGQ/l7AAhV+Op60VZvPlYwSYYrjD9x3oq0S7FNpC7l25JOTWlYX0UcXlyMV547is0IWHGPzqaHCIyyKpGcjkUmBqMqlGcNw2T9cdP6VSuFaXfcDiNcBfek8+Itksfp2p1zcCWEIvTI/KpGyK+djO/PDYPT2op9yFnMezqODiiqEV4pVRCDuznIxj+op/nx/9NP0/wooptIVxkky+WQpfJ9cf4VXUuxCrkk0UVNrDuaMEZiXJ5bvRRRQcrk2f\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [16549, 41761, 64927, 90924, 137038]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"replyMarkup\":{\"rows\":[{\"buttons\":[{\"kind\":\"KeyboardButtonCallback\",\"text\":\"🇮🇳 ভারত\"},{\"kind\":\"KeyboardButtonCallback\",\"text\":\"🇧🇩 বাংলাদেশ\"}]},{\"buttons\":[{\"kind\":\"KeyboardButtonUrl\",\"text\":\"এখনই যোগ দিন\",\"url\":\"https://baji.social/bj/tgndt\"}]}]},\"meta\":{\"views\":2433,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":7,\"publishDate\":\"2024-09-26T03:15:14Z\",\"deletedAt\":null,\"reactions\":[{\"count\":7,\"emoticon\":\"❤\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":137038,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$57\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1619,\"publishDate\":\"2024-09-25T09:39:53Z\",\"message\":\"আপনার পছন্দের স্লট খেলা খুঁজছেন? JILI Slot Fortune Gem 2 খেলুন!আপনার বাজির ১০০০ গুণ পর্যন্ত অসাধারণ পুরস্কার জিততে পারবেন! বিশেষ ৪র্থ রিলে কেবল মাল্টিপ্লায়ার সিম্বল রয়েছে, যা উত্তেজনা এবং সম্ভাবনাকে বাড়িয়ে তোলে। সর্বোচ্চ ৭৫,১২৫,০০০ টাকার বিশাল পুরস্কার জিততে এখনই যোগ দিন এবং ভাগ্যকে পরীক্ষা করুন!\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6314151170289025883, \\\"date\\\": \\\"2024-09-25T09:39:53+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgooJATUwtMDLkL9TVxY1SMv0xzjtVYM0jbycj09KzV5aouTURRax525GMZzj8aja0yu6NgR7VZyPJPJ9P8/hUIJRiw4HpQ7rYNCtJ5YTbsKuMZyaKvXUCSRB0HzEZBoqo1E1qS4voIbjfEw65GAKiDL6bR79qrRStE4Ydql+0MR/q0Pvjmp5XHYrmT3LIuFMflheevSomII6bj7GmC7YD7ic8EY60vnEg5jQD1xg043Qmk9yQOyxKvPA5FFVzIWNFQ43dy1pohqPGEw4OfYCn+ZFkfe/BVoorotcxQ0zx4ON27sSoqMzMx52n/AICKKKiw7kkMZnbcQAo6kDFFFFFjGU2mfw==\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [24004, 69456, 118251, 161176, 244419]}], \\\"has_stickers\\\": false}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":302,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":304,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":306,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":306,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":310,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":319,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":319,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":333,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":340,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":340,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":342,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":344,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":346,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":351,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":351,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":359,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":376,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":376,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":377,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":381,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":384,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":384,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":384,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":392,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":407,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":410,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":410,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":410,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":418,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":421,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":421,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":421,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":430,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":430,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":444,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":447,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":447,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":447,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":455,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":458,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":458,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":458,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":464,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":464,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":485,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":488,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":488,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":488,\"length\":9}],\"meta\":{\"views\":2899,\"forwardsCount\":1,\"commentsCount\":0,\"reactionsCount\":24,\"publishDate\":\"2024-09-25T09:39:53Z\",\"deletedAt\":null,\"reactions\":[{\"count\":12,\"emoticon\":\"👍\"},{\"count\":12,\"emoticon\":\"❤\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":244419,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$58\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1618,\"publishDate\":\"2024-09-25T09:31:03Z\",\"message\":\"বাংলাদেশের বিপক্ষে দ্বিতীয় টেস্টে ছয় রেকর্ডের কাছাকাছি পৌঁছে গেছেন আর অশ্বিন। চতুর্থ ইনিংসে 100 ছুঁতে তার একটি উইকেট  প্রয়োজন।\\n\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6314151170289025879, \\\"date\\\": \\\"2024-09-25T09:31:03+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgounbIAANy54qNQgLRiMA9cYon3GPEPBz0FWUT5ATjeeCaYGYsk8kxB2hS2AuKlms1kQBl2yEfez3qVLZ0umbdhByv1qRnWROeDUO5SsYsyLHlChWQYzznNFX7qFJuhzxhWPY0VSkhOLKkF3KH5ar8N2SfLK8jvmsdQ3VQeO4qeN3PIyrDqcUMSZrPO0Ue8kEZ+6B1pfMgY8cGs/e5QhxuPUDGKkUyeWAAM/ypbj22LjOkn7kdfXFFV4w32pXPQD9aKLILszI5vLTbtzznqRTjccY2Yz/tmiirsiLii7I/h/HcakW7BP3e/wDeNFFKyHctQv5vzkYHrk80UUVNjKUncw==\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [18306, 42406, 61210, 85841, 130062]}], \\\"has_stickers\\\": false}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":132,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":134,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":136,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":136,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":140,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":149,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":149,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":163,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":170,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":170,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":172,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":174,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":176,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":181,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":181,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":189,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":206,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":206,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":207,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":211,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":214,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":214,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":214,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":222,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":237,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":240,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":240,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":240,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":248,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":251,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":251,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":251,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":260,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":260,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":274,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":277,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":277,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":277,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":285,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":288,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":288,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":288,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":294,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":294,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":315,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":318,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":318,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":318,\"length\":9}],\"meta\":{\"views\":2751,\"forwardsCount\":1,\"commentsCount\":0,\"reactionsCount\":6,\"publishDate\":\"2024-09-25T09:31:03Z\",\"deletedAt\":null,\"reactions\":[{\"count\":2,\"emoticon\":\"👍\"},{\"count\":2,\"emoticon\":\"❤\"},{\"count\":2,\"emoticon\":\"🔥\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":130062,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$59\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1617,\"publishDate\":\"2024-09-25T05:33:31Z\",\"message\":\"২০২৪ রিপাবলিক ব্যাংক ক্যারিবিয়ান প্রিমিয়ার লিগ (CPL) এর প্লে-অফ করার জন্য চারটি দল কোয়ালিফাই করেছে   কিন্তু এটি বার্বাডোস রয়্যালস এবং সেন্ট লুসিয়া কিংসকে প্রভিডেন্সে স্তম্ভিত করেছে । ক্রিজে জেসন হোল্ডার এবং মহেশ থেকশানার সাথে শেষ ওভারে রয়্যালসকে ২১ রানের প্রয়োজন ছিল বলে শেষের পর্যায়ে পড়েছিলেন অ্যালিক আথানাজে এবং নাইম ইয়ং।\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaDocument\\\", \\\"nopremium\\\": false, \\\"spoiler\\\": false, \\\"video\\\": true, \\\"round\\\": false, \\\"voice\\\": false, \\\"document\\\": {\\\"_\\\": \\\"Document\\\", \\\"id\\\": 6314151169832783934, \\\"date\\\": \\\"2024-09-25T05:33:31+00:00\\\", \\\"mime_type\\\": \\\"video/mp4\\\", \\\"size\\\": 133156693, \\\"attributes\\\": [{\\\"_\\\": \\\"DocumentAttributeVideo\\\", \\\"duration\\\": 176.109, \\\"w\\\": 1080, \\\"h\\\": 1920, \\\"round_message\\\": false, \\\"supports_streaming\\\": true, \\\"nosound\\\": false}, {\\\"_\\\": \\\"DocumentAttributeFilename\\\", \\\"file_name\\\": \\\"Video250924 (BJbdt).mp4\\\"}], \\\"thumbs\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgWzYwGIA61NNEvlhthXsTmkFng53094Rt5IHvz/jSFYpMBmirItMjIcflRRcDQAOaNyk4AAPc+tUY3mcZFyFPoSc/yqWKIMrYcOQP4RQF7bljj1FFMiCsXjcKWU9QOtFTJ8rs0F0ZiyNkBWI/HFWoLlogc4LHvuBxRRVWBq5HFdCJ2fBLN1ooop2DlRw==\\\"}]}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":334,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":336,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":338,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":338,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":342,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":351,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":351,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":365,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":372,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":372,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":374,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":376,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":378,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":383,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":383,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":391,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":408,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":408,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":409,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":413,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":416,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":416,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":416,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":424,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":439,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":442,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":442,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":442,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":450,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":453,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":453,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":453,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":462,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":462,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":476,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":479,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":479,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":479,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":487,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":490,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":490,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":490,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":496,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":496,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":517,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":520,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":520,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":520,\"length\":9}],\"meta\":{\"views\":3067,\"forwardsCount\":2,\"commentsCount\":0,\"reactionsCount\":6,\"publishDate\":\"2024-09-25T05:33:31Z\",\"deletedAt\":null,\"reactions\":[{\"count\":6,\"emoticon\":\"🔥\"}],\"isAd\":false},\"album\":[],\"photo\":null,\"video\":{\"width\":1080,\"height\":1920,\"size\":133156693,\"durationSeconds\":176.109,\"url\":\"\",\"thumbUrl\":\"\",\"filename\":\"Video250924 (BJbdt).mp4\",\"thumbBase64\":\"$5a\"}},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1616,\"publishDate\":\"2024-09-25T05:22:45Z\",\"message\":\"হুররে! আমাদের 'আল্টিমেট ফিয়েস্তা স্পিন' ক্যাম্পেইন এখন বিজয়ীদের উদযাপন করার সময়! ১০০ জন ভাগ্যবান প্লেয়ারদের অভিনন্দন যারা প্রত্যেকে একটি দুর্দান্ত ৳৫৭৭ বোনাস পেয়েছে। আপনার অবিশ্বাস্য সাপোর্ট এর জন্য এই ক্যাম্পেইনটি একটি বিশাল সফলতা পেয়েছে! আমরা সত্যিই এই আনন্দে আপনার যোগদানকে প্রশংসা করি।\\n\\n'আল্টিমেট ফিয়েস্তা স্পিন' অ্যাডভেঞ্চারে অংশগ্রহণ করার জন্য আপনাকে ধন্যবাদ। আরও রোমাঞ্চকর ক্যাম্পেইন এবং বেশি বেশি জেতার সুযোগ পেতে Baji-এর সাথেই সাথেই থাকুন!\\n\\n\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6314151170289025664, \\\"date\\\": \\\"2024-09-25T05:22:44+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgobSrneAOtRZaUlYxkDqalVH2FMgjsce9ZyfREUqfVkjyTFvKRtmBknGagmHnR4k/1i8Zp5iMc8fzABvUU14njlbzCdrEkN61KjZaHRoyo5jCbfL2uO+etFOlUbiP1NFaqVzJodZz+WxQnAbjNXwojkABypHSspIt65z+lWFaVE25Jx04qJx1uiouxekId41YDk8n2xTr94yIxu4GeKzvOkEgO0nFMlnd3+cYx2qkguWJfJ3EuTmiqZkJPWiko2DmBPL2/NjP0P+NKxj28AZx6H/GiitOXUgipaKKYBRRRQB8=\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [20056, 46609, 76272, 100743, 151922]}], \\\"has_stickers\\\": false}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":457,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":459,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":461,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":461,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":465,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":474,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":474,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":488,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":495,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":495,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":497,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":499,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":501,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":506,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":506,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":514,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":531,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":531,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":532,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":536,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":539,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":539,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":539,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":547,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":562,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":565,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":565,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":565,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":573,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":576,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":576,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":576,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":585,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":585,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":599,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":602,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":602,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":602,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":610,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":613,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":613,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":613,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":619,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":619,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":640,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":643,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":643,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":643,\"length\":9}],\"meta\":{\"views\":2605,\"forwardsCount\":1,\"commentsCount\":0,\"reactionsCount\":17,\"publishDate\":\"2024-09-25T05:22:45Z\",\"deletedAt\":null,\"reactions\":[{\"count\":8,\"emoticon\":\"❤\"},{\"count\":5,\"emoticon\":\"👍\"},{\"count\":4,\"emoticon\":\"😁\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":151922,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$5b\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1615,\"publishDate\":\"2024-09-24T10:36:31Z\",\"message\":\"গতকালের ম্যাচটি ছিল এককথায় অবিস্মরণীয়! আল নাসের আল হামজকে পরাজিত করে মাঠে দারুণ উল্লাস ছড়িয়েছে, যেখানে প্রতিটি মুহূর্ত ছিল চরম উত্তেজনার! দুর্দান্ত গোল, চোখধাঁধানো দক্ষতা এবং তীব্র প্রতিদ্বন্দ্বিতা – ভক্তদের জন্য এটি ছিল সত্যিই স্মরণীয় একটি রাত। আপনার প্রিয় মুহূর্তটি কোনটি ছিল? ⚽️\\n\\nআল হামজ (1) - (2) আল নাসের\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6311899370475338945, \\\"date\\\": \\\"2024-09-24T10:36:31+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgohiDlVYHAJ545FSeWuzLuSM8nPBpLpJEzGCAGA59qWzQAFCB6nvmkMQRKmSqn8OopJI1mgJbIkHIJqeUIkBw/Tu496qGcSRAPnJ/iHrmmg0IZVRBsKFZBjPPWir4iS7tsEYZOA9FO5JS85p8CQjKjAIGKf5rRRoRtBII4qukUjjKIxA7gU945njwYn+U8cGgaFM+9MD7vp/OoZm3AAE4FAIRHVhh+n05pgI5zT0AtwzbItkg+Q85HWiqq5ZtqgnPAFFJsL2J45FWMg5znPSnebHz1+m0UUUW1EQsId2SXwfQColUs2F5J6UUUguX7eARLk8t3NFFFByttsw==\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [19189, 50911, 73245, 103083, 152782]}], \\\"has_stickers\\\": false}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":317,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":319,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":321,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":321,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":325,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":334,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":334,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":348,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":355,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":355,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":357,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":359,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":361,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":366,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":366,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":374,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":391,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":391,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":392,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":396,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":399,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":399,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":399,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":407,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":422,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":425,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":425,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":425,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":433,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":436,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":436,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":436,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":445,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":445,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":459,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":462,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":462,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":462,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":470,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":473,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":473,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":473,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":479,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":479,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":500,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":503,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":503,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":503,\"length\":9}],\"meta\":{\"views\":2985,\"forwardsCount\":4,\"commentsCount\":0,\"reactionsCount\":21,\"publishDate\":\"2024-09-24T10:36:31Z\",\"deletedAt\":null,\"reactions\":[{\"count\":13,\"emoticon\":\"👍\"},{\"count\":6,\"emoticon\":\"❤\"},{\"count\":2,\"emoticon\":\"🔥\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":152782,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$5c\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1614,\"publishDate\":\"2024-09-24T10:35:36Z\",\"message\":\"গতকালের ম্যাচটি ছিল এককথায় অবিস্মরণীয়! আল নাসের আল হামজকে পরাজিত করে মাঠে দারুণ উল্লাস ছড়িয়েছে, যেখানে প্রতিটি মুহূর্ত ছিল চরম উত্তেজনার! দুর্দান্ত গোল, চোখধাঁধানো দক্ষতা এবং তীব্র প্রতিদ্বন্দ্বিতা – ভক্তদের জন্য এটি ছিল সত্যিই স্মরণীয় একটি রাত। আপনার প্রিয় মুহূর্তটি কোনটি ছিল? ⚽️\\n\\nআল হামজ (1) - (2) আল নাসের\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6312040086488858463, \\\"date\\\": \\\"2024-09-24T10:00:01+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgoeY4eV2LkcmqhgyOOvpirDkGMjB3A8nH3qcWiWNtpO7HrxQpWCUSubUAj5/0prWbMpMeWI9qm3I3yk+vQ5705ZyAQFbOc5A70nKQ1GPcoyBFXbsKuMZyaKuS2TTR+YowcZwetFWrdTNvsRQyl4SD19alkY/KVJyPvAGqMcvl8YyM884qX7QuTiMgH/aouUkjQyoB9eOufx61XWOFox5g5/i9ajiYsAdo/xp7SKRwQD7rWbi7FJq5PEZIYwy/dGBRVXzG4VpCV6laKlxuVr2IY5tkYXLcewp4uEyT849MY/wAKKK1cTMTzoyTnzPzFRMy5+TOPeiihbgWbeI8O/wCAooooOaUncw==\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [25324, 80329, 144862, 192050, 293171]}], \\\"has_stickers\\\": false}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":317,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":319,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":321,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":321,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":325,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":334,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":334,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":348,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":355,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":355,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":357,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":359,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":361,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":366,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":366,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":374,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":391,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":391,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":392,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":396,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":399,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":399,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":399,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":407,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":422,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":425,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":425,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":425,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":433,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":436,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":436,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":436,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":445,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":445,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":459,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":462,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":462,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":462,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":470,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":473,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":473,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":473,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":479,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":479,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":500,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":503,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":503,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":503,\"length\":9}],\"meta\":{\"views\":1,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":0,\"publishDate\":\"2024-09-24T10:35:36Z\",\"deletedAt\":\"2024-09-24T10:35:54Z\",\"reactions\":[],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":293171,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$5d\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1613,\"publishDate\":\"2024-09-24T10:15:00Z\",\"message\":\"২৪ সেপ্টেম্বর থেকে ১ অক্টোবর পর্যন্ত চলমান JILI ফিশ টুর্নামেন্টের রাউন্ড ৪-এর উত্তেজনায় ডুবে যান! সমস্ত মুদ্রার জন্য উন্মুক্ত, এটি আপনার খেলার, জেতার এবং রোমাঞ্চকর  ফিশ-থিমযুক্ত গেম উপভোগ করার সুযোগ। মিস করবেন না—মজায় যোগ দিন এবং বড় পুরস্কারের জন্য প্রতিযোগিতা করুন !\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6312040086488858463, \\\"date\\\": \\\"2024-09-24T10:00:01+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgoeY4eV2LkcmqhgyOOvpirDkGMjB3A8nH3qcWiWNtpO7HrxQpWCUSubUAj5/0prWbMpMeWI9qm3I3yk+vQ5705ZyAQFbOc5A70nKQ1GPcoyBFXbsKuMZyaKuS2TTR+YowcZwetFWrdTNvsRQyl4SD19alkY/KVJyPvAGqMcvl8YyM884qX7QuTiMgH/aouUkjQyoB9eOufx61XWOFox5g5/i9ajiYsAdo/xp7SKRwQD7rWbi7FJq5PEZIYwy/dGBRVXzG4VpCV6laKlxuVr2IY5tkYXLcewp4uEyT849MY/wAKKK1cTMTzoyTnzPzFRMy5+TOPeiihbgWbeI8O/wCAooooOaUncw==\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [25324, 80329, 144862, 192050, 293171]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"replyMarkup\":{\"rows\":[{\"buttons\":[{\"kind\":\"KeyboardButtonUrl\",\"text\":\"আরও  বিস্তারিত জানতে\",\"url\":\"https://bit.ly/3AO5Yz6\"}]}]},\"meta\":{\"views\":2853,\"forwardsCount\":1,\"commentsCount\":0,\"reactionsCount\":11,\"publishDate\":\"2024-09-24T10:15:00Z\",\"deletedAt\":null,\"reactions\":[{\"count\":6,\"emoticon\":\"👍\"},{\"count\":5,\"emoticon\":\"🔥\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":293171,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$5e\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1612,\"publishDate\":\"2024-09-24T09:59:05Z\",\"message\":\"২৪ সেপ্টেম্বর থেকে ১ অক্টোবর পর্যন্ত JILI সুপার টুর্নামেন্টের রাউন্ড ৪ এর জন্য প্রস্তুত হন! উত্তেজনাপূর্ণ গেমগুলিতে প্রতিদ্বন্দ্বিতা করার এবং অবিশ্বাস্য পুরস্কার জেতার সুযোগটি মিস করবেন না। অ্যাকশনে যোগ দিন এবং টুর্নামেন্টের রোমাঞ্চের অভিজ্ঞতা নিন!\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6312040086488858460, \\\"date\\\": \\\"2024-09-24T09:57:53+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgozsg1IsErKGVcg9801LaWTOxcge9SpbzKTuQMq9RuoZt6gIZFYB2Vc9802WNQpPmISPQ1NskMe/y4l5z05qN4jIxLj5/QcUrvqx/EiJjEYxtUhuM89aKfJb+Wm7P5+tFWtTFxaJbWdmHlqPm/nU4EpLJlQp71nxStE25OtTJcOQBvCn6VEoNvQpSb0uWCGXaA7FeCBSqwVm43e+MVVYzdd5NRmSTPLNSdN9S1oSyh5CQWyueBRUe8+tFbLlRWgiGMJznd9P8A69ODxcc4x/sf/XooqLHMPDqeEck+4xRzn5koorRbHRTba1JEQH5itFFFZNnn1KknIw==\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [22197, 60414, 109618, 146125, 225622]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"replyMarkup\":{\"rows\":[{\"buttons\":[{\"kind\":\"KeyboardButtonUrl\",\"text\":\"আরও  বিস্তারিত জানতে\",\"url\":\"https://bit.ly/3AO5Yz6\"}]}]},\"meta\":{\"views\":2952,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":8,\"publishDate\":\"2024-09-24T09:59:05Z\",\"deletedAt\":null,\"reactions\":[{\"count\":8,\"emoticon\":\"👍\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":225622,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$5f\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1611,\"publishDate\":\"2024-09-24T04:02:50Z\",\"message\":\"গয়ানা আমাজন ওয়ারিয়র্স বনাম অ্যান্টিগুয়া ও বারবুডা ফ্যালকনস, ২৩তম ম্যাচের হাইলাইটস | CPL২০২৪\\n\\nবর্তমান চ্যাম্পিয়ন গয়ানা আমাজন ওয়ারিয়র্স অ্যান্টিগুয়া ও বারবুডা ফ্যালকনসকে ২৭ রানে হারিয়ে ২০২৪ সালের রিপাবলিক ব্যাংক ক্যারিবিয়ান প্রিমিয়ার লিগ (CPL)-এর শেষ পর্যায়ে জায়গা করে নিয়েছে। ফ্যালকনসের পরাজয়ের ফলে তারা এখন টুর্নামেন্ট থেকে বাদ পড়েছে এবং এই বছরের ইভেন্টের শেষ চারটি দল নিশ্চিত হয়েছে। ফ্যালকনস টস জিতে প্রথমে ফিল্ডিং করার সিদ্ধান্ত নেয় এবং ওয়ারিয়র্সকে ১৩৫/৭-এ সীমাবদ্ধ করে।\\n\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaDocument\\\", \\\"nopremium\\\": false, \\\"spoiler\\\": false, \\\"video\\\": true, \\\"round\\\": false, \\\"voice\\\": false, \\\"document\\\": {\\\"_\\\": \\\"Document\\\", \\\"id\\\": 6309869289302135126, \\\"date\\\": \\\"2024-09-24T04:02:50+00:00\\\", \\\"mime_type\\\": \\\"video/mp4\\\", \\\"size\\\": 138669488, \\\"attributes\\\": [{\\\"_\\\": \\\"DocumentAttributeVideo\\\", \\\"duration\\\": 180.013, \\\"w\\\": 1080, \\\"h\\\": 1920, \\\"round_message\\\": false, \\\"supports_streaming\\\": true, \\\"nosound\\\": false}, {\\\"_\\\": \\\"DocumentAttributeFilename\\\", \\\"file_name\\\": \\\"Video240924 (BJbdt).mp4\\\"}], \\\"thumbs\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgWzYwGIA61NNEvlhthXsTmgWTAj5qc1uSCMfiM/wCNK4rFJgM0Va+xsO/6UUXQy4Dj1pfOyACelUo3mYZFztPcEn/CpoUG04IkPqvb9KWwJkxdfWinRxjywXCsT/EB1FFQ5A3FbmSsjZADEfjirMMxjbLMDx/eBoorSyE4pix3yxKVVTjOaKKKOVC5UQ==\\\"}]}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":496,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":498,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":500,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":500,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":504,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":513,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":513,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":527,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":534,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":534,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":536,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":538,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":540,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":545,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":545,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":553,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":570,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":570,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":571,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":575,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":578,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":578,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":578,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":586,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":601,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":604,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":604,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":604,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":612,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":615,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":615,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":615,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":624,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":624,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":638,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":641,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":641,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":641,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":649,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":652,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":652,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":652,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":658,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":658,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":679,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":682,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":682,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":682,\"length\":9}],\"meta\":{\"views\":2916,\"forwardsCount\":1,\"commentsCount\":0,\"reactionsCount\":11,\"publishDate\":\"2024-09-24T04:02:50Z\",\"deletedAt\":null,\"reactions\":[{\"count\":9,\"emoticon\":\"👍\"},{\"count\":2,\"emoticon\":\"🔥\"}],\"isAd\":false},\"album\":[],\"photo\":null,\"video\":{\"width\":1080,\"height\":1920,\"size\":138669488,\"durationSeconds\":180.013,\"url\":\"\",\"thumbUrl\":\"\",\"filename\":\"Video240924 (BJbdt).mp4\",\"thumbBase64\":\"$60\"}},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1610,\"publishDate\":\"2024-09-23T10:25:19Z\",\"message\":\"USD $3,500,000 এর বিশাল প্রাইজ পুলের সাথে PP ডেইলি স্লট টুর্নামেন্টের জন্য প্রস্তুত হোন! ২৩শে সেপ্টেম্বর ২০২৪ ) থেকে ৩০শে সেপ্টেম্বর, ২০২৪ পর্যন্ত, আপনার প্রিয় প্রাগম্যাটিক প্লে গেমগুলি খেলুন (নির্দিষ্ট শিরোনাম ব্যতীত) এবং আপনার জেতার সুযোগ নিন! দৈনিক  র‍যান্ডম পুরস্কার পাওয়ার এই অবিশ্বাস্য সুযোগটি মিস করবেন না!\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6307608152685789580, \\\"date\\\": \\\"2024-09-23T10:24:23+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgoqRwq0YOTuz0xUi23uT+FPUlVVNmGJxVhPkPIJPoe9byrxT5TRIrPCBHwOagaIntV1uTlW+Xspxj/ABqZI0PzEEcfd60lXg1Zg0+pkyeWEwEKuMZ560VduLYyKTjGBnOKKnkvqjNoHAMYzkueh9KZ/pG8DBznAyvWjeUk5chRyCKb585IJfGDxnH+FczV3c2uupYKOvWIfXZ/9amn7WvCoQAeyYpnnOVw0x65xgHmlW5nc4MvPXtRYVyw/mLCOeT97iiqRLsSWfPfA75oq1K2g9tyqsgyMk49qlWeMDqxP0FFFMzuO+0x98ZP+wKaZ4yRyR9FFFFArjDNg/Kcj3oooosFzw==\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [24592, 70870, 131561, 181709, 282931]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"replyMarkup\":{\"rows\":[{\"buttons\":[{\"kind\":\"KeyboardButtonUrl\",\"text\":\"আরো বিস্তারিত জানতে\",\"url\":\"https://bit.ly/3MBSqJR\"}]}]},\"meta\":{\"views\":3446,\"forwardsCount\":7,\"commentsCount\":0,\"reactionsCount\":40,\"publishDate\":\"2024-09-23T10:25:19Z\",\"deletedAt\":null,\"reactions\":[{\"count\":26,\"emoticon\":\"👍\"},{\"count\":10,\"emoticon\":\"❤\"},{\"count\":2,\"emoticon\":\"👎\"},{\"count\":2,\"emoticon\":\"🔥\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":282931,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$61\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1609,\"publishDate\":\"2024-09-23T09:46:43Z\",\"message\":\"টনি পপোভিক নতুন প্রধান কোচ হিসেবে অস্ট্রেলিয়ার দায়িত্ব গ্রহণ করেছেন, গ্রাহাম আর্নল্ডের পদত্যাগের পর, যিনি ২০২৬ বিশ্বকাপের এশিয়ান কোয়ালিফাইয়ে খারাপ শুরু করার কারণে চলে যান। অস্ট্রেলিয়ার 'সোনালী প্রজন্মের' একজন সদস্য হিসেবে, পপোভিক ১০ অক্টোবর চীনের বিরুদ্ধে একটি গুরুত্বপূর্ণ জয় পেতে সোকারুদের নেতৃত্ব দিতে প্রস্তুত, কারণ তারা বর্তমানে জাপানের পিছনে পাঁচ পয়েন্টে রয়েছে।\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6307617489944689916, \\\"date\\\": \\\"2024-09-23T09:46:42+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgoiFqKHgVEJ9BT0mDpmmyMNvJqiRkFuJBl2KnPTFSS2YZPlI3dqjjmIyeoPX2qdJgc1K8ypFGQIq7dhWQYzk0VPdBJACB83rRVCIg/GF4FM3HPNNDkIVPI/lTSRnigBzfKcipQcOMGmPHIEJK8dai3kFT6CgC+hXI3cmioYJoiRvzntiigCON0VMNnr/dBp4liDA/Nx0+RaKKVhXEe7HBUfNnoUGKrFiTnj8KKKRRLBCZWyRhe5ooooMJzdz8=\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [18195, 35134, 48554, 67445, 102446]}], \\\"has_stickers\\\": false}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":369,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":371,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":373,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":373,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":377,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":386,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":386,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":400,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":407,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":407,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":409,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":411,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":413,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":418,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":418,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":426,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":443,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":443,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":444,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":448,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":451,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":451,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":451,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":459,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":474,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":477,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":477,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":477,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":485,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":488,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":488,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":488,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":497,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":497,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":511,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":514,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":514,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":514,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":522,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":525,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":525,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":525,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":531,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":531,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":552,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":555,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":555,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":555,\"length\":9}],\"meta\":{\"views\":3219,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":11,\"publishDate\":\"2024-09-23T09:46:43Z\",\"deletedAt\":null,\"reactions\":[{\"count\":6,\"emoticon\":\"❤\"},{\"count\":5,\"emoticon\":\"👍\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":102446,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$62\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1608,\"publishDate\":\"2024-09-23T05:26:31Z\",\"message\":\"আপনি কোন প্লেয়ারের  এবং কত নাম্বার জার্সি পেতে চান?\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6307608152685789276, \\\"date\\\": \\\"2024-09-23T05:14:48+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgXrAUoXL7R1pxTMR5x3pYyCBkkDGc05SaMXBrcR0+T7mCO+aKlhwkIydwJOaK0jG6uJpplISErtyB7mpAf9HDDGV7ZqJERo9zB8+2KTaN3yrJjtxWT13Nr9yV5gYlUHnqaKrNkHoR9aKq4m22OWUqoGAfwFL559B+Q/wAKKKkZG7lzzj8BiiiimB8=\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 720, \\\"h\\\": 1280, \\\"sizes\\\": [17156, 43618, 74193, 112403, 187536]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"replyMarkup\":{\"rows\":[{\"buttons\":[{\"kind\":\"KeyboardButtonCallback\",\"text\":\"👍\"},{\"kind\":\"KeyboardButtonCallback\",\"text\":\"❤️\"},{\"kind\":\"KeyboardButtonCallback\",\"text\":\"😍\"}]},{\"buttons\":[{\"kind\":\"KeyboardButtonUrlAuth\",\"text\":\"Open Comments\",\"url\":\"https://commentsbot.xyz/thread/DzLxSjlzN\"}]},{\"buttons\":[{\"kind\":\"KeyboardButtonUrl\",\"text\":\"আরো বিস্তারিত জানার জন্য\",\"url\":\"https://www.facebook.com/baji.bgd/posts/pfbid0u8oZhsTHt1446D4KzCkaSLLPdT9ypeyqQErYLGCP3sXrXniG5z5Qd6NwmNfQ4XrBl\"}]}]},\"meta\":{\"views\":3532,\"forwardsCount\":1,\"commentsCount\":0,\"reactionsCount\":27,\"publishDate\":\"2024-09-23T05:26:31Z\",\"deletedAt\":null,\"reactions\":[{\"count\":20,\"emoticon\":\"👍\"},{\"count\":7,\"emoticon\":\"❤\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":720,\"height\":1280,\"size\":187536,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$63\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1607,\"publishDate\":\"2024-09-23T03:02:07Z\",\"message\":\"বার্বাডোস রয়্যালস বনাম সেন্ট লুসিয়া কিংস, ২২তম ম্যাচের হাইলাইটস | ক্যারিবিয়ান প্রিমিয়ার লিগ ২০২৪\\n\\nশীর্ষে থাকা বার্বাডোস রয়্যালস প্রভিডেন্সে একটি ম্যাচ খেলেছিল, যেখানে তারা ৯৬/৯ স্কোর করেছিল এবং ৭ উইকেটে পরাজিত হয়েছিল। সেন্ট লুসিয়া কিংস অসাধারণ একটি পারফরম্যান্স প্রদর্শন করে ২০২৪ সালের রিপাবলিক ব্যাংক ক্যারিবিয়ান প্রিমিয়ার লিগ (সিপিএল) প্লে-অফের একটি স্থান নিশ্চিত করেছে। রয়্যালস টস জিতে ব্যাট করার সিদ্ধান্ত নেয়। উইকেটগুলো নিয়মিতভাবে পড়তে থাকে, কারণ জোসেফ এবং রোস্টন চেজ দুর্দান্ত বল করেন কিংসের হয়ে, তারা মিলে সাতটি উইকেট নেন। রয়্যালস কোনোমতে তাদের ২০ ওভার পূর্ণ করতে সক্ষম হয়েছিল, মূলত নীচের সারির কেশব মহারাজ এবং মাহীশ থিকশানার প্রতিরোধের জন্য।\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaDocument\\\", \\\"nopremium\\\": false, \\\"spoiler\\\": false, \\\"video\\\": true, \\\"round\\\": false, \\\"voice\\\": false, \\\"document\\\": {\\\"_\\\": \\\"Document\\\", \\\"id\\\": 6305356352415863248, \\\"date\\\": \\\"2024-09-23T03:01:15+00:00\\\", \\\"mime_type\\\": \\\"video/mp4\\\", \\\"size\\\": 124835965, \\\"attributes\\\": [{\\\"_\\\": \\\"DocumentAttributeVideo\\\", \\\"duration\\\": 163.997, \\\"w\\\": 1080, \\\"h\\\": 1920, \\\"round_message\\\": false, \\\"supports_streaming\\\": true, \\\"nosound\\\": false}, {\\\"_\\\": \\\"DocumentAttributeFilename\\\", \\\"file_name\\\": \\\"Video230924 (BJbdt).mp4\\\"}], \\\"thumbs\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgWzYwGIA61NNEvlhthXsTmohBg/ep7KCMYx75P+NIViswGeKKmEAxnePxooAsqnNSJt4HH1qrEHbDCdVYeucj9KnhiBBKuGYDqooC6RLsznA/SinQuSWjZssh6iipk+V2YrmUsjZADEfjirUFw0QOcFjxncDiiiqsNq5HFdLE7Pglm60UUU7Byow==\\\"}]}}\",\"entities\":[],\"replyMarkup\":{\"rows\":[{\"buttons\":[{\"kind\":\"KeyboardButtonCallback\",\"text\":\"👍\"},{\"kind\":\"KeyboardButtonCallback\",\"text\":\"❤️\"},{\"kind\":\"KeyboardButtonCallback\",\"text\":\"😍\"}]}]},\"meta\":{\"views\":3109,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":15,\"publishDate\":\"2024-09-23T03:02:07Z\",\"deletedAt\":null,\"reactions\":[{\"count\":10,\"emoticon\":\"👍\"},{\"count\":5,\"emoticon\":\"❤\"}],\"isAd\":false},\"album\":[],\"photo\":null,\"video\":{\"width\":1080,\"height\":1920,\"size\":124835965,\"durationSeconds\":163.997,\"url\":\"\",\"thumbUrl\":\"\",\"filename\":\"Video230924 (BJbdt).mp4\",\"thumbBase64\":\"$64\"}},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1606,\"publishDate\":\"2024-09-22T11:25:33Z\",\"message\":\"উত্তেজনাপূর্ণ সাক্ষাৎ: বর্নমাউথ লিভারপুলের বিরুদ্ধে শ্বাসরুদ্ধকর লড়াই\\n\\nগতকাল বর্নমাউথ একটি কঠিন চ্যালেঞ্জের সম্মুখীন হয়েছিল, যেহেতু তারা লিভারপুলের কাছে ৩-০ গোলে পরাজিত হয়। লিভারপুল ম্যাচের শুরুতেই শক্তিশালীভাবে আক্রমণ শুরু করে এবং দ্রুত একটি গোল করে এগিয়ে যায়। তারা পরবর্তীতে আরও দুটি গোল যোগ করে। চেরিরা কিছু প্রাণবন্ত প্রচেষ্টা চালালেও, লিভারপুলের দৃঢ় প্রতিরক্ষা ভাঙতে তারা ব্যর্থ হয়। এটি ছিল একটি হতাশাজনক ফলাফল, কিন্তু দলটি আবারও শক্তি নিয়ে ফিরে আসার জন্য প্রস্তুতি নেবে! 💪⚽️\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaDocument\\\", \\\"nopremium\\\": false, \\\"spoiler\\\": false, \\\"video\\\": true, \\\"round\\\": false, \\\"voice\\\": false, \\\"document\\\": {\\\"_\\\": \\\"Document\\\", \\\"id\\\": 6305475305830093279, \\\"date\\\": \\\"2024-09-22T11:25:33+00:00\\\", \\\"mime_type\\\": \\\"video/mp4\\\", \\\"size\\\": 46153247, \\\"attributes\\\": [{\\\"_\\\": \\\"DocumentAttributeVideo\\\", \\\"duration\\\": 59.993, \\\"w\\\": 1080, \\\"h\\\": 1920, \\\"round_message\\\": false, \\\"supports_streaming\\\": true, \\\"nosound\\\": false}, {\\\"_\\\": \\\"DocumentAttributeFilename\\\", \\\"file_name\\\": \\\"AFC022924_Baji.mp4\\\"}], \\\"thumbs\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgWzIk8xgnc8A0qpvO3cBj171N9kXHDn8qDbDAw36VJqmVnGGI9KKnNrn+OimS9S8TSZz0qmspZHYyMCPugHrTS7rtOSCPvEdanlI5S9kUVVkeSNjhmKHoc0UcorEEZDIVyOOck1LJlwBmMep3DmiiqLuyPz2iIC4PH1ooopibP\\\"}]}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":491,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":493,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":495,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":495,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":499,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":508,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":508,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":522,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":529,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":529,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":531,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":533,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":535,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":540,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":540,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":548,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":565,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":565,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":566,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":570,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":573,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":573,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":573,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":581,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":596,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":599,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":599,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":599,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":607,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":610,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":610,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":610,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":619,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":619,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":633,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":636,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":636,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":636,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":644,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":647,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":647,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":647,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":653,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":653,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":674,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":677,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":677,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":677,\"length\":9}],\"meta\":{\"views\":3148,\"forwardsCount\":2,\"commentsCount\":0,\"reactionsCount\":24,\"publishDate\":\"2024-09-22T11:25:33Z\",\"deletedAt\":null,\"reactions\":[{\"count\":13,\"emoticon\":\"❤\"},{\"count\":11,\"emoticon\":\"👍\"}],\"isAd\":false},\"album\":[],\"photo\":null,\"video\":{\"width\":1080,\"height\":1920,\"size\":46153247,\"durationSeconds\":59.993,\"url\":\"\",\"thumbUrl\":\"\",\"filename\":\"AFC022924_Baji.mp4\",\"thumbBase64\":\"$65\"}},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1605,\"publishDate\":\"2024-09-22T09:53:53Z\",\"message\":\"গায়ানা অ্যামাজন ওয়ারিয়র্স বনাম সেন্ট কিটস অ্যান্ড নেভিস প্যাট্রিয়টস, ২১তম ম্যাচ হাইলাইটস | সিপিএল ২০২৪\\n\\nগায়ানা অ্যামাজন ওয়ারিয়র্স টানা দুটি হারের পর শেষ ম্যাচে জয় তুলে নিয়েছে। তারা সেন্ট কিটস অ্যান্ড নেভিস প্যাট্রিয়টসকে ৩০ রানে পরাজিত করেছে। শিমরন হেটমায়ার আবারও ওয়ারিয়র্সের হয়ে নায়ক হয়ে ওঠেন, ধীরগতির পিচে মাত্র ৩৩ বলে ৬৩ রানের বিধ্বংসী ইনিংস খেলেন। তিনি এখন দলের হয়ে সর্বোচ্চ রান সংগ্রাহক, ৬ ইনিংসে ২১৬ রান করেছেন প্রায় ১৯০ স্ট্রাইক রেটে। তবে, অলরাউন্ডার রোমারিও শেফার্ড শেষ দুই ম্যাচে নিচের দিকে নেমে গুরুত্বপূর্ণ ক্যামিও ইনিংস খেলেছেন। বোলিংয়ে, তাদের বেশ কিছু শক্তিশালী বিকল্প রয়েছে। গুডাকেশ মোটি ৬ ইনিংসে ১০ উইকেট নিয়ে শীর্ষস্থানে রয়েছেন এবং তার ইকোনমি রেট ৬.৮০। ওয়ারিয়র্সরা তাদের জয়ের ধারা অব্যাহত রাখবে।\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaDocument\\\", \\\"nopremium\\\": false, \\\"spoiler\\\": false, \\\"video\\\": true, \\\"round\\\": false, \\\"voice\\\": false, \\\"document\\\": {\\\"_\\\": \\\"Document\\\", \\\"id\\\": 6305475305830093243, \\\"date\\\": \\\"2024-09-22T09:53:53+00:00\\\", \\\"mime_type\\\": \\\"video/mp4\\\", \\\"size\\\": 107225899, \\\"attributes\\\": [{\\\"_\\\": \\\"DocumentAttributeVideo\\\", \\\"duration\\\": 140.44, \\\"w\\\": 1080, \\\"h\\\": 1920, \\\"round_message\\\": false, \\\"supports_streaming\\\": true, \\\"nosound\\\": false}, {\\\"_\\\": \\\"DocumentAttributeFilename\\\", \\\"file_name\\\": \\\"Video220924 (BJbdt).mp4\\\"}], \\\"thumbs\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgWzYwGIA61NNEvlhthXsTmlFgQfv042pYEDGfXJ/xpXFYosBmirgsGxncBRRdDLo6UvmZBUY3A/pVCJ5nGRchT3BJ/wqaBO6sHYenFTsK6LJPPFFEWTEDu3HJ+YUVDkxtpbmOsjZADEfjirEM5jJLMCcf3hRRWrSE0mOjvhGMAHnk4oooo5ULkRw==\\\"}]}}\",\"entities\":[],\"meta\":{\"views\":3176,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":8,\"publishDate\":\"2024-09-22T09:53:53Z\",\"deletedAt\":null,\"reactions\":[{\"count\":5,\"emoticon\":\"❤\"},{\"count\":3,\"emoticon\":\"🔥\"}],\"isAd\":false},\"album\":[],\"photo\":null,\"video\":{\"width\":1080,\"height\":1920,\"size\":107225899,\"durationSeconds\":140.44,\"url\":\"\",\"thumbUrl\":\"\",\"filename\":\"Video220924 (BJbdt).mp4\",\"thumbBase64\":\"$66\"}},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1604,\"publishDate\":\"2024-09-22T09:41:40Z\",\"message\":\"আপনি কি চিনতে পেরেছেন \\nকে এই প্লেয়ার? \\nকমেন্ট করে আপনার উত্তর জানান।\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6305326635993381601, \\\"date\\\": \\\"2024-09-22T09:29:57+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgozw6PH84+YDg0GCQc44pluCZBxnFWzIozleKTbGkipSVIoXJyQfTnFDFAfu5/GncmwF0MeNgDeuetFRkjPAwKKYF+GJI4FYjlhyad5Syx5Umq0dwREY35GOD6VZgO1MDjFbKz0MXdalADBO7II9s1Jvj9P/HRQcidyTjk02Xtzk/596xNhjY7HP4Yop0MRlfHbuaKQnJIZViCbaCj9D39KKKtOzE1dEUuTO4H940IhkcKvWiipY27IvxoI1CiiiikcrZ/\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1200, \\\"h\\\": 1200, \\\"sizes\\\": [20390, 43549, 69845, 103910, 167147]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"replyMarkup\":{\"rows\":[{\"buttons\":[{\"kind\":\"KeyboardButtonCallback\",\"text\":\"👍\"},{\"kind\":\"KeyboardButtonCallback\",\"text\":\"❤️\"},{\"kind\":\"KeyboardButtonCallback\",\"text\":\"😍\"}]},{\"buttons\":[{\"kind\":\"KeyboardButtonUrlAuth\",\"text\":\"Open Comments\",\"url\":\"https://commentsbot.xyz/thread/6dczNr1kf\"}]},{\"buttons\":[{\"kind\":\"KeyboardButtonUrl\",\"text\":\"এখনই যোগ দিন\",\"url\":\"https://baji.social/bj/tgndt\"}]}]},\"meta\":{\"views\":2943,\"forwardsCount\":2,\"commentsCount\":0,\"reactionsCount\":9,\"publishDate\":\"2024-09-22T09:41:40Z\",\"deletedAt\":null,\"reactions\":[{\"count\":6,\"emoticon\":\"❤\"},{\"count\":3,\"emoticon\":\"👍\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1200,\"height\":1200,\"size\":167147,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$67\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1603,\"publishDate\":\"2024-09-22T09:21:33Z\",\"message\":\"বর্নমাউথ চেলসির বিরুদ্ধে সাহসিকতার সাথে লড়াই করেছে! ⚽️💙\\n\\nএই উত্তেজনাপূর্ণ ম্যাচে আমাদের দল অসাধারণ দক্ষতা ও সংকল্প প্রদর্শন করেছে। যদিও চেলসি শেষ পর্যন্ত জয়লাভ করেছে, কিন্তু আমাদের খেলোয়াড়রা প্রতিটি মুহূর্তে প্রাণবন্ত ফুটবল খেলেছে। এবং এর চমৎকার পারফরম্যান্স আমাদের আশা জাগিয়েছে। গোল এবং রক্ষণাত্মক খেলা—প্রত্যেকটি পাল্টা আক্রমণ ছিল দারুণ!\\n\\nআপনাদের মতে ম্যাচের কোন মুহূর্তগুলো সবচেয়ে স্মরণীয় ছিল? মন্তব্যে জানাতে ভুলবেন না!\\n\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaDocument\\\", \\\"nopremium\\\": false, \\\"spoiler\\\": false, \\\"video\\\": true, \\\"round\\\": false, \\\"voice\\\": false, \\\"document\\\": {\\\"_\\\": \\\"Document\\\", \\\"id\\\": 6305475305830093221, \\\"date\\\": \\\"2024-09-22T09:21:33+00:00\\\", \\\"mime_type\\\": \\\"video/mp4\\\", \\\"size\\\": 46767131, \\\"attributes\\\": [{\\\"_\\\": \\\"DocumentAttributeVideo\\\", \\\"duration\\\": 59.993, \\\"w\\\": 1080, \\\"h\\\": 1920, \\\"round_message\\\": false, \\\"supports_streaming\\\": true, \\\"nosound\\\": false}, {\\\"_\\\": \\\"DocumentAttributeFilename\\\", \\\"file_name\\\": \\\"AFC021924_baji.mp4\\\"}], \\\"thumbs\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgWzIk8xgnc8A05U3nbuUY9e9OEBx0cfhQYeMAN+VSaqSIXGGI9KKk8gt/+qimS9TSL0m6qKylkdjIwI+6AetIXcbTkgj7xHWs+QixfyDRVSR5I2OGcoehzRT5AsQRkMhXI45yTipZMuAMxj1O4c0UVZV2Ree0RAXBwPrRRRTFdnw==\\\"}]}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":434,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":436,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":438,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":438,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":442,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":451,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":451,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":465,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":472,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":472,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":474,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":476,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":478,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":483,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":483,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":491,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":508,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":508,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":509,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":513,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":516,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":516,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":516,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":524,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":539,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":542,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":542,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":542,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":550,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":553,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":553,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":553,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":562,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":562,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":576,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":579,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":579,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":579,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":587,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":590,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":590,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":590,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":596,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":596,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":617,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":620,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":620,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":620,\"length\":9}],\"meta\":{\"views\":3080,\"forwardsCount\":1,\"commentsCount\":0,\"reactionsCount\":12,\"publishDate\":\"2024-09-22T09:21:33Z\",\"deletedAt\":null,\"reactions\":[{\"count\":8,\"emoticon\":\"👍\"},{\"count\":4,\"emoticon\":\"❤\"}],\"isAd\":false},\"album\":[],\"photo\":null,\"video\":{\"width\":1080,\"height\":1920,\"size\":46767131,\"durationSeconds\":59.993,\"url\":\"\",\"thumbUrl\":\"\",\"filename\":\"AFC021924_baji.mp4\",\"thumbBase64\":\"$68\"}},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1602,\"publishDate\":\"2024-09-22T09:20:30Z\",\"message\":\"বর্নমাউথ চেলসির বিরুদ্ধে সাহসিকতার সাথে লড়াই করেছে! ⚽️💙\\n\\nএই উত্তেজনাপূর্ণ ম্যাচে আমাদের দল অসাধারণ দক্ষতা ও সংকল্প প্রদর্শন করেছে। যদিও চেলসি শেষ পর্যন্ত জয়লাভ করেছে, কিন্তু আমাদের খেলোয়াড়রা প্রতিটি মুহূর্তে প্রাণবন্ত ফুটবল খেলেছে। এবং এর চমৎকার পারফরম্যান্স আমাদের আশা জাগিয়েছে। গোল এবং রক্ষণাত্মক খেলা—প্রত্যেকটি পাল্টা আক্রমণ ছিল দারুণ!\\n\\nআপনাদের মতে ম্যাচের কোন মুহূর্তগুলো সবচেয়ে স্মরণীয় ছিল? মন্তব্যে জানাতে ভুলবেন না!\\n\\n#Bj #Baji #Sports #BJSports #AFCBournemouth #MatchDay #Football #PremierLeague #Excitement\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaWebPage\\\", \\\"webpage\\\": {\\\"_\\\": \\\"WebPage\\\", \\\"id\\\": 2541134615399094605, \\\"url\\\": \\\"https://www.facebook.com/baji.bgd/\\\", \\\"display_url\\\": \\\"facebook.com/login\\\", \\\"has_large_media\\\": false, \\\"type\\\": \\\"article\\\", \\\"site_name\\\": \\\"Facebook\\\", \\\"title\\\": \\\"Log in or sign up to view\\\", \\\"description\\\": \\\"See posts, photos and more on Facebook.\\\"}, \\\"force_large_media\\\": false, \\\"force_small_media\\\": false, \\\"manual\\\": false, \\\"safe\\\": false}\",\"entities\":[{\"kind\":\"MessageEntityHashtag\",\"offset\":433,\"length\":3},{\"kind\":\"MessageEntityHashtag\",\"offset\":437,\"length\":5},{\"kind\":\"MessageEntityHashtag\",\"offset\":443,\"length\":7},{\"kind\":\"MessageEntityHashtag\",\"offset\":451,\"length\":9},{\"kind\":\"MessageEntityHashtag\",\"offset\":461,\"length\":15},{\"kind\":\"MessageEntityHashtag\",\"offset\":477,\"length\":9},{\"kind\":\"MessageEntityHashtag\",\"offset\":487,\"length\":9},{\"kind\":\"MessageEntityHashtag\",\"offset\":497,\"length\":14},{\"kind\":\"MessageEntityHashtag\",\"offset\":512,\"length\":11},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":525,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":527,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":529,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":529,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":533,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":542,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":542,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":556,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":563,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":563,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":565,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":567,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":569,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":574,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":574,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":582,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":599,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":599,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":600,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":604,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":607,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":607,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":607,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":615,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":630,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":633,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":633,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":633,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":641,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":644,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":644,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":644,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":653,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":653,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":667,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":670,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":670,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":670,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":678,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":681,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":681,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":681,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":687,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":687,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":708,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":711,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":711,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":711,\"length\":9}],\"meta\":{\"views\":12,\"forwardsCount\":0,\"commentsCount\":0,\"reactionsCount\":0,\"publishDate\":\"2024-09-22T09:20:30Z\",\"deletedAt\":\"2024-09-22T09:21:04Z\",\"reactions\":[],\"isAd\":false},\"album\":[],\"photo\":null,\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1601,\"publishDate\":\"2024-09-22T03:54:24Z\",\"message\":\"Place Baji-তে KM Power Ball-এর উত্তেজনা অনুভব করতে প্রস্তুত হোন, যেখানে প্রতিটি কার্ড আপনাকে বিশাল জয়ের কাছাকাছি নিয়ে আসে! আপনার বিঙ্গো কার্ডের উপরের প্যাটার্ন বা লাইনগুলিকে মেলাতে লক্ষ্য করুন এবং প্রতিটি বেটিং রাউন্ডের পরে সেগুলিকে বিশেষ সোনা, হীরা বা রেইনবো বোনাস কার্ডে রূপান্তরিত হতে দেখুন। আপনি যত বেশি খেলবেন, বিশাল পুরস্কার জেতার সম্ভাবনা তত বেশি হবে! মিস করবেন না।\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6303223506472649940, \\\"date\\\": \\\"2024-09-22T03:54:24+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgoz5UxGDjBNNhTe+PWp7vy/LXBywpbeGaKOO5TGCfypNlWFu7MwpkZx0JPrVMcVrzMbqIJnDDkj0qvDAsMuJ49zHlQehFCBlZjEYxtUh+M89aKs6mE81NiKpI5xRVkGeRmtiAO1nCkfXGTmsmrSTsu1VPAGBUNFJlxsmQjjPQkUTjLRMXB8v070yKeBkZZ3AbscVHLcrg7X39/u4HpSd+g42F2K0svmkM2e1FQb95JLEE+gopp2Ja1IlcKmMc+6g0vm4ORj/vgUUVbEBnz2BPuoo832X/vkUUVNrjuSxAzEcAIO4AGaKKKDGU3cw==\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1080, \\\"h\\\": 1080, \\\"sizes\\\": [22129, 53041, 82931, 114929, 174407]}], \\\"has_stickers\\\": false}}\",\"entities\":[],\"meta\":{\"views\":3248,\"forwardsCount\":2,\"commentsCount\":0,\"reactionsCount\":18,\"publishDate\":\"2024-09-22T03:54:24Z\",\"deletedAt\":null,\"reactions\":[{\"count\":14,\"emoticon\":\"👍\"},{\"count\":4,\"emoticon\":\"🔥\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1080,\"height\":1080,\"size\":174407,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$69\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1600,\"publishDate\":\"2024-09-21T10:28:19Z\",\"message\":\"আপনি কি চিনতে পেরেছেন\\nকে এই প্লেয়ার?🤔\\nকমেন্ট করে আপনার উত্তর জানান।\\n\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaPhoto\\\", \\\"spoiler\\\": false, \\\"photo\\\": {\\\"_\\\": \\\"Photo\\\", \\\"id\\\": 6300971706658962253, \\\"date\\\": \\\"2024-09-21T10:28:19+00:00\\\", \\\"sizes\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgozw6PH84+YDg0GCQc44pluCZBxnFWzIozleKTbGkipSVIoXJyQfTnFDFAfu5/GncmwF0MeNgDeuetFRkjPAwKKYF+GJI4FYjlhyad5Syx5Umq0dwREY35GOD6VZgO1MDjFbKz0MXdalADBO7II9s1Jvj9P/HRQcidyTjk02Xtzk/596xNhjY7HP4Yop0MRlfHbuaKQnJIZViCbaCj9D39KKKtOzE1dEUuTO4H940IhkcKvWiipY27IvxoI1CiiiikcrZ/\\\"}, {\\\"_\\\": \\\"PhotoSizeProgressive\\\", \\\"type\\\": \\\"y\\\", \\\"w\\\": 1200, \\\"h\\\": 1200, \\\"sizes\\\": [20390, 43533, 69821, 103853, 167094]}], \\\"has_stickers\\\": false}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":71,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":73,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":75,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":75,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":79,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":88,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":88,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":102,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":109,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":109,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":111,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":113,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":115,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":120,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":120,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":128,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":145,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":145,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":146,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":150,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":153,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":153,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":153,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":161,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":176,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":179,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":179,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":179,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":187,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":190,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":190,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":190,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":199,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":199,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":213,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":216,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":216,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":216,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":224,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":227,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":227,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":227,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":233,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":233,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":254,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":257,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":257,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":257,\"length\":9}],\"meta\":{\"views\":1950,\"forwardsCount\":9,\"commentsCount\":0,\"reactionsCount\":33,\"publishDate\":\"2024-09-21T10:28:19Z\",\"deletedAt\":\"2024-09-22T09:42:29Z\",\"reactions\":[{\"count\":22,\"emoticon\":\"👍\"},{\"count\":11,\"emoticon\":\"❤\"}],\"isAd\":false},\"album\":[],\"photo\":{\"width\":1200,\"height\":1200,\"size\":167094,\"url\":\"\",\"thumbUrl\":\"\",\"thumbBase64\":\"$6a\"},\"video\":null},{\"channel\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"messageId\":1599,\"publishDate\":\"2024-09-21T05:24:03Z\",\"message\":\"ত্রিনবাগো নাইট রাইডার্স বনাম অ্যান্টিগা ও বারবুডা ফ্যালকন্স, ২০তম ম্যাচের হাইলাইটস | CPL ২০২৪\\n\\nপোর্ট অফ স্পেনের একটি রোমাঞ্চকর ম্যাচে ত্রিনবাগো নাইট রাইডার্স অ্যান্টিগা ও বারবুডা ফ্যালকন্সের কাছে ছয় উইকেটে হেরে যায়, ফ্যালকন্স এক ওভার বাকি থাকতে টার্গেট তাড়া করে। এই জয়ে ফ্যালকন্সের অগ্রগতির আশা বেঁচে রইল এবং এ বছরের রিপাবলিক ব্যাংক CPL-এ নাইট রাইডার্সের বিরুদ্ধে তাদের দ্বিতীয় জয় নিশ্চিত হলো।\\n\\n\\n🔈  Baji  সদস্য  হিসাবে সাইন-আপ করুন  👑\\n 🛡এখনই Baji App ডাউনলোড  করুন!! ✅\\n  \\n📱 Facebook               📱 Twitter\\n📱 Instagram              📱 Threads\\n📱 Tiktok                     📱 Pinterest\",\"mediaRaw\":\"{\\\"_\\\": \\\"MessageMediaDocument\\\", \\\"nopremium\\\": false, \\\"spoiler\\\": false, \\\"video\\\": true, \\\"round\\\": false, \\\"voice\\\": false, \\\"document\\\": {\\\"_\\\": \\\"Document\\\", \\\"id\\\": 6300971706202722234, \\\"date\\\": \\\"2024-09-21T05:24:03+00:00\\\", \\\"mime_type\\\": \\\"video/mp4\\\", \\\"size\\\": 121795689, \\\"attributes\\\": [{\\\"_\\\": \\\"DocumentAttributeVideo\\\", \\\"duration\\\": 160.56, \\\"w\\\": 1080, \\\"h\\\": 1920, \\\"round_message\\\": false, \\\"supports_streaming\\\": true, \\\"nosound\\\": false}, {\\\"_\\\": \\\"DocumentAttributeFilename\\\", \\\"file_name\\\": \\\"Video210924 (BJbdt).mp4\\\"}], \\\"thumbs\\\": [{\\\"_\\\": \\\"PhotoStrippedSize\\\", \\\"type\\\": \\\"i\\\", \\\"bytes\\\": \\\"ASgWzYwGIA61NNEvlhthXsTmkFoQfvU5ouOgGe/P+NK4rFNgM8UVZFoSuQwoouhmgSCRg0eYpOOMfzrPiMjAEXCqfQ54/SpAu2JmDhyPQUrBdFssueoopY4wYV3oPM7nFFQ9AbiZCyNkAMR+OKmWVlVgxByMfeBoorSwrDor5kLFiWLdTRRRRZCcUz8=\\\"}]}}\",\"entities\":[{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":402,\"length\":2,\"documentId\":\"6298391521779517687\"},{\"kind\":\"MessageEntityBold\",\"offset\":404,\"length\":2},{\"kind\":\"MessageEntityTextUrl\",\"offset\":406,\"length\":4,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":406,\"length\":4},{\"kind\":\"MessageEntityBold\",\"offset\":410,\"length\":9},{\"kind\":\"MessageEntityTextUrl\",\"offset\":419,\"length\":14,\"url\":\"https://baji.social/bj/tgndt\"},{\"kind\":\"MessageEntityBold\",\"offset\":419,\"length\":14},{\"kind\":\"MessageEntityBold\",\"offset\":433,\"length\":7},{\"kind\":\"MessageEntityBold\",\"offset\":440,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":440,\"length\":2,\"documentId\":\"6298286084627368260\"},{\"kind\":\"MessageEntityBold\",\"offset\":442,\"length\":2},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":444,\"length\":2,\"documentId\":\"5895483165182529286\"},{\"kind\":\"MessageEntityBold\",\"offset\":446,\"length\":5},{\"kind\":\"MessageEntityTextUrl\",\"offset\":451,\"length\":8,\"url\":\"https://bjbaji5.com/page/guest/appDownload.jsp\"},{\"kind\":\"MessageEntityBold\",\"offset\":451,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":459,\"length\":17},{\"kind\":\"MessageEntityBold\",\"offset\":476,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":476,\"length\":1,\"documentId\":\"6298616277418117026\"},{\"kind\":\"MessageEntityBold\",\"offset\":477,\"length\":4},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":481,\"length\":2,\"documentId\":\"5323261730283863478\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":484,\"length\":8,\"url\":\"https://www.facebook.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":484,\"length\":8},{\"kind\":\"MessageEntityItalic\",\"offset\":484,\"length\":8},{\"kind\":\"MessageEntityBold\",\"offset\":492,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":507,\"length\":2,\"documentId\":\"5330337435500951363\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":510,\"length\":7,\"url\":\"https://x.com/baji_bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":510,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":510,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":518,\"length\":2,\"documentId\":\"5319160079465857105\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":521,\"length\":9,\"url\":\"https://www.instagram.com/baji.bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":521,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":521,\"length\":9},{\"kind\":\"MessageEntityBold\",\"offset\":530,\"length\":1},{\"kind\":\"MessageEntityItalic\",\"offset\":530,\"length\":1},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":544,\"length\":2,\"documentId\":\"5334592721594105691\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":547,\"length\":7,\"url\":\"https://www.threads.net/@baji.bgd\"},{\"kind\":\"MessageEntityBold\",\"offset\":547,\"length\":7},{\"kind\":\"MessageEntityItalic\",\"offset\":547,\"length\":7},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":555,\"length\":2,\"documentId\":\"5327982530702359565\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":558,\"length\":6,\"url\":\"https://www.tiktok.com/@bj.live88\"},{\"kind\":\"MessageEntityBold\",\"offset\":558,\"length\":6},{\"kind\":\"MessageEntityItalic\",\"offset\":558,\"length\":6},{\"kind\":\"MessageEntityBold\",\"offset\":564,\"length\":3},{\"kind\":\"MessageEntityItalic\",\"offset\":564,\"length\":3},{\"kind\":\"MessageEntityCustomEmoji\",\"offset\":585,\"length\":2,\"documentId\":\"5346103513120258857\"},{\"kind\":\"MessageEntityTextUrl\",\"offset\":588,\"length\":9,\"url\":\"https://www.pinterest.com/baji_bgd/\"},{\"kind\":\"MessageEntityBold\",\"offset\":588,\"length\":9},{\"kind\":\"MessageEntityItalic\",\"offset\":588,\"length\":9}],\"meta\":{\"views\":4075,\"forwardsCount\":4,\"commentsCount\":0,\"reactionsCount\":9,\"publishDate\":\"2024-09-21T05:24:03Z\",\"deletedAt\":null,\"reactions\":[{\"count\":5,\"emoticon\":\"👍\"},{\"count\":4,\"emoticon\":\"❤\"}],\"isAd\":false},\"album\":[],\"photo\":null,\"video\":{\"width\":1080,\"height\":1920,\"size\":121795689,\"durationSeconds\":160.56,\"url\":\"\",\"thumbUrl\":\"\",\"filename\":\"Video210924 (BJbdt).mp4\",\"thumbBase64\":\"$6b\"}}],\"chats\":[{\"id\":{\"internalId\":\"1ZP9sP\",\"telegramId\":\"1829680439\"},\"title\":\"baji 🇧🇩\",\"membersCount\":45421,\"peer\":\"PEER_TYPE_CHANNEL\",\"username\":\"baji_bgd\",\"photoId\":\"6187992883995458813\",\"photoUrl\":\"https://img.telemetr.io/c/1ZP9sP/6187992883995458813?ty=x\",\"err\":9.288655,\"postViews\":4219,\"country\":{\"countryId\":\"bangladesh\"},\"language\":{\"languageId\":\"bn\"},\"category\":[{\"categoryId\":\"GrV1hfO57\",\"slug\":\"bets-and-casino\"}],\"telegramFlags\":{\"verified\":false,\"scam\":false,\"fake\":false,\"restricted\":false},\"collectorFlags\":{\"verified\":false,\"cheater\":false,\"blocked\":false,\"onlyForOwners\":false,\"cheaterInfo\":{\"participants\":0.20746865757233585,\"views\":0.4530670859847248,\"appeal\":false}},\"isPlaceholder\":false,\"link\":\"https://t.me/baji_bgd\"}],\"cursor\":\"CL8M\"}}]}]]\n"])
#         </script>
#         <script>
#             self.__next_f.push([1, ""])
#         </script>
#         <script defer src="https://static.cloudflareinsights.com/beacon.min.js/vcd15cbe7772f49c399c6a5babf22c1241717689176015" integrity="sha512-ZpsOmlRQV6y907TI0dKBHq9Md29nnaEIPlkf84rnaERnq6zvWvPUqr2ft8M1aS28oN72PdrCzSjY4U6VaAw1EQ==" data-cf-beacon='{"rayId":"8cb18b548a98dd38","serverTiming":{"name":{"cfExtPri":true,"cfL4":true}},"version":"2024.8.0","token":"1609be6e019447be903c2b33934f2915"}' crossorigin="anonymous"></script>
#     </body>
# </html>
# '''

# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(html_content, 'html.parser')

# cards = soup.select('div[class*="container/post"]')
# # print(cards)
# for card in cards:
#     telegram_link = card.select_one('.post-image a')
#     if telegram_link and telegram_link.has_attr('href'):
#         print("Telegram Link:", telegram_link['href'])
#     else:
#         print("No link found in this card.")
# # Extract the channel name
# channel_name = soup.select_one('.channel-name__title').get_text(strip=True)
# print("Channel Name:", channel_name)

# # Extract the post content
# post_content = soup.select_one('.whitespace-pre-line').get_text(strip=True)
# print("Post Content:", post_content)

# # Extract the Telegram post link
# telegram_link = soup.select_one('.post-image a')['href']
# print("Telegram Post Link:", telegram_link)

# # Extract the Telegram post link
# spans_in_post_image = soup.select('.flex.flex-wrap.gap-2 span')
# print(spans_in_post_image)

# # Extract post date and time
# post_date = soup.select_one('.flex.flex-wrap.items-center.justify-between a').get_text(strip=True)
# print("Post Date:", post_date)
