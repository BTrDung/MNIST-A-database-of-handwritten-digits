from datatrain import train_images, train_labels
from func import model

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_images, train_labels, batch_size=50, validation_split=0.2, epochs=100, verbose=1)

model.save("main.h5")
