#!/bin/bash
pip3 install Pillow -t ./
zip runtime.zip ./*
rm -r PIL
rm -r Pillow-*