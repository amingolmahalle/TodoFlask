import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Todo Flask application")

    parser.add_argument('-d', '--debug', action='store_false', help='Debug True/False')

    return parser.parse_args()
