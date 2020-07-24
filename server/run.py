from sys import argv
from src.app import app

def main():
    print("moi")

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,debug=True)