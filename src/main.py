import flet


def main(page: flet.Page):
    page.title = "Hello, Flet!"

    page.add(flet.Text("Welcome to Flet!"))


flet.run(main)
