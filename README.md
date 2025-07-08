# RecSysProject

# 1. Objetive
1. Research how a group recommendation is made.
2. Build a recommender system to recommend board games to groups. 

# 2. Tasks
1. Find books and articles about groups recommendations. 
2. Explore data. 
   1. Select relevant features and build dataset to be used. 
3. Preprocessing
   1. Filter date to reduce computational cost, keep only top 100 games of each category. 
   2. Split train and test interactions or ratings. 
   3. Add more information to games, generate embeddings from descriptions and cover images. 
   4. Generate groups of users. 
4. Consensus methods
   1. Write functions for all consensus methods discussed. 
      1. Plurality/majority voting
      2. Average
      3. Multiplicative
      4. Borda count
      5. Copeland score
      6. Approval voting
      7. Least Misery
      8. Most pleasure
      9. Average without Misery
      10. Fairness
      11. Most respected person (or Dictatorship)
5. Models
   1. Individual recommendations methods
      1. SVDpp
      2. Random
      3. Most Popular
   2. Proposed method: XGBoost regressor based on user characterization and similarity with items.
6. Poster 
7. Extend results
8. Paper

# 3. How to run

1. Create uv venv, and make the library RecGroupSys. 
2. Download data from https://www.kaggle.com/datasets/threnjen/board-games-database-from-boardgamegeek/data. 
3. Run EDA:
   1. Run EDA_games.ipynb
   2. Run EDA_user.ipynb
4. Run preprocessing::
   1. Run preprocessing.ipynb
   2. Run preprocessing2.ipynb
   3. Run preprocessing3.ipynb
5. Run baseline models: 
   1. Run Basic_model.ipynb
   2. Run Proposed_model.ipynb