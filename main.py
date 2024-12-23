import customtkinter as ctk
from untils import autoPlay
from clockcalc import Strtime
from threading import Thread

class Application:

        def __init__(self):
                print('Programa iniciado...')
                # Defining tab
                self.mainRoot = ctk.CTk()
                self.mainRoot.geometry('400x400')
                self.mainRoot.title('Time and video synchronizer')
                # Defining widgets (ignore it)
                ctk.CTkLabel(self.mainRoot, text='Video moment').pack(pady=2)
                self.date1 = ctk.CTkEntry(self.mainRoot) # Entry to video time
                self.date1.pack(pady=2)
                ctk.CTkLabel(self.mainRoot, text='Accurate frame').pack(pady=2)
                self.frame = ctk.CTkEntry(self.mainRoot) # Entry to exact frame
                self.frame.pack(pady=2)
                ctk.CTkLabel(self.mainRoot, text='Video FPS').pack(pady=2)
                self.fps = ctk.CTkEntry(self.mainRoot) # Entry to video fps
                self.fps.pack(pady=2)
                ctk.CTkLabel(self.mainRoot, text='Time of day to play (24 hours)').pack(pady=2)
                self.date2 = ctk.CTkEntry(self.mainRoot) # Entry to day hours
                self.date2.pack(pady=2)
                self.autoPlayCheck = ctk.CTkCheckBox(self.mainRoot, text='AutoPlay') # 1 = AutoPlay
                self.autoPlayCheck.pack(pady=2)
                ctk.CTkButton(self.mainRoot, width=10, height=10, text='Submit', command=self.submit).pack(pady=2)
                self.calculated = ctk.CTkLabel(self.mainRoot, text='')
                self.calculated.pack(pady=2)
                # Starting root
                self.mainRoot.mainloop()

        def submit(self) -> None:
                print('Iniciando cálculo...')
                # Taking the millisecond of the frames
                milliSeconds = self.milliOfFrame()
                print('Milliseconds: {}'.format(milliSeconds))
                # Creating the format
                videoFormat = self.date1.get()
                dateFormat = self.date2.get()
                # Creating the object to calculate
                videoMoment = Strtime( videoFormat , float(milliSeconds) ) # HH:mm:ss;ms
                dateTime = Strtime(dateFormat) # HH:mm:ss;0.0
                # Calculating
                hoursToPlay, secondsToPlay = dateTime.decreaseOtherTime(videoMoment) # Datetime - VideoMoment
                # Formating
                hoursToPlay = self.addZeroLeft(hoursToPlay)
                # Changing the text
                self.calculated.configure(text = "Play at {} and {} delay".format(hoursToPlay, secondsToPlay))
                # AutoPlay
                if self.autoPlayCheck.get() == 1:
                        print('Iniciando autoplay...')
                        # Clearing root
                        self.clearRoot()
                        # Adding label
                        ctk.CTkLabel(self.mainRoot, text = 'Aguardando horário {} e {} delay.'.format(hoursToPlay, secondsToPlay)).pack(pady=2)
                        ctk.CTkLabel(self.mainRoot, text = 'Fique no vídeo aguardando.').pack(pady=2)
                        # Initializing
                        autoPlayThread = Thread(target=autoPlay, args=(hoursToPlay, secondsToPlay))
                        autoPlayThread.start()

        def milliOfFrame(self) -> float:
                """Returns the number of frames in milliseconds."""
                millisecondsPerFrame = 1000 / int(self.fps.get())
                return millisecondsPerFrame * int(self.frame.get())

        def clearRoot(self) -> None:
                """Just clean the window."""
                for widget in self.mainRoot.winfo_children():
                        widget.destroy()

        def addZeroLeft(self, hoursToPlay: str) -> str:
                """It doesn't change the calculation, it just adds a zero to the left IF it's only 1 digit."""
                hours = hoursToPlay.split(':')
                for index, hour in enumerate(hours):
                        if len(hour) == 1:
                                hours[index] = '0{}'.format(hour)
                return ':'.join(hours)

if __name__ == '__main__':
        Application()