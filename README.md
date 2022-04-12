# Queue System for Speech Recognition

For this project I referenced [this tutorial](https://blog.logrocket.com/optimizing-task-queues-celery-flask/) for help with Celery and Redis.

# Setup 
1. Set up virtual environment for project
2. Install requirements from `requirements.txt`:
3. Install the Redis Server on your local machine

# Running Application

In one terminal, run the Redis Server with the command `redis-server`.

In another terminal, navigate to the root of the project directory and start the application with the command `flask run`.

Finally in a third terminal, navigate to the root of the project directory and start celery: `celery -A app.celery worker --loglevel=info`.

You can now upload audio (`.wav`) files to the server and see the resulting recognized text in the celery terminal!

# Usage

To upload a file, navigate to `http://127.0.0.1:5000/upload` in a browser and select the desired `.wav` file from your machine. 

 <img width="433" alt="Screen Shot 2022-04-11 at 8 31 44 PM" src="https://user-images.githubusercontent.com/18174572/162855603-142502ec-a9ce-467b-b01d-2fdc29757350.png">
 
<img width="388" alt="Screen Shot 2022-04-11 at 8 31 55 PM" src="https://user-images.githubusercontent.com/18174572/162855605-749ce877-a784-41e1-a13b-09abceb97f25.png">

Once you click "submit", you will be redirected to another page (`http://127.0.0.1:5000/uploader`) which shows the task ID for the task you just submitted.

<img width="454" alt="Screen Shot 2022-04-11 at 8 32 06 PM" src="https://user-images.githubusercontent.com/18174572/162863221-ce060857-d1e2-43a9-8882-7751a96e431a.png">

In the celery terminal you can see the result: 

<img width="526" alt="Screen Shot 2022-04-11 at 9 53 20 PM" src="https://user-images.githubusercontent.com/18174572/162863344-b9b0b78d-8172-49f9-b02a-c5938a7b86ba.png">

And in the `\results` directory you can see a text file containing the transcribed audio message.

<img width="628" alt="Screen Shot 2022-04-11 at 9 53 35 PM" src="https://user-images.githubusercontent.com/18174572/162863462-3b59ef54-9bf0-483a-abf7-401a426779f5.png">

