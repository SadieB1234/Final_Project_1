<<<<<<< Updated upstream
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from TV_Window import *

class Controller(QMainWindow, Ui_MainWindow):

=======
<<<<<<< Updated upstream
class Television:
>>>>>>> Stashed changes
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3


    def __init__(self, status=False, muted=False, volume=min_volume, channel=min_channel, *args, **kargs):
        self.status = status
        self.muted = muted
        self.volume = volume
        self.channel = channel

        super().__init__(*args, **kargs)
        self.setupUi(self)

        self.PowerButton.clicked.connect(lambda: self.power())
        self.Vol_Up.clicked.connect(lambda: self.volume_up())
        self.Vol_Down.clicked.connect(lambda: self.volume_down())
        self.Channel_Up.clicked.connect(lambda: self.channel_up())
        self.Channel_Down.clicked.connect(lambda: self.channel_down())
        self.MuteButton.clicked.connect(lambda: self.muted())
        self.Channel_Down.clicked.connect(lambda: self.channel_down())

        #keypad buttons
        self.KeypadButton_0.clicked.connect(lambda: self.keypad())
        self.KeypadButton_1.clicked.connect(lambda: self.keypad())
        self.KeypadButton_2.clicked.connect(lambda: self.keypad())
        self.KeypadButton_3.clicked.connect(lambda: self.keypad())
        self.KeypadButton_4.clicked.connect(lambda: self.keypad())
        self.KeypadButton_5.clicked.connect(lambda: self.keypad())
        self.KeypadButton_6.clicked.connect(lambda: self.keypad())
        self.KeypadButton_7.clicked.connect(lambda: self.keypad())
        self.KeypadButton_8.clicked.connect(lambda: self.keypad())
        self.KeypadButton_9.clicked.connect(lambda: self.keypad())

    def keypad(self):
        pass

    def channel_view(self):
        if self.status == True:
            if self.channel == 0:
                movie = QMovie('animations/crime_scene.gif')
                self.TV_label.setMovie(movie)
                movie.start()

            elif self.channel == 1:
                movie = QMovie('animations/nature_doc.gif')
                self.TV_label.setMovie(movie)
                movie.start()

            elif self.channel == 2:
                movie = QMovie('animations/hockey.gif')
                self.TV_label.setMovie(movie)
                movie.start()

            elif self.channel == 3:
                movie = QMovie('animations/kids_cartoon.gif')
                self.TV_label.setMovie(movie)
                movie.start()

            elif self.channel == 4:
                movie = QMovie('animations/talk_show.gif')
                self.TV_label.setMovie(movie)
                movie.start()

            else:
                movie = QMovie('animations/static.gif')
                self.TV_label.setMovie(movie)
                movie.start()
        else:
            pass

    def power(self): #used to turn tv on and off via status variable
        if self.status == True:
            self.status = False
            self.channel_view()

        else:
            self.status = True
            self.channel_view()

    def mute(self): #used to mute and unmute via muted variable
        if self.status:
            if self.muted:
                self.muted = False

            else:
                self.muted = True


    def channel_up(self): #increase channel value when tv is on, if at max goes to min,
        if self.status:
            if self.channel == Controller.max_channel:
                self.channel = Controller.min_channel
            else:
                self.channel += 1

    def channel_down(self): #decrease channel value when tv is on, if on min goes to max
        if self.status:
            if self.channel == Controller.min_channel:
                self.channel = Controller.max_channel
            else:
                self.channel -= 1

    def volume_up(self): #increase vol when tv is on, if max stays at max
        if self.status:
            if self.muted:
                self.muted = False

            if self.volume == Controller.max_volume:
                pass
            else:
                self.volume += 1

    def volume_down(self): #decrease vol when tv on, if min stays at min
        if self.status:
            if self.muted:
                self.muted = False
            if self.volume == Controller.min_volume:
                pass
            else:
<<<<<<< Updated upstream
                self.volume -= 1
=======
                self.__volume -= 1


    def __str__(self): #sends status in form of "TV status: Power = [status]. Channel = [channel], Volume = [volume]"
        return f'TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.min_volume if self.__muted else self.__volume}'
=======
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

import sys
from TV_Window import *

