# spotify-openai
Integration between spotify and openai


Project Statement
Full Stack application that takes in a spotify playlist, trains an OpenAI model based on it, and spits out some result.

# Local Implementation
The only thing missing here is an environment file that contains tokens.

`environment.sh`
```
SPOTIFY_TOKEN="{insert spotify token here}"
OPENAI_TOKEN="{insert openai token here}"
```


# Roadmap
- [ ] Set up git repository
- [ ] Set up development environment
- [ ] Build jupyter notebook to flesh out idea
	- [ ] Connect with Spotify to get playlist information
	- [ ] Fetch playlist information
	- [ ] Grab music information from each song in the playlist
	- [ ] Parse the data in some way
		- [ ] Lyrics
		- [ ] Audio feature analysis
		- [ ] Low level audio analysis 
			- [ ] Segments, beats, etc
		- [ ] .WAV file
	- [ ] Pass the data to a new openai model
	- [ ] Generate information from it
		- [ ] Lyrics
			- [ ] Generate new lyrics
			- [ ] Get sentiment analysis
		- [ ] Audio feature analysis
			- [ ] given another playlist, sort the songs by most similar
		- [ ] Low level audio analysis
			- [ ] Generate new segments
		- [ ] .WAV file
			- [ ] generate a new song
	- [ ] Secondary analysis
		- [ ] Train OpenAI model between low level audio feature analysis to WAV file
		- [ ] Use generated audio analysis segment to generate WAV file
