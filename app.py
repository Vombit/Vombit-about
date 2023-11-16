from flask import Flask, render_template
app = Flask(__name__)

projects = [
    {
        'title': 'Buy-Item-by-Pattern',
        'description': 'Бот предназначен для автоматической скупки предметов Steam, и уведомление в телеграм',
        'icons': ['Python', 'docker'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/buy-item-by-pattern',
        'project_link': '',
        'image': '6.jpg',
        'packages': []
    },
    {
        'title': 'Quasar',
        'description': 'Стриминговая платформа музыки',
        'icons': ['Python', 'docker', 'django', 'jquery'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/quasar',
        'project_link': '',
        'image': '8.jpg',
        'packages': []
    },
    {
        'title': 'IO-AI',
        'description': 'Телеграм-бот совмещенный с OpenAI',
        'icons': ['Python', 'docker'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/io-ai',
        'project_link': '',
        'image': '5.jpg',
        'packages': []
    },
    {
        'title': 'Device-Moving-View',
        'description': 'Отслеживание местоположения, мониторинг и управление товаром',
        'icons': ['NodeJs', 'docker', 'jquery'],
        'language': 'Node.js',
        'github_link': 'https://github.com/Vombit/Device_Moving_View',
        'project_link': '',
        'image': '2.jpg',
        'packages': []
    },
    {
        'title': 'File-Separator',
        'description': 'Программа предназначенная для разбиения файлов на куски',
        'icons': ['Python', 'qt'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/file-separator',
        'project_link': '',
        'image': '7.jpg',
        'packages': []
    },
    {
        'title': 'Sound-Waves',
        'description': 'Клиент-серверное приложения для трансляции звука в сети',
        'icons': ['Python'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/Sound-Waves',
        'project_link': '',
        'image': '4.jpg',
        'packages': []
    },
    {
        'title': 'Yumi-v2.0',
        'description': 'Discord-бот с активностями и экономикой',
        'icons': ['NodeJs', 'discordjs'],
        'language': 'Node.js',
        'github_link': 'https://github.com/Vombit/Discord-Yumi-Bot-v2.0',
        'project_link': '',
        'image': '3.jpg',
        'packages': []
    },
    {
        'title': 'VkCustom',
        'description': 'Изменение дизайна для Вконтакте',
        'icons': ['JavaScript'],
        'language': 'JavaScript',
        'github_link': 'https://github.com/Vombit/VkCustom',
        'project_link': 'https://chrome.google.com/webstore/detail/vkcustom/oehnhecdbdmdbkamifpmcddelbmfgjfh',
        'image': '1.jpg',
        'packages': []
    },
]

@app.route('/')
def index() -> str:
    """Function printing python version."""
    return render_template('index.html', projects=projects)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
