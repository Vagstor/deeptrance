import utils, config.constants as constants, config.config as config
import utils, time, os, sc_selenium

def main():
    try:
        sc_selenium.login()
        sc_selenium.open_file()
        sc_selenium.pass_to_cell()
        
        client = utils.create_ds_client()
        message = utils.create_starting_message()
        completion = utils.create_completion(client, message)
        message = utils.add_string_to_completion()
    finally:
        sc_selenium.
    
if __name__ == "main":
    main()