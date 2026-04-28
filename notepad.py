import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView


class NotePadApp(App):

    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Desktop path
        self.desktop_path = os.path.expanduser("~/Desktop")

        # File chooser (shows Desktop files)
        self.file_chooser = FileChooserListView(
            path=self.desktop_path,
            filters=["*.txt"],
            size_hint=(1, 0.4)
        )

        # Text area
        self.text_area = TextInput(
            multiline=True,
            font_size=18,
            size_hint=(1, 0.45)
        )

        # Buttons
        button_layout = BoxLayout(size_hint=(1, 0.15), spacing=10)

        open_button = Button(text="Open")
        save_button = Button(text="Save")
        clear_button = Button(text="Clear")

        open_button.bind(on_press=self.open_file)
        save_button.bind(on_press=self.save_file)
        clear_button.bind(on_press=self.clear_text)

        button_layout.add_widget(open_button)
        button_layout.add_widget(save_button)
        button_layout.add_widget(clear_button)

        main_layout.add_widget(self.file_chooser)
        main_layout.add_widget(button_layout)
        main_layout.add_widget(self.text_area)

        return main_layout

    def open_file(self, instance):
        if self.file_chooser.selection:
            self.current_file = self.file_chooser.selection[0]

            with open(self.current_file, "r") as file:
                self.text_area.text = file.read()

    def save_file(self, instance):
        if hasattr(self, "current_file"):
            with open(self.current_file, "w") as file:
                file.write(self.text_area.text)

    def clear_text(self, instance):
        self.text_area.text = ""


NotePadApp().run()