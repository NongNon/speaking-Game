from PIL import Image

class Game_p:
    colorM=[
        {
            'image':Image.open("images\\colors\\color mode_201122_1.jpg"),
            'ans':['เหลือง','yellow']
        },
        {
            'image':Image.open("images\\colors\\color mode_201122_2.jpg"),
            'ans':['ฟ้า','blue']
        },
        {
            'image':Image.open("images\\colors\\color mode_201122_3.jpg"),
            'ans':['ส้ม','แสด','orange']
        },
        {
            'image':Image.open("images\\colors\\color mode_201122_4.jpg"),
            'ans':['เขียว','green']
        },
        {
            'image':Image.open("images\\colors\\color mode_201122_5.jpg"),
            'ans':['ม่วง','purple']
        },
        {
            'image':Image.open("images\\colors\\color mode_201122_6.jpg"),
            'ans':['ชมพู','pink']
        },
        {
            'image':Image.open("images\\colors\\color mode_201122_7.jpg"),
            'ans':['ดำ','black']
        },
        {
            'image':Image.open("images\\colors\\color mode_201122_8.jpg"),
            'ans':['น้ำเงิน','คราม']
        },
        {
            'image':Image.open("images\\colors\\color mode_201122_9.jpg"),
            'ans':['เทา','gray']
        },
        {
            'image':Image.open("images\\colors\\color mode_201122_10.jpg"),
            'ans':['แดง','red']
        },
    ]

    advanceM=[
        {
            'image':Image.open("images\\advance\\221163_201122_0.jpg"),
            'ans':['เขียว','green']
        },
        {
            'image':Image.open("images\\advance\\221163_201122_1.jpg"),
            'ans':['แดง','red']
        },
        {
            'image':Image.open("images\\advance\\221163_201122_2.jpg"),
            'ans':['เหลือง','yellow']
        },
        {
            'image':Image.open("images\\advance\\221163_201122_3.jpg"),
            'ans':['เขียว','green']
        },
        {
            'image':Image.open("images\\advance\\221163_201122_4.jpg"),
            'ans':['ฟ้า','blue']
        },
        {
            'image':Image.open("images\\advance\\221163_201122_5.jpg"),
            'ans':['ชมพู','pink']
        },
        {
            'image':Image.open("images\\advance\\221163_201122_6.jpg"),
            'ans':['ม่วง','purple']
        },
        {
            'image':Image.open("images\\advance\\221163_201122_7.jpg"),
            'ans':['น้ำเงินเข้ม']
        },
        {
            'image':Image.open("images\\advance\\221163_201122_8.jpg"),
            'ans':['น้ำตาล']
        },
        {
            'image':Image.open("images\\advance\\221163_201122_9.jpg"),
            'ans':['ส้ม','แสด','orange']
        },
        {
            'image':Image.open("images\\advance\\221163_201122_10.jpg"),
            'ans':['น้ำเงิน']
        },
    ]

    animalM=[
        {
            'image':Image.open("images\\animal\\GetOut.jpg"),
            'ans':['เหี้ย','ตู๊บ','ตู่','ควาย']
        },
        {
            'image':Image.open("images\\animal\\0.jpg"),
            'ans':['ควาย','กระบือ']
        },
        {
            'image':Image.open("images\\animal\\1.jpg"),
            'ans':['แมว','cat']
        },
        {
            'image':Image.open("images\\animal\\2.jpg"),
            'ans':['จระเข้']
        },
        {
            'image':Image.open("images\\animal\\3.jpg"),
            'ans':['เป็ด','duck']
        },
        {
            'image':Image.open("images\\animal\\4.jpg"),
            'ans':['ช้าง','elephent']
        },
        {
            'image':Image.open("images\\animal\\5.jpg"),
            'ans':['จิงโจ้']
        },
        {
            'image':Image.open("images\\animal\\6.jpg"),
            'ans':['โคอาล่า']
        },
        {
            'image':Image.open("images\\animal\\7.jpg"),
            'ans':['เสือดาว']
        },
        {
            'image':Image.open("images\\animal\\8.jpg"),
            'ans':['สิงโต']
        },
        {
            'image':Image.open("images\\animal\\9.jpg"),
            'ans':['นกฮูก']
        },
        {
            'image':Image.open("images\\animal\\10.jpg"),
            'ans':['แพนด้า']
        },
        {
            'image':Image.open("images\\animal\\11.jpg"),
            'ans':['หมู','pig']
        },
        {
            'image':Image.open("images\\animal\\12.jpg"),
            'ans':['หนอน','worm']
        },
    ]

    flagM=[
        {
            'image':Image.open("images\\flag\\flag mode_201122_1.jpg"),
            'ans':['พม่า','เมียนมาร์','myanmar']
        },
        {
            'image':Image.open("images\\flag\\flag mode_201122_2.jpg"),
            'ans':['ลาว']
        },
        {
            'image':Image.open("images\\flag\\flag mode_201122_3.jpg"),
            'ans':['มาเลเซีย']
        },
        {
            'image':Image.open("images\\flag\\flag mode_201122_4.jpg"),
            'ans':['กัมพูชา','เขมร']
        },
        {
            'image':Image.open("images\\flag\\flag mode_201122_5.jpg"),
            'ans':['ไทย']
        },
        {
            'image':Image.open("images\\flag\\flag mode_201122_6.jpg"),
            'ans':['เยอรมัน']
        },
        {
            'image':Image.open("images\\flag\\flag mode_201122_7.jpg"),
            'ans':['เกาหลีใต้']
        },
        {
            'image':Image.open("images\\flag\\flag mode_201122_8.jpg"),
            'ans':['แคนาดา','Canada']
        },
        {
            'image':Image.open("images\\flag\\flag mode_201122_9.jpg"),
            'ans':['จีน']
        },
        {
            'image':Image.open("images\\flag\\flag mode_201122_10.jpg"),
            'ans':['บราซิล']
        },
    ]

