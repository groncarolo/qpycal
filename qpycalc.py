import logging

from QConsole import QConsole


def main():
    logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG, force=True)

    try:
        QConsole().cmdloop()
    except KeyboardInterrupt:
        print("")
    print("")


if __name__ == "__main__":
    main()
