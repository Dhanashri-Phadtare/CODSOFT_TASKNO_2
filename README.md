# 🎮 Tic-Tac-Toe AI

A Python-based Tic-Tac-Toe game where a human player competes against an
AI opponent powered by the **Minimax algorithm**.

This project demonstrates fundamental Artificial Intelligence concepts such
as game-state evaluation, recursion, decision-making, and backtracking.

---

## 📌 Project Overview

This application allows a human player to play Tic-Tac-Toe against an
AI-controlled opponent.

- **Human Player:** X
- **AI Player:** O
- **AI Algorithm:** Minimax
- **Interface:** Command Line

The AI evaluates possible future moves and selects the move that provides
the best possible outcome.

---

## ✨ Features

-  Human vs AI gameplay
-  AI opponent using the Minimax algorithm
-  Game-state evaluation
-  Recursive decision-making
-  Backtracking
-  Winner detection
-  Draw detection
-  Input validation
-  Prevents selection of occupied positions
-  Handles invalid user input
-  Simple command-line interface

---

## 🧠 How the AI Works

The AI uses the **Minimax algorithm** to determine the best possible move.

The algorithm explores different possible future game states and assigns a
score to each outcome.

### Scoring System

| Result | Score |
|---|---:|
| AI Wins | `+1` |
| Draw | `0` |
| Human Wins | `-1` |

The AI attempts to **maximize** its score, while the human player's turn
is treated as the **minimizing** stage.

### Minimax Process

```text
                 Current Board
                      ↓
              Find Available Moves
                      ↓
              Simulate Each Move
                      ↓
              Explore Future States
                      ↓
                 Evaluate Result
                      ↓
                  Assign Score
                      ↓
               Choose Best Move
