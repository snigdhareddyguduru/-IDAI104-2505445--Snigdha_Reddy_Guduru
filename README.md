
Introduction & Initial Research

Before developing the application, I began by learning more about the physics of rocket trajectories and the engineering challenges of space missions. I researched how the forces of thrust, gravity, and drag affect the trajectory of a rocket and how Newton’s Second Law of motion relates to the dynamics of rocket launches. I investigated how the addition of payload affects the amount of fuel required and how drag affects the maximum altitude of a rocket. I also investigated real-world space mission data to learn more about the relationship between variables such as cost, scientific return, and crew size and the success of space missions.

Designing and Building the Application
After gaining an understanding of the theoretical foundations, I started working on the design of the Streamlit application. The aim was to not only display the data but also integrate real mission data analysis with a mathematical model of a rocket simulation.

First, I organized the data by changing the data types, handling missing values, and checking for consistency. Next, I developed the necessary graphics, such as scatter plots, bar charts, line plots, and box plots. Each of these plots was designed to solve a particular question in the field of engineering, like whether more fuel is needed for heavier payloads or whether increased spending leads to success.

After finishing the data analysis component, I moved on to the implementation of the rocket simulation for launch. By using a time-stepping approach, I defined acceleration as follows:

a = (Thrust − Gravity − Drag) / Mass
I added fuel consumption to reduce the mass dynamically and contrasted two cases: one with drag and one without drag. This enabled the simulation to show the effect of air resistance on the maximum altitude achieved.

Lastly, I organized the dashboard into tabs, included interactive sliders for the thrust and payload, and improved the layout.
<img width="1440" height="900" alt="Screenshot 2026-02-18 at 10 28 11 AM" src="https://github.com/user-attachments/assets/7909b98b-7669-46e7-82b4-6eb79688b1ad" />


Challenges Faced
One of the biggest challenges was the proper implementation of the physics simulation. At the start, the altitude values did not behave as expected due to incorrect mass update and force calculation. To solve this, it was important to study the formula and ensure the correct calculation of the drag force and gravity at each time step.

Another challenge faced was the data formatting issue. The data had some columns to be converted to a numeric format, and incorrect formatting caused problems while generating the visualization. Proper cleaning of the data was necessary to get the correct correlation output.

Another challenge faced while styling the dashboard was choosing colors and the overall look and feel, as it had to be professional and aerospace-related.



Post-Development Improvements
<img width="1440" height="900" alt="Screenshot 2026-02-18 at 10 30 10 AM" src="https://github.com/user-attachments/assets/85509ce9-6170-44aa-bac5-ccb30ec5de03" />
<img width="1440" height="900" alt="Screenshot 2026-02-18 at 10 30 21 AM" src="https://github.com/user-attachments/assets/47630a3b-ef8c-418b-a78a-092e3fd5a35c" />
<img width="1440" height="900" alt="Screenshot 2026-02-18 at 10 30 30 AM" src="https://github.com/user-attachments/assets/8d5e35cd-9328-4607-bad5-21eccf012507" />


After building the initial version of the app, I improved it by:

Adding interactive filters by mission type

Comparing simulation results with and without drag

Including correlation heatmaps

Refining visual clarity and layout

Enhancing explanatory text to connect simulation results to real engineering scenarios


Conclusion
These improvements strengthened the analytical depth of the project.

This project showed the ways in which mathematics, data analysis, and engineering intersect in the real world, particularly in the context of aerospace engineering. By combining real mission data with a physics-based simulation, I was able to learn more about the ways in which payload, fuel consumption, drag, and thrust can affect the performance of a rocket.

In addition to the technical skills, this project also taught me more about the ways in which differential equations can be used to model real-world physical systems, as well as the ways in which data visualization can be used to support engineering decisions.

This project has improved my skills in both mathematical reasoning and the ways in which I can use theory to create interactive analytical tools.
