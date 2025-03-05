# toolbox

การสอบของ DSToolBox

1.สร้าง repository ใหม่ "รหัสประจำตัว-ฟังก์ชัน"
-> เข้าไปที่ github.com แล้วทำการสร้าง repository กด New กรอกชื่อ folder “65114540xxx-ฟังชั่นที่ได้”

2.สร้าง web project พร้อม .gitignore
3.commit push
-การเลือกเพิ่มทั้งหมดของ project ที่เราสร้างเข้าไปใน github
git add .
-การเอาขึ้น github แล้วคอมเม้นไว้ว่าเอาขึ้นเพื่ออะไร เช่น -m "Initial Django project setup"
git commit -m "Initial Django project setup"
git commit -m "janenie"
-การเพิ่มไฟล์ที่จะเอาขึ้นไปยัง branch main
git push origin main
git push origin cojectjanenie
4.ลบ directory แล้ว clone ใหม่
-การลบโฟลเดอร์ทั้งหมด
	rmdir /s /q toolbox_65114540420
-ทำการ clone ใหม่
	git clone https://github.com/Phanumatlaloed/projectgenni
-cd เพื่อเข้าไปยัง folder ที่เราสร้างขึ้น
cd 65114540420
->clone github ลงมาก่อนแล้วทำการเข้า cd โฟลเดอร์
->สร้างสภาพแวดล้อมให้เว็บ python -m venv venv 
แล้วทำการเปิดใช้งาน venv\Scripts\activate
ทำการติดตั้ง django pip install django
เริ่มโปรเจค django-admin startproject web_project
gitignore สามารถเพิ่มเข้าไปได้เลยตอนสร้าง repo


5.สร้างและแก้ไข branch ตามชื่อฟังก์ชัน
-เช็ค branch
	git branch

-สร้าง branch ใหม่
git branch Janenienew2

-การสลับไปใช้ branch อื่นนอกจาก main
git checkout -b  Janenienew2
git push origin Janenienew2
-การ push ไปยัง branch ที่สร้างเสร็จ
	git push -u origin Janenienew2

6.เพิ่มฟังก์ชันบนเว็บตามที่กำหนด
เพิ่ม A-E ในไฟล์ view และ model

7.commit push

8.สร้าง docker image
สร้างไฟล์
FROM python:3.12


WORKDIR /myproject


COPY . .


RUN pip install django


RUN python manage.py migrate


EXPOSE 9999


CMD ["python", "manage.py", "runserver", "0.0.0.0:9999"]




 

แล้วต่อด้วยคำสั่งเพื่อสร้าง docker
-docker build -t myproject .


ใช้ docker images เพื่อเช็คไฟล์ที่มีอยู่

- สร้าง docker image
- เปิดเว็บด้วย docker
PS C:\Users\janee\webb\Project-B\course_search> echo > .dockerignore (สร้างdockerignore)
PS C:\Users\janee\webb\Project-B\course_search> docker build -t mydjangoapp .
PS C:\Users\janee\webb\Project-B\course_search> docker run -p 9999:9999 mydjangoapp



9.เปิดเว็บด้วย docker
