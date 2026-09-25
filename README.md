# ENGF0034-2026 Course Materials

This repository contains the official lecture slides and code examples for ENGF0034 in 2026. We manage all materials here so you can easily download them and receive updates throughout the term.

---

### 📥 One-Time Setup: Downloading the Repository

To get a copy of the course materials on your computer, you need to "clone" this repository. You only need to do this once. There are two methods: SSH (recommended) and HTTPS.

---

#### **Option 1: Using SSH (Recommended)**

This method is the industry standard and provides a smoother, password-free experience after a one-time setup.

1.  **First-Time Setup:** If you have not used SSH with GitHub before, you need to generate an SSH key and add it to your GitHub account.
    * **Follow the official GitHub guide:** [**Connecting to GitHub with SSH**](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

2.  **Clone the Repository:** Once your key is set up, run the following command in your terminal:

    ```bash
    git clone git@github.com:UCL-ENGF0034-2026/course-materials.git
    ```

---

#### **Option 2: Using HTTPS (Alternative)**

This method has a slightly simpler initial setup but may ask for your credentials more often.

1.  **First-Time Setup:** You will need a **Personal Access Token (PAT)** to authenticate. A PAT acts as a secure password for GitHub.
    * **Follow the official GitHub guide:** [**Creating a Personal Access Token**](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
    * **Important:** When you generate the token, copy it and save it somewhere safe like a password manager. You will not be able to see it again.

2.  **Clone the Repository:** Run the following command in your terminal. When prompted for a password, **paste your Personal Access Token**, not your GitHub account password.

    ```bash
    git clone [https://github.com/UCL-ENGF0034-2026/course-materials.git](https://github.com/UCL-ENGF0034-2026/course-materials.git)
    ```

---

### 🔄 Staying Up-to-Date: Pulling Changes

We will add new materials throughout the term. To get the latest content, navigate into your `course-materials` folder in the terminal and simply run:

```bash
git pull
```

---

### 💻 Using a Visual Editor (like VS Code)

While using Git in the terminal is a fundamental skill, you can also perform these actions directly from a graphical interface like Visual Studio Code. The underlying concepts are the same.

* **Cloning:** Instead of `git clone`, you can use the "Clone Repository" command from the command palette or the Source Control tab.
* **Pulling:** Instead of `git pull`, you can use the "Sync Changes" button (often a circular arrow icon 🔃) in the bottom status bar to download the latest updates.

For detailed, up-to-date instructions, please refer to the official VS Code documentation:
* [**Using Version Control in VS Code**](https://code.visualstudio.com/docs/editor/versioncontrol)