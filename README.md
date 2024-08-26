# GoogleAIHackathon-May2024
Instructions:
- For some reason the Netherlands are foresaken by google, condemned to a fate of luddite-ity so use Express VPN to connect from the US
- TODO create requirements.txt - uvicorn, google-generativeai, fastapi
- Make sure correct environment is running 
- To run the fastapi app, use the command: cd /fastApiProject then uvicorn main:app --reload & connect to localhost:8000 in your browser
- To run the front-end, use the command: cd /vite_frontend then npm run dev & connect to http://localhost:5173/ in your browser
- Vue front-end is in the vite-frontend directory
- FastAPI backend is in the FastApiProject directory

# Important resources
- Our github repo: [Click here](https://github.com/heliagh2/GoogleAIHackathon-May2024)
- Our roadmap: [Click here](https://docs.google.com/document/d/1o3Mu4OIEc3xfQuphIISexPNrz5cM4Ie7D6mNQToQiuc/edit)
- How to build a vuejs / fastapi app: [Click here](https://medium.com/@sangeeth123sj/how-to-create-a-web-app-using-fastapi-vuejs-and-mongodb-for-generating-and-showcasing-images-193ccdb20091)
- Google API quickstart: [Click here](https://ai.google.dev/tutorials/python_quickstart)
- Google hackathon devpost: [Click here](https://devpost.com/software/googleaihackathon-may2024)
- Google AI studio: [Click here](https://aistudio.google.com/), [Quickstart](https://ai.google.dev/tutorials/ai-studio_quickstart)
- Google AI Python SDK for the Gemini API: [Click here](https://github.com/google/generative-ai-python)
- Google Gemini cookbook: [Click here](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Prompting.ipynb)
- Google Gemini example: [Click here](https://github.com/google-gemini/cookbook/blob/main/examples/Story_Writing_with_Prompt_Chaining.ipynb)
- Fast API documentation: [Click here](https://fastapi.tiangolo.com/)

# Structure of App
- Front end: Vue js
- Backend: Fast API
- Hosting: Google cloud

# Road map
1. Make sure everyone can run app locally
2. Back-end: Create all pages (front page, chat page, dashboard, terms & conditions, privacy)
3. Dashboard: figure out how to collect metrics, display in charts
4. Front-end: Make it pretty
5. System prompting: Create instructions for Gemini
6. Deploy

# Roles

## Helia
- [ ] Dick around with python api 
- [ ] In a python file just call google gemini api 
- [ ] Write prompt you want to give to google and python gives response 
- [ ] As part of that have demo conversation in mind
- [ ] Optimize response with system prompt
- [ ] Write prompts for the lessons
- [ ] Secretly evaluate the person and give back numeric score & output that value to json file, dont show to user. Gemini gives multiple outputs (one to user one to json) - Gemini json response  (search this)
  - Ex. count mistakes, or give score 1 - 100 for language proficiency

- [ ] Look into system prompt for chat gpt - what to put so the system is helpful
- [ ] Look into duo lingo levels & role play scenarios

- [ ] Measuring progress
  - Little test to begin with 
  - Point system - once reached certain points, move to next unit 
  - Output json of specific format to extract data from the chat history

### Prompting 

* Prompting :)
* How to address the user
* nothing sexual, violent, hate speech, bigoted, self harm, etc.
* Constraints & restrictions - get this from generic chat gpt prompt (safety settings)
* Instructions - don't say no I don't want to help you etc., be patient, kind, funny, etc. 
* If they’re not learning try alternate strategies
* Maybe use images? 
* Point system - define min. Length of time 
* Gamify? 
* Repeat certain prompts sometimes to help upkeep

## Chris
- [x] Fast API backend 
- [x] Build little demo app based on tutorial
- [ ] How to write scores to file & display in dashboard
- [ ] Build dashboard
- [ ] How to deploy???

### Metrics
- What are the metrics we want to show the user?
- How do we measure progress?
  - \# of dutch words / day or ratio to english
  - \# of new dutch words / day
  - Spelling mistakes % of dutch words 
  - Grammatical mistakes % of dutch words 
  - Subject proficiency - score for each role play scenario


## Esrion
- [ ] Vue js frontend 
- [ ] What should everything look like - look into very clean & minimal vue js templates
- [ ] What is the interface 
  - [ ] Frontpage - welcome & about us, contact, FAQ
  - [ ] Chat page
  - [ ] Dashboard - progress - learning plan 
  - [ ] Terms & Conditions
  - [ ] Privacy/GDPR
    - Trustpilot

# User story
* User goes to front page, reads about 
* Open chat page
* Ask proficiency -> if higher than lvl 1 -> Mini language test
* Ask what you want to learn dutch for
* Use to choose role play scenarios
* How often do you want to practice
* Keep track of score, once reach certain level of proficiency, level up
* Decide what counts as “complete level” or “complete role play”
* Start at language level that you tested at
* The login retains user conversation, progress
* Level up when reach certain score

# Dashboard
* Usage (time)
* Streak (daily)
* Level
* Prompts “completed”
* Profile info (achievements, following others, avatar)
* V2.0: If you don't show up for a long time
  * Do mini quiz, if fail go one level down

# Lessons
* Define what qualifies each level, amount of english mixed with dutch
  * https://www.eur.nl/en/education/language-training-centre/cefr-levels
* Level 1 - No Dutch
* Level 2 - Beginner dutch
* Level 3  - Basic dutch
* Level 4 - Intermediate
* Level 5 - Advanced
* Level 6 - Daily upkeep - just conversation
  * User can choose own role play scenario with restrictions 


 

