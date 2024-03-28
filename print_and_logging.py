"""
The purpose of this script it to test different methods of using the logging module to print
information to both a logfile and to stdout.
"""
import logging

if __name__=='__main__':
    print('--------------------------------------------------')
    logging.info('This is an INFO message.')
    logging.warning('This is a WARNING message.')
    print('END')
