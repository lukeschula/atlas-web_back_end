#!/usr/bin/env python3
''' Filtered Logger Module'''

import re
import typing
import logging
import os
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    '''Redacting Formatter class'''

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        ''' Obfuscates Logging Message '''
        original_message = super(RedactingFormatter, self).format(record)
        record_message = record.getMessage()
        filtered_message = filter_datum(self.fields,
                                        RedactingFormatter.REDACTION,
                                        record_message,
                                        RedactingFormatter.SEPARATOR)
        return original_message.replace(record_message, filtered_message)


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''Filter Datum Method'''
    for field in fields:
        field_pattern = rf"({field}=)[^{separator}]*?({separator})"
        message = re.sub(field_pattern, rf"\1{redaction}\2", message)

    return message


def get_logger() -> logging.Logger:
    ''' Returns Logger object'''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()

    redacted_formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(redacted_formatter)

    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    ''' Returns Database Connection Point'''
    connection = mysql.connector.connect(host=os.getenv
                                         ('PERSONAL_DATA_DB_HOST'),
                                         database=os.getenv
                                         ('PERSONAL_DATA_DB_NAME'),
                                         user=os.getenv
                                         ('PERSONAL_DATA_DB_USERNAME'),
                                         password=os.getenv
                                         ('PERSONAL_DATA_DB_PASSWORD'))
    return connection


def main():
    ''' Main Function Entry Point'''
    def row_formatter(row: typing.List[str]) -> str:
        """" Formats SQL query data for logging """
        return (f"name={row[0]};email={row[1]};phone={row[2]};ssn={row[3]};"
                f"password={row[4]};ip={row[5]};last_login={row[6]};"
                f"user_agent={row[7]};")

    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT name, email, phone, ssn, password, ip,"
                   "last_login, user_agent FROM users;")
    for row in cursor:
        formatted_row = row_formatter(row)
        logger = get_logger()
        logger.info(formatted_row)


if __name__ == '__main__':
    main()