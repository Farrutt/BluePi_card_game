# Project Title
เกมส์จับคู่ไพ่ ที่มีจำนวนไพ่ 12 ใบ โดยหน้าไพ่จะมีเลข 1-6 เลขละ 2 ใบ การเปิดไพ่จะเปิดได้ทีละ 1 ใบ 
ถ้าใบที่ 1 กับ ใบที่ 2 เป็นเลขเดียวกัน ไพ่ 2 ใบนั้นจะถูกเปิดไว้ แต่ถ้าไม่ตรงกัน ไพ่จะคว่ำลงทั้ง 2 ใบ
การเปิดไพ่ 1 ใบ เท่ากับ การคลิก 1 ครั้ง จำนวนคลิกน้อยที่สุดคือดี (น้อยสุด 12 ครั้ง)
## Language and Database
* **Programming Language** : Python 3.7

* **Database** : MongoDB and MariaDB
    * MongoDB
        * database name : Card_game
        * collection name : transaction_card
    * MariaDB
        * database name : bluepi

## File and Folder Description
* **Folder**
    * **api** : คือ โฟลเดอร์ที่เก็บไฟล์เกี่ยวกับ Api ที่ใช้ใน project
        * **File in**
			* **game.py** : คือ ไฟล์ Api ทั้งหมดที่เกี่ยวกับตัวเกมส์
			* **login.py** : คือ ไฟล์ Api ทั้งหมดที่เกี่ยวกับการ login

    * **config** : คือ โฟลเดอร์ที่เก็บไฟล์เกี่ยวกับการ config, connect db, lib, ตั้งค่าหรือตัวแปรต่างๆ
        * **File in**
			* **db_connect.py** : คือ ไฟล์เกี่ยวกับการเชื่อมต่อ database ของ MariaDB
			* **lib.py** : คือ ไฟล์ที่ใช้ import library ต่างๆที่ใช้ในโปรเจค
			* **mongo_connect.py** : คือ ไฟล์เกี่ยวกับการเชื่อมต่อ database ของ MongoDB
			* **value.py** : คือ ไฟล์ที่เก็บตัวแปรที่กำหนดค่าตายตัวไว้
    * **document** : คือ โฟลเดอร์ที่เก็บไฟล์เอกสาร หรือ data ต่างๆเช่น ไฟล์ URL published documentation postman, database structure, database example data, example postman api
        * **File in**
        	* **API_Card_Game.postman_collection.json** : คือ ไฟล์ตัวอย่าง Collection API ที่สามารถนำไป import ใน Postman ได้
        	* **publish_api_postman.txt** : คือ ไฟล์ที่เก็บ URL published documentation postman
            * **Card_Game_API.docx** : คือ ไฟล์ document อธิบายเกี่ยวกับ api ต่างๆ (word)
            * **Card_Game_API.pdf** : คือ ไฟล์ document อธิบายเกี่ยวกับ api ต่างๆ (pdf)
        * **Folder**
        	* **MariaDB** : คือ โฟลเดอร์ที่เก็บ structure sql, example data ของ MariaDB
				* **File in 2**
					* **structure_sql_mariaDB.txt** : คือ sql structure นำไป run แล้วจะได้โครงสร้างตารางของ mariaDB
					* **tb_account_202106281553.csv** : คือ ตัวอย่างข้อมูลของตาราง tb_account ของ mariaDB
					* **tb_token_202106281554.csv** : คือ ตัวอย่างข้อมูลของตาราง tb_token ของ mariaDB
			
        	* **MongoDB** : คือ โฟลเดอร์ที่เก็บ example data ของ MongoDB
            	* **File in 2**
               	* **transaction_card.json** : คือ ตัวอย่างข้อมูลของ collection transaction_card ของ MongoDB
    * **database** : คือ โฟลเดอร์ที่เก็บไฟล์เกี่ยวกับการ query database แบบต่างๆ
        * **File in**
			* **db_insert.py** : คือ ไฟล์ที่ใช้เก็บคำสั่ง query insert ค่าต่างๆ ของ MariaDB
			* **db_select.py** : คือ ไฟล์ที่ใช้เก็บคำสั่ง query select ค่าต่างๆ ของ MariaDB
			* **db_update.py** : คือ ไฟล์ที่ใช้เก็บคำสั่ง query update ค่าต่างๆ ของ MariaDB
			* **mongo_insert.py** : คือ ไฟล์ที่ใช้เก็บคำสั่ง insert ค่าต่างๆ ของ MongoDB
			* **mongo_select.py** : คือ ไฟล์ที่ใช้เก็บคำสั่ง find ค่าต่างๆ ของ MongoDB
			* **mongo_update.py** : คือ ไฟล์ที่ใช้เก็บคำสั่ง update ค่าต่างๆ ของ MongoDB
    * **function** : คือ โฟลเดอร์ที่เก็บไฟล์เกี่ยวกับ function ย่อยในการทำงาน
        * **File in**
        	* **action_click.py** : คือ ไฟล์ที่ใช้เก็บ function ของการคลิกเปิดไพ่
        	* **generate_card.py** : คือ ไฟล์ที่ใช้เก็บ function ของการ generate ไพ่ใหม่เมื่อกด newgame
        	* **generate_key.py** : คือ ไฟล์ที่ใช้เก็บ function ของการ generate token หรือ secret key ต่างๆจาก api login
    * **method** : คือ โฟลเดอร์ที่เก็บไฟล์ที่เป็นตัวกลางในการจัดการ process จากทุกๆ Api
        * **File in**
        	* **game_process.py** : คือ ไฟล์ที่ใช้ในการเก็บ function การประมวลผลเกี่ยวกับตัว game ทั้งหมด
        	* **login_process.py** : คือ ไฟล์ที่ใช้ในการเก็บ function การประมวลผลเกี่ยวกับการ login ทั้งหมด
