#!/bin/bash
sam build --user-container
cd .aws-sam/build/ThumbGeneratorFunction/
zip runtime.zip ./* -r
mv runtime.zip ../../../
cd -