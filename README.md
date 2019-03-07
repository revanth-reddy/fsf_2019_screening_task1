# fsf_2019_screening_task1

Hi! This is the screening task for  **Python fossee Summer Fellowship 2019**. It's a Task Manager app in **Django** .


## Prerequisites

After cloning the repo, install the dependencies present in requirements.txt file using the following command :

```
pip3 -r install requirements.txt
```
## Running the Application
I have used a virtual environment called **myvenv**. 
```
To activate virtual environment use following command in the homedirectory:
> source myvenv/bin/activate
```
To activate it 
There's already a database included in the repo ( db.sqlite3 ). So, there's no need of migrations. You can directly run the server using :
```
> python3 manage.py runserver
```
## About the Application :

### Team Model : -
-   Any authenticated user can create any nunmber of teams and add other authenticated users to them
-   Only Team creator can edit Team details and its member.
-   Every Team creator is a member of that team also.
### Task Model : -
-   A Task is created in a team and Task creator can assign task to no user or other users.
-   If a single user tries to create Task then he is assigned to that task always.
-   Task creator **only** can update the task and other members of same team to which the task belongs can view it.
- Every Task has comments part, where Team members can comment.

###  Comments Model : -
-  Every Comment is associated to a task and has an author and creation date
- Comments creator a.k.a author **only** can edit or delete the comment.

##  Built With
-   [Django](https://www.djangoproject.com/)  - The web framework used
- HTML, CSS, Js, jQuery
- Ajax
```
No third party apps used 😉
```