import flet as ft
from bd.connectiondb import DataBase

class AppToDo:
    def __init__(self, page: ft.Page):
        self.page = page
        self.configurar_pagina()
        self.banco-dados = DataBase()
        self.usuario = None
        self.verificar_usuario()

    def configurar_pagina(self):
        self.page.title = 'Aplicativo ToDo'
        self.page.window_width = 400
        self.page.window.height = 750
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.padding = 20
        self.definir_cores()

    def definir_cores(self):
        self.cor = {
            'primaria': '#3498db',
            'secundaria': '#2ecc71',
            'fundo': '#121212',
            'texto': '#ffffff',
            'texto_secundario': '#b3b3b3',
            'destaque': '#e74c3c',
            'item_fundo': '#1e1e1e',
            'borda': '#333333',
            'checkbox': '#3498db',
            'botao': '#3498db'
        }
    def verificar_usuario(self):
        if self.usuario is None:
            self.pedir_nome_usuario()
        else:
            self.main()
    def pedir_nome_usuario(self):
        def salvar_usuario(e):
            self.usuario = campo_usuario.value if campo_usuario.value else "Usuário"
            self.page.controls.clear()
            self.main()
        campo_usuario = ft.TextField(
            label="Digite seu nome",
            border_color=self.cor['primaria'],
            focused_border_color=self.cor['secundaria'],
            text_style=ft.TextStyle(color=self.cor['texto']),
            bgcolor=self.cor['item_fundo'],
            border_radius=8,
        )