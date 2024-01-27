# Song-Popularity-Predictor

Attempt to help musicians and lables save money, time and energy when promoting songs. This focus of this peoject is to see how machine learning can help predict the popuparity of a song even before it is released. Enabling entertainers make informed decisons.

Train data = 40,000 songs
Test data =  10,000 songs

Variables:

1. id: Unique identifier for each song.
2. song_duration_ms: Duration of the song in milliseconds.
3. acousticness: A measure of the acoustic quality of the song.
4. danceability: A measure of how suitable a song is for dancing.
5. energy: A measure of the intensity and activity of the song.
6. instrumentalness: Indicates the song's likelihood of being instrumental.
7. key: The key the song is in.
8. liveness: Detects the presence of an audience in the recording.
9. loudness: The overall loudness of a track in decibels.
10. audio_mode: Modality of the music (major or minor).
11. speechiness: Measures the presence of spoken words in a song.
12. tempo: The overall estimated tempo of a song.
13. time_signature: An estimated overall time signature of a song.
14. audio_valence: The musical positiveness conveyed by a song.
15. song_popularity: A score indicating the popularity of the song, which will be the target variable for our prediction model.