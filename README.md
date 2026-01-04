# 🚀 cli-codeforces-tracker

A **Python-based CLI tool** that fetches and displays useful statistics of a **Codeforces user** using the official Codeforces API.

---

## 📌 Features

* 🔍 Fetches **Codeforces user details**

  * Handle
  * Avatar URL
  * Rank
  * Current Rating
  * Maximum Rating
  * Contribution score

* ✅ Calculates **total number of unique problems solved**

  * Counts only **Accepted (OK)** submissions
  * Avoids duplicate problems using a set

* 🎨 Stylish ASCII banner using **pyfiglet**

* 💻 Simple **command-line interface**

---

## 🛠️ Tech Stack

* **Python 3**
* **Requests** – for API calls
* **PyFiglet** – for ASCII art banner
* **Codeforces Public API**

---

## 📂 Project Structure

```

codeforces-tracker/
│
├── Src
│    ├──tracker.py        # Main Python script
├── LICENSE
├── README.md             # Project documentation
├── requirements.txt      # Project dependencies

```

---

## 📦 Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/Priyanshu-777/cli-codeforces-tracker.git
cd src
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

**requirements.txt**

```
requests
pyfiglet
```

---

## ▶️ Usage

Run the script using:

```
python tracker.py
```

You will be prompted to enter a Codeforces handle:

```
Enter codeforce handle: tourist
```

### 📤 Sample Output

```
==========================================================================================
  ____          _       __
 / ___|___   __| | ___ / _| ___  _ __ ___ ___  ___ 
| |   / _ \ / _` |/ _ \ |_ / _ \| '__/ __/ _ \/ __|
| |__| (_) | (_| |  __/  _| (_) | | | (_|  __/\__ \
 \____\___/ \__,_|\___|_|  \___/|_|  \___\___||___/

 _____               _
|_   _| __ __ _  ___| | _____ _ __ 
  | || '__/ _` |/ __| |/ / _ \ '__|
  | || | | (_| | (__|   <  __/ |   
  |_||_|  \__,_|\___|_|\_\___|_|   


==========================================================================================

Enter codeforce handle: tourist          

Handle: tourist
Avatar: https://userpic.codeforces.org/422/title/50a270ed4a722867.jpg
Rank: legendary grandmaster
Rating: 3585
Max Rating: 4009
Contribution: 85

Total Problem Solved: 2935

==========================================================================================
```

---

## 🧠 How It Works

### 🔹 User Information

* Uses the endpoint:

  ```
  https://codeforces.com/api/user.info
  ```
* Fetches and prints user profile details

### 🔹 Problem Solving Stats

* Uses the endpoint:

  ```
  https://codeforces.com/api/user.status
  ```
* Iterates over submissions
* Counts **unique accepted problems** using:

  ```python
  (contestId, problemIndex)
  ```

---


## 🌟 Future Enhancements

* 📊 Difficulty-wise problem stats
* 🏷️ Tag-based analysis
* 📈 Rating graph visualization
* 💾 Export data to JSON / CSV
* 🌐 Web-based dashboard (Flask / FastAPI)

---

## 🤝 Contribution

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Author

**Priyanshu Singh**

📍 India

💻 Tech Enthusiast

---


