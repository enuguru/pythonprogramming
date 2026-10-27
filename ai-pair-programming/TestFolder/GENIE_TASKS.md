# Genie Task Pack for This Repository

A curated, incremental set of programming tasks you can attempt with Genie (AI pair programmer). Each task includes ideas and prompt starters. Many tasks reference files that already exist here so you can iterate quickly.

Tip: When you open a task, show Genie the target file path and paste any relevant snippet or error. Ask for small, testable steps.

---

## How to Use
- Starter prompt: "Genie, help me with [Task #]. We’re working in C:\Users\karth\pythonprogramming\ai-pair-programming\TestFolder."
- Be specific about goals, constraints, and what success looks like.
- Prefer iterative cycles: ask Genie to propose, you review, then refine.

---

## Very Easy (Warm‑ups)
1. Print Hello Variations (helloworld.py)
   - Goal: Add a function greet(name) that returns a greeting. Add a __main__ block to accept a name from input.
   - Prompt: "Add greet(name) to helloworld.py and a main to read input. Write minimal docstrings."

2. Fibonacci Refactor (new file)
   - Goal: Write iterative and recursive Fibonacci with input validation and basic timing.
   - Prompt: "Create fibonacci_utils.py with fib_iter(n), fib_rec(n), and simple benchmarking in __main__."

3. Perfect Number Checker (perfect.py)
   - Goal: Add a function is_perfect(n) and a simple CLI to test a list of numbers from argv.
   - Prompt: "Extend perfect.py with is_perfect(n) and CLI that prints results for numbers passed as args."

4. Prime Range (primes.py or prime-number-program.py)
   - Goal: Add a function primes_in_range(a, b) returning a list. Include basic doctests.
   - Prompt: "Refactor primes.py to expose primes_in_range(a,b) with doctests and a main."

5. Armstrong Numbers (armstrong_numbers.py)
   - Goal: Add unit tests inline (doctest or simple asserts in __main__).
   - Prompt: "Add doctests to armstrong_numbers.py and run them in __main__."

---

## Beginner
6. Look-and-Say Sequence (experiment.py)
   - Goal: Turn print-only script into reusable module: function next_term(s) and generator sequence(n_terms).
   - Prompt: "Refactor experiment.py: expose next_term(s) and a generator. Keep existing output under __main__."

7. Remove Duplicates CLI (remove_duplicates.py, duplicate_lines.txt)
   - Goal: Extend script to accept an input file and optional output path; preserve order; write summary stats.
   - Prompt: "Turn remove_duplicates.py into a CLI with argparse: input path, output path (optional), and stats."

8. CSV Quick Stats (students_bar_chart.csv)
   - Goal: Write a small script to compute min/avg/max score per subject and print a neat table.
   - Prompt: "Create students_stats.py that reads students_bar_chart.csv and prints min/avg/max per subject."

9. Type Hints and Docstrings
   - Goal: Add type hints and Google-style docstrings to 3 small modules (choose: primes.py, perfect.py, armstrong_numbers.py).
   - Prompt: "Add type hints and Google docstrings; ensure mypy-friendly signatures."

10. Basic Logging
   - Goal: Add logging to two scripts using logging module with INFO and ERROR levels (no prints).
   - Prompt: "Replace prints with logging in X.py and Y.py, add a basicConfig, and keep messages informative."

---

## Intermediate (Data & Visualization)
11. Recreate a Bar Chart (students_bar_chart.py)
   - Goal: Change styles, add value labels, improve colors, and save as students_bar_chart_v2.png.
   - Prompt: "Update students_bar_chart.py with clear style, value labels, and save as *_v2.png."

12. CSV Plot Enhancements (read_and_plot_csv_example.py)
   - Goal: Add CLI options for which columns to plot and output filename.
   - Prompt: "Add argparse to select x/y columns and save path; validate columns and handle errors gracefully."

13. Exploratory Data Analysis (movies.csv)
   - Goal: Compute descriptive stats, top-10 by rating/count, and histogram plots.
   - Prompt: "Create movies_eda.py: read movies.csv, compute stats, and save histograms."

