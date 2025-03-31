from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
import pytesseract
import cv2
from PIL import Image as PILImage

class ImageToTextApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical")
        
        self.img_display = Image(size_hint=(1, 0.5))
        self.layout.add_widget(self.img_display)

        self.file_chooser = FileChooserIconView(size_hint=(1, 0.3))
        self.file_chooser.bind(on_selection=self.load_image)
        self.layout.add_widget(self.file_chooser)

        self.extract_btn = Button(text="Extract Text", size_hint=(1, 0.1))
        self.extract_btn.bind(on_press=self.extract_text)
        self.layout.add_widget(self.extract_btn)

        self.text_label = Label(text="", size_hint=(1, 0.1))
        self.layout.add_widget(self.text_label)

        return self.layout

    def load_image(self, chooser, selection):
        if selection:
            self.image_path = selection[0]
            self.img_display.source = self.image_path

    def extract_text(self, instance):
        if hasattr(self, 'image_path'):
            image = cv2.imread(self.image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray)
            self.text_label.text = text

if __name__ == "__main__":
    ImageToTextApp().run()