import PySimpleGUI as sg
from PIL import Image

def main():
    defult_image = Image.open('.\imagesPng\Pokémon logo.png')
    #画像のサイズを変更
    defult_image.thumbnail((400,400))
    #変更した画像を一時ファイルに保持
    defult_image.save('.\\imagesPng\\resized_image.png')

    layout = [[sg.Image(filename='.\\imagesPng\\resized_image.png', key='-image-')],
              [sg.Button('OK',expand_x=True,expand_y=True),sg.Button('イーブイシリーズ',expand_x=True, expand_y=True)]]
    
    window = sg.Window('ポケモン図鑑', layout, resizable=True)

    while True:
        event, values = window.read()

        if event in [sg.WIN_CLOSED, 'OK']:
            break

        window.close()

sample = main()