14. Mall Customers KMeans (mall_kmeans_clustering.py, Mall_Customers_Clustered.csv)
   - Goal: Make k configurable; save inertia and silhouette; write results to CSV.
   - Prompt: "Enhance mall_kmeans_clustering.py: argparse for k, output metrics, and write labeled CSV."

15. Plot Suite Consistency (mall_plots.py)
   - Goal: Ensure all saved plots share consistent styling, titles, legends, and file naming.
   - Prompt: "Standardize plot styles across mall_* plots and ensure files are saved to disk with clear names."

---

## Intermediate (Algorithms & Design)
16. Sieve of Eratosthenes (new file)
   - Goal: Implement sieve(n) returning primes up to n with unit tests.
   - Prompt: "Create sieve.py with sieve(n) and a small pytest-style test function."

17. Memoization Decorator (new file)
   - Goal: Implement a simple memoize decorator and apply to recursive Fibonacci.
   - Prompt: "Create decorators.py with memoize; apply to fib_rec; include timing comparison."

18. CLI Utilities Package
   - Goal: Factor repeated CLI patterns into a small utils module (arg parsing, file IO helpers).
   - Prompt: "Create cli_utils.py to share parse_args and safe_read/write utilities. Refactor two scripts to use it."

19. Error Handling Patterns
   - Goal: Add robust try/except, custom exceptions, and user-friendly messages to two scripts that read files.
   - Prompt: "Introduce custom exceptions and centralized error handling for file-reading scripts."

20. Configuration File Support
   - Goal: Allow a script to read default settings from a JSON or YAML config.
   - Prompt: "Add config loading to X.py with CLI override precedence (CLI > config > defaults)."

---

## Testing & Quality
21. Pytest on Clustering (test_mall_kmeans_clustering.py)
   - Goal: Flesh out tests to check that labels length equals rows and inertia is positive.
   - Prompt: "Expand test_mall_kmeans_clustering.py with cases for label count, dtype, and inertia > 0."

22. Plot File Existence (test_mall_kmeans_plots.py)
   - Goal: Ensure plotting functions save files and do not raise exceptions.
   - Prompt: "Add tests that call plotting with a tmpdir and assert files exist."

23. Pre-Commit Style Checks
   - Goal: Add black/ruff configs (even if not installed yet) and reformat 3 files.
   - Prompt: "Create pyproject.toml with black & ruff settings; reformat primes.py, perfect.py, armstrong_numbers.py."

24. Doctest Coverage
   - Goal: Add doctests to small pure functions and run them via python -m doctest -v.
   - Prompt: "Add doctests for is_perfect, is_armstrong, and primes_in_range; show example I/O."

25. CI Thought Exercise
   - Goal: Draft a GitHub Actions YAML (no need to activate here) to run pytest and flake8.
   - Prompt: "Create .github/workflows/python-ci.yml that sets up Python, installs deps, and runs tests/linters."

---

## Debugging & Refactoring
26. Fix Off-by-One in Look-and-Say (experiment.py)
   - Goal: Add tests for look_and_say edge cases: empty string, single char, repeated digits.
   - Prompt: "Write unit tests for look_and_say and handle empty input explicitly; keep behavior consistent."

27. Improve primes.py Design
   - Goal: Separate I/O from computation; expose is_prime(n) and primes_in_range.
   - Prompt: "Refactor primes.py to pure functions and a main guard. Add simple tests."

28. Simplify Data Visualization Scripts
   - Goal: Extract a function make_scatter(df, x, y, hue, out) for reuse across scripts.
   - Prompt: "Create viz_utils.py with make_scatter and refactor two plot scripts to call it."

29. Defensive CLI Parsing
   - Goal: Use argparse with good error messages and --help examples in at least 2 scripts.
   - Prompt: "Replace manual sys.argv parsing with argparse and add examples to help epilog."

30. Logging + Exceptions
   - Goal: Replace bare except with explicit exception types and log.tracebacks where appropriate.
   - Prompt: "Audit files for bare except; replace with specific exceptions and logging.exception in failure paths."

---

## Data Science Focus
31. Elbow & Silhouette (kmeans_clustering_example.py)
   - Goal: Parameterize range of k, return best k by silhouette, and save plots.
   - Prompt: "Add function choose_best_k(X, k_range) returning best_k and metrics; save elbow/silhouette plots."

