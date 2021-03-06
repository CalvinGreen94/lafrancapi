import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import concatenate
from tensorflow.keras.optimizers import Adam,RMSprop
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import os
# from tf.python.framework import ops
# ops.reset_default_graph()
# from tf.keras import backend as k
os.environ['KERAS_BACKEND' ] = 'tensorflow'
os.environ['MKL_THREADING_LAYER'] = 'GNU'
# from keras.callbacks import TensorBoard
import pandas as pd
import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout
# from tensorflow.keras.layers.normalization import BatchNormalization
# from tensorflow.keras.layers.core import Dropout, Activation
from sklearn.preprocessing import MinMaxScaler
import time
import numpy as np
import random
from collections import deque
class Agent:
	def __init__(self, state_size, is_eval=False, model_name=""):
		self.state_size = state_size # normalized previous days
		self.action_size = 3 # sit, buy, sell
		self.memory = deque(maxlen=1020)
		self.inventory = []
		self.model_name = model_name
		self.is_eval = is_eval
		self.gamma = 0.9
		self.epsilon = .89
		self.epsilon_min = 0.09
		self.epsilon_decay = 0.9999887
		self.model = load_model("models/" + model_name) if is_eval else self._model()

	def _model(self):
		batch_size = 225
		dr = 0.12

		visible = Input(shape=(self.state_size,))
		hidden1 = Dense(5, activation='sigmoid')(visible)
		hidden1 = Dense(5, activation='sigmoid')(hidden1)
		hidden1 = Dense(5, activation='sigmoid')(hidden1)
		hidden1 = Dense(5, activation='sigmoid')(hidden1)
		hidden1 = Dense(5, activation='sigmoid')(hidden1)
		hidden1 = Dense(self.action_size, activation="linear")(hidden1)
		hidden1 = Dropout(dr)(hidden1)

		hidden2 = Dense(self.action_size, activation="linear")(hidden1)
		merge0 = concatenate([hidden1,hidden2],axis=1)
		hidden3 = Dense(5, activation='sigmoid')(merge0)
		hidden3 = Dense(5, activation='sigmoid')(hidden3)
		hidden3 = Dense(5, activation='sigmoid')(hidden3)
		hidden3 = Dense(self.action_size, activation="relu")(hidden3)
		hidden3 = Dropout(dr)(hidden3)

		hidden4 = Dense(self.action_size, activation="relu")(hidden3)
		output =Dense(self.action_size, activation="sigmoid")(hidden4)
		model = Model(inputs=visible, outputs=output)
		model.compile(loss='mse',optimizer='rmsprop')
		return model

	def act(self, state):
		if not self.is_eval and random.random() <= self.epsilon:
			return random.randrange(self.action_size)
		action = self.model.predict(state)
		return np.argmax(action[0])

	def expReplay(self, batch_size):
		mini_batch = []
		l = len(self.memory)
		for i in range(l - batch_size + 1, l):
			mini_batch.append(self.memory[i])
		for state, action, reward, next_state, done in mini_batch:
			target = reward
			if not done:
				target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])

			target_f = self.model.predict(state)
			target_f[0][action] = target
			self.model.fit(state, target_f, epochs=1, verbose=0,shuffle=False)

		if self.epsilon > self.epsilon_min:
			self.epsilon *= self.epsilon_decay
