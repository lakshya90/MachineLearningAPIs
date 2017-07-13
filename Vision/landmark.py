
from google.cloud import vision

def detect_landmarks_uri(uri):
    """Detects landmarks in the file located in Google Cloud Storage or on the
    Web."""
    vision_client = vision.Client()
    image = vision_client.image(source_uri=uri)

    landmarks = image.detect_landmarks()
    print('Landmarks:')

    for landmark in landmarks:
	print('Landmark mID: {0}'.format(landmark.mid))
	print ('Landmark Description: {0}'.format(landmark.description))
	print ('Landmark score :{0}'.format(landmark.score))
	print ('Landmark Latitude :{0}'.format(landmark.locations[0].latitude))
	print ('Landmark Longitude :{0}'.format(landmark.locations[0].longitude))

if __name__ == '__main__':
    uri = "gs://india-devrel-experimental.appspot.com/SolveForIndia/charminar.jpg"
    detect_landmarks_uri(uri)
