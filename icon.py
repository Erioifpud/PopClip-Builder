from PIL import Image, ImageFont, ImageDraw


def create(text, file, font='Ubuntu Mono Bold for Powerline.ttf'):
    tmp = list(text)
    tmp.insert(len(text) // 2, '\n')
    text = ''.join(tmp)

    img = Image.new(mode='RGBA', size=(256, 256), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    fontSize = 200
    width, height = 300, 300
    fontObj = None
    while width > 256 or height > 256:
        fontObj = ImageFont.truetype(font, fontSize)
        width, height = draw.multiline_textsize(text, font=fontObj)
        fontSize -= 1

    offsetWidth = (256 - width) // 2
    offsetHeight = (256 - height) // 2
    draw.multiline_text((offsetWidth, offsetHeight), text, font=fontObj,
                        fill=(0, 0, 0, 255), align='center')
    del draw
    img.save(file, format='png')
