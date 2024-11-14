# Fabric Inspector Backend

Backend for Cloth Hole Detection using YOLOv8 and FastAPI. This project is designed to detect holes in fabric images by leveraging a YOLOv8 model and serves as a backend API for a mobile application.

## Table of Contents

- [Overview](#overview)
- [Features](#features)

## Overview

This FastAPI-based backend service uses a YOLOv8 TFLite model to detect holes in fabric images. The API takes an image as input and returns detection results, including bounding boxes and detection confidence scores.

## Features

- **Image Upload**: Accepts images through an API endpoint for processing.
- **Hole Detection**: Detects holes in fabric images using a trained YOLOv8 model.
- **Results**: Returns detection confidence and positions of detected holes.
- **API Documentation**: Interactive API documentation with FastAPI's auto-generated Swagger UI.

