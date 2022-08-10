# bookinventry
To start project  First Go to CMD (command prompt) and enter following CODE :-
git clone https://github.com/ketanu0690/bookinventry.git
virtualenv env
.\env\Scripts\activate.bat
cd bookinventry
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
http://127.0.0.1:8000/  

// when you open the web portal it will ask you to Login / Register
you Can register with New User or Login With Admin

You will See Ebooks Which ic Google Book Api fetched data 
![image](https://user-images.githubusercontent.com/78308610/184005607-a7982ed0-8842-4fdb-aa09-d0ee83d3fad9.png)

 For You List Of All Books might be Empty so i suggest to create 5 random books like
-spider man	stan lee	10
-Dr strange	Marvel	10
-Man of Steel	DC compnay	20
-Batman DarkKnights	Joker	40
-unity book	Aamir khan	23
-youtube book	money maker	43
-family man	amazone prime	12
![image](https://user-images.githubusercontent.com/78308610/184006193-14708be1-52ad-4021-91bb-cc3177cfa297.png)
![image](https://user-images.githubusercontent.com/78308610/184006253-389d6826-079e-4c8d-87a7-4f76549127c6.png)

 you can Create Store where you can store you books store or type vise
 ![image](https://user-images.githubusercontent.com/78308610/184006456-0872a29a-150a-4d2e-91dd-0f34edab9a92.png)

In View Store You can see and manage your Store 
![image](https://user-images.githubusercontent.com/78308610/184006543-041deb87-2608-4e8f-b4d6-827b20846704.png)
![image](https://user-images.githubusercontent.com/78308610/184006601-b6b0bf2b-918b-45a2-a433-c728f0624df2.png)

and can update from the selected books 
![image](https://user-images.githubusercontent.com/78308610/184006723-9af04a3e-2e70-4dbb-b66a-8ee408d434fe.png)

Edit and delete for books from store  is possible 
![image](https://user-images.githubusercontent.com/78308610/184006882-83981179-d1e0-45fe-903f-eae8b65fe103.png)


