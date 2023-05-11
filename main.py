from TV_Class import *

def main() -> None:
    """
    Function to load window and run TV_Class
    """
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()