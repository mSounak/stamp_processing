# Stamp Processing
 > A package develop by Sun* AI Research Team as part of the PDF Converter project. 

 This is a Deep Learning based package for detecting and removing stamp from document images.
 This package uses  [Yolov5](https://github.com/ultralytics/yolov5) for the stamp detection model and [fastai](https://github.com/fastai/fastai) Unet for stamp removal model

 ## Install
 Due to the requirements of the used libraries, stamp-processing requires **Python 3.8 or higher**.

 `stamp-processing` is published on [Pypi](https://pypi.org/project/stamp-processing/). To install the package, use `pip`:

 ```bash
 pip install stamp_processing
 ```

 **Note**: This package uses PyTorch. If you need GPU support, you may want to install PyTorch with CUDA support first:
 ```bash
 pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
 pip install stamp_processing
 ```

 ## How to use
 Check out [example](https://github.com/sun-asterisk-research/stamp_processing/blob/master/example/example.md) for basic usage or run  `getting_started.ipynb` in the `example` folder for example usage.

 ## Documentation
 Documentation will be available soon.

 ## Changelog
 See [CHANGELOG.md](CHANGELOG.md) for version history and breaking changes.

 ## Contact 
 Create an issue if you run into any bug or want to suggest a feature on [Github](https://github.com/sun-asterisk-research/stamp_processing)
