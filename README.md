# Med-Info
## Introduction
### The Project
In order to gain an easier access to information regarding medical symptoms and the danger it may impose on our health, we came up with Med-Info. Med-Info takes a symptom and returns an article relating to the symptom giving the user an in depth of the symptom provided. Based on the information, the user can discern whether it poses a great threat to their health or not as well as sicknesses that contain the symptom.
### The Context
This project is our Portfolio Project, concluding our Foundations at ALX Africa. The team presents a working program at the end of the three weeks of development.
### The Team
* Frank Ng'ang'a - [@Ranci-18](https://github.com/Ranci-18)
* James Yuri - [@yurijames2022](https://github.com/yurijames2022)
* Cliff Omanyo - [@printfCAT](https://github.com/printfCAT)
## Features
* A user friendly landing page
* Secure protocol (HTTPS)
* Easy usage
## How it Works
### Backend & Frontend
1. Once user is at the landing page, they can login from the top or scroll down to find login
![Alt text](<https://github.com/Ranci-18/Health_Web_Service/blob/main/screenshots/Annotation%202023-09-04%20203152.png>)
![Alt text](<../Health_Web_Service/screenshots/Screenshot 2023-09-11 124028.png>)
2. Login is done using a unique ID
![Alt text](<../Health_Web_Service/screenshots/Annotation 2023-09-04 203617.png>)
3. If user does not have a unique ID, they can sign up and get one randomly generated for them
![Alt text](<../Health_Web_Service/screenshots/Annotation 2023-09-04 203712.png>)
4. Once they have signed up with assigned ID, they are redirected to the login page where they can now log in
5. After log in, they are redirected to the search page
![Alt text](<../Health_Web_Service/screenshots/Screenshot 2023-09-11 124721.png>)
6. User types in the symptom they want to know about and submit
7. The keyword is sent to the backend and received by the medical API
8. The API filters the information and returns specific article(s)
9. The results are sent to the frontend and displayed on the screen below the search bar
![Alt text](<../Health_Web_Service/screenshots/Screenshot 2023-09-11 124818.png>)
10. Once user is done, they can logout at the bottom of the search page or at the homepage. They can also decide to stay logged in by leaving everything as it is. Their session will be reserved
### Database
Our database stores the unique IDs for the users which will be used during login. We used MySQL database and PHP as the Object Relational Mapper.
## Challenges
* Learning new technologies: PHP & Advanced HTML
* Learning new concepts
* Failing code
* Finding an adequate API
## Acknowledgments
* ALX Africa Staff - For the help, advice and resources they provided us with during this project and during all our curriculum.
* Cohort 11 and all ALX Africa students - For your friendship, invaluable support, and insight not only for this project, but over the entirety of our time in alxswe program.
* YOU - For reading this documentation and testing out __Med-Info__. We hope you enjoyed the ride!