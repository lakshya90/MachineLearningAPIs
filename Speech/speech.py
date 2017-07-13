def transcribe_gcs(gcs_uri):
    """Transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech
    speech_client = speech.Client()

    audio_sample = speech_client.sample(
        content=None,
        source_uri=gcs_uri,
        encoding='FLAC',
        sample_rate_hertz=44100)

    
    hint=['Solve For India']
    alternatives = audio_sample.recognize('en-US',speech_contexts=hint)
    for alternative in alternatives:
        print('Transcript: {}'.format(alternative.transcript))

if __name__ == '__main__':
	gcs_uri = "gs://india-devrel-experimental.appspot.com/SolveForIndia/recording.flac"
	transcribe_gcs(gcs_uri)
