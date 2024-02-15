from flask import Flask, render_template, request
app = Flask(__name__)


description = {
    'about_title': 'Обо мне',
    'about_text': 'Привет! Я разработчик с опытом в Python, JavaScript и SQL. Моя страсть к кодированию вдохновляет меня на поиск новых решений и возможностей. Мое вдохновение – создание уникальных проектов. Тут вы можете ознакомиться с некоторыми из моих проектов. (Не забудте нажать на "...", чтоб узнать больше о проекте)',
    'about_text2': 'Давайте вместе создадим что-то удивительное!',
    'sub_text': 'Так же двукратный призер регионального чемпионата WorldSkills (2021-2022) по компетенции "Интернет вещей (IoT)".',
    'project_text': 'Ознакомьтесь с моими проектами!'
}

description_en = {
    'about_title': 'About Me',
    'about_text': 'Hello! I\'m a developer experienced in Python, JavaScript, and SQL. My passion for coding inspires me to seek new solutions and possibilities. My inspiration lies in creating unique projects. Here, you can explore some of my projects. (Don\'t forget to click on "..." to learn more about the project)',
    'about_text2': 'Let\'s create something amazing together!',
    'sub_text': 'I\'m also a two-time winner of the regional WorldSkills championship (2021-2022) in the "Internet of Things (IoT)" competition.',
    'project_text': 'Explore my projects!'
}

