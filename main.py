from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
import phone

Builder.load_file('phonebook.kv')


class PhoneBookApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=[15,], spacing=15)
        layout.canvas.before.add(Color(0.65, 0.65, 0.65, 1))  # Устанавливаем цвет фона
        layout.canvas.before.add(Rectangle(pos=(0, 0), size=(5000, 5000)))  # Рисуем прямоугольник фона


        search_input = TextInput(multiline=True, hint_text='Введите имя или номер для поиска', font_size=16, size_hint=(1, None), height=60, padding=[10, 20, 10, 20], halign='center', background_color=(1, 1, 1, 1),)
        search_button = Button(text='Найти!!!', font_size=14, size_hint=(1, None), height=60, background_color=(0.8, 0.8, 0.8, 1), halign='center', padding=[10, ])
        search_results = ScrollView()
        # search_results.canvas.before.add(Color(1, 0, 0, 1))  # Устанавливаем красный цвет фона
        # search_results.canvas.before.add(Rectangle(pos=(0, 0), size=(5000, 5000)))  # Рисуем прямоугольник фона

        # grid_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        # grid_layout.bind(minimum_height=grid_layout.setter('height'))

        layout.add_widget(search_input)
        layout.add_widget(search_button)
        layout.add_widget(search_results)
        search_button.bind(on_press=lambda _: self.perform_search(search_input, search_results))
        return layout

    def perform_search(self, search_input, search_results):
        query = search_input.text
        res = phone.phones
        
        results = [f'Результаты поиска по запросу "{query}":']
        for key, value in res.items():
            if query in key or query in value["number"]:
                results.append(f'Имя: {key}, \nПодразделение: {value["department"]}, \nДолжность: {value["position"]}, \nТелефон: {value["number"]}, \nПочта: {value["email"]}\n--------------------------------------------------------')

        self.display_results(search_results, results, search_input)


    def display_results(self, search_results, results, search_input):
        search_input.text = ''
        search_results.clear_widgets()

        # layout = BoxLayout(orientation='vertical', spacing=5)
        layout = GridLayout(cols=1)
        # layout.padding = [10, 20, 10, 20]
        layout.size_hint_y = None
        # layout.halign = 'left'
        # layout.valign = 'top'
        layout.height = len(results) * 160  # Задайте высоту в соответствии с количеством результатов

        with layout.canvas.before:
            Color(1, 1, 1, 1)  # Устанавливаем цвет фона
            Rectangle(pos=(0, 0), size=(1920, layout.height))  # Рисуем прямоугольник фона

        for result in results:
            result_label = Label(text=result, font_size=16, color=(0, 0, 0, 1), halign='left', )
            layout.add_widget(result_label)
        search_results.add_widget(layout)


################################
    # def display_results(self, search_results, results, search_input):
    #     search_input.text = ''
    #     search_results.clear_widgets()
    #     layout = BoxLayout(orientation='vertical', spacing=10, padding=[10, 20, 10, 20])
    #     layout.size_hint_y = None
    #     layout.height = len(results) * 160
    #     with layout.canvas.before:
    #         Color(1, 1, 1, 1)
    #         Rectangle(pos=(0, 0), size=(2600, layout.height))
    #     for result in results:
    #         result_label = Label(text=result, font_size=16, color=(0, 0, 0, 1), halign='center')
    #         layout.add_widget(result_label)
    #     scroller = ScrollView(size_hint=(1, None), height=400, do_scroll_x=False, bar_color=(0, 1, 0, 0.2))
    #     scroller.add_widget(layout)
    #     search_results.add_widget(scroller)
################################################################


if __name__ == '__main__':
    PhoneBookApp().run()




