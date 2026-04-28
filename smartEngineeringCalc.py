from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from sympy import symbols, solve, diff, simplify


class SmartEngineeringCalculator(App):

    def build(self):
        self.x = symbols('x')

        main = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        self.title_label = Label(
            text="Smart Engineering Calculator",
            font_size=28,
            size_hint=(1, 0.12)
        )

        self.input_box = TextInput(
            hint_text="Enter expression like x**2 - 5*x + 6",
            multiline=False,
            font_size=22,
            size_hint=(1, 0.15)
        )

        self.mode = Spinner(
            text="Choose Operation",
            values=("Solve Equation", "Derivative", "Simplify"),
            size_hint=(1, 0.15)
        )

        self.button = Button(
            text="Calculate",
            font_size=22,
            size_hint=(1, 0.15)
        )

        self.button.bind(on_press=self.calculate)

        self.result = Label(
            text="Result will appear here",
            font_size=22
        )

        main.add_widget(self.title_label)
        main.add_widget(self.input_box)
        main.add_widget(self.mode)
        main.add_widget(self.button)
        main.add_widget(self.result)

        return main

    def calculate(self, instance):
        try:
            expr_text = self.input_box.text
            expr = eval(expr_text, {"x": self.x})
            

            if self.mode.text == "Solve Equation":
                answer = solve(expr, self.x)

            elif self.mode.text == "Derivative":
                answer = diff(expr, self.x)

            elif self.mode.text == "Simplify":
                answer = simplify(expr)

            else:
                answer = "Choose operation"

            self.result.text = str(answer)

        except Exception as e:
            self.result.text = "Invalid Input"


SmartEngineeringCalculator().run()