from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import audio
import threading

class CustomBar(BoxLayout):
    def adder(self):
        print("hello")

class Customviewer(BoxLayout):
    pass

class MyBox(BoxLayout):
    def print_text(self):
        if self.ids.spinner_id.text == 'Select':
            return
        audio.functions.function_associations[self.ids.input_box.text] = self.ids.spinner_id.text
        self.ids.hintbox.add_widget(Label(text=self.ids.input_box.text+" : "+self.ids.spinner_id.text))
        
    def spinner_clicked(self, text):
        if False:
            new_button = Button(text=f"Button", id = f"helpme")
            self.ids.spite.add_widget(new_button)
        
second_thread = None
class MyApp(App):
    def build(self):
        global second_thread
        self.title = "Speechactions"
        print("hello")
        second_thread = threading.Thread(target = audio.start_to_listen, daemon=True)
        #second_thread.start()
        return MyBox()

if __name__ == "__main__":
    MyApp().run()