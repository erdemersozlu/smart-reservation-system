# Smart Restaurant Reservation System 🍽️

A robust Python-based management tool designed to automate restaurant table assignments and booking cancellations.

## 🚀 Overview
This project simulates a real-world reservation desk. It processes incoming requests from a transaction log, checks for table availability based on party size, and dynamically updates the restaurant's occupancy status.

## ✨ Key Features
- **Dynamic Allocation:** Automatically finds the best-fitting table for incoming groups.
- **Transaction Processing:** Handles both `RES` (Reservation) and `CANCEL` (Cancellation) commands in real-time.
- **Error Handling:** Robustly manages scenarios like overbooking, capacity limits, and missing files.
- **Reporting:** Generates a clean, formatted occupancy report after processing all data.

## 🛠️ Technical Skills Demonstrated
- **File I/O:** Reading and parsing structured text data.
- **Data Structures:** Efficient use of Python dictionaries for fast resource tracking.
- **Clean Code:** Adherence to PEP 8 standards with meaningful naming and modular functions.

## 📦 How to Run
1. Ensure you have Python 3.x installed.
2. Place `tables.txt` and `reservations.txt` in the same directory as the script.
3. Run the application:
   ```bash
   python restaurant_manager.py
