
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

The **Memory Machine/MeMa** represents a device specifically engineered to serve as an extensive memory repository, catering to the *unique needs of older adults*. With a paramount focus on **accessibility** and **usability**, this innovative solution enables individuals to **store and safeguard their treasured memories** through a user-friendly interface. The Memory Machine seamlessly integrates advanced technologies, including `Text-to-Speech (TTS)`` utilizing [gTTS](https://gtts.readthedocs.io/en/latest/), [speech recognition](https://pypi.org/project/SpeechRecognition/), and [facial recognition](https://pypi.org/project/face-recognition/), thereby enhancing the overall user experience and facilitating effortless interaction with the device.

The fundamental objective of the Memory Machine is to **empower older adults in capturing and reliving moments of profound significance**. Through its intuitive design, this device allows users to **store memories in diverse formats**, ranging from *spoken anecdotes* to *visual content*. The incorporation of *TTS* functionality enables the machine to convert *text-based memories* into *highly naturalized speech*, rendering them accessible to individuals with **visual impairments**. Moreover, the integration of speech recognition capabilities facilitates *hands-free* interaction, further *augmenting accessibility* and simplifying the device's operation.

A notable feature of the Memory Machine is it's **facial recognition functionality**, which removes the necessity to remember long, complicated passwords. As the target use-case is **older people**, MeMa 3.1 allows for a facial-based login system, similar to the iOS FaceID system. It's important that **memories are protected and secure**, which is a fundamental value in MeMa's Design.

In summary, the **Memory Machine provides a robust and inclusive solution for storing and reliving memories**, while specifically addressing the requirements of older adults. By seamlessly incorporating `TTS`, `speech recognition`, and `facial recognition` technologies, this device ensures *accessibility* and *ease of use*, ultimately **enabling individuals to engage with their memories in a personalized and meaningful manner**. The Memory Machine stands as a testament to the advancements in memory preservation technology, consistently evolving, improving and adapting to new ways to capture and store memories.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Setup & Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

MeMa has several dependencies that are going to be listed under this section. 

**Operating System Dependencies**<br>
MeMa 3.1 is currently available to deploy on Linux devices. Developed on [Ubuntu 22.04.2 LTS](https://releases.ubuntu.com/jammy/), this is the reccommended system. As MeMa should be used as a standalone device, it's **reccommended to use this version of Ubuntu** to avoid any errors.

There is no current support for **macOS** or **Windows** compatiable versions of MeMa, however with the current libraries this is possible to add.

**Device & Hardware Dependencies**<br>
MeMa 3.1 has several device-specific dependencies. These are pretty straight-forward, the device should contain the following:
* **Webcam/Camera** (Higher Quality for better Facial Recognition)
* **Microphone** (Higher Quality for better Speech Recognition)
* **Speaker**

In terms of processing-specific requirements, currently MeMa is too demanding to run on small embedded systems such as **Raspberry Pi**, and it is reccommended to run MeMa on a mini-pc inside of the operating shell.

**Python 3.11.4, PI & Tkinter Dependencies**<br>
It's important that your **system repository** is up to date, firstly run the following command to update any new package data.<br>
> sudo apt-get update

Now we must install Python 3.8, Tkinter and PIP. Tkinter is a graphics framework that comes as part of the standard library for the macOS and Windows versions of Python, however the Linux release does not include this base.

PIP (or pip) is Pythons package manager which we will later use to install further dependencies and libraries, such as **opencv**, **pillow** and **face_recognition**. For now, run the following 3 commands to install Python 3.8, PIP and Tkinter.
> sudo apt-get install python3.8
> sudo apt install python3-pip
> sudo apt-get install python3.8-tk

**Python Packages/Libraries**<br>
Several libraries are required to run MeMa, these are available in `requirements.txt` in the main repository. PIP will be able to perform a **one-line install of all package dependencies** using the following command. More information about the required packages is available in the [wiki](https://github.com/tobybenjaminclark/mema/wiki).
> pip install -r 'requirements.txt'

### Installation
In terms of installation, MeMa is easy to run and setup. Simply run the file at `codebank/mema_main_window.py`, this should setup and start the program. To create a new user, simply say 'new'.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/mema/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/mema](https://github.com/github_username/mema)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/mema.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/mema/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/mema.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/mema/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/mema.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/mema/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/mema.svg?style=for-the-badge
[issues-url]: https://github.com/tobybenjaminclark/mema/issues
[license-shield]: https://img.shields.io/github/license/github_username/mema.svg?style=for-the-badge
[license-url]: https://github.com/github_username/mema/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://uk.linkedin.com/in/toby-clark-14350815a?original_referer=https%3A%2F%2Fwww.google.com%2F
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 