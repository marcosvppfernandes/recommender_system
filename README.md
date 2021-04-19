# Board Game Recommender System 

## Supervised personalized recommender system using collaborative filtering for board games. 

### Author:
[Marcos V Panyagua Fernandes](https://www.linkedin.com/in/marcosvprestesfernandes/)

![cover](capimages/board_game_cafe.jpg)

## Contents:
* **capimages**: images and a text document crediting each one of them.
* **model_pkl**: The pickled model, that is used on the app.
* **notebooks**: jupyter notebooks containing EDA, FSM, first approaches, walkthrough of feature engineering and more technical analysis. Also contains the gridsearch and how it was decided which parameters were the optimal one to be used on the final notebook.
* **app**: The functional application with source code, images and walkthrough.
* **final_notebook**: A concise notebook with everything that was done to reach the results, mostly focusing on the modeling process.


## Data from [Board Game Geek](https://boardgamegeek.com/)
![logo_data](capimages/bgg_logo.jfif)
- The data last update was on August of 2020
- Contains 3 different datasets(which for our project we are going to use only the first 2):
  - **bgg_reviews**: With 15.8 million rows, containing the nickname of the user, rating for a specific game, ID of that game, name of the game and written review.
  - **games**: With information on over 19 thousand games. Counts with 56 columns, among these it has the year published, the weight (a kind of measure of difficulty), board game designer, minumum and maximum amount of players and the playing time.
  - **reviews_summary**: It has all the information of the first dataset in a summarized way.
- This dataset is property of BoardGameGeek and have to follow their [Terms of Use](https://boardgamegeek.com/wiki/page/XML_API_Terms_of_Use#) and it was obtained from this [kernel](https://www.kaggle.com/jvanelteren/boardgamegeek-reviews?select=bgg-15m-reviews.csv)

