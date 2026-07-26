import math

def kmeans_pill_cluster_game():
    # 1. Scenario: Pharmaceutical Recycling & Unsupervised Sorting Automation
    print("--- 🔴🔵 THE PILL COLOR CLUSTER: K-MEANS SORTING ENGINE 🔴🔵 ---")
    print("Mission: Group unlabeled pill returns into distinct color clusters.")
    print("Goal: Compute Centroids using Euclidean distance to route unknown tablets.")

    # 2. Unlabeled Feature Data Matrix (No Target Labels Provided)
    # Features: [Red Channel Intensity (0-255), Blue Channel Intensity (0-255)]
    unlabeled_pills = [
        {"id": "Pill A", "features": [240.0, 50.0]},  # Predominantly Red
        {"id": "Pill B", "features": [220.0, 60.0]},  # Predominantly Red
        {"id": "Pill C", "features": [40.0,  210.0]}, # Predominantly Blue
        {"id": "Pill D", "features": [50.0,  230.0]}, # Predominantly Blue
    ]

    print("\n--- 🖥️ UNLABELED OPTICAL SCANNER INPUT LOGS ---")
    for pill in unlabeled_pills:
        print(f"{pill['id']}: Red Intensity = {pill['features'][0]} | Blue Intensity = {pill['features'][1]}")

    # 3. Helper Function: Calculate 2D Euclidean Distance
    def euclidean_distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    # 4. Step 1: Initialize Centroids (K = 2)
    # For demonstration, we pick Pill A as Centroid 1 and Pill C as Centroid 2
    c1 = unlabeled_pills[0]["features"] # [240.0, 50.0]
    c2 = unlabeled_pills[2]["features"] # [40.0, 210.0]

    print("\n--- 📊 STEP 1: CENTROID INITIALIZATION (K = 2) ---")
    print(f"Initial Centroid 1 (Cluster 1 - Red Bin) : Red={c1[0]}, Blue={c1[1]}")
    print(f"Initial Centroid 2 (Cluster 2 - Blue Bin): Red={c2[0]}, Blue={c2[1]}")

    # 5. Step 2: Assign Training Points to Nearest Centroids
    cluster_1 = []
    cluster_2 = []

    for pill in unlabeled_pills:
        dist_c1 = euclidean_distance(pill["features"], c1)
        dist_c2 = euclidean_distance(pill["features"], c2)
        
        if dist_c1 < dist_c2:
            cluster_1.append(pill)
        else:
            cluster_2.append(pill)

    # 6. Step 3: Recalculate Centroids (Mean of Assigned Vectors)
    new_c1_x = sum(p["features"][0] for p in cluster_1) / len(cluster_1)
    new_c1_y = sum(p["features"][1] for p in cluster_1) / len(cluster_1)
    new_c1 = [new_c1_x, new_c1_y]

    new_c2_x = sum(p["features"][0] for p in cluster_2) / len(cluster_2)
    new_c2_y = sum(p["features"][1] for p in cluster_2) / len(cluster_2)
    new_c2 = [new_c2_x, new_c2_y]

    print("\n--- 🔄 STEP 2: RECOMPUTING CONVERGED CENTROIDS ---")
    print(f"Updated Centroid 1 Mean: Red={new_c1[0]:.1f}, Blue={new_c1[1]:.1f}")
    print(f"Updated Centroid 2 Mean: Red={new_c2[0]:.1f}, Blue={new_c2[1]:.1f}")

    # 7. Incoming Unknown Pill Telemetry
    # A fresh unknown tablet passes under the RGB camera: Red=230.0, Blue=55.0
    test_pill_x = [230.0, 55.0]
    print(f"\n--- 🚨 AUTOMATION INTAKE: SCANNING UNKNOWN TABLET ---")
    print(f"RGB Camera Telemetry -> Red Channel: {test_pill_x[0]} | Blue Channel: {test_pill_x[1]}")

    # 8. Inference: Calculate Distance to Final Centroids
    dist_to_c1 = euclidean_distance(test_pill_x, new_c1)
    dist_to_c2 = euclidean_distance(test_pill_x, new_c2)

    print(f"\nEuclidean Distance to Centroid 1 (Red Bin) : {dist_to_c1:.2f} units")
    print(f"Euclidean Distance to Centroid 2 (Blue Bin): {dist_to_c2:.2f} units")

    if dist_to_c1 < dist_to_c2:
        assigned_cluster = 1
        verdict = "🔴 ROUTED TO RED BIN (Cluster 1)"
    else:
        assigned_cluster = 2
        verdict = "🔵 ROUTED TO BLUE BIN (Cluster 2)"

    print(f"\nAutomated Sorting Action: {verdict}")

    # 9. Ground Truth Verification
    actual_bin = 1
    if assigned_cluster == actual_bin:
        print("\n🏆 SUCCESS: K-Means accurately mapped the pill to its correct optical cluster!")
        print("The automated sorting arm pneumatic valve deflected the tablet safely into the Red Bin.")
    else:
        print("\n💥 SORTING FAULT: Optical misalignment! Tablet deflected into the wrong recycling container.")

if __name__ == "__main__":
    kmeans_pill_cluster_game()
