import PySimpleGUI as sg
from PIL import Image
import os

sg.theme('DarkBrown1')

#一時ファイルのパス

temp_path = './temp'

go_next_frag = None

def main():
    global go_next_frag
    defult_image = Image.open('.\\imagesPng\\Pokémon logo.png')
    #画像のサイズを変更
    defult_image.thumbnail((400,400))
    
    #変更した画像を一時ファイルに保持
    defult_image.save('./temp/resized_image.png')

    frame_1 = [[sg.Text('フォルダの読み込み'), sg.Button('参照', key='-browsefile-')],[sg.Listbox(values=[], size=(60, 30), key='-image_list-',enable_events=True)]]

    frame_in_frame = [
                     [sg.Button('前へ', key='-back-'), sg.Button('次へ', key='-next-')],
                     [sg.Text('',key='text', size=(60,1))], [sg.Text('',key='-filepath-')]
                     ]
    frame_2 = [
               [sg.Image(filename='.\\temp\\resized_image.png', key='-image-', size=(400, 400))],
               [sg.Frame('group', layout=frame_in_frame, size=(400,200))]
               ]
    
    layout = [
        [sg.Frame('ローカル画像検索',frame_1,size=(250,600), expand_x=True, expand_y=True), sg.Frame('画像表示',frame_2,size=(450, 600))],
            ]

    window = sg.Window('ポケモン図鑑', layout, size=(700,600), )

    while True:
        event, values = window.read(timeout=100)

        if event == sg.WINDOW_CLOSED:
             break
        #選択したフォルダのパスを表示
        if event == '-browsefile-':
            go_next_frag = True
            folder = sg.popup_get_folder('画像が保存されているフォルダを選択してね')
            images_dict = image_listup(folder)
            window['-filepath-'].update(f'参照元：{folder}')
            if images_dict:
                image_key = list(images_dict.keys())#画像をインデックス番号で管理するためのリスト
                window['-image_list-'].update(values=list(images_dict.keys()))
                #画像のインデックスを初期化
                current_index = 0
                image_resize(images_dict[image_key[current_index]])
                window['-image-'].update(filename=f'./temp/{image_key[current_index]}')
            else:sg.popup('表示できる画像がありません', title='error')

        #リストボックスから画像をクリックしたときに画像を表示
        if event == '-image_list-':
            key = values['-image_list-'][0]
            #画像のリサイズ
            image_resize(images_dict[key])
            window['-image-'].update(filename=f'./temp/{key}')
            window['text'].update(f'ファイル名：{key}')

            #前へボタンを押したとき
        if event == '-back-':
            if go_next_frag != True:
                pass
            else:
                current_index -= 1
                if current_index < 0:
                    current_index = len(image_key) - 1
                image_resize(images_dict[image_key[current_index]])
                window['-image-'].update(filename=f'./temp/{image_key[current_index]}')

        #次へ画像を表示したとき
        if event == '-next-':
            if go_next_frag != True:
                pass
            else:
                current_index += 1
                if current_index >= len(image_key):
                    current_index = 0
                image_resize(images_dict[image_key[current_index]])
                window['-image-'].update(filename=f'./temp/{image_key[current_index]}')

        #ウインドウのサイズ取得
        # window_size = window.size
        # print(window_size[0], window_size[1])
    window.close()

def image_read(dir):
    i = 0
    for file in os.listdir(dir):
        if file.endswith('.png'):
            image = Image.open(dir + '\\' + file)
            image.thumbnail((400,400))
            image.save(f'{dir}\\resized_image{i}.png')
            i += 1

#PNG画像をリストアップ
def image_listup(dir):
    image_list = {}
    if os.path.exists(dir):
        for file in os.listdir(dir):
            if file.endswith('.png'):
                image_list[f'{file}'] = os.path.join(dir, file)
    return image_list

#画像のリサイズ
def image_resize(image_path):
    file_name = os.path.basename(image_path)
    if not os.path.exists(f'./temp/{file_name}'):
        image = Image.open(image_path)
        image.thumbnail((400,400))
        image.save(f'./temp/{file_name}')

    else:pass

if __name__ == '__main__':

    sample = main()

