Village Boys – Azerbaijan
====

This repository presents the **Village Boys Team**'s self-driving car — **Hoqqa**, developed and programmed by our team from Azerbaijan for the **World Robot Olympiad™ 2025 – Future Engineers Category (Self-Driving Cars)**, under the theme *The Future of Robots*. Here, you'll find comprehensive details about our robot’s design, architecture, and features — a result of our team's commitment to pushing the boundaries of autonomous technologies and innovative robotics.

## List of Dictionaries

* [`List-of-Materials`](https://github.com/AlibaliAlibayov/WRO2025-FE-VillageBoys/tree/main/List-of-Materials) contains the list of all the materials necessary to build the robot.
* [`Team-Photos`](https://github.com/AlibaliAlibayov/WRO2025-FE-VillageBoys/tree/main/Team-Photos) contains multiple photos of the whole team.
* [`Vehicle-Models`](https://github.com/AlibaliAlibayov/WRO2025-FE-VillageBoys/tree/main/Vehicle-Models) contains multiple 3D models of the vehicle's view.
* [`Vehicle-Photos`](https://github.com/AlibaliAlibayov/WRO2025-FE-VillageBoys/tree/main/Vehicle-Photos) contains multiple photos of the vehicle.
* [`Vehicle-Schemes`](https://github.com/AlibaliAlibayov/WRO2025-FE-VillageBoys/tree/main/Vehicle-Schemes) contains the wiring diagrams of the whole robot including all of its components.
* [`src`](https://github.com/AlibaliAlibayov/WRO2025-FE-VillageBoys/tree/main/src) contains the main and other programs of the robot.
* [`videos`](https://github.com/AlibaliAlibayov/WRO2025-FE-VillageBoys/tree/main/src) contains 2 video links showcasing each challenge round.
  
## Content

- [1. Introduction](#1-introduction)
- [2. The Team](#2-the-team)
  - [2.1 🧠 Our autonomous car's logic](#21-our-autonomous-cars-logic)
  - [2.2 💡 Flow Diagram](#22-flow-diagram)
  - [2.3 🖥️ Why Python?](#23-why-python)
  - [2.4 🎯 Why ROS?](#24-why-ros)
- [3. ⚙️ Mobility Management](#3-mobility-management)
  - [3.1 🧱 Bill of Materials (BOM)](#31-bill-of-materials-bom)
  - [3.2 🔌 Wiring Diagram](#32-wiring-diagram)
  - [3.3 🧰 Reasons for Using Our Motors](#33-reasons-for-using-our-motors)
  - [3.4 ⚙️ Motors Axle System](#34-motors-axle-system)
  - [3.5 ⚙️ Ackermann Steering System](#35-ackermann-steering-system)
    - [3.5.1 How does the System Works](#351-how-does-the-system-works)
    - [3.5.2 Enhanced Precision](352-enhanced-precision)
- [4. 🔋 Power and Sense Management](#4-power-and-sense-management)
  - [4.1 🔌 Power Distribution Diagram](#41-power-distribution-diagram)
  - [4.2 ⚡ Power Source](#42-power-source)
    - [4.2.1 Charger](#421-charger)
  - [4.3 📷 Reasons for Using Our Sensors and Camera](#43-reasons-for-using-our-sensors-and-camera)
    - [4.3.1 STL-19P TOF Lidar](#431-stl-19p-tof-lidar)
    - [4.3.2 Monocular Camera](#432-monocular-camera)
- [5. 🏎️ Building the Robot](#5-building-the-robot)
  - [5.1 🖨️ Designing, Printing, and Ensembling](#51-designing-printing-and-ensembling)
    - [5.1.1 3D Printing Process](#511-3d-printing-process)
    - [5.1.2 The Systems](#512-the-systems)
    - [5.1.3 Camera Housing](#513-camera-housing)
    - [5.1.4 Chassis](#514-chassis)
  - [5.2 📍 Code for the Camera](#52-code-for-the-camera)
- [6. 🛠️ Assembly Instructions](#6-assembly-instructions)
- [7. 📌 Principal Strategy](#7-principal-strategy)
  - [7.1 🔒 Open challenge](#71-open-challenge)
    - [7.1.1 PID Controller](#711-pid-controller)
    - [7.1.2 Configuring](#712-configuring)
    - [7.1.3 Pseudo Code](#713-pseudo-code)
  - [7.2 🔒 Obstacle Challenge](#72-obstacle-challenge)
    - [7.2.1 "Follow the Gap"](#721-follow-the-gap)
    - [7.2.2 Configuring](#722-configuring)
    - [7.2.3 Pseudo Code](#723-pseudo-code)
  - [7.3 🔒 Parking Strategy](#73-parking-strategy)


## 1. Introduction


 This engineering documentation offers a comprehensive overview of the **Village Boys Team's** self-driving robot, developed and programmed by our team from the Philippines for the **Future Engineers Category at the WRO Azerbaijan 2025 Local Finals**. Within this document, you'll find insights into the robot’s design, functionality, and features — all reflecting our dedication to advancing autonomous technology.

 The documentation highlights key aspects of the robot’s development, including:

 * **Mobility Management** – covering motor selection, chassis design, and assembly, all guided by principles of speed, torque, and power;
 * **Power and Sense Management** – detailing the power sources and sensor setup, supported by a wiring diagram and a full Bill of Materials (BOM);
 * **Obstacle Management** – outlining our navigation strategies through flow diagrams and code breakdowns.

 To complement the technical information, we've included visual documentation such as real and 3D model images of the robot from multiple angles, along with team photos. Additionally, performance videos showcase the robot in action across various challenge scenarios.


## 2. The Team

 Our team consists of three dedicated members, each bringing unique strengths and expertise to the table. As the _Village Boys Team_, our primary goal is to work with maximum efficiency while combining our individual skills to learn from one another and grow together. Through close collaboration, we aim not only to enhance our personal knowledge in robotics, AI, and embedded systems, but also to continuously improve the performance, intelligence, and reliability of our robot — _Hoqqa_. We believe that teamwork, curiosity, and perseverance are the key drivers behind our success in building a competitive and innovative autonomous vehicle.
  
  <p align="center">
    <img src="assets/Alibali_Profile_Photo.jpg" alt="Alibali" width="400"/>
  </p>

  **Alibali Alibayov** is a graduate of School No. 4 in the Aliabad settlement of the Zaqatala district. As a core contributor to the Hoqqa project, he focuses on the integration of the Raspberry Pi board with the ROS 2 framework, utilizing both a depth camera and LIDAR for real-time perception and decision-making. His primary objective is to ensure that the results achieved in simulation can be effectively and reliably applied in real-world scenarios, bridging the gap between virtual testing and physical performance.

  <p align="center">
    <img src="assets/HajiHajiyev_Profile_Photo.jpg" alt="Alibali" width="400"/>
  </p>
  
**Haji Hajiyev** is a graduate of the Zagatala City Lyceum named after Academician Zarifa Aliyeva. As a technical contributor to the Hoqqa project, he specializes in 3D modeling of the car’s components. His primary focus is on refining the digital model based on insights gained from physical testing. By analyzing real-world performance, he ensures that the design maintains both structural strength and aerodynamic efficiency, while continuously improving the mechanical layout of the vehicle.

  <p align="center">
    <img src="assets/NihatMuradli_Profile_Photo.png" alt="Alibali" width="400"/>
  </p>
  
**Nihat Muradli** is a student at the European Azerbaijan School. As a technical contributor to the Hoqqa project, he focuses on refining the vehicle’s parts through simulation-driven design improvements. In addition to his design work, he is responsible for the electrical integration of the system, ensuring reliable communication between hardware components. He also manages the project documentation, aligning it with WRO standards to clearly present the team’s work and progress.


## Robot Specifications

The Village Boys Team proudly presents our self-driving car — the Hoqqa robot, developed for the World Robot Olympiad Azerbaijan 2025 Local Finals. Designed with precision, agility, and performance in mind, Hoqqa reflects the innovation and strong collaboration of our trio. Engineered to meet the challenges of the competition, the robot features some significant sensors equipped with the **Nuwa HP60C Cam**,**Lidar** and **IMU** delivering optimal speed, maneuverability, and power efficiency.

Below, you'll find the key specifications that showcase Hoqqa’s capabilities — a testament to our team's dedication to excellence and readiness to compete on the competition.

  * **Dimensions:** 195mm (L) x 160mm (W) x 230mm (H)
  * **Weight:** 1.23kg
  * **Maximum Speed:** 6.53m/s
  * **Steering Torque:** 100Ncm
  * **Working Voltage:** 11.1V–7.6V
  * **Drive System:** Rear-wheel drive (RWD)
  * **Steering Geometry:** Parallel steering
