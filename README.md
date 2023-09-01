
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/tobybenjaminclark/mema">
    <img src="imagebank/mema_logo.png" alt="Logo" width="300" height="200">
  </a>

<h3 align="center">Memory Machine (MeMa)</h3>

  <p align="center">
    Memory Machine is an accessible and user-friendly device designed for older adults to store and cherish their memories. By integrating advanced technologies such as text-to-speech, speech recognition, and facial recognition, it enables effortless interaction, enhances accessibility, and provides a secure repository for preserving and reliving precious moments.
    <br />
    <a href="https://github.com/tobybenjaminclark/mema/wiki">Wiki</a>
    ·
    <a href="https://github.com/tobybenjaminclark/mema">Demo</a>
    ·
    <a href="https://github.com/tobybenjaminclark/mema/issues">Issues</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Project Vision</a>
    </li>
    <li>
      <a href="#setup-&-getting-started">Setup & Installation</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Features & Roadmap</a></li>
    <li><a href="#contact">Contact Points</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<p align="center">
  <a href="https://github.com/tobybenjaminclark/mema">
    <img src="imagebank/prototype_digital/prototype_digital_preliminary_version_two.png" alt="Logo" width="300" height="240">
  </a>
</p>

The **Memory Machine/MeMa** represents a device specifically engineered to serve as an extensive memory repository, catering to the *unique needs of older adults*. With a paramount focus on **accessibility** and **usability**, this innovative solution enables individuals to **store and safeguard their treasured memories** through a user-friendly interface. The Memory Machine seamlessly integrates advanced technologies, including `Text-to-Speech (TTS)` utilizing [gTTS](https://gtts.readthedocs.io/en/latest/), [speech recognition](https://pypi.org/project/SpeechRecognition/), and [facial recognition](https://pypi.org/project/face-recognition/), thereby enhancing the overall user experience and facilitating effortless interaction with the device.

The fundamental objective of the Memory Machine is to **empower older adults in capturing and reliving moments of profound significance**. Through its intuitive design, this device allows users to **store memories in diverse formats**, ranging from *spoken anecdotes* to *visual content*. The incorporation of *TTS* functionality enables the machine to convert *text-based memories* into *highly naturalized speech*, rendering them accessible to individuals with **visual impairments**. Moreover, the integration of speech recognition capabilities facilitates *hands-free* interaction, further *augmenting accessibility* and simplifying the device's operation.

A notable feature of the Memory Machine is it's **facial recognition functionality**, which removes the necessity to remember long, complicated passwords. As the target use-case is **older people**, MeMa 3.1 allows for a facial-based login system, similar to the iOS FaceID system. It's important that **memories are protected and secure**, which is a fundamental value in MeMa's Design.

In summary, the **Memory Machine provides a robust and inclusive solution for storing and reliving memories**, while specifically addressing the requirements of older adults. By seamlessly incorporating `TTS`, `speech recognition`, and `facial recognition` technologies, this device ensures *accessibility* and *ease of use*, ultimately **enabling individuals to engage with their memories in a personalized and meaningful manner**. The Memory Machine stands as a testament to the advancements in memory preservation technology, consistently evolving, improving and adapting to new ways to capture and store memories.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Setup & Getting Started

MeMa can be setup on either
1.  MeMa Shell (see [wiki](https://github.com/tobybenjaminclark/mema/wiki) for setup)
2.  Linux Device with Physical Interface Emulators

### Prerequisites

For both options, MeMa has several dependencies that are going to be listed under this section. Further information on how to construct your own working, MeMa Shell is available in the [wiki](https://github.com/tobybenjaminclark/mema/wiki), and the `.stl` files are available in `/modelbank/`. This section is only going to **overview setting up the virtual prototype**.

**Operating System Dependencies**<br>
MeMa 3.1 is currently available to deploy on Linux devices. Developed on [Ubuntu 22.04.2 LTS](https://releases.ubuntu.com/jammy/), this is the reccommended system. As MeMa should be used as a standalone device, it's **reccommended to use this version of Ubuntu** to avoid any errors.

There is no current support for **macOS** or **Windows** compatiable versions of MeMa, however with the current libraries this is possible to add.

**Device & Hardware Dependencies**<br>
MeMa 3.1 has several device-specific dependencies. These are pretty straight-forward, the device should contain the following:
* **Webcam/Camera** (Higher Quality for better Facial Recognition)
* **Microphone** (Higher Quality for better Speech Recognition)
* **Speaker/Headphones** (Headphones are reccommended)

In terms of processing-specific requirements, currently MeMa is too computationally demanding to run on small embedded systems such as **Raspberry Pi**, and it is reccommended to run MeMa on a mini-pc inside of the operating shell. For a more-specific reccommended set of requirements, see below:

> `Recommended RAM: ` 8GB DDR4<br>
> `Recommended CPU: ` Intel i5 (or equivalent) 4-Cores @2.4GHz<br>
> `Storage/HDD/SSD: ` 3GB of available space<br>
>

**Python 3.11.4, PI & Tkinter Dependencies**<br>
It's important that your **system repository** is up to date, firstly run the following command to update any new package data.<br>
> sudo apt-get update

Now we must install Python 3.8, Tkinter and PIP. Tkinter is a graphics framework that comes as part of the standard library for the macOS and Windows versions of Python, however the Linux release does not include this base.

PIP (or pip) is Pythons package manager which we will later use to install further dependencies and libraries, such as **opencv**, **pillow** and **face_recognition**. For now, run the following 3 commands to install Python 3.8, PIP and Tkinter.
> sudo apt-get install python3.8<br>
> sudo apt install python3-pip<br>
> sudo apt-get install python3.8-tk

**Python Packages/Libraries**<br>
Several libraries are required to run MeMa, these are available in `requirements.txt` in the main repository. PIP will be able to perform a **one-line install of all package dependencies** using the following command. More information about the required packages is available in the [wiki](https://github.com/tobybenjaminclark/mema/wiki).
> pip install -r 'requirements.txt'

### Installation
In terms of installation, MeMa is easy to run and setup. Simply run the file at `codebank/mema_main_window.py` with the `--emulator` flag to show that you want to emulate the buttons. This should setup and start the program. To create a new user, simply say 'new'.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

**Setting up an account with MeMa**<br>
To start using **MeMa**, the user needs to create an account. The process can be initiated by saying the command `New` or selecting the `Make Account` option on the device's interface.  MeMa only needs the users **name** and a picture of their **face** to create an account.

**Logging in to MeMa**<br>
After creating an account, the user can log in using facial recognition. They need to **position their face in front of the camera**, and MeMa will **recognize their face and grant access to their account**. This is symbolized by a **white circle around the users face.** This system eliminates the need for remembering long and complicated passwords.

**Creating Memories with MeMa**<br>
Once logged in, the user can create new memories to store in MeMa. Within MeMa a **memory** is a *collection of associated data, such as videos, pictures and labels, centered around a past event or memory*. This is handled using **memory frames**. In MeMa, a **memory frame** a *slice* or *section* of a memory, think of it like a *segment of a photo-reel*, where the user can store a **picture** or **video** alongside a **label** or **caption**. One or more **memory frames** make up a **memory** within MeMa.

>The user is able to **record live** using the devices camera and microphone, allowing the creation of **new memories** on the spot, or **digitize photograph memories**. Memories are captioned using **Speech Recognition**, the user simply talks about the memory, and MeMa will automatically transcribe and store the caption underneath the displayed memory.

**Viewing Memories with MeMa**<br>
Once memories are created and stored, the user can easily access and relive them. They can view their memories inside of MeMa, through its intuitive, easy-to-use interface. As a memory isn't just one photo, one video or one label; MeMa displays memories as **collections of data, together to emphasize remembering, reliving and reminiscing** on moments in he past.

_For more examples, please refer to the [wiki](https://github.com/tobybenjaminclark/mema/wiki)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Features & Roadmap

Current
* **Account Creation** and **Management**.
* **Facial-Recognition Login** System
* Memory **Creation** and **Editing**
* Recording **Video**
* Recording **Images**
* Recording **Labels**
* **Viewing Memories**
* **Video Generation** from **Memories**

Future
* Exporting Memories as Videos (writing to DVD)
* Recording of audio over memories (music etc...)
* Full MeMa Shell


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact Points

**Toby Benjamin Clark**<br>
Happy to help with any queries/implementation concerns. Please contact me by one of the below methods explaining the issue that you are facing and I will get back to you as soon as possible with assistance.
<p align = "center">
<a href="https://github.com/tobybenjaminclark/">GitHub</a>
·
<a href="https://www.linkedin.com/in/toby-clark-14350815a/">LinkedIn</a>
·
<a href="mailto:tobybenjaminclark@gmail.com">Email</a>
</p>

Project Link: [https://github.com/tobybenjaminclark/mema](https://github.com/tobybenjaminclark/mema)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>