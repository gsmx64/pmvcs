""" Setup Parser file for Python MVC Shell Framework Package """
import configparser

from pathlib import Path


class SetupParser():
    """ Class for PMVCS Setup Parser """

    @staticmethod
    def parser_access(file: Path) -> configparser.ConfigParser:
        """
        Parses a file with ConfigParser, returns read only data
        """
        parser = configparser.ConfigParser(allow_no_value=True)
        parser.sections()
        parser.optionxform = lambda option: option
        parser.read(file, 'UTF-8')

        return parser

    @staticmethod
    def parser_write(parser: configparser.ConfigParser,
                     section: str, option: str, value: str,
                     cfg_file: Path) -> None:
        """
        Writes a file with ConfigParser
        """
        parser.set(section, option, value)

        with open(cfg_file, 'w', encoding='utf-8') as file:
            parser.write(file)