* **File**
    * **main.py** : คือ ไฟล์ที่ใช้ในการกำหนดค่าต่างๆที่ใช้ในการ run project
    * **requirements.txt** : คือ ไฟล์ที่ใช้ในการเก็บชื่อและเวอร์ชั่นของ library เพื่อใช้ในการ install
# Folder step Work
api > method > function,database > method > api
# API Description
### 1. /card_game/add_user 
**Method: POST**

เป็น api ที่ใช้ในการเพิ่ม user เข้าสู่ฐานข้อมูลของเกมส์ โดยจะรับค่าแบบ json body ซึ่งเป็น key 2 ตัว คือ username, password ถ้า username ที่ใส่เข้าไป ไม่ซ้ำกับ username ที่มีอยู่แล้วในฐานข้อมูล ก็จะสามารถเพิ่ม user ได้
**Example request** :
``` 
{
    "username" : "farruttz",
    "password" : "1234567"
}
```
**Example response** :
``` 
{
    "status_code": 200,
    "message": "add_user success",
    "data": {
        "username": "farruttz",
        "password": "1234567"
    }
}
```
### 2. /card_game/login
**Method: POST**

เป็น api ที่ใช้ในการ login เข้าสู่ตัวเกมส์ โดยจะรับค่าแบบ json body ซึ่งเป็น key 2 ตัว คือ username, password ถ้า username และ password ถูกต้องตามข้อมูลที่มีในฐานข้อมูล ก็จะสามารถ login ได้ และ api จะ response token (อยู่ใน key data)ที่ใช้สำหรับการ Authen ใน api ตัวอื่นๆ
**Example request** :
``` 
{
    "username" : "farruttz",
    "password" : "1234567"
}
```
**Example response** :
``` 
{
    "status_code": 200,
    "message": "login success",
    "data": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImRhcnR6IiwicGFzc3dvcmQiOiIxMjM0NTYifQ._Bm-Az9CzJ7GYkWBx6Qg8fmB7DtrRd-ETm5MUE2j82Q" // This is Token
}
```
### 3. /card_game/new_game
**Method: POST**

