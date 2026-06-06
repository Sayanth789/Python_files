import logging 

def main():
    # Configure the logging system 
    logging.basicConfig(
        filename="app.log",
        level=logging.ERROR
    )


    # Variables (to make the calles that follow work)

    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    logging.critical("Host %s Unknown ", hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is depreacted')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got Here')

if __name__ == "__main__":
    main() 

    


