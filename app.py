from flask import Flask, render_template
app = Flask(__name__)

projects = [
    {
        'title': 'Buy-Item-by-Pattern',
        'description': 'Бот предназначен для автоматической скупки предметов Steam, и уведомление в телеграм',
        'icons': ['Python', 'docker'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/buy-item-by-pattern',
        'image': '6.jpg',
        'popup_description': '',
        'packages': [
            'steampy==0.80',
            'python-dotenv==1.0.0',
            'Pillow==9.5.0',
            'python-telegram-bot==20.3',
            'playwright==1.34.0'
            ]
    },
    {
        'title': 'Quasar',
        'description': 'Стриминговая платформа музыки',
        'icons': ['Python', 'docker', 'django', 'jquery'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/quasar',
        'image': '8.jpg',
        'popup_description': '',
        'packages': [
            'asgiref==3.6.0',
            'backports.zoneinfo==0.2.1',
            'cutlet==0.1.19',
            'Django==4.1.5',
            'django-cleanup==6.0.0',
            'fugashi==1.2.1',
            'jaconv==0.3.3',
            'mojimoji==0.0.12',
            'mutagen==1.46.0',
            'Pillow==9.4.0',
            'six==1.16.0',
            'sorl-thumbnail==12.9.0',
            'sqlparse==0.4.3',
            'transliterate==1.10.2',
            'tzdata==2022.7',
            'unidic-lite==1.0.8'
            ]
    },
    {
        'title': 'IO-AI',
        'description': 'Телеграм-бот совмещенный с OpenAI',
        'icons': ['Python', 'docker'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/io-ai',
        'image': '5.jpg',
        'popup_description': '',
        'packages': [
            'openai==0.27.2',
            'python-telegram-bot==20.2',
            'python-dotenv==1.0.0'
            ]
    },
    {
        'title': 'Device-Moving-View',
        'description': 'Отслеживание местоположения, мониторинг и управление товаром',
        'icons': ['NodeJs', 'docker', 'jquery'],
        'language': 'Node.js',
        'github_link': 'https://github.com/Vombit/Device_Moving_View',
        'image': '2.jpg',
        'popup_description': '',
        'packages': [
            'body-parser: ^1.19.0',
            'cookie-parser: ^1.4.5',
            'dotenv: ^9.0.2',
            'ejs: ~2.6.1',
            'express: ~4.16.1',
            'express-session: ^1.17.2',
            'fast-csv: ^4.3.6',
            'fast-csv-delims: 0.0.211',
            'fs: 0.0.1-security',
            'jimp: ^0.16.1',
            'multer: ^1.4.2',
            'mysql2: ^2.2.5',
            'qrcode: ^1.4.4',
            'url: ^0.11.0'
            ]
    },
    {
        'title': 'File-Separator',
        'description': 'Программа предназначенная для разбиения файлов на куски',
        'icons': ['Python', 'qt'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/file-separator',
        'image': '7.jpg',
        'popup_description': '',
        'packages': [
            'cryptography==41.0.5',
            'PyQt5==5.15.10'
            ]
    },
    {
        'title': 'Sound-Waves',
        'description': 'Клиент-серверное приложения для трансляции звука в сети',
        'icons': ['Python'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/Sound-Waves',
        'image': '4.jpg',
        'popup_description': '',
        'packages': [
            'Flask==3.0.0',
            'PyAudio==0.2.14',
            'Kivy==2.2.1',
            'urllib3==2.1.0'
            ]
    },
    {
        'title': 'Yumi-v2.0',
        'description': 'Discord-бот с активностями и экономикой',
        'icons': ['NodeJs', 'discordjs'],
        'language': 'Node.js',
        'github_link': 'https://github.com/Vombit/Discord-Yumi-Bot-v2.0',
        'image': '3.jpg',
        'popup_description': '',
        'packages': [
            "@discordjs/opus: ^0.4.0",
            "discord.js: ^12.5.1",
            "distube: ^2.8.11",
            "dotenv: ^8.2.0",
            "ffmpeg-static: ^4.2.7",
            "fs: 0.0.1-security",
            "jimp: ^0.16.1",
            "mysql2: ^2.2.5"
            ]
    },
    {
        'title': 'VkCustom',
        'description': 'Изменение дизайна для Вконтакте',
        'icons': ['JavaScript'],
        'language': 'JavaScript',
        'github_link': 'https://github.com/Vombit/VkCustom',
        'image': '1.jpg',
        'popup_description': '',
        'packages': []
    },
]

@app.route('/')
def index() -> str:
    """Function printing python version."""
    return render_template('index.html', projects=projects)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