เป็น api ที่ใช้ในการ new game (ปุ่ม new game) โดยต้องใส่ request Header Authorization ในรูปแบบ Type Bearer Token คือ Token ที่ได้จากการ Login ไปด้วย ซึ่งเมื่อใช้ api ตัวนี้ จะเป็นการ generate ตำแหน่งตัวเลข 1-6 หรือ สุ่มตำแหน่งไพ่ ทั้ง 12 ใบ และได้ออกมาเป็น list ของไพ่ทั้ง 12 ใบ ในรูปแบบของ row, column และเก็บไว้ใน MongoDB จากนั้นตัว api นี้จะ response id ของชุดไพ่นี้ออกมาให้

**Example response** :
``` 
{
    "status_code": 200,
    "message": "success",
    "data": "60d95767e3eea131e4cafa6c" // This is id of card game
}
```
### 4. /card_game/get_global_score
**Method: GET**

เป็น api ที่ใช้ในการ get คะแนนที่ดีที่สุดของ user จาก user ทั้งหมด หรือก็คือ Global best โดยต้องใส่ request Header Authorization ในรูปแบบ Type Bearer Token คือ Token ที่ได้จากการ Login และตัว api จะ response ค่า Global best ออกมาให้
**Example response** :
``` 
{
    "status_code": 200,
    "message": "success",
    "data": 12 // This is Global best
}
```
### 5. /card_game/get_my_score
**Method: GET**

เป็น api ที่ใช้ในการ get คะแนนที่ดีที่สุดของตัวเอง หรือก็คือ My best โดยต้องใส่ request Header Authorization ในรูปแบบ Type Bearer Token คือ Token ที่ได้จากการ Login และตัว api จะ response ค่า My best ออกมาให้
``` 
{
    "status_code": 200,
    "message": "success",
    "data": 14 // This is My best
}
```
### 6. /card_game/action_open_card
**Method: POST**

เป็น api ที่ใช้ในการเปิดไพ่ในแต่ละครั้ง(เมื่อคลิกเลือกไพ่ใช้ api ตัวนี้) โดยต้องใส่ request Header Authorization ในรูปแบบ Type Bearer Token คือ Token ที่ได้จากการ Login และ request แบบ json body ซึ่งเป็น key 3 ตัว คือ

**Request**

* transaction_id (Type: String) คือ id ของชุดไพ่ ที่ได้จากการใช้ api /card_game/new_game 
* position_column (Type: String) คือ column ของไพ่ใบที่ user คลิกเลือก (มีค่าตั้งแต่ 0-2)
* position_row (Type: String) คือ row ของไพ่ใบที่ user คลิกเลือก (มีค่าตั้งแต่ 0-3)
และ response ใน key data ที่ได้จะประกอบด้วย

**Response**

* this_card (Type: Int) คือ เลขหน้าไพ่ใบที่กดเปิด
* card_all (Type: Array) คือ ไพ่ทั้งหมดในชุด พร้อมสถานะ 
    * number (Type: Int) = หมายเลขหน้าไพ่ (ถ้าเป็น null คือไพ่ใบนั้นคว่ำอยู่)
    * status_open (Type: Boolean) = true คือเปิดแล้ว, false คือยังไม่ถูกเปิด(คว่ำ)
    * status_success (Type: Boolean) = true จับคู่สำเร็จแล้ว, false จับคู่ยังไม่สำเร็จ

    โดยจะได้ออกมาเป็น type Array ที่มีรูปแบบเป็น column, row ดังนี้ [ [0,0] , [0,1] , [0,2] ] , [ [1,0] , [1,1] , [1,2] ] , [ [2,0] , [2,1] , [2,2] ] หรือมองให้เป็นตำแหน่งไพ่ จะได้
