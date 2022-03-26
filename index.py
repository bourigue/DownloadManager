import os
import sys

import pafy
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox


from main import Ui_MainWindow


class MainApp (QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
         super (MainApp, self).__init__(parent)
         self.setupUi(self)

         self.Handel_Buttons()
    def Handel_Buttons(self):
        self.pushButton_6.clicked.connect(self.Playlist_Download)
        self.pushButton_7.clicked.connect(self.Playlist_Save_Browse)


    def Playlist_Save_Browse(self):
        playlist_save_location = QFileDialog.getExistingDirectory(self, "Select Download Directory")
        self.lineEdit_6.setText(playlist_save_location)

    def Playlist_Download(self):
            playlist_url = self.lineEdit_5.text()
            save_location = self.lineEdit_6.text()

            if playlist_url == '' or save_location == '':
                QMessageBox.warning(self, "Data ror", "Provide a valid Playlist URL or save location")

            else:

                playlist = pafy.get_playlist(playlist_url)
                playlist_videos = playlist['items']

                self.lcdNumber_2.display(len(playlist_videos))

            os.chdir(save_location)
            if os.path.exists(str(playlist['title'])):
                os.chdir(str(playlist['title']))

            else:
                os.mkdir(str(playlist['title']))
                os.chdir(str(playlist['title']))

            current_video_in_download = 1
            quality = self.comboBox_2.currentIndex()

            QApplication.processEvents()

            for video in playlist_videos:
                current_video = video['pafy']
                current_video_stream = current_video.videostreams
                self.lcdNumber.display(current_video_in_download)
                download = current_video_stream[quality].download(callback=self.Playlist_Progress)
                QApplication.processEvents()

                current_video_in_download += 1

    def Playlist_Progress(self, total, received, ratio, rate, time):
                read_data = received
                if total > 0:
                    download_percentage = read_data * 100 / total
                    self.progressBar_3.setValue(download_percentage)
                    remaining_time = round(time / 60, 2)

                    self.label_6.setText(str('{} minutes remaining'.format(remaining_time)))
                    QApplication.processEvents()








def main():

   app = QApplication(sys.argv)
   myWin = MainApp()
   myWin.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
    main()

