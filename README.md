# 🔴🔵 The Pill Color Cluster: K-Means Sorting Engine

An interactive Unsupervised Machine Learning simulation designed to teach **K-Means Clustering**, **Centroid Convergence**, and **Euclidean Distance Metrics** from scratch. You play as a Robotics Automation Engineer in a pharmaceutical recycling facility constructing an optical sorting module that groups unlabeled pill returns into distinct color bins based on Red and Blue RGB spectral telemetry.

## 🎓 Learning Objectives

This project focuses on teaching:
* **Unsupervised Learning:** Grouping multi-dimensional data vectors ($X$) without relying on pre-existing ground-truth target labels ($y$).
* **K-Means Clustering:** Partitioning an unlabeled feature space into $K$ non-overlapping clusters through iterative distance calculations.
* **Centroid Recalculation ($\mu_k$):** Recomputing geometric cluster centers using the arithmetic mean of all assigned vector coordinates.
* **Euclidean Distance Inferences:** Applying standard $L_2$ spatial distance formulas ($\sqrt{\sum (p_i - q_i)^2}$) to assign fresh data points to their nearest cluster.

---

## ✨ Features

* **Pharmaceutical Automation Scenario:** Contextualizes clustering algorithms within a real-world central recycling, triage, and robotic sorting pipeline.
* **Transparent Step-by-Step Execution:** Prints initial centroid assignments, vector distance calculations, and updated cluster means dynamically at runtime.
* **Physical Post-Inference Routing:** Demonstrates how geometric spatial closeness translates directly into automated physical sorting actions (e.g., pneumatic valve deflections).
* **Zero External Dependencies:** Programmed entirely using standard Python loops and the built-in `math` module—no heavy matrix frameworks required.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You only need **Python 3** installed.

### 2. Setup and Execution
1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/pill-color-cluster-kmeans.git](https://github.com/YOUR_USERNAME/pill-color-cluster-kmeans.git)
    cd pill-color-cluster-kmeans
    ```
2.  **Save the Code:** Save the provided script as `pill_cluster.py`.
3.  **Run the Script:**
    ```bash
    python pill_cluster.py
    ```

### 3. Gameplay Instructions
1.  **Inspect Unlabeled Scanner Inputs:** Examine the raw RGB color channel logs from mixed pill returns entering the optical chamber.
2.  **Observe Centroid Initialization ($K = 2$):** Watch the system establish initial seed centroids ($\mu_1, \mu_2$) across the Red and Blue feature dimensions.
3.  **Follow the Convergence Loop:** See the algorithm calculate Euclidean distances for each sample, group the pills, and compute the updated cluster means.
4.  **Route an Unknown Intake Tablet:** Trace an incoming tablet scan ($230.0$ Red, $55.0$ Blue) as the model measures proximity to each centroid and fires the pneumatic deflection arm into the correct bin.

---

## 🧠 Code Structure Highlights

### Euclidean Distance Metric
The distance helper computes the straight-line spatial separation between any two feature coordinates in 2D space.

```python
# Euclidean Distance: sqrt((x2 - x1)^2 + (y2 - y1)^2)
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

