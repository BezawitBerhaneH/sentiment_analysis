{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e9c1892b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 31962 entries, 0 to 31961\n",
      "Data columns (total 3 columns):\n",
      " #   Column  Non-Null Count  Dtype \n",
      "---  ------  --------------  ----- \n",
      " 0   id      31962 non-null  int64 \n",
      " 1   label   31962 non-null  int64 \n",
      " 2   tweet   31962 non-null  object\n",
      "dtypes: int64(2), object(1)\n",
      "memory usage: 749.2+ KB\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import re\n",
    "import string\n",
    "import nltk\n",
    "import warnings\n",
    "\n",
    "# Ignore warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "\n",
    "# Load the dataset\n",
    "df = pd.read_csv(r'C:\\Users\\bezaw\\Desktop\\train_tweets.csv')\n",
    "\n",
    "# Display the first few rows of the dataset\n",
    "df.head()\n",
    "\n",
    "# Data type information\n",
    "df.info()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "54cb3ce2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def remove_pattern(input_txt, pattern):\n",
    "    r = re.findall(pattern, input_txt)\n",
    "    for word in r:\n",
    "        input_txt = re.sub(word, \"\", input_txt)\n",
    "    return input_txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f346244d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Remove Twitter handles (@user)\n",
    "df['clean_tweet'] = np.vectorize(remove_pattern)(df['tweet'], \"@[\\w]*\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6487cd0d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>label</th>\n",
       "      <th>tweet</th>\n",
       "      <th>clean_tweet</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>@user when a father is dysfunctional and is s...</td>\n",
       "      <td>when a father is dysfunctional and is so sel...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>@user @user thanks for #lyft credit i can't us...</td>\n",
       "      <td>thanks for #lyft credit i can't use cause th...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>bihday your majesty</td>\n",
       "      <td>bihday your majesty</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>#model   i love u take with u all the time in ...</td>\n",
       "      <td>#model   i love u take with u all the time in ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>factsguide: society now    #motivation</td>\n",
       "      <td>factsguide: society now    #motivation</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id  label                                              tweet  \\\n",
       "0   1      0   @user when a father is dysfunctional and is s...   \n",
       "1   2      0  @user @user thanks for #lyft credit i can't us...   \n",
       "2   3      0                                bihday your majesty   \n",
       "3   4      0  #model   i love u take with u all the time in ...   \n",
       "4   5      0             factsguide: society now    #motivation   \n",
       "\n",
       "                                         clean_tweet  \n",
       "0    when a father is dysfunctional and is so sel...  \n",
       "1    thanks for #lyft credit i can't use cause th...  \n",
       "2                                bihday your majesty  \n",
       "3  #model   i love u take with u all the time in ...  \n",
       "4             factsguide: society now    #motivation  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e32bee38",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['clean_tweet'] = df['clean_tweet'].str.replace(\"[^a-zA-Z#]\", \" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2c345c4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['clean_tweet'] = df['clean_tweet'].apply(lambda x: \" \".join([w for w in x.split() if len(w)>3]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "77812357",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>label</th>\n",
       "      <th>tweet</th>\n",
       "      <th>clean_tweet</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>@user when a father is dysfunctional and is s...</td>\n",
       "      <td>when father dysfunctional selfish drags kids i...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>@user @user thanks for #lyft credit i can't us...</td>\n",
       "      <td>thanks #lyft credit can't cause they don't off...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>bihday your majesty</td>\n",
       "      <td>bihday your majesty</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>#model   i love u take with u all the time in ...</td>\n",
       "      <td>#model love take with time urð±!!! ððð...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>factsguide: society now    #motivation</td>\n",
       "      <td>factsguide: society #motivation</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id  label                                              tweet  \\\n",
       "0   1      0   @user when a father is dysfunctional and is s...   \n",
       "1   2      0  @user @user thanks for #lyft credit i can't us...   \n",
       "2   3      0                                bihday your majesty   \n",
       "3   4      0  #model   i love u take with u all the time in ...   \n",
       "4   5      0             factsguide: society now    #motivation   \n",
       "\n",
       "                                         clean_tweet  \n",
       "0  when father dysfunctional selfish drags kids i...  \n",
       "1  thanks #lyft credit can't cause they don't off...  \n",
       "2                                bihday your majesty  \n",
       "3  #model love take with time urð±!!! ððð...  \n",
       "4                    factsguide: society #motivation  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f93f146c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>label</th>\n",
       "      <th>tweet</th>\n",
       "      <th>clean_tweet</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>@user when a father is dysfunctional and is s...</td>\n",
       "      <td>when father dysfunctional selfish drags kids i...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>@user @user thanks for #lyft credit i can't us...</td>\n",
       "      <td>thanks #lyft credit can't cause they don't off...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>bihday your majesty</td>\n",
       "      <td>bihday your majesty</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>#model   i love u take with u all the time in ...</td>\n",
       "      <td>#model love take with time urð±!!! ððð...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>factsguide: society now    #motivation</td>\n",
       "      <td>factsguide: society #motivation</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id  label                                              tweet  \\\n",
       "0   1      0   @user when a father is dysfunctional and is s...   \n",
       "1   2      0  @user @user thanks for #lyft credit i can't us...   \n",
       "2   3      0                                bihday your majesty   \n",
       "3   4      0  #model   i love u take with u all the time in ...   \n",
       "4   5      0             factsguide: society now    #motivation   \n",
       "\n",
       "                                         clean_tweet  \n",
       "0  when father dysfunctional selfish drags kids i...  \n",
       "1  thanks #lyft credit can't cause they don't off...  \n",
       "2                                bihday your majesty  \n",
       "3  #model love take with time urð±!!! ððð...  \n",
       "4                    factsguide: society #motivation  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# remove short words\n",
    "df['clean_tweet'] = df['clean_tweet'].apply(lambda x: \" \".join([w for w in x.split() if len(w)>3]))\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "913c5ed1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    [when, father, dysfunctional, selfish, drags, ...\n",
       "1    [thanks, #lyft, credit, can't, cause, they, do...\n",
       "2                              [bihday, your, majesty]\n",
       "3    [#model, love, take, with, time, urð±!!!, ð...\n",
       "4                  [factsguide:, society, #motivation]\n",
       "Name: clean_tweet, dtype: object"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# individual words considered as tokens\n",
    "tokenized_tweet = df['clean_tweet'].apply(lambda x: x.split())\n",
    "tokenized_tweet.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "dd7c9b70",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    [when, father, dysfunct, selfish, drag, kid, i...\n",
       "1    [thank, #lyft, credit, can't, caus, they, don'...\n",
       "2                              [bihday, your, majesti]\n",
       "3    [#model, love, take, with, time, urð±!!!, ð...\n",
       "4                       [factsguide:, societi, #motiv]\n",
       "Name: clean_tweet, dtype: object"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# stem the words\n",
    "from nltk.stem.porter import PorterStemmer\n",
    "stemmer = PorterStemmer()\n",
    "\n",
    "tokenized_tweet = tokenized_tweet.apply(lambda sentence: [stemmer.stem(word) for word in sentence])\n",
    "tokenized_tweet.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c34fc80e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>label</th>\n",
       "      <th>tweet</th>\n",
       "      <th>clean_tweet</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>@user when a father is dysfunctional and is s...</td>\n",
       "      <td>when father dysfunct selfish drag kid into dys...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>@user @user thanks for #lyft credit i can't us...</td>\n",
       "      <td>thank #lyft credit can't caus they don't offer...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>bihday your majesty</td>\n",
       "      <td>bihday your majesti</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>#model   i love u take with u all the time in ...</td>\n",
       "      <td>#model love take with time urð±!!! ððð...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>factsguide: society now    #motivation</td>\n",
       "      <td>factsguide: societi #motiv</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id  label                                              tweet  \\\n",
       "0   1      0   @user when a father is dysfunctional and is s...   \n",
       "1   2      0  @user @user thanks for #lyft credit i can't us...   \n",
       "2   3      0                                bihday your majesty   \n",
       "3   4      0  #model   i love u take with u all the time in ...   \n",
       "4   5      0             factsguide: society now    #motivation   \n",
       "\n",
       "                                         clean_tweet  \n",
       "0  when father dysfunct selfish drag kid into dys...  \n",
       "1  thank #lyft credit can't caus they don't offer...  \n",
       "2                                bihday your majesti  \n",
       "3  #model love take with time urð±!!! ððð...  \n",
       "4                         factsguide: societi #motiv  "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# combine words into single sentence\n",
    "for i in range(len(tokenized_tweet)):\n",
    "    tokenized_tweet[i] = \" \".join(tokenized_tweet[i])\n",
    "    \n",
    "df['clean_tweet'] = tokenized_tweet\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b32fc066",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
