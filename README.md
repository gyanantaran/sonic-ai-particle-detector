# sonic-ai-particle-detector

Using a self-made AI model to accurately count the number of particles in a container from the audio signal of the collisions inside the container.

## Introduction

This project aims to accurately determine the number of particles in a container by analyzing the audio signal generated from collisions between the particles and the container walls. To accomplish this, an artificial intelligence (AI) model will be developed that is trained on the audio data to recognize different sound patterns corresponding to different numbers of particles. By using the AI model, we hope to accurately count the number of particles in a container and provide a more efficient and reliable method for particle detection.

## Libraries

This project uses several Python libraries for audio processing and visualization:

- `wave`: The wave module is part of Python's standard library and is used to read and write WAV audio files.
- `numpy`: The numpy library is used for numerical computing and provides efficient array operations for processing audio data.
- `pygame`: The pygame library is used for creating interactive applications with multimedia capabilities, including audio playback and visualization.

These libraries are used together to simulate a container of particles, generate audio signals from particle collisions, and visualize the container and particle movement using the pygame library. The numpy library is used for processing the audio signals and extracting features, which are then used to train and test the AI model for particle detection.

## Simulating the Particle Box

The project simulates a container of particles in a box with fixed dimensions. The particle movements are modeled using simple physics principles of momentum and energy conservation. The positions and velocities of the particles are updated at every time step based on the collisions with the walls of the container.

## Generating Audio Signals

The collisions between the particles and the walls of the container generate audio signals. The audio signals are generated by taking the dot product of the velocity of the particle and the normal vector of the wall that it collides with. The resulting audio signals are then processed using the libraries mentioned above to extract features for training and testing the AI model.

## AI Model

The AI model used for particle detection is a convolutional neural network (CNN) which is trained on the audio signals generated from the simulated particle box. The CNN architecture consists of several layers of convolutional and pooling operations followed by fully connected layers. The model is trained using backpropagation and gradient descent optimization to minimize the loss function.

## Validation

The trained model is validated using a test set of audio signals generated from the simulated particle box with different numbers of particles. The model's accuracy is evaluated based on how well it can accurately detect the number of particles in the box from the audio signals. The results are presented in the form of confusion matrix and classification report.

## Experimenting and Contributing

This is a simple physics simulation using the Pygame library in Python. The simulation contains balls moving inside a rectangular window and colliding with each other and the walls.

### Installation
1. Clone the repository:

```
git clone https://github.com/<username>/pygame-physics-simulation.git
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

### Usage

Run the simulation with the following command:
```
python main.py
```


### Controls

- Press `ESC` to exit the simulation.

### Future Improvements

- Add different types of entities (e.g., squares, triangles).
- Implement gravity and friction.
- Add audio effects on collisions.
