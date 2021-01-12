{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 49,
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
       "      <th>Unnamed: 0</th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>Nationality</th>\n",
       "      <th>Club</th>\n",
       "      <th>Value</th>\n",
       "      <th>Wage</th>\n",
       "      <th>Position</th>\n",
       "      <th>Crossing</th>\n",
       "      <th>Finishing</th>\n",
       "      <th>...</th>\n",
       "      <th>Penalties</th>\n",
       "      <th>Composure</th>\n",
       "      <th>Marking</th>\n",
       "      <th>StandingTackle</th>\n",
       "      <th>SlidingTackle</th>\n",
       "      <th>GKDiving</th>\n",
       "      <th>GKHandling</th>\n",
       "      <th>GKKicking</th>\n",
       "      <th>GKPositioning</th>\n",
       "      <th>GKReflexes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>12897.000000</td>\n",
       "      <td>12897</td>\n",
       "      <td>12897.000000</td>\n",
       "      <td>12897</td>\n",
       "      <td>12897</td>\n",
       "      <td>1.289700e+04</td>\n",
       "      <td>12897.000000</td>\n",
       "      <td>12897</td>\n",
       "      <td>12897.000000</td>\n",
       "      <td>12897.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>12897.000000</td>\n",
       "      <td>12897.000000</td>\n",
       "      <td>12897.000000</td>\n",
       "      <td>12897.000000</td>\n",
       "      <td>12897.000000</td>\n",
       "      <td>12897.000000</td>\n",
       "      <td>12897.000000</td>\n",
       "      <td>12897.000000</td>\n",
       "      <td>12897.000000</td>\n",
       "      <td>12897.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>NaN</td>\n",
       "      <td>12326</td>\n",
       "      <td>NaN</td>\n",
       "      <td>156</td>\n",
       "      <td>650</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>27</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>NaN</td>\n",
       "      <td>J. Rodríguez</td>\n",
       "      <td>NaN</td>\n",
       "      <td>England</td>\n",
       "      <td>V-Varen Nagasaki</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>GK</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>NaN</td>\n",
       "      <td>9</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1368</td>\n",
       "      <td>30</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1641</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>6605.040862</td>\n",
       "      <td>NaN</td>\n",
       "      <td>24.795379</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.112449e+06</td>\n",
       "      <td>7517.562224</td>\n",
       "      <td>NaN</td>\n",
       "      <td>47.076374</td>\n",
       "      <td>42.876328</td>\n",
       "      <td>...</td>\n",
       "      <td>46.459874</td>\n",
       "      <td>55.942932</td>\n",
       "      <td>45.655811</td>\n",
       "      <td>46.186710</td>\n",
       "      <td>44.386679</td>\n",
       "      <td>17.218345</td>\n",
       "      <td>16.962317</td>\n",
       "      <td>16.797938</td>\n",
       "      <td>16.950221</td>\n",
       "      <td>17.315965</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>3782.545526</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.872212</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>6.498424e+06</td>\n",
       "      <td>23061.985387</td>\n",
       "      <td>NaN</td>\n",
       "      <td>18.043470</td>\n",
       "      <td>19.096935</td>\n",
       "      <td>...</td>\n",
       "      <td>15.479313</td>\n",
       "      <td>11.280631</td>\n",
       "      <td>19.456346</td>\n",
       "      <td>21.172586</td>\n",
       "      <td>20.726546</td>\n",
       "      <td>18.085618</td>\n",
       "      <td>17.349624</td>\n",
       "      <td>16.971411</td>\n",
       "      <td>17.369297</td>\n",
       "      <td>18.335817</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>1000.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>12.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>3357.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.500000e+05</td>\n",
       "      <td>1000.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>28.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>37.000000</td>\n",
       "      <td>49.000000</td>\n",
       "      <td>29.000000</td>\n",
       "      <td>25.000000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>8.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>6622.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.000000e+05</td>\n",
       "      <td>2000.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>51.000000</td>\n",
       "      <td>45.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>47.000000</td>\n",
       "      <td>56.000000</td>\n",
       "      <td>51.000000</td>\n",
       "      <td>54.000000</td>\n",
       "      <td>51.000000</td>\n",
       "      <td>11.000000</td>\n",
       "      <td>11.000000</td>\n",
       "      <td>11.000000</td>\n",
       "      <td>11.000000</td>\n",
       "      <td>11.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>9876.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>28.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>8.500000e+05</td>\n",
       "      <td>4000.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>61.000000</td>\n",
       "      <td>59.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>58.000000</td>\n",
       "      <td>63.000000</td>\n",
       "      <td>62.000000</td>\n",
       "      <td>64.000000</td>\n",
       "      <td>62.000000</td>\n",
       "      <td>14.000000</td>\n",
       "      <td>14.000000</td>\n",
       "      <td>14.000000</td>\n",
       "      <td>14.000000</td>\n",
       "      <td>14.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>13125.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>45.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.185000e+08</td>\n",
       "      <td>565000.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>93.000000</td>\n",
       "      <td>95.000000</td>\n",
       "      <td>...</td>\n",
       "      <td>91.000000</td>\n",
       "      <td>96.000000</td>\n",
       "      <td>93.000000</td>\n",
       "      <td>93.000000</td>\n",
       "      <td>91.000000</td>\n",
       "      <td>90.000000</td>\n",
       "      <td>92.000000</td>\n",
       "      <td>91.000000</td>\n",
       "      <td>90.000000</td>\n",
       "      <td>94.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>11 rows × 42 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          Unnamed: 0          Name           Age Nationality  \\\n",
       "count   12897.000000         12897  12897.000000       12897   \n",
       "unique           NaN         12326           NaN         156   \n",
       "top              NaN  J. Rodríguez           NaN     England   \n",
       "freq             NaN             9           NaN        1368   \n",
       "mean     6605.040862           NaN     24.795379         NaN   \n",
       "std      3782.545526           NaN      4.872212         NaN   \n",
       "min         0.000000           NaN     16.000000         NaN   \n",
       "25%      3357.000000           NaN     21.000000         NaN   \n",
       "50%      6622.000000           NaN     24.000000         NaN   \n",
       "75%      9876.000000           NaN     28.000000         NaN   \n",
       "max     13125.000000           NaN     45.000000         NaN   \n",
       "\n",
       "                    Club         Value           Wage Position      Crossing  \\\n",
       "count              12897  1.289700e+04   12897.000000    12897  12897.000000   \n",
       "unique               650           NaN            NaN       27           NaN   \n",
       "top     V-Varen Nagasaki           NaN            NaN       GK           NaN   \n",
       "freq                  30           NaN            NaN     1641           NaN   \n",
       "mean                 NaN  2.112449e+06    7517.562224      NaN     47.076374   \n",
       "std                  NaN  6.498424e+06   23061.985387      NaN     18.043470   \n",
       "min                  NaN  0.000000e+00    1000.000000      NaN      5.000000   \n",
       "25%                  NaN  2.500000e+05    1000.000000      NaN     35.000000   \n",
       "50%                  NaN  5.000000e+05    2000.000000      NaN     51.000000   \n",
       "75%                  NaN  8.500000e+05    4000.000000      NaN     61.000000   \n",
       "max                  NaN  1.185000e+08  565000.000000      NaN     93.000000   \n",
       "\n",
       "           Finishing  ...     Penalties     Composure       Marking  \\\n",
       "count   12897.000000  ...  12897.000000  12897.000000  12897.000000   \n",
       "unique           NaN  ...           NaN           NaN           NaN   \n",
       "top              NaN  ...           NaN           NaN           NaN   \n",
       "freq             NaN  ...           NaN           NaN           NaN   \n",
       "mean       42.876328  ...     46.459874     55.942932     45.655811   \n",
       "std        19.096935  ...     15.479313     11.280631     19.456346   \n",
       "min         2.000000  ...      5.000000     12.000000      3.000000   \n",
       "25%        28.000000  ...     37.000000     49.000000     29.000000   \n",
       "50%        45.000000  ...     47.000000     56.000000     51.000000   \n",
       "75%        59.000000  ...     58.000000     63.000000     62.000000   \n",
       "max        95.000000  ...     91.000000     96.000000     93.000000   \n",
       "\n",
       "        StandingTackle  SlidingTackle      GKDiving    GKHandling  \\\n",
       "count     12897.000000   12897.000000  12897.000000  12897.000000   \n",
       "unique             NaN            NaN           NaN           NaN   \n",
       "top                NaN            NaN           NaN           NaN   \n",
       "freq               NaN            NaN           NaN           NaN   \n",
       "mean         46.186710      44.386679     17.218345     16.962317   \n",
       "std          21.172586      20.726546     18.085618     17.349624   \n",
       "min           2.000000       3.000000      1.000000      1.000000   \n",
       "25%          25.000000      23.000000      8.000000      8.000000   \n",
       "50%          54.000000      51.000000     11.000000     11.000000   \n",
       "75%          64.000000      62.000000     14.000000     14.000000   \n",
       "max          93.000000      91.000000     90.000000     92.000000   \n",
       "\n",
       "           GKKicking  GKPositioning    GKReflexes  \n",
       "count   12897.000000   12897.000000  12897.000000  \n",
       "unique           NaN            NaN           NaN  \n",
       "top              NaN            NaN           NaN  \n",
       "freq             NaN            NaN           NaN  \n",
       "mean       16.797938      16.950221     17.315965  \n",
       "std        16.971411      17.369297     18.335817  \n",
       "min         1.000000       1.000000      1.000000  \n",
       "25%         8.000000       8.000000      8.000000  \n",
       "50%        11.000000      11.000000     11.000000  \n",
       "75%        14.000000      14.000000     14.000000  \n",
       "max        91.000000      90.000000     94.000000  \n",
       "\n",
       "[11 rows x 42 columns]"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "d = pd.read_csv('data_sf.csv')\n",
    "d.describe(include='all')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
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
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>Nationality</th>\n",
       "      <th>Club</th>\n",
       "      <th>Value</th>\n",
       "      <th>Wage</th>\n",
       "      <th>Position</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>L. Messi</td>\n",
       "      <td>31</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>FC Barcelona</td>\n",
       "      <td>110500000</td>\n",
       "      <td>565000</td>\n",
       "      <td>RF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Cristiano Ronaldo</td>\n",
       "      <td>33</td>\n",
       "      <td>Portugal</td>\n",
       "      <td>Juventus</td>\n",
       "      <td>77000000</td>\n",
       "      <td>405000</td>\n",
       "      <td>ST</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Neymar Jr</td>\n",
       "      <td>26</td>\n",
       "      <td>Brazil</td>\n",
       "      <td>Paris Saint-Germain</td>\n",
       "      <td>118500000</td>\n",
       "      <td>290000</td>\n",
       "      <td>LW</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>De Gea</td>\n",
       "      <td>27</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Manchester United</td>\n",
       "      <td>72000000</td>\n",
       "      <td>260000</td>\n",
       "      <td>GK</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>K. De Bruyne</td>\n",
       "      <td>27</td>\n",
       "      <td>Belgium</td>\n",
       "      <td>Manchester City</td>\n",
       "      <td>102000000</td>\n",
       "      <td>355000</td>\n",
       "      <td>RCM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>E. Hazard</td>\n",
       "      <td>27</td>\n",
       "      <td>Belgium</td>\n",
       "      <td>Chelsea</td>\n",
       "      <td>93000000</td>\n",
       "      <td>340000</td>\n",
       "      <td>LF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>L. Modrić</td>\n",
       "      <td>32</td>\n",
       "      <td>Croatia</td>\n",
       "      <td>Real Madrid</td>\n",
       "      <td>67000000</td>\n",
       "      <td>420000</td>\n",
       "      <td>RCM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>L. Suárez</td>\n",
       "      <td>31</td>\n",
       "      <td>Uruguay</td>\n",
       "      <td>FC Barcelona</td>\n",
       "      <td>80000000</td>\n",
       "      <td>455000</td>\n",
       "      <td>RS</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Sergio Ramos</td>\n",
       "      <td>32</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Real Madrid</td>\n",
       "      <td>51000000</td>\n",
       "      <td>380000</td>\n",
       "      <td>RCB</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>J. Oblak</td>\n",
       "      <td>25</td>\n",
       "      <td>Slovenia</td>\n",
       "      <td>Atlético Madrid</td>\n",
       "      <td>68000000</td>\n",
       "      <td>94000</td>\n",
       "      <td>GK</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>R. Lewandowski</td>\n",
       "      <td>29</td>\n",
       "      <td>Poland</td>\n",
       "      <td>FC Bayern München</td>\n",
       "      <td>77000000</td>\n",
       "      <td>205000</td>\n",
       "      <td>ST</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>T. Kroos</td>\n",
       "      <td>28</td>\n",
       "      <td>Germany</td>\n",
       "      <td>Real Madrid</td>\n",
       "      <td>76500000</td>\n",
       "      <td>355000</td>\n",
       "      <td>LCM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>D. Godín</td>\n",
       "      <td>32</td>\n",
       "      <td>Uruguay</td>\n",
       "      <td>Atlético Madrid</td>\n",
       "      <td>44000000</td>\n",
       "      <td>125000</td>\n",
       "      <td>CB</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>David Silva</td>\n",
       "      <td>32</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Manchester City</td>\n",
       "      <td>60000000</td>\n",
       "      <td>285000</td>\n",
       "      <td>LCM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>N. Kanté</td>\n",
       "      <td>27</td>\n",
       "      <td>France</td>\n",
       "      <td>Chelsea</td>\n",
       "      <td>63000000</td>\n",
       "      <td>225000</td>\n",
       "      <td>LDM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>P. Dybala</td>\n",
       "      <td>24</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>Juventus</td>\n",
       "      <td>89000000</td>\n",
       "      <td>205000</td>\n",
       "      <td>LF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>H. Kane</td>\n",
       "      <td>24</td>\n",
       "      <td>England</td>\n",
       "      <td>Tottenham Hotspur</td>\n",
       "      <td>83500000</td>\n",
       "      <td>205000</td>\n",
       "      <td>ST</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>A. Griezmann</td>\n",
       "      <td>27</td>\n",
       "      <td>France</td>\n",
       "      <td>Atlético Madrid</td>\n",
       "      <td>78000000</td>\n",
       "      <td>145000</td>\n",
       "      <td>CAM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>M. ter Stegen</td>\n",
       "      <td>26</td>\n",
       "      <td>Germany</td>\n",
       "      <td>FC Barcelona</td>\n",
       "      <td>58000000</td>\n",
       "      <td>240000</td>\n",
       "      <td>GK</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>T. Courtois</td>\n",
       "      <td>26</td>\n",
       "      <td>Belgium</td>\n",
       "      <td>Real Madrid</td>\n",
       "      <td>53500000</td>\n",
       "      <td>240000</td>\n",
       "      <td>GK</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Sergio Busquets</td>\n",
       "      <td>29</td>\n",
       "      <td>Spain</td>\n",
       "      <td>FC Barcelona</td>\n",
       "      <td>51500000</td>\n",
       "      <td>315000</td>\n",
       "      <td>CDM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>E. Cavani</td>\n",
       "      <td>31</td>\n",
       "      <td>Uruguay</td>\n",
       "      <td>Paris Saint-Germain</td>\n",
       "      <td>60000000</td>\n",
       "      <td>200000</td>\n",
       "      <td>LS</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>M. Neuer</td>\n",
       "      <td>32</td>\n",
       "      <td>Germany</td>\n",
       "      <td>FC Bayern München</td>\n",
       "      <td>38000000</td>\n",
       "      <td>130000</td>\n",
       "      <td>GK</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>S. Agüero</td>\n",
       "      <td>30</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>Manchester City</td>\n",
       "      <td>64500000</td>\n",
       "      <td>300000</td>\n",
       "      <td>ST</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>G. Chiellini</td>\n",
       "      <td>33</td>\n",
       "      <td>Italy</td>\n",
       "      <td>Juventus</td>\n",
       "      <td>27000000</td>\n",
       "      <td>215000</td>\n",
       "      <td>LCB</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Name  Age Nationality                 Club      Value  \\\n",
       "0            L. Messi   31   Argentina         FC Barcelona  110500000   \n",
       "1   Cristiano Ronaldo   33    Portugal             Juventus   77000000   \n",
       "2           Neymar Jr   26      Brazil  Paris Saint-Germain  118500000   \n",
       "3              De Gea   27       Spain    Manchester United   72000000   \n",
       "4        K. De Bruyne   27     Belgium      Manchester City  102000000   \n",
       "5           E. Hazard   27     Belgium              Chelsea   93000000   \n",
       "6           L. Modrić   32     Croatia          Real Madrid   67000000   \n",
       "7           L. Suárez   31     Uruguay         FC Barcelona   80000000   \n",
       "8        Sergio Ramos   32       Spain          Real Madrid   51000000   \n",
       "9            J. Oblak   25    Slovenia      Atlético Madrid   68000000   \n",
       "10     R. Lewandowski   29      Poland    FC Bayern München   77000000   \n",
       "11           T. Kroos   28     Germany          Real Madrid   76500000   \n",
       "12           D. Godín   32     Uruguay      Atlético Madrid   44000000   \n",
       "13        David Silva   32       Spain      Manchester City   60000000   \n",
       "14           N. Kanté   27      France              Chelsea   63000000   \n",
       "15          P. Dybala   24   Argentina             Juventus   89000000   \n",
       "16            H. Kane   24     England    Tottenham Hotspur   83500000   \n",
       "17       A. Griezmann   27      France      Atlético Madrid   78000000   \n",
       "18      M. ter Stegen   26     Germany         FC Barcelona   58000000   \n",
       "19        T. Courtois   26     Belgium          Real Madrid   53500000   \n",
       "20    Sergio Busquets   29       Spain         FC Barcelona   51500000   \n",
       "21          E. Cavani   31     Uruguay  Paris Saint-Germain   60000000   \n",
       "22           M. Neuer   32     Germany    FC Bayern München   38000000   \n",
       "23          S. Agüero   30   Argentina      Manchester City   64500000   \n",
       "24       G. Chiellini   33       Italy             Juventus   27000000   \n",
       "\n",
       "      Wage Position  \n",
       "0   565000       RF  \n",
       "1   405000       ST  \n",
       "2   290000       LW  \n",
       "3   260000       GK  \n",
       "4   355000      RCM  \n",
       "5   340000       LF  \n",
       "6   420000      RCM  \n",
       "7   455000       RS  \n",
       "8   380000      RCB  \n",
       "9    94000       GK  \n",
       "10  205000       ST  \n",
       "11  355000      LCM  \n",
       "12  125000       CB  \n",
       "13  285000      LCM  \n",
       "14  225000      LDM  \n",
       "15  205000       LF  \n",
       "16  205000       ST  \n",
       "17  145000      CAM  \n",
       "18  240000       GK  \n",
       "19  240000       GK  \n",
       "20  315000      CDM  \n",
       "21  200000       LS  \n",
       "22  130000       GK  \n",
       "23  300000       ST  \n",
       "24  215000      LCB  "
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "small_d = d[d.columns[1:8]].head(25)\n",
    "small_d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Spain        4\n",
       "Uruguay      3\n",
       "Germany      3\n",
       "Argentina    3\n",
       "Belgium      3\n",
       "France       2\n",
       "Slovenia     1\n",
       "Italy        1\n",
       "Poland       1\n",
       "Croatia      1\n",
       "Brazil       1\n",
       "Portugal     1\n",
       "England      1\n",
       "Name: Nationality, dtype: int64"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = small_d['Nationality'].value_counts()\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Spain', 'Uruguay', 'Germany', 'Argentina', 'Belgium', 'France',\n",
       "       'Slovenia', 'Italy', 'Poland', 'Croatia', 'Brazil', 'Portugal',\n",
       "       'England'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "V-Varen Nagasaki     30\n",
       "Shonan Bellmare      30\n",
       "Vissel Kobe          29\n",
       "Padova               29\n",
       "FC Emmen             29\n",
       "                     ..\n",
       "Cruzeiro              8\n",
       "GD Chaves             7\n",
       "Dinamo Zagreb         7\n",
       "Vitória Guimarães     7\n",
       "Atlético Mineiro      6\n",
       "Name: Club, Length: 650, dtype: int64"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = d['Club'].value_counts()\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "650"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(s.index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[649]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Spain        0.16\n",
       "Uruguay      0.12\n",
       "Germany      0.12\n",
       "Argentina    0.12\n",
       "Belgium      0.12\n",
       "France       0.08\n",
       "Slovenia     0.04\n",
       "Italy        0.04\n",
       "Poland       0.04\n",
       "Croatia      0.04\n",
       "Brazil       0.04\n",
       "Portugal     0.04\n",
       "England      0.04\n",
       "Name: Nationality, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "s = small_d['Nationality'].value_counts(normalize=True)\n",
    "display(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GK     0.127239\n",
       "ST     0.117237\n",
       "CB     0.108785\n",
       "CM     0.082732\n",
       "LB     0.077692\n",
       "RB     0.073505\n",
       "RM     0.059394\n",
       "LM     0.056447\n",
       "CDM    0.053578\n",
       "CAM    0.049081\n",
       "RCB    0.032411\n",
       "LCB    0.031713\n",
       "LW     0.018764\n",
       "RCM    0.018609\n",
       "RW     0.018376\n",
       "LCM    0.018066\n",
       "LDM    0.011476\n",
       "RDM    0.010700\n",
       "LS     0.009382\n",
       "RS     0.008839\n",
       "RWB    0.005428\n",
       "LWB    0.004652\n",
       "CF     0.003954\n",
       "LF     0.000620\n",
       "RF     0.000465\n",
       "LAM    0.000465\n",
       "RAM    0.000388\n",
       "Name: Position, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "s = d['Position'].value_counts(normalize=True)\n",
    "display(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LS     0.009382\n",
       "RS     0.008839\n",
       "RWB    0.005428\n",
       "LWB    0.004652\n",
       "CF     0.003954\n",
       "LF     0.000620\n",
       "RF     0.000465\n",
       "LAM    0.000465\n",
       "RAM    0.000388\n",
       "Name: Position, dtype: float64"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[s < 0.01]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(211750.0, 329500.0]     9\n",
       "(93528.999, 211750.0]    8\n",
       "(329500.0, 447250.0]     6\n",
       "(447250.0, 565000.0]     2\n",
       "Name: Wage, dtype: int64"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " small_d['Wage'].value_counts(bins=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "small_df = small_d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "s = small_df['Wage'].value_counts(bins=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
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
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>Nationality</th>\n",
       "      <th>Club</th>\n",
       "      <th>Value</th>\n",
       "      <th>Wage</th>\n",
       "      <th>Position</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>L. Messi</td>\n",
       "      <td>31</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>FC Barcelona</td>\n",
       "      <td>110500000</td>\n",
       "      <td>565000</td>\n",
       "      <td>RF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>L. Suárez</td>\n",
       "      <td>31</td>\n",
       "      <td>Uruguay</td>\n",
       "      <td>FC Barcelona</td>\n",
       "      <td>80000000</td>\n",
       "      <td>455000</td>\n",
       "      <td>RS</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Name  Age Nationality          Club      Value    Wage Position\n",
       "0   L. Messi   31   Argentina  FC Barcelona  110500000  565000       RF\n",
       "7  L. Suárez   31     Uruguay  FC Barcelona   80000000  455000       RS"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "small_df.loc[(small_df['Wage'] > s.index[3].left) & (small_df['Wage'] <= s.index[3].right)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "small_df = d[d.columns[0:7]].head(25)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(211750.0, 329500.0]     9\n",
       "(93528.999, 211750.0]    8\n",
       "(329500.0, 447250.0]     6\n",
       "(447250.0, 565000.0]     2\n",
       "Name: Wage, dtype: int64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "s = small_df['Wage'].value_counts(bins=4)\n",
    "display(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "IntervalIndex([(211750.0, 329500.0], (93528.999, 211750.0], (329500.0, 447250.0], (447250.0, 565000.0]],\n",
       "              closed='right',\n",
       "              dtype='interval[float64]')"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Interval(447250.0, 565000.0, closed='right')"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.index[3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "565000.0"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.index[3].left\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "565000.0"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.index[3].right"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      True\n",
       "1     False\n",
       "2     False\n",
       "3     False\n",
       "4     False\n",
       "5     False\n",
       "6     False\n",
       "7      True\n",
       "8     False\n",
       "9     False\n",
       "10    False\n",
       "11    False\n",
       "12    False\n",
       "13    False\n",
       "14    False\n",
       "15    False\n",
       "16    False\n",
       "17    False\n",
       "18    False\n",
       "19    False\n",
       "20    False\n",
       "21    False\n",
       "22    False\n",
       "23    False\n",
       "24    False\n",
       "Name: Wage, dtype: bool"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "small_df['Wage'] > s.index[3].left"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
