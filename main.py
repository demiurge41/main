import flet as ft
import datetime

def main(page: ft.Page):
    page.title = 'Моё первое приложение!'
    page.theme_mode = ft.ThemeMode.LIGHT
    text_hello = ft.Text(value='Hello world')

    geeting_history = []

    hisrory_text = ft.Text('История приветствий:')



    def text_name(_):
        name = (name_input.value or "").strip()

        if name:
            text_hello.color=None

            now = datetime.datetime.now()
            text_time = now.strftime('%Y:%m:%d - %H:%M:%S')
            
            
            text_hello.value = f'{text_time} - Hello {name}'
            name_input.value = ""
            

            geeting_history.append(text_hello.value)
            print(geeting_history)
            hisrory_text.value = 'История приветствий:\n' + '\n'.join(geeting_history)

        
        else:
            text_hello.value = 'Введите имя!'
            text_hello.color=ft.Colors.RED_900
        

    elevated_button = ft.ElevatedButton('send', on_click=text_name, icon=ft.Icons.SEARCH, color=ft.Colors.RED, icon_color=ft.Colors.BLACK)
    
  
    name_input = ft.TextField(label='Введите что нибудь...', on_click=text_name, expand= True)

    def thememode(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
    
    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)


    def clear_hisrory(_):
        print(geeting_history)
        geeting_history.clear()
        print(geeting_history)
        hisrory_text.value = 'История приветствий:'

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_hisrory)

    main_obj = ft.Row([name_input, elevated_button, thememode_button, clear_button])

    #добавление в страницу
    page.add(text_hello, main_obj, hisrory_text)



ft.app(target=main)

