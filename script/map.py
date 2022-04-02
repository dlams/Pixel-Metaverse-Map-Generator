import cv2
from PIL import Image
import os

#메세지 포멧
def alert(msg):
    print('[ ' + '\033[91m' + '!' + '\033[97m' + ' ]', end=' ')
    print(msg)
#픽셀 별 맵 분류
def map_class(x, y):
    check = f'{custom_map[y, x]}'.replace('[ ', '[')
    #기본 흙 시리즈
    if check == "[62 197 170]":
        return "grass"
    #벽돌 시리즈
    elif check == "[107 111 165]":
        return "brick1"
    elif check == "[141 141 152]":
        return "brick2"
    elif check == "[73 73 82]":
        return "brick3"
    #길 시리즈
    elif check == "[33 33 36]":
        return "road1"
    elif check == "[87 87 93]":
        return "road2"
    elif check == "[42 42 44]":
        return "road3"
    elif check == "[25 25 27]":
        return "road4"
    elif check == "[18 18 19]":
        return "road5"
    #나머지 None 처리
    else:
        return "None"

#Map File Select
custom_map = cv2.imread("resource/custom/custom_map.png")
alert('맵 로딩 중...')

#변수 초기화 및 설정
h, w, c = custom_map.shape
map_dir = {}

#폴더내 파일 검색 후 리소스 로딩
for map_type in os.listdir(f'{os.getcwd()}/resource/map'):
    index = map_type.replace('.png', '').replace('map_', '')
    map_dir[index] = Image.open(f"resource/map/{map_type}")
#배경이미지 만들기
alert('맵 생성 중...')
bin_x = 30 + (w-1)*15 + (h-1)*15
bin_y = 23 + (w+h-2)*8
bin = Image.new("RGBA", (bin_x, bin_y))
#맵 만들기
for y in range(h):
    for x in range(w - 1, -1, -1):
        pixel = map_class(x, y)
        if pixel == "None":
            continue
        bin.paste(map_dir[pixel], (x*15+y*15, (w-1-x)*8+y*8-4), map_dir[pixel])
#맵 저장
bin.save('test.png')
alert('맵 생성이 완료됬습니다.')
