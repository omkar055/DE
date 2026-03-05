Your Mac
│
├─ Browser / VSCode
│
└─ GitHub Codespaces (Remote Linux VM)
      │
      ├─ Python
      ├─ pip
      ├─ uv  ← installed here
      └─ your project (/workspaces/DE)

create virtual environment (different from virtual machines and docker containers) to isolate packages and avoid dependency conflicts

    uv init --python 3.13 to initialize project for the first time

    