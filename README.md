# 🚦 Traffic Control with DQN and SUMO

An intelligent traffic signal control system using Deep Q-Networks (DQN) and SUMO simulation.

## 📌 Overview

This project implements a DQN agent that learns to optimize traffic flow in a simulated urban environment. The system evaluates performance using key metrics like average waiting time, stopped vehicles, and traffic flow.

## 🚀 Features

- 🧠 DQN-based traffic signal control
- 🚗 Realistic traffic simulation with SUMO
- ⚖️ Combined reward system (waiting time + average speed)
- 📊 Performance visualization tools
- 🎮 GUI mode for live simulation viewing
- ⚡ GPU acceleration support

## 📋 Prerequisites

| Requirement       | Installation Guide                     |
|-------------------|----------------------------------------|
| Python 3.7+      | [python.org](https://www.python.org/)  |
| SUMO             | [sumo.dlr.de](https://www.eclipse.org/sumo/) |
| PyTorch          | `pip install torch`                    |
| stable-baselines3| `pip install stable-baselines3`        |
| sumo-rl          | `pip install sumo-rl`                  |

## 🏗️ Project Structure

```plaintext
.
├── train_eval.py       # Training and evaluation script
├── plot.py             # Results visualization
├── models/             # Saved model checkpoints
├── logs/               # TensorBoard logs
├── map.net.xml         # SUMO network file
└── map.rou.xml         # SUMO route definition