class Gui_Image:
    AMain={
        'background1':Image.open("images\\system\\bg.jpg"),
        'background2':Image.open("images\\system\\bg2.png"),
    }
    Menu={
        'advanceM':Image.open("images\\system\\advance_mode.png"),
        'animalM':Image.open("images\\system\\animal_mode.png"),
        'colorM':Image.open("images\\system\\color_mode.png"),
        'flagM':Image.open("images\\system\\flag_mode.jpg"),

        'Howto':Image.open("images\\system\\Howto.jpg"),
        'start_info':Image.open("images\\system\\info_start.jpg"),
        'color_info':Image.open("images\\system\\info_color.jpg"),
        'advance_info':Image.open("images\\system\\info_advance.jpg"),
        'animal_info':Image.open("images\\system\\info_animal.jpg"),
        'flag_info':Image.open("images\\system\\info_flag.jpg"),
    }
    Game={
        'start':Image.open("images\\system\\start.jpg"),
        'status_mic':Image.open("images\\system\\mic.jpg"),
    }
    End={
        'menu':Image.open("images\\system\\menu_symbol.png"),
        'again':Image.open("images\\system\\again_symbol.png"),
    }
class Command:
    Menu={
        'colorM':['color','สี'],
        'advanceM':['advance','เทพ'],
        'animalM':['animal','สัตว์'],
        'flagM':['flag','ธง'],
        'exit':['ออกเกม','ปิดเกม','ปิดโปรแกรม'],
        'go':['เข้า','ตกลง','ยืนยัน'],
    }
    Game={
        'exit':['กลับ','เมนู','menu'],
        'next':['เปลี่ยน','ข้าม'],
        'start':['เริ่ม','ไปเลย','go','start'],
    }
    EndGame={
        'menu':['กลับ','เมนู','menu'],
        'again':['อีกครั้ง','เอาใหม่','again'],
    }

class Sound:
    sound_fx={
        'correct': "Sound\\correct.wav",
        'select': "Sound\\select.wav"
    }
