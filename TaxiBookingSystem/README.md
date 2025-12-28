# 🚕 Taxi Booking System — Python Backend Project

A mini system design and console-based backend project inspired by real-world ride-hailing platforms like Uber/Ola.

## 🏗 System Design Overview

User App → TaxiBookingSystem → Driver/Trip DB → Output

## ✨ Features
- Register users and drivers
- Store driver real-time location (x, y coordinates)
- Find the nearest available driver based on distance
- Start & complete rides
- Generate fare based on distance
- Maintain trip history

## 🧠 System Design Highlights
- Clean OOP architecture (User, Driver, Trip service separation)
- Prevents double booking using driver availability flag
- Extendable for scalable design (Redis Geo, SQS, DynamoDB integration)
- Console-based execution for fresher coding rounds

## 🧮 Tech Stack
| Component | Tech |
|----------|------|
| Language | Python |
| Architecture | Console-based + OOP |
| Future scaling | Redis, DynamoDB, FastAPI |

## 📌 How to Run
```bash
python3 main.py
