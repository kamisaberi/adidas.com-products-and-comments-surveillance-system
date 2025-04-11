
# Adidas.com Products and Comments Surveillance System

**Adidas.com Products and Comments Surveillance System** is a Python-based tool designed to monitor and analyze products and user comments on adidas.com. It automates the process of tracking new product listings and user feedback, providing timely insights for market analysis and customer sentiment.

---

## 🚀 Features

- **Automated Product Tracking** – Continuously monitors adidas.com for new product listings and updates.
- **User Comment Analysis** – Collects and analyzes user comments to gauge customer sentiment.
- **Data Logging** – Maintains logs of retrieved data for auditing and further analysis.
- **Customizable Preferences** – Allows users to set preferences for monitoring specific product categories or regions.

---

## 🛠️ Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/kamisaberi/adidas.com-products-and-comments-surveillance-system.git
```

2. **Navigate to the Project Directory:**

```bash
cd adidas.com-products-and-comments-surveillance-system
```

3. **Install Required Dependencies:**

```bash
pip install -r req.txt
```

---

## ⚙️ Usage

1. **Set Preferences:**

Configure your monitoring preferences in the `prefs` directory. This includes specifying product categories, regions, and other parameters.

2. **Run the Main Script:**

```bash
python main.py
```

3. **Monitor Logs:**

Logs are stored in the `logs` directory. Regularly check this directory to review the system's activity and any potential issues.

---

## 🐞 Known Issues

- **Item Tracking** – Newly added items require manual updates to the `AdidasThread.Globals.gotten_items_list`.
- **Error Handling in Threads** – When threads fail, a rollback or retry mechanism is still needed.
- **Preference Retrieval** – `retrieve_preferences` should iterate through project IDs until a known product is matched.
- **Thread Conflict Prevention** – `check_preferences` should notify `main.py` to pause launching new `get_items` threads when one is in progress.

---

## 🗂️ Project Structure

```
adidas.com-products-and-comments-surveillance-system/
├── .idea/                  # IDE-specific settings
├── crap/                   # Miscellaneous files
├── files/                  # Retrieved raw files
├── in/                     # Input data
├── logs/                   # Activity logs
├── out/                    # Output and parsed data
├── prefs/                  # User-defined monitoring preferences
├── threads/                # Multithreaded scraping modules
├── .gitignore              # Ignored files
├── README.md               # Project documentation
├── req.txt                 # Python dependencies
└── main.py                 # Main executable
```

## bugs :
- anytime we find new items that added to store we should update `AdidasThread.Globals.gotten_items_list` items 
- (`IMPORTANT`) should find another way to check which items downloaded
- *****(`IMPORTANT`)(`SOLUTION`) at retrieve_preferences thread I should traverse items project_id until we reach first item that we have inside model_product_objects
  - first I should check , I need to get new reminder or not  ??????
- `IMPORTANT` create a mechanism  that while threads that  getting items gets an error, they could revert their procedure or we should surveillance gotten data after a scheduled time BUG-#10 
- `ACCEPTED`(IMPORTANT) when check_preferences found uot new items has been added to the store it should create a flag for main.py to prevent it to create new get_items thread and after all get_items thread finished it can update the data eg items_info and ...
  `REJECTED`(OR)(IMPORTANT) when check_preferences found uot new items has been added to the store it should create a flag for get_items threads to should not update items_info and items until update proccess finished . the main problem is that we should change all items_start properies of all running threads so they update items_info an items correctly  
- `IMPORTANT`(`SOLVED`) I should remove next_start_index and solve it using trace items_info and get the next order value
- `IMPORTANT`(`SOLVED`) I should reorder items_info after any time thread retrieve items
- `IMPORTANT` I should create thread to check items based on top-sellers to find out which one has new review
- `IMPORTANT` I should modify ItemInfo class states to keep items total reviews and keep how many of them downloaded

## Changes : 
- `AdidasThread.Globals.gotten_items_list` changed to `AdidasThread.Globals.assigned_items_indices`

## Fixed
- (FIXED) we should store `AdidasThread.Globals.gotten_items_list` anytime we want to finish a job or at scheduled time 
- (FIXED)should move variables from `Settings` class to `Globals` class



---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request if you find a bug or want to propose an improvement.

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 📬 Contact

For questions, suggestions, or collaborations, feel free to reach out through the [GitHub repository](https://github.com/kamisaberi/adidas.com-products-and-comments-surveillance-system).
