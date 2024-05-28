# PAL Marker for Jupyter Notebook

Note: this repository assumes the bare minimum to get an `.ipynb` loaded in VS Code, specifically having just the Jupyter Lab package installed. As such, this should be compatible with Conda / Google Colab.

This provides two exmaple automarkers. The globally based solution assumes the output will be in the global scope, and, you can read the output from the global scope in the test runner. Meanwhile, the function based approach will call some function with a list of parameters. You may need to modify the test runner and the error logger for the exact desired function output, but, this should be relatively easy; just change which values in the list you're using as the inputs, and which are the outputs.
