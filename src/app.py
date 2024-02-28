import os
import pandas as pd
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
import matplotlib.pyplot as plt
# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

conection = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = client_id,client_secret=client_secret))
artist_id = '2AbQwU2cuEGfD465wCXlg2'
response = conection.artist_top_tracks(artist_id)

data =[]

for track in response['tracks']:
   
    dic ={'name' : track['name'],
          'popularity' : track['popularity'],
          'duration_min': round((track['duration_ms'])/60000,2)}
    data.append(dic)

df = pd.DataFrame(data)

df = df.sort_values(by='popularity',ascending=False)
print(df.head(3))

df_num = df.drop(columns='name')
corelacion = df_num.corr()
print(corelacion)



plt.scatter(df['duration_min'], df['popularity'])
plt.xlabel('Duración (min)')
plt.ylabel('Popularidad')
plt.title('Gráfico de dispersión: Duración vs Popularidad')

plt.show()