32. Gender-based Segmentation (mall_silhouette_gender_plot.py)
   - Goal: Ensure grouping by gender works; add separate plots per gender subgroup.
   - Prompt: "Refactor to produce and save silhouette plots per gender; ensure file names are descriptive."

33. Train/Test Split for Linear Regression (linear_regression_example.py)
   - Goal: Add a function that returns R^2 on holdout data; report coefficients.
   - Prompt: "Add train_test_evaluate(df) with R^2 and coefficient output; handle missing values."

34. Readme-style Report (new file)
   - Goal: Autogenerate a short .md report summarizing dataset stats and plots produced.
   - Prompt: "Create report_generator.py that scans outputs and writes REPORT.md with links and brief commentary."

35. Robust CSV Reader (data_analysis_example.py)
   - Goal: Add delimiter detection and encoding fallback; log warnings for malformed rows.
   - Prompt: "Enhance CSV loading with sniffer and encodings ['utf-8', 'latin-1'] and row-level error handling."

---

## Performance & Reliability
36. Time Critical Sections
   - Goal: Add a tiny profiling helper to measure sections in kmeans scripts.
   - Prompt: "Create timing.py with context manager timer(name); instrument kmeans code and print timings."

37. Caching
   - Goal: Cache intermediate CSV transformations to avoid recomputation.
   - Prompt: "Add a simple cache layer that saves transformed DataFrame to a feather/parquet if present."

38. Large File Streaming
   - Goal: Modify a CSV reader to iterate in chunks and compute stats incrementally.
   - Prompt: "Refactor data_analysis_example.py to process CSV in chunks with pandas.read_csv(..., chunksize=...)."

39. Robust File Paths
   - Goal: Replace hard-coded relative paths with Pathlib and configurable output directory.
   - Prompt: "Use pathlib.Path for all file paths and add --outdir CLI param with default './outputs'."

40. Retry and Backoff (if downloading data)
   - Goal: Add retry logic around any external requests with exponential backoff.
   - Prompt: "Wrap requests.get calls (if present) with retry/backoff; isolate in a util function."

---

## Stretch Projects
41. Package This Repo (thought exercise)
   - Goal: Turn utilities into a tiny package (no publish); add __init__.py and setup metadata.
   - Prompt: "Propose a simple package layout and create minimal __init__.py files."

42. CLI Tool: stats
   - Goal: Build a unified CLI (python -m stats) that exposes CSV stats and plotting subcommands.
   - Prompt: "Create stats/__main__.py with subparsers: describe, plot, cluster."

43. Notebook Conversion
   - Goal: Create a Jupyter notebook that runs a subset of plotting and EDA tasks.
   - Prompt: "Generate a notebook eda.ipynb that loads movies.csv and produces 2–3 plots."

44. Synthetic Data Generator (synthetic_data.csv)
   - Goal: Produce a script to generate and save synthetic customer data for clustering demos.
   - Prompt: "Create generate_synthetic.py parameterized by n_samples and feature ranges; write CSV."

45. Minimal Web App (Streamlit)
   - Goal: Build a simple Streamlit app to upload CSV and visualize scatter/histograms.
   - Prompt: "Create app.py using streamlit: upload CSV, select columns, and render plots."

---

## Prompt Templates You Can Reuse
- Refactor: "Genie, refactor <file> to extract pure functions, add type hints, and keep backward-compatible CLI."
- Test: "Genie, write pytest tests for <function> covering edge cases and typical cases."
- Plot: "Genie, standardize plotting styles across these scripts and save to a specified outdir."
- Debug: "Genie, this function fails on <input>. Here’s the traceback: <paste>. Help me fix with tests first."
- Performance: "Genie, profile this script and propose 2 optimizations measured with before/after timings."
- Documentation: "Genie, write a clear docstring and usage examples for <function> and add doctests."

---

## Getting Started Now
Try Tasks 6, 11, and 21 together:
- 6: Make experiment.py reusable.
- 11: Improve students_bar_chart.py visuals and save students_bar_chart_v2.png.
- 21: Add a small pytest test to validate clustering outputs.

If you want a random pick: "Genie, pick a random task number from 1–45 and guide me through it step by step."