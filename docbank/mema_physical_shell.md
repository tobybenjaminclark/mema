# What is the MeMa Physical Prototype?
The MeMa Physical Shell is a physical deployment for the Memory Machine. It consists of a **3D Printed Shell** and **Internal Hardware**. This guide can be split up into essentially 2 sections, how to print the shell and how to connect the prototype.

<p align="center">
  <img src="https://github.com/tobybenjaminclark/mema/blob/main/imagebank/specifications/mema_diagram_physical_shell_angles.png" />
</p>

# 3D Printing the MeMa Shell
The **MeMA 3D-Shell** was printed using [**PLA Plastic**](https://en.wikipedia.org/wiki/3D_printing_filament) on a [**Flashforge Creator-3**](https://www.flashforge.com/product-detail/1). The test-shell was printed using [GEEETECH Filament](https://www.geeetech.com/), with a nozzle temperature of 220°c and a build plate temperature of 65°c. However, these should be tweaked to your devices. settings. It is also reccommended to perform a test print beforehand, to avoid wasting large amounts of filament.

There are 2 supplied mema models in the repository, a **whole-piece** model and a **4 section** model. Due to the large size of mema, we reccommend printing the **4 section** model, and then combining afterwards, however if your printer is able to print the **whole-piece** model, then this would provide optimal strength. These models are all available in the `modelbank` directory, alongisde `gcode` for the `flashforge creator-3`. If you are using a different printer, then you will need to **slice** the models yourself, using a model slicer such as [Cura](https://ultimaker.com/software/ultimaker-cura/).

> :warning: If your 3D printer **does not support a large build plate**, you can break the model down furhter using [Blender](https://www.blender.org/). ([Tutorial](https://www.youtube.com/watch?v=moPDPB4MY2U)) Blender is a free, open-source, general purpose, 3D Modelling Software that can be used to split down a 3D model.

### 4-Component Shell Guide
* This was the **tried and tested** method of printing the MeMa3 shell. It is **highly recommended** to print MeMa using this technique. However, if you have a 3D printer large enough to print the MeMa shell in one, this will provide heightened structural integrity.
* The models available to print this are available in `modelbank/`, but will require **slicing** by whatever 3D modelling software you desire.
* This guide will provide settings for the [**Flashforge Creator-3**](https://www.flashforge.com/product-detail/1) 3D Printer, please tweak these settings according to your own individual setup
<p align="center">
  <img src="https://github.com/tobybenjaminclark/mema/blob/main/imagebank/specifications/mema_diagram_physical_shell_print.png" />
</p>

##### **Slicing & Infil Settings**

MeMa3 was printed using **40% Hexagonal Infil**, with a **4-layer thick shell** and generated supports and brim. Supports **will most likely be required** due to the **complex structure of MeMa**. This resulted in each part taking approximately 18 to 23 hours a piece, depending on complexity and required supports, e.g. *the front 2 pieces take longer to print*.

<br>

##### **Temperature & Adhesive Settings ([Flashforge Creator-3](https://www.flashforge.com/product-detail/1))**
Just another note that these worked for the **Flashforge Creator 3** with **GEEE PLA**, these will **most likely change depending on your individual printer setup**, and should be set as the result of multiple test prints. Guides for finding the best settings for your printer are available online.
> **Right Extruder** Temperature of **220°c** or 428°f.
> **Build Plate** Temperature of **65°c** or 149°f.
> This was printed using **GEEE** PLA, however any PLA should work.

> :warning: Do not touch the extruder tip or build plate while it is hot.

<br>

##### **PLA Usage & Requirements**
When printing MeMa, we used a total of **2 Reels (2kg)** of **GEEETECH PLA** Filament. This accounted for **1 misprint** of a quadrant section, and may vary depending on how the print proceeds. It is **reccommended to use the same PLA type and colour for all 4 segments of MeMa**, however this is not required.
<br>

##### **4-Component Shell Reference Sheet**
> :warning: **These settings should only be used for the 4-compartment large shell**. This is because other parts of the MeMa shell require more integrity and strength, hence requiring different infil types and percentages. These should be visible in their dedicated, separate sections.
<div align="center">
  <table class="center">
    <thead>
      <tr>
        <th class = "tg-fymr">Setting Name</th>
        <th class="tg-0pky">Setting Value</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="tg-fymr">3D Printer</td>
        <td class="tg-0pky">Flashforge Creator 3</td>
      </tr>
      <tr>
        <td class="tg-fymr">Filament Type</td>
        <td class="tg-0pky">PLA (GEEETECH)</td>
      </tr>
      <tr>
        <td class="tg-fymr">Extruder Temperature</td>
        <td class="tg-0pky">220°C</td>
      </tr>
      <tr>
        <td class="tg-fymr">Build Plate Temperature</td>
        <td class="tg-0pky">65°C</td>
      </tr>
      <tr>
        <td class="tg-fymr">Infil Type</td>
        <td class="tg-0pky">Hexagonal</td>
      </tr>
      <tr>
        <td class="tg-fymr">Infil Percentage</td>
        <td class="tg-0pky">40% (increase for strength)</td>
      </tr>
      <tr>
        <td class="tg-fymr">Generate Supports</td>
        <td class="tg-0pky">Yes, lattice-type recommended</td>
      </tr>
      <tr>
        <td class="tg-fymr">Generate Brim</td>
        <td class="tg-0pky">Yes, 3mm thick, 6mm reach</td>
      </tr>
    </tbody>
  </table>
</div>

# Internal Hardware
MeMa requires a certain amount of processing power to run effectively. It also requires a few more external hardware components, that will be described in this section.

#### Processing and Interfaces (What to run MeMa on)
The Physical MeMa prototype was constructed using a **miniature PC** as the processing centre. In the future, this code could be modified to run on a **micro-controller** such as a **raspberry pi**. However, currently this is limited due to MeMa's **facial-recognition technology**.

I will now go on to list the **processing requirements** of MeMa, essentially listing the reccommended system specifications to run MeMa on. Please note that the **codebase** can be modified and **further optimized** to run on systems with less processing power or RAM.

> **Recommended RAM:** 8GB DDR4<br>
> **Recommended CPU:** Intel i5 (or equivalent) 4-Cores @2.4GHz<br>
> **Storage/HDD/SSD:** 3GB of available space<br>
>
<br>

#### DVD/Disc External Peripheral
In terms of the **DVD-Drive** we used an external USB DVD Drive that supports both **reading** and **writing** to a disc. This was **15cm by 15cm**, however we had to shave a small part of the front of the disc drive off the tray to easily open through the MeMa Slot.

> :warning: Please note that the issue of alternate DVD Drive sizes can be **rectified by modifying the supplied MeMa Model**, dependent on your DVD Drive model and dimensions, however MeMa's design is **centred around forward-tray DVD Drives**, rather than ones that flip open allowing for top-down disc insertion. To do this, I would reccommend editing the model using **Blender** and the provided `.blend` files.

# External Hardware (MeMa Tablet)
The MeMa Tablet is the communication interface between the MeMa internal and the user, it provides **4 digital inputs**, a **display** and a **scaler input**. We constructed it using a **Bluefruit Feather Arduino** and some basic electronics.

> External Display & Connecting Cables
> Bluefruit Feather Arduino Microcontroller (supports USB)
> 4x Digital Buttons & 4x 10oHm resistors
> 1x Potentiometer (turning knob input)
> Wires & Solder
> 3D Printed MeMa Tablet Shell (see separate guide for this)

### How to construct the MeMa Tablet
Paragraph with diagrams