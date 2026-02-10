from music21 import converter, instrument, note, chord
from keras.models import Sequential 
from keras.layers import Dense, Dropout, LSTM, Activation
from keras.callbacks import ModelCheckpoint 


midi = converter.parse('input_file.mid')
notes_to_parse = None

# Extract notes/chords from stream ...

# Prepare sequence for the notework 
# (Convert notes to integers, create input/output pairs)

# Create the LSTM network 


model = Sequential() 
model.add(LSTM(512, input_shape=(network_input.shape[1], network_input.shape[2]), return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(512))
model.add(Dense(256))
model.add(Dropout(0.3))
model.add(Dense(n_vocab))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')


# # 4. Train the model
model.fit(network_input, normalized_output, epochs=200, batch_size=128)

'''
  Key Components
---------------------

music21.converter: Parses MIDI files.
music21.instrument: Handles different instruments.
music21.note.Note / chord.Chord: Represents musical elements.
LSTM Layers: Essential for learning sequential, time-dependent data like music.
ModelCheckpoint: Saves the best weights during training. 


'''