from aggiehub.models import Toxic
import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

processing_len = 140
model = load_model("E:\FALL2019\IUI634\Project\detoxit\detoxit_model.h5")
category = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
weights = [0.05, 0.25, 0.2, 0.2, 0.15,0.15]
tknzr = Tokenizer(char_level=False, oov_token=None, num_words=None, split=' ', lower=True, filters='!"#$%&()*+,\t-./:;\n<=>?@[\]^_`{|}~ ', document_count=0)


def predict(str_comment):
	result = dict()
	new_sent = [str_comment]
	new_sent = tknzr.texts_to_sequences(new_sent, maxlen=processing_len, padding='post', truncating='post')
	prediction = model.predict(new_sent)
	for i in range(0,6):
		result.add(i, ('{:.0}'.format(prediction[0][i])))
	return result

def getPredictions(str_comment):
	res = predict(str_comment)
	score = 0.0
	for i in range(0,6):
		score += (res[0][i]) * weights[i]
	return score

def save_to_db(score):
	Toxic.objects.create(id=_id, score=score)
