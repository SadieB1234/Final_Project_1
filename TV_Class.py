from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
import sys
from TV_Window import *

class Controller(QMainWindow, Ui_MainWindow):
    """
    Class representing details for TV ui functionality
    """

    def __init__(self, *args:tuple, **kargs:tuple) -> None:
        """
        Constructor to create initial state of Controller object
        """
        self.status = False
        self.muted = False
        self.volume = 0.5
        self.channel = 0
        self.sound = QSoundEffect()

        super().__init__(*args, **kargs)
        self.setupUi(self)

        #setting functions/lambda of clicking buttons on remote
        self.channel_symbol.setVisible(False) #False until TV is on
        self.PowerButton.clicked.connect(lambda: self.power())
        self.Vol_Up.clicked.connect(lambda: self.volume_up())
        self.Vol_Down.clicked.connect(lambda: self.volume_down())
        self.Channel_Up.clicked.connect(lambda: self.channel_up())
        self.Channel_Down.clicked.connect(lambda: self.channel_down())
        self.MuteButton.clicked.connect(lambda: self.mute())

        #setting functions of each keypad button
        self.KeypadButton_0.clicked.connect(lambda: self.keypad(0))
        self.KeypadButton_1.clicked.connect(lambda: self.keypad(1))
        self.KeypadButton_2.clicked.connect(lambda: self.keypad(2))
        self.KeypadButton_3.clicked.connect(lambda: self.keypad(3))
        self.KeypadButton_4.clicked.connect(lambda: self.keypad(4))
        self.KeypadButton_5.clicked.connect(lambda: self.keypad(5))
        self.KeypadButton_6.clicked.connect(lambda: self.keypad(6))
        self.KeypadButton_7.clicked.connect(lambda: self.keypad(7))
        self.KeypadButton_8.clicked.connect(lambda: self.keypad(8))
        self.KeypadButton_9.clicked.connect(lambda: self.keypad(9))

    def keypad(self,num:int) -> None:
        """
        Function for changing the channel (self.channel) via the keypad buttons
        :param num: num of channel that matches keypad num
        """
        if self.status == True: #checking if TV is on
            self.channel = num
            self.channel_view()

    def channel_view(self) -> None:
        """
        Function for controlling/changing the tv screen view, does the animation
        for each channel and the sound associated with each adn clears the screen if power is off
        """
        if self.status == True: #checking if TV is on
            if self.channel == 1: #crime show
                movie = QMovie('animations/crime_scene.gif')
                movie.setScaledSize(QSize(441, 351))  # sets to size of frame
                self.sound.setSource(QtCore.QUrl.fromLocalFile('noise/crimescene_noise.wav'))
                self.sound.setLoopCount(-2)  # infinite looping
                self.TV_label.setMovie(movie)

            elif self.channel == 2: #documentary
                self.sound.setSource(QtCore.QUrl.fromLocalFile('noise/documentary_noise.wav'))
                self.sound.setLoopCount(-2)  # infinite looping
                movie = QMovie('animations/nature_doc.gif')
                movie.setScaledSize(QSize(441, 351))  # sets to size of frame
                self.TV_label.setMovie(movie)

            elif self.channel == 3: #sports
                self.sound.setSource(QUrl.fromLocalFile('noise/hockey_noise.wav')) #link to sound
                self.sound.setLoopCount(-2)  # infinite looping
                movie = QMovie('animations/hockey.gif')
                movie.setScaledSize(QSize(441, 351))  # sets to size of frame
                self.TV_label.setMovie(movie)

            elif self.channel == 5: #kids cartoon
                self.sound.setSource(QUrl.fromLocalFile('noise/cartoon_noise.wav'))
                self.sound.setLoopCount(-2)  # infinite looping
                movie = QMovie('animations/kids_cartoon.gif')
                movie.setScaledSize(QSize(441, 351))  # sets to size of frame
                self.TV_label.setMovie(movie)

            elif self.channel == 7: #talkshow
                self.sound.setSource(QUrl.fromLocalFile('noise/talkshow_noise.wav'))
                self.sound.setLoopCount(5)  # infinite looping
                movie = QMovie('animations/talk_show.gif')
                movie.setScaledSize(QSize(441, 351))  # sets to size of frame
                self.TV_label.setMovie(movie)

            else: #static rainbow
                self.sound.setSource(QUrl.fromLocalFile('noise/static_noise.wav'))
                self.sound.setLoopCount(5)  # infinite looping
                movie = QMovie('animations/static.gif')
                movie.setScaledSize(QSize(441, 351))  # sets to size of frame
                self.TV_label.setMovie(movie)
            #for every channel
            movie.start()
            self.channel_symbol.setText(str(self.channel))
            self.sound.play()

        else:
            self.sound.stop()
            self.TV_label.clear() #makes screen black

    def power(self) -> None:
        """
        Function for turning TV on and off, off if self.status is False and on if self.status is True
        :return:
        """
        if self.status == True: #checking if TV is on
            self.status = False
            self.mute_symbol.setVisible(False)
            self.channel_symbol.setVisible(False)
            self.sound.stop()
            self.channel_view()

        else:
            self.status = True
            if self.muted:
                self.mute_symbol.setVisible(True)
            self.channel_symbol.setVisible(True)
            self.channel_view()

    def channel_up(self) -> None:
        """
        Function to increase channel value when TV is on (self.status == True)
        """
        if self.status: #checking if TV is on
            self.channel += 1
            self.channel_view()

    def channel_down(self) -> None:
        """
        Function to decrease channel value when TV is on (self.status == True)
        """
        if self.status: #checking if TV is on
           self.channel -= 1
           self.channel_view()

    def mute(self) -> None:
        """
        Function to mute and unmute the TV sound when TV is on (self.status == True)
        """
        if self.status: #checking if TV is on
            if self.muted:
                self.muted = False
                self.sound.setVolume(self.volume)
                self.mute_symbol.setVisible(False)

            else:
                self.muted = True
                self.sound.setVolume(0)
                self.mute_symbol.setVisible(True)

    def volume_up(self) -> None:
        """
        Function to increase volume when TV is on (self.status == True) dnd unmuted (self.muted == False)
        """
        if self.status: #checking if TV is on
            if self.muted != True: #doesnt change volume if muted
                self.volume += .1
                self.sound.setVolume(self.volume)

    def volume_down(self) -> None:
        """
        Function to decrease volume when TV is on (self.status == True) dnd unmuted (self.muted == False)
        """
        if self.status: #checking if TV is on
            if self.muted != True: #doesnt change volume if muted
                self.volume -= .1
                self.sound.setVolume(self.volume)