projects = [
    {
        'title': 'Интернет магазин FeelBro',
        'description': 'Интернет магазин вещей для FeelBro',
        'icons': ['Python', 'JavaScript', 'docker', 'jquery'],
        'language': 'Python',
        'github_link': '',
        'image': '9.jpg',
        'popup_description': 'Разработка интернет-магазина для бренда FeelBro была захватывающим творческим и техническим процессом. Несмотря на трудности с интеграцией доставки, опыт работы принес удовлетворение. <br><br>Сайт был создан с нуля без использования типичных шаблонов, обеспечив в какой то степени индивидуальность бренда. Основное внимание уделялось интуитивной понятности для пользователей, что привело к созданию стильного и функционального интерфейса. <br><br>Результат – успешный и понятный веб-магазин, отражающий особенности <a href="https://feelbro.store" target="_blank">FeelBro</a>',
        'packages': [
            'Django==5.0',
            'Pillow==10.2.0',
            'yookassa==3.0.0',
            'mysqlclient==2.2.1'
        ]
    },
    {
        'title': 'Caelum',
        'description': 'Бесконечное файловое хранилище',
        'icons': ['Python', 'JavaScript', 'qt'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/caelum',
        'image': '10.jpg',
        'popup_description': 'Это продолжение взгляда, на мою программу для разделения файлов на чанки.<br><br> Данная программа позволяет загружать бесконечное количество файлов на сервера мессенджеров, обходя ограничения по размеру файлов. Теперь достаточно просто поместить программу и файл данных на флешку, чтобы получить доступ ко всей вашей информации в любом месте с доступом к интернету и возможностью запустить программу.<br> Это устраняет необходимость в крупных носителях данных. Конечно же, не стоит ожидать абсолютной гарантии сохранности данных, поэтому избегайте хранения чрезвычайно важной информации в данном контексте.<br><br> Проект был разработан исключительно в целях удовлетворения интереса и упрощения доступа к информации.',
        'packages': [
            'auto-py-to-exe==2.42.0',
            'PyQtWebEngine==5.15.6',
            'requests==2.31.0',
            'PyQt5==5.15.10'
        ]
    },
    {
        'title': 'Buy-Item-by-Pattern',
        'description': 'Бот предназначен для автоматической скупки предметов Steam, и уведомление в телеграм',
        'icons': ['Python', 'docker'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/buy-item-by-pattern',
        'image': '6.jpg',
        'popup_description': 'В одном из прошлых заказов мне предстояло выполнить увлекательный, но несколько нетипичный проект. Это была задача, связанная с автоматизацией покупок в CS (Counter-Strike). Моя задача заключалась в том, чтобы создать систему, способную действовать от имени пользователя игры, покупая различные предметы в игровом мире. После успешной покупки система отправляла уведомления через Telegram-бота, дабы держать клиента в курсе процесса.<br><br>Разработка этой системы была увлекательным вызовом. Необходимость создания механизма, который эмулировал бы поведение человека в игре, требовала внимательного и тщательного подхода. Каждый шаг должен был быть точно спланирован и реализован, чтобы избежать возможных проблем с безопасностью и обнаружением системой steam.',
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
        'popup_description': 'Когда сервисы стриминга музыки, вроде Spotify и подобных, начали ограничивать доступ или становиться недоступными для определенных регионов, возникла идея создать собственную платформу для прослушивания музыки. Ведь каждый имеет право на музыкальное наслаждение, независимо от своего местоположения.<br><br>Важным моментом было обеспечение удобства использования и доступности этой платформы для пользователей, при этом сохраняя разнообразие музыкального контента. Такой подход позволял бы различным сообществам и географическим регионам создавать собственные кураторские системы или коллективы, делиться музыкальными предпочтениями и обогащать свой контент.<br><br>Таким образом, эта идея представляла собой не просто альтернативу для доступа к музыке, но и возможность для каждого создать свою уникальную музыкальную платформу, адаптированную под свои предпочтения и нужды.',
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
        'popup_description': 'Один из проектов, над которым я работал, — создание персонального бота с доступом к функциям ChatGPT. Этот проект был задуман и реализован исключительно для удовольствия и развлечения.<br><br>Идея заключалась в том, чтобы разработать своего рода виртуального помощника, способного не только отвечать на вопросы, но и поддерживать увлекательные разговоры, предоставлять информацию и даже выполнять определенные задачи, используя возможности и знания ChatGPT.',
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
        'popup_description': 'Одним из самых значимых и запоминающихся проектов, который, по моему мнению, была работа, где я приобрел огромное количество новых знаний и навыков. Этот проект стал настоящей школой для меня, ведь именно здесь я познакомился с новыми методами разработки, такими как использование kanban-досок, проведение спринтов, участие в совещаниях и применение различных стратегий решения проблем.<br><br>Один из ключевых моментов этой работы заключался в том, что она научила меня не только следовать инструкциям, но и активно искать решения проблем самостоятельно. Это был ценный опыт, который сделал меня более самостоятельным и уверенным в своих силах разработчиком.<br><br>Хотелось бы выразить огромную благодарность нашему наставнику, который играл ключевую роль в этом проекте. Его поддержка, мудрые советы и экспертное руководство были неоценимы.',
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
        'popup_description': 'Однажды у меня зародилась увлекательная идея создать программу, способную разбивать файлы на небольшие части, или чанки, и объединять их обратно при необходимости. Это была необычная, но практичная идея, которая позволяла обойти ограничения размера файла на различных сервисах. Идея заключалась в том, чтобы сделать возможным загружать файлы любого размера на сервисы, имеющие ограничения на размер загружаемых файлов.<br><br>В ходе работы над проектом я также попытался внедрить систему шифрования для каждого чанка файла. Это позволяло безопасно передавать и распространять файлы, сохраняя их конфиденциальность. Идея состояла в том, чтобы каждый чанк был зашифрован отдельно, что делало их независимыми друг от друга и усиливало безопасность при передаче или хранении данных.<br><br>Для меня этот проект стал настоящим вызовом и возможностью погрузиться в мир файловых систем, шифрования данных и оптимизации процесса работы с большими файлами.',
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
        'popup_description': 'Один из моих экспериментальных проектов заключался в создании программы, способной транслировать аудио сигналы с музыкальных источников или микрофона через локальную сеть. В рамках этого проекта была разработана серверная часть приложения, а также клиентское приложение на платформе Kivy для обеспечения удобства пользователей.<br><br>Хотя этот проект остался на стадии прототипа, он был увлекательным опытом в разработке программного обеспечения. Работа над ним позволила мне окунуться в мир разработки пользовательского интерфейса под различные операционные системы, что стало непривычным, но увлекательным вызовом. Использование фреймворка Kivy для создания клиентской части приложения открыло новые горизонты в создании интерфейсов и адаптации под разные платформы.<br><br>Одним из наиболее интересных аспектов этого проекта было работа с захватом аудио сигналов и музыкальных дорожек из системы. Это потребовало глубокого погружения в технические нюансы, связанные с обработкой звука, его захватом и передачей через сеть.',
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
        'popup_description': 'Этот проект прошел через много изменений. На пике популярности Discord-серверов была идея создать бота для удовлетворения их потребностей.<br><br>Изначально он включал множество функций, от активности и профилей пользователей до экономики и трансляции музыки. На пике популярности число пользователей достигло ~200 000.<br><br>Однако, поддерживать такой амбициозный проект стало сложно в одиночку.<br><br>В конечном итоге, решено было оставить его в прошлом и двигаться дальше. Этот опыт стал важным уроком о необходимости адаптации к изменениям в динамичной сфере, как сообщества Discord.',
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
        'popup_description': 'Изменение стиля для Вконтакте <br> <br>Дополнение добавляет в соц. сеть Vk.com тёмную тему, которая незначительно меняет дизайн сети и не даёт нагрузку на глаза в тёмное время суток.Расширь свои возможности. <br><br> Самый первый мой общедоступный проект, появился в следствии необходимости темной темы для Вк, когда её ещё не было. Самый простой принцип работы заменением оригинального css файла и добавление js скрипта, позволяющего изменять backgroud сайта на свое изображение/gif.<br>Расширение: <a href="https://chrome.google.com/webstore/detail/vkcustom/oehnhecdbdmdbkamifpmcddelbmfgjfh" target="_blank">chromewebstore</a> <br><br>Через призму времени, можно многое было бы изменить и улучшить, но я больше не вернусь...',
        'packages': ['none']
    },
]

projects_en = [
    {
        'title': 'FeelBro Online Store',
        'description': 'Online store for FeelBro merchandise',
        'icons': ['Python', 'JavaScript', 'docker', 'jquery'],
        'language': 'Python',
        'github_link': '',
        'image': '9.jpg',
        'popup_description': 'The development of the online store for the FeelBro brand was an exciting and technical process. Despite challenges with delivery integration, the experience brought satisfaction. <br><br>The website was built from scratch without using typical templates, ensuring a degree of uniqueness for the brand. The primary focus was on intuitive user-friendliness, leading to the creation of a stylish and functional interface. <br><br>The result is a successful and user-friendly web store, reflecting the characteristics of <a href="https://feelbro.store" target="_blank">FeelBro</a>.',
        'packages': [
            'Django==5.0',
            'Pillow==10.2.0',
            'yookassa==3.0.0',
            'mysqlclient==2.2.1'
        ]
    },
    {
        'title': 'Caelum',
        'description': 'Infinite file storage',
        'icons': ['Python', 'JavaScript', 'qt'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/caelum',
        'image': '10.jpg',
        'popup_description': 'This is a follow-up to my previous post about my program for splitting files into smaller chunks.<br><br> This program allows you to upload an unlimited number of files to Messenger servers, bypassing the file size limit.<br> Now, all you need to do is to put the program and your data file on a USB drive to access all your information from anywhere with internet access and the ability to run the program.<br> This eliminates the need for bulky storage media. However, you should be aware that there is no absolute guarantee of data security. Therefore, it is not recommended to store extremely sensitive information in this manner.<br><br> The project was created solely for the purpose of satisfying our users interest and providing easy access to information.',
        'packages': [
            'auto-py-to-exe==2.42.0',
            'PyQtWebEngine==5.15.6',
            'requests==2.31.0',
            'PyQt5==5.15.10'
        ]
    }, 
   {
        'title': 'Buy-Item-by-Pattern',
        'description': 'A bot designed for automatic purchase of Steam items and notifying via Telegram.',
        'icons': ['Python', 'docker'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/buy-item-by-pattern',
        'image': '6.jpg',
        'popup_description': 'In one of my previous orders, I was tasked with an exciting yet somewhat atypical project. It involved automating purchases in CS (Counter-Strike). My goal was to create a system capable of acting on behalf of a game user, buying various items within the game world. Upon successful purchase, the system sent notifications through a Telegram bot to keep the client informed about the process.<br><br>Developing this system was an intriguing challenge. The need to create a mechanism that mimicked human behavior in the game required a meticulous approach. Every step had to be precisely planned and implemented to avoid potential security issues and detection by the Steam system.',
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
        'description': 'Music streaming platform.',
        'icons': ['Python', 'docker', 'django', 'jquery'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/quasar',
        'image': '8.jpg',
        'popup_description': 'When music streaming services like Spotify began restricting access or becoming unavailable in certain regions, the idea of creating our own music platform emerged. After all, everyone deserves the pleasure of music regardless of their location.<br><br>Ensuring user-friendliness and accessibility of this platform while maintaining a diverse range of music content was crucial. This approach would allow different communities and geographic regions to create their own curatorial systems or collectives, sharing musical preferences and enriching their content.<br><br>Thus, this idea represented not just an alternative for accessing music but also an opportunity for everyone to create a unique music platform tailored to their preferences and needs.',
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
        'description': 'Telegram bot combined with OpenAI.',
        'icons': ['Python', 'docker'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/io-ai',
        'image': '5.jpg',
        'popup_description': 'One of the projects I worked on involved creating a personal bot with access to ChatGPT features. This project was conceived and implemented solely for enjoyment and entertainment.<br><br>The idea was to develop a kind of virtual assistant capable not only of answering questions but also engaging in interesting conversations, providing information, and even performing specific tasks using the capabilities and knowledge of ChatGPT.',
        'packages': [
            'openai==0.27.2',
            'python-telegram-bot==20.2',
            'python-dotenv==1.0.0'
        ]
    },
        {
        'title': 'Device-Moving-View',
        'description': 'Tracking location, monitoring, and managing goods.',
        'icons': ['NodeJs', 'docker', 'jquery'],
        'language': 'Node.js',
        'github_link': 'https://github.com/Vombit/Device_Moving_View',
        'image': '2.jpg',
        'popup_description': 'One of the most significant and memorable projects, in my opinion, was a job where I acquired a vast amount of new knowledge and skills. This project became a true school for me as it introduced me to new development methods such as using kanban boards, conducting sprints, participating in meetings, and applying various problem-solving strategies.<br><br>One of the key aspects of this work was that it taught me not only to follow instructions but also actively seek solutions to problems independently. It was a valuable experience that made me a more self-reliant and confident developer.<br><br>I would like to express immense gratitude to our mentor who played a pivotal role in this project. His support, wise advice, and expert guidance were invaluable.',
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
        'description': 'A program designed to split files into chunks.',
        'icons': ['Python', 'qt'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/file-separator',
        'image': '7.jpg',
        'popup_description': 'Once, I had an intriguing idea to create a program capable of dividing files into smaller parts or chunks and merging them back when needed. It was an unusual yet practical idea that circumvented file size limitations on various services. The idea was to enable uploading files of any size to services with restrictions on uploaded file sizes.<br><br>During the project, I also attempted to implement an encryption system for each file chunk. This allowed the safe transmission and distribution of files while maintaining their confidentiality. The concept was to encrypt each chunk separately, making them independent from each other and enhancing security during data transmission or storage.<br><br>For me, this project was a real challenge and an opportunity to delve into the world of file systems, data encryption, and optimizing the process of working with large files.',
        'packages': [
            'cryptography==41.0.5',
            'PyQt5==5.15.10'
        ]
    },
    {
        'title': 'Sound-Waves',
        'description': 'Client-server application for audio streaming over a network.',
        'icons': ['Python'],
        'language': 'Python',
        'github_link': 'https://github.com/Vombit/Sound-Waves',
        'image': '4.jpg',
        'popup_description': 'One of my experimental projects involved creating a program capable of streaming audio signals from music sources or a microphone over a local network. Within this project, I developed the server-side application as well as a client application on the Kivy platform to ensure user convenience.<br><br>Although this project remained at the prototype stage, it was an engaging experience in software development. Working on it allowed me to dive into the world of creating user interfaces for different operating systems, which was an unfamiliar yet fascinating challenge. Using the Kivy framework to create the client-side application opened new horizons in interface creation and adaptation for various platforms.<br><br>One of the most interesting aspects of this project was working with capturing audio signals and music tracks from the system. This required a deep dive into technical nuances related to sound processing, capturing, and transmission over a network.',
        'packages': [
            'Flask==3.0.0',
            'PyAudio==0.2.14',
            'Kivy==2.2.1',
            'urllib3==2.1.0'
        ]
    },
    {
        'title': 'Yumi-v2.0',
        'description': 'Discord bot with activities and economy.',
        'icons': ['NodeJs', 'discordjs'],
        'language': 'Node.js',
        'github_link': 'https://github.com/Vombit/Discord-Yumi-Bot-v2.0',
        'image': '3.jpg',
        'popup_description': 'This project went through many changes. At the peak of Discord server popularity, there was an idea to create a bot to cater to their needs.<br><br>Initially, it included numerous features, from user activities and profiles to economy and music streaming. At its peak, the user count reached ~200,000.<br><br>However, maintaining such an ambitious project became challenging alone.<br><br>In the end, it was decided to leave it in the past and move forward. This experience became an important lesson about the necessity of adapting to changes in the dynamic realm, such as the Discord community.',
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
        'description': 'Customizing Vkontakte design.',
        'icons': ['JavaScript'],
        'language': 'JavaScript',
        'github_link': 'https://github.com/Vombit/VkCustom',
        'image': '1.jpg',
        'popup_description': 'Customizing the style for Vkontakte.<br><br>The extension adds a dark theme to the social network Vk.com, which slightly changes the network\'s design and reduces eye strain during dark hours. Expand your possibilities.<br><br>My very first public project arose from the need for a dark theme for Vk when it didn\'t exist yet. The simplest working principle involved replacing the original CSS file and adding a JS script to change the site\'s background to a custom image/gif.<br>Extension: <a href="https://chromewebstore.google.com/detail/vkcustom/oehnhecdbdmdbkamifpmcddelbmfgjfh" target="_blank">chromewebstore</a><br><br>Looking back, much could have been changed and improved, but I won\'t go back...',
        'packages': ['none']
    },
]

@app.route('/')
def index() -> str:
    supported_languages = ["ru", "en"]
    lang = request.accept_languages.best_match(supported_languages)
    print(lang)
    
    project = projects_en
    descr = description_en
    if lang == "ru":
        project = projects
        descr = description
    
    return render_template('index.html', projects=project, description=descr)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
