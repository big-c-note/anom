# Anom

This repo will contain a best effort implementation of anomaly detection on linux server logs in an effort to id unprobablistic events (such events may be a security concern).


## Initial Design

### Preprocessing

[] Create a flexible preprocessing framework for auth logs using config files.
[] Dump configurations into newly made research folder so the user can try out different preprocessing techniques.
[] Allow for regex substitutions.
[] Create a command line interface.

### Modeling

[] Create a command line interface.
[] Allow the user to set a default preprocessing output as a model input.
[] Dump configurations and data into newly made research folders along with diagnotic tools to determine the best model.
[] Allow for several model types (poentially accepting custom functions as well); start with sklearn implmentation but move to custom cpp with pybind11.
[] Implement at least one model from scratch using cpp, pytorch and pybind11

### Automation

[] Allow the user to set a schedule for training with either batch or online learning.
[] Allow for a few choices of notification when anomalies; gmail email, Linux pop up, etc.

### Documentation

[] Create sphynx docs from the numpy doc strings.
[] Create gifs of each process.
[] Add jupyter notebook containing math notation for any model built from scratch.
[] Add a contribution guide.
[] Add a license.
