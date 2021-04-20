 [programmer : ekoabdulaziz96@gmail.com]

informasi : 
 1. file ERD            : ERD.jpg
 2. file PDF Test       : Homework Test - Fullstack
 3. code user           : app_middleware
 3. code dataset        : app_dataset
 4. code task           : app_dataset          

Run Program [LOCAL DEVELOPMENT]: 
1. pastikan python sudah terisntall di laptop/PC anda 
    - buka cmd/powershell, tepat diluar folder bismillah_konvergenAI
2. siapkan virtualenvironment baru dan aktifkan. (tidak wajib)
    - pip install virtualenv
    - virtualenv venv
    - ./venv/script/activate  (powershell)
3. masuk ke folder program 
    - cd bismillah_konvergenAI
4. install requirements program
    - pip install -r requirements.txt
5. perhatian, Database default yang digunakan adalah sqlite3 dan sudah di migrasi serta sudah di input beberapa data sesuai petunjuk test pada file PDF
    - bila ingin mengganti dengan Database postgreSQl, silahkan buka file 'app_rootwen/settings.py' dan isi konfigurasinya pada variabel DATABASES
        referensi : https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04 
    - kemudian lakukan perintah 'python manage.py migrate' pada cmd/powershell
    - bila berhasil akan ada pesan 'Applying ...'
6. jalankan program
    - python manage.py runserver


struktur folder:
-bismillah_konvergenAI
-venv


NB:
- deployment/production: https://bismillah-konvergen-ai.herokuapp.com/ [DB:postgreSQL]
- github public : https://github.com/ekoabdulaziz96/bismillah_konvergenAI
- untuk informasi production silahkan hubungi ekoabdulaziz96@gmail.com

TERIMAKSIH, SEMANGAT!!