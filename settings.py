import os

class Scrapper:
    main_directory = os.path.dirname(__file__)
    all_proxies_file = f"{main_directory}/proxies/all_proxies_list.txt"
    validated_proxies_file = f"{main_directory}/proxies/validated_proxies_list.txt"
    