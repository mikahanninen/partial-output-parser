# Partial output parser

This repository contains a Python script that will read an incomplete `output.xml` file and extract the last keyword that has been run.

By default, the script will try to read the file named `output.xml` but the environment variable `BROKEN_OUTPUT_FILE` can be given (without file extension .xml, for example. `BROKEN_OUTPUT_FILE=myoutput` would match `myoutput.xml`.

The script also saves a fixed (valid) XML file as `output_fixed.xml` and generates a HTML log file `output_fixed.html` from that using `rebot`.

The incomplete output.xml is something that appears at least in some RPA cases where execution gets stuck and the RFW run is terminated in some way or another and then log.html is not automatically generated.

