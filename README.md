This is a keyboard trainer

Tutorial:

1) Open project and click on the entry field. 
If it is your first time of typing practice, you can click on the button 'Clear all statistics'. 
As a result, your speed of typing and count of mistakes will be counted correctly. 
If you want to start with old statistics, don't press the button.
![alt text](https://github.com/baiburinam/keyboard_trainer/blob/566fe64bec2d7c04bf6c3b2a1aafc385bb55ac85/src/image/start.png)

2) Above the entry field you can see a text to type. 
You need to type this text into entry field. 
If you make a mistake, it will not be visible in entry field. 
It ignores all mistakes. You shouldn't use 'delete' button to fix your text.

3) One line is one task. 
After writing one task, you will be able to start a new one.

4) After completing all tasks you can exit or restart.

![alt text](https://github.com/baiburinam/keyboard_trainer/blob/fa2d2fb0a3806a1f3a0a1158e4a8f67778fc337d/src/image/choose_menu.png)

5) All your saved score will be used in your next practices.

![alt text](https://github.com/baiburinam/keyboard_trainer/blob/fa2d2fb0a3806a1f3a0a1158e4a8f67778fc337d/src/image/image_result.png)

6) If you want to close app, please, use exit button or press 'escape'.

If you want to use your text as a task, you need:
1) Create a file named "example_task.json" with a task (or change it).
2) It should have a structure:

{

  "1": "example1",

  "2": "example2"

}

3) Lines shouldn't be too long (80 characters are enough).
4) Add file to project
5) Start practice

Reminder: if you want to clear statistics, press the button 'Clear all statistics'.
