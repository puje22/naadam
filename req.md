naadam-wrestling-analysis/
│
├── data/
│   ├── raw/                # scraped HTML or JSON from devjee.mn
│   ├── processed/          # cleaned match results
│   └── wrestlers.csv       # master wrestler table
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_title_progression.ipynb
│   ├── 03_simulation_engine.ipynb
│   ├── 04_monte_carlo.ipynb
│   └── 05_visualizations.ipynb
│
├── src/
│   ├── scraper.py          # pulls match results from devjee.mn
│   ├── parser.py           # extracts round-by-round results
│   ├── wrestler.py         # Wrestler class (rank, title, age)
│   ├── titles.py           # title progression logic
│   ├── tournament.py       # bracket generation + match simulation
│   ├── probability.py      # win probability model (rank + title + age)
│   └── simulate.py         # Monte Carlo simulation
│
├── app/
│   └── streamlit_app.py    # optional interactive app
│
├── README.md               # project explanation
└── requirements.txt