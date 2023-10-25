# Partial output parser

This repository contains a Python script that will read an incomplete `output.xml` (`BASENAME`) file and extract the last keyword that has been run.
The script also saves a fixed (valid) XML file as `BASENAME_fixed.xml` and generates a HTML log file `BASENAME_fixed.html` from that using `rebot`.

Giving the source file `BASENAME`:

1. by default will try to read file `output.xml`
2. if `task.py` is given argument then that will be used, for example. `python task.py myoutput` will try to read file `myoutput.xml`
3. if environment variable `BROKEN_OUTPUT_FILE` is given (step 2 has precedence over this), `BROKEN_OUTPUT_FILE=myoutput` will try to read file `myoutput.xml`

The incomplete `output.xml` is something that appears at least in some RPA cases where execution gets stuck and the RFW run is terminated in some way or another and then log.html is not automatically generated.
