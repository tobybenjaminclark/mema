# What is the MeMa Physical Prototype?
The MeMa Physical Shell is a physical deployment for the Memory Machine. It consists of a **3D Printed Shell** and **Internal Hardware**. This guide can be split up into essentially 2 sections, how to print the shell and how to connect the prototype.



# 3D Printing the MeMa Shell
The **MeMA 3D-Shell** was printed using [**PLA Plastic**](https://en.wikipedia.org/wiki/3D_printing_filament) on a [**Flashforge Creator-3**](https://www.flashforge.com/product-detail/1). The test-shell was printed using [GEEETECH Filament](https://www.geeetech.com/), with a nozzle temperature of 220 degrees and a build plate temperature of 65 degrees. However, these should be tweaked to your devices. settings. It is also reccommended to perform a test print beforehand, to avoid wasting large amounts of filament.

There are 2 supplied mema models in the repository, a **whole-piece** model and a **4 section** model. Due to the large size of mema, we reccommend printing the **4 section** model, and then combining afterwards, however if your printer is able to print the **whole-piece** model, then this would provide optimal strength. These models are all available in the `modelbank` directory, alongisde `gcode` for the `flashforge creator-3`. If you are using a different printer, then you will need to **slice** the models yourself, using a model slicer such as [Cura](https://ultimaker.com/software/ultimaker-cura/).

> :warning: If your 3D printer **does not support a large build plate**, you can break the model down furhter using [Blender](https://www.blender.org/). ([Tutorial](https://www.youtube.com/watch?v=moPDPB4MY2U)) Blender is a free, open-source, general purpose, 3D Modelling Software that can be used to split down a 3D model.

### 4-Component Shell Guide
* This was the **tried and tested** method of printing the MeMa3 shell. It is **highly recommended** to print MeMa using this technique.
* The models available to print this are available in `modelbank/`
* This guide will provide settings for the [**Flashforge Creator-3**](https://www.flashforge.com/product-detail/1) 3D Printer, please tweak these settings according to your own individual setup
<p align="center">
  <img src="https://github.com/tobybenjaminclark/mema/blob/main/imagebank/specifications/mema_diagram_physical_shell_print.png" />
</p>

# Internal Hardware