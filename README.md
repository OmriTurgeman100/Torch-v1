# Torch: A Customizable Micro-Monitoring System

**Torch** is a micro-monitoring system that enables users to create custom hierarchies and define rules for each layer. It utilizes multiprocessing in the backend for efficient performance. With Torch, users can structure their monitoring framework as needed and define specific actions or conditions at every level.

---

## Key Features

- **Custom Monitoring Hierarchies**: Design monitoring structures that suit your needs.
- **Rule-Based Management**: Define rules and conditions for nodes and parent entities, enabling dynamic status updates.
- **Efficient Backend**: Multiprocessing ensures fast and scalable performance.
- **Script Integration**: Submit results from custom black-box scripts to Torch's API to create reports and build hierarchies.
- **Web-Based Interface**: Easily manage nodes, configure rules, and visualize monitoring paths.

---

## How It Works

### Step 1: Generate Reports from Custom Scripts
Users start by creating custom scripts and sending results to Torch's API to generate a report. This forms the basis for monitoring hierarchies.

![Step 1](https://github.com/user-attachments/assets/1ecc19fa-248e-4dcb-980c-c6c3f9a913ae)

### Step 2: Build the Monitoring Hierarchy
Select the generated reports and use them to create a hierarchical structure. Nodes represent the building blocks of the hierarchy.

![Hierarchy Selection](https://github.com/user-attachments/assets/91cece15-def2-4b29-8911-0d3e3b180077)

### Step 3: Define Rules and Conditions
At each level of the hierarchy, define custom rules and conditions. These determine how the parent entities react when conditions are met.

#### Example Rules for Nodes:
![Node Rules](https://github.com/user-attachments/assets/39456823-49f9-4de3-a44c-ac634bfb35c7)

#### Example Rules for Parent Entities:
![Parent Rules](https://github.com/user-attachments/assets/f6539403-9758-4de3-adcc-12f4a734e46d)

When conditions are triggered, parent entities update their status dynamically based on the rules. Visual indicators (e.g., color changes) reflect these updates.

![Dynamic Updates](https://github.com/user-attachments/assets/e3de6e42-fc89-4af5-8209-0df94efcc95a)

### Step 4: Monitor Real-Time Status
Torch provides a clear view of the monitoring path, with statuses propagated throughout the hierarchy based on conditions.

![Report Example](https://github.com/user-attachments/assets/16d34ee6-3c96-42de-a12f-3b48aa94738a)

---

Torch is designed to maximize performance by utilizing native SQL for all database interactions. By bypassing Object-Relational Mappers (ORMs), it eliminates the additional abstraction layers and overhead that can slow down query execution. This approach ensures precise control over database operations, allowing for faster, more efficient data handling and greater flexibility in optimizing queries to suit specific performance needs.

![Desktop Screenshot 2024 11 28 - 02 57 52 52](https://github.com/user-attachments/assets/aae59a75-ebd4-499e-b766-15fb7c7426d5)

![Desktop Screenshot 2024 11 28 - 03 04 05 83](https://github.com/user-attachments/assets/8c0a6316-430f-4b96-b654-d9c498f19f31)

![Desktop Screenshot 2024 11 28 - 03 04 28 40](https://github.com/user-attachments/assets/4d099755-8cf2-4110-9304-05364467663f)

![Desktop Screenshot 2024 11 28 - 03 05 56 50](https://github.com/user-attachments/assets/cccaaa30-246f-43ba-a91e-512062b06ffc)

![Desktop Screenshot 2024 11 28 - 03 06 09 30](https://github.com/user-attachments/assets/70326a52-1ec8-480e-b2b9-d397c647ddd1)

---

## System Requirements

Torch requires the following dependencies:
- **Python**
- **Node.js**

### Starting the Application
To launch the web-based interface, run the following script:

![Desktop Screenshot 2024 11 28 - 02 28 47 78](https://github.com/user-attachments/assets/297d6cf4-18dc-44cf-b4d8-8bdf938385c1)

```bash
python run.py