``` 
                                        [ [0,0] , [0,1] , [0,2] , [0,3]] ,
                                        [ [1,0] , [1,1] , [1,2] , [1,3] ] ,
                                        [ [2,0] , [2,1] , [2,2] , [2,3] ]
``` 
* click (Type: Int) = จำนวนครั้งที่คลิก
* status_game (Type: String) = สถานะที่บ่งบอกว่าเกมส์นี้จบ(จับคู่ครบ)หรือยัง In_progress = เกมส์ยังไม่จบ, Complete = เกมส์นี้จบแล้ว(ครบคู่)
* global_score (Type: Int) = คะแนนที่ดีที่สุดของ user ทั้งหมด
* my_best (Type: Int) = คะแนนที่ดีที่สุดของตัวเอง
``` 
{
    "status_code": 200,
    "message": "success",
    "data": {
        "this_card": 5, // เลขหน้าไพ่ใบที่กดเปิด
        "card_all": [
            [
                {
                    "number": null,
                    "status_open": false,
                    "status_success": false
                },
                {
                    "number": null,
                    "status_open": false,
                    "status_success": false
                },
                {
                    "number": null,
                    "status_open": false,
                    "status_success": false
                },
                {
                    "number": null,
                    "status_open": false,
                    "status_success": false
                }
            ],
            [
                {
                    "number": null,
                    "status_open": false,
                    "status_success": false
                },
                {
                    "number": null,
                    "status_open": false,
                    "status_success": false
                },
                {
                    "number": null,
                    "status_open": false,
                    "status_success": false
                },
                {
                    "number": null,
                    "status_open": false,
                    "status_success": false
                }
            ],
            [
                {
                    "number": 3,
                    "status_open": true,
                    "status_success": true
                },
                {
                    "number": null,
                    "status_open": false,
                    "status_success": false
                },
                {
                    "number": null,
                    "status_open": false,
                    "status_success": false
                },
                {
                    "number": 3,
                    "status_open": true,
                    "status_success": true
                }
            ]
        ], // ไพ่ทั้งหมดในชุด id 
        "click": 26, // จำนวนครั้งที่คลิก
        "status_game": "In_progress", // สถานะของเกมส์ In_progress = เกมส์ยังไม่จบ, Complete = เกมส์นี้จบแล้ว(ครบคู่)
        "global_score": 12, // Global Best
        "my_best": 12 // My Best
    }
}
```
# API Response Template
**Example response API** :
``` 
{
    "status_code": xxx,
    "message": "xxx",
    "data": xxx
}
```
* status_code คือ ค่า status code ของ response api นั้นๆ 
    * 200 --> OK
    * 400 --> Bad Request
    * 401 --> Unauthorized
* message คือ ข้อความอธิบาย Response ของ api
* data คือ ข้อมูล, สิ่งที่ได้จากการใช้ api

# Deployment
### Usage : Docker
* #### Install Docker
``` 
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```
ทำการตั้งค่าการเรียกใช้ ``` docker ``` แบบไม่ต้องมีคำสั่ง ``` sudo ```
``` 
$ sudo groupadd docker
```
``` 
$ sudo usermod -aG docker $USER
```
``` 
$ systemctl restart docker
``` 
``` 
$ docker run hello-world
```
ถ้าขึ้นดังนี้แสดงว่า Docker พร้อมใช้งาน
``` 
Hello from Docker!
```
* #### Install Docker compose
```
$ sudo apt install docker-compose
``` 
```
$ docker-compose up -d
```
* #### Git clone and deploy
Clone project จาก git
``` 
$ git clone https://github.com/Farrutt/BluePi_card_game.git
``` 
เข้าไปใน project
``` 
$ cd BluePi_card_game
``` 
Build image
``` 
$ docker image build -t BluePi_card_game:0.0.1 .
``` 
git push
``` 
$ docker push BluePi_card_game:0.0.1
``` 
deploy project
``` 
$ docker stack deploy -c docker-stack.yml BluePi_card_game
``` 
check service
``` 
$ docker ps
``` 

