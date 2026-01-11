# 🚀 cli-codeforces-tracker

A **Python-based CLI tool that fetches and displays useful statistics of a Codeforces user** using the official Codeforces API.

Unlike web dashboards, this tool is designed for developers who prefer **terminal workflows, automation, and customization**.


## 📌 Features

* 🔍 Fetches **Codeforces user details**
  * Handle 
  * Avatar URL
  * Rank
  * Current Rating
  * Maximum Rating
  * Contribution score

* ✅ Calculates **total number of problems solved**

* 📊 **Difficulty-wise problem statistics** 

  * Organizes solved problems based on their difficulty levels (A, B, C, D, E, etc.)

  * Shows the total number of problems solved at each level

  * Helps evaluate performance as problem difficulty increases

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

Problems solved by difficulty:
    A: 473
    B: 468
    C: 467
    D: 461
    E: 414
    F: 274
    G: 159
    H: 102
    I: 45
    J: 26
    K: 15
    L: 10
    M: 7
    N: 3
    O: 3
    P: 1
    Q: 2
    R: 2
    S: 1
    T: 1
    U: 1

==========================================================================================
```

---

## 🧠 How It Works

This project works by interacting directly with the **official Codeforces Public API** to fetch user-related data in real time. Below is a step-by-step breakdown of how each part of the script functions internally.

---

### 🔹 1. Program Flow Overview

1. The program starts by printing a decorative header using **pyfiglet**.
2. The user is prompted to enter a **Codeforces handle**.
3. Two API calls are made:
   * One to fetch **user profile information**
   * One to fetch **submission history**
4. The received JSON data is parsed and relevant statistics are displayed in the terminal.



### 🔹 2. Fetching User Information (`get_user_info`)

* API Endpoint Used:

  ```
  https://codeforces.com/api/user.info
  ```

* The handle entered by the user is appended as a query parameter:

  ```python
  url = f"https://codeforces.com/api/user.info?handles={handle}"
  ```

* The API returns a JSON response containing an array of user objects.
* The script extracts the **first object** from `response["result"]` and displays:

  * Handle
  * Avatar URL
  * Rank (if available)
  * Current Rating (or `Unrated`)
  * Maximum Rating
  * Contribution score



### 🔹 3. Fetching Submission Data (`get_user_submissions`)

* API Endpoint Used:

  ```
  https://codeforces.com/api/user.status
  ```

* This endpoint returns **all submissions** made by the user.

* The script iterates over each submission and:

  * Checks if the verdict is **"OK"** (accepted by Codeforces)
  * Extracts the problem’s `contestId`, `index`, and `rating`

* Each solved problem is stored uniquely using:

  ```python
  (contestId, problemIndex)
  ```


### 🔹 4. Difficulty-wise Problem Statistics

* On Codeforces, problems in a contest are labeled by **problem indices** such as:
  * **A, B, C, D, E, F, ...**
* These indices naturally represent increasing difficulty within a contest:
  * **A / B** → Easier problems
  * **C / D** → Medium-level problems
  * **E and above** → Hard problems

* This project uses the **problem index** to categorize difficulty levels.

* For each uniquely solved problem, the script:

  * Extracts the problem `index` (A, B, C, ...)
  * Increments the count for that index

* Internally, a dictionary is used:

  * **Key** → Problem index (A, B, C, D, ...)
  * **Value** → Number of problems solved

* This breakdown helps users:

  * Understand how far they usually solve in contests
  * Identify the hardest level they consistently reach
  * Track improvement across higher problem levels


### 🔹 6. Codeforces API Reference

* For complete and official API documentation, refer to:

  🔗  **Codeforces API Documentation** 
  [https://codeforces.com/apiHelp](https://codeforces.com/apiHelp)

    This page lists:
    * Available API endpoints
    * Request formats
    * Response structures
    * Error codes

---



## 🌟 Future Enhancements

* 🏷️ Tag-based analysis
* 📈 Rating graph visualization
* 💾 Export data to JSON / CSV
* 🌐 Web-based dashboard (Flask / FastAPI)



---

## 📜 License

This project is licensed under the **MIT License**.

---


## 🤝 Contribution

Contributions are welcome!  
Fork the repo, make your changes, and open a pull request.

---


