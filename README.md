


<!-- PROJECT LOGO -->
<div align="center">

<h3 align="center">Tune Cube</h3>

  <p>
This code repository contains the implementation of an automated script for extracting top Spotify songs, downloading videos, and archiving them in AWS S3 buckets. A weekly trigger is set up to execute this script. The project utilizes a Raspberry Pi as a media player for displaying the downloaded videos. The code makes use of third-party libraries such as NumPy, Spotify API, and PyTube to facilitate the development and execution of the script
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

Product Images coming soon...

### Built With

* Python
* NumPy
* Spotify API
* PyTube
* Youtube Data API
* Raspberry Pi
* S3

<!-- USAGE EXAMPLES -->
## System Diagram
![image](https://user-images.githubusercontent.com/26352484/236096011-91fd3aa8-7f27-4dbc-8b0c-a36a32bedbff.png)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/udallmo/tune-cube.git
   ```
2. Install packages
   ```sh
   pip install -r requirements.txt
   ```
3. Add in Google Cloud Authorizations and Spotify API keys

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Running the script
   ```sh
   python .\main.py
   ```

<!-- ROADMAP -->
## Roadmap

- [ ] Setup the Terraform to do weekly scraps
- [ ] Enable LED colorization to the cube



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