class Controller(QMainWindow, Ui_MainWindow):

    def __init__(self, status=False, muted=False, *args, **kargs):
        self.status = status
        self.muted = muted
        self.volume = 0.5
        self.channel = 0
        self.sound = QSoundEffect()

        super().__init__(*args, **kargs)
        self.setupUi(self)

        self.mute_symbol = QLabel(self)
        pixmap = QPixmap('animations/mute_symbol.png')
        scaled_pixmap = pixmap.scaled(30, 30, Qt.IgnoreAspectRatio)
        self.mute_symbol.setPixmap(scaled_pixmap)
        self.mute_symbol.move(85, 375)
        self.mute_symbol.setVisible(False)
        self.channel_symbol.setVisible(False)
        self.PowerButton.clicked.connect(lambda: self.power())
        self.Vol_Up.clicked.connect(lambda: self.volume_up())
        self.Vol_Down.clicked.connect(lambda: self.volume_down())
        self.Channel_Up.clicked.connect(lambda: self.channel_up())
        self.Channel_Down.clicked.connect(lambda: self.channel_down())
        self.MuteButton.clicked.connect(lambda: self.mute())

    def keypad(self,num):
        if self.status == True:
            self.channel = num
            self.channel_view()

    def channel_view(self):
        if self.status == True:
            if self.channel == 1: #crime show
                movie = QMovie('animations/crime_scene.gif')
                movie.setScaledSize(QSize(441, 351))  # sets to size of frame
                self.sound.setSource(QtCore.QUrl.fromLocalFile('noise/crimescene_noise.wav'))
                self.sound.setLoopCount(-2)  # infinite looping
                self.TV_label.setMovie(movie)
                movie.start()
                if self.muted == False:
                    self.sound.play()

            elif self.channel == 2: #documentary
                self.sound.setSource(QtCore.QUrl.fromLocalFile('noise/documentary_noise.wav'))
                self.sound.setLoopCount(-2)  # infinite looping
                movie = QMovie('animations/nature_doc.gif')
                movie.setScaledSize(QSize(441, 351))  # sets to size of frame
                self.TV_label.setMovie(movie)
                movie.start()
                if self.muted == False:
                    self.sound.play()

            elif self.channel == 3: #sports
                self.sound.setSource(QUrl.fromLocalFile('noise/hockey_noise.wav')) #link to sound
                self.sound.setLoopCount(-2)  # infinite looping
                movie = QMovie('animations/hockey.gif')
                movie.setScaledSize(QSize(441, 351))  # sets to size of frame
                self.TV_label.setMovie(movie)
                movie.start()
                if self.muted == False:
                    self.sound.play()

            elif self.channel == 5: #kids cartoon
                self.sound.setSource(QUrl.fromLocalFile('noise/cartoon_noise.wav'))
                self.sound.setLoopCount(-2)  # infinite looping
                movie = QMovie('animations/kids_cartoon.gif')
                movie.setScaledSize(QSize(441, 351))  # sets to size of frame
                self.TV_label.setMovie(movie)
                movie.start()
                if self.muted == False:
                    self.sound.play()

            elif self.channel == 7: #talkshow
                self.sound.setSource(QUrl.fromLocalFile('noise/talkshow_noise.wav'))
                self.sound.setLoopCount(5)  # infinite looping
                movie = QMovie('animations/talk_show.gif')
                movie.setScaledSize(QSize(441, 351))  # sets to size of frame
                self.TV_label.setMovie(movie)
                movie.start()
                if self.muted == False:
                    self.sound.play()

            else: #static rainbow
                self.sound.setSource(QUrl.fromLocalFile('noise/static_noise.wav'))
                self.sound.setLoopCount(5)  # infinite looping
                movie = QMovie('animations/static.gif')
                movie.setScaledSize(QSize(441, 351))  # sets to size of frame
                self.TV_label.setMovie(movie)
                movie.start()
                if self.muted == False:
                    self.sound.play()
            self.channel_symbol.setText(str(self.channel))
        else:
            self.sound.stop()
            self.TV_label.clear()

    def power(self): #used to turn tv on and off via status variable
        if self.status == True:
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

    def channel_up(self): #increase channel value when tv is on, if at max goes to min,
        if self.status:
            self.channel += 1
            self.channel_view()

    def channel_down(self): #decrease channel value when tv is on, if on min goes to max
        if self.status:
           self.channel -= 1
           self.channel_view()

    def mute(self): #used to mute and unmute via muted variable
        if self.status:
            if self.muted:
                self.muted = False
                self.sound.setVolume(self.volume)
                self.mute_symbol.setVisible(False)

            else:
                self.muted = True
                self.sound.setVolume(0)
                self.mute_symbol.setVisible(True)

    def volume_up(self): #increase vol when tv is on, if max stays at max
        if self.status:
            if self.muted != True:
                self.volume += .1
                self.sound.setVolume(self.volume)

    def volume_down(self): #decrease vol when tv on, if min stays at min
        if self.status:
            if self.muted != True:
                self.volume -= .1
                self.sound.setVolume(self.volume)


>>>>>>> Stashed changes
>>>>>>> Stashed changes
