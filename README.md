# Quickstart

When you initialize a class (eg `LinearSweepVoltammetry`) it will take
parameters from baseline.yaml file. You can override these parameters
by passing them to the constructor. For example:

```python
from thales.experiments import LinearSweepVoltammetry

experiment = LinearSweepVoltammetry(
    connection=connection,
    measurement_id='lsv_123',
    start_potential=0.0,
    end_potential=1.0,
    scan_rate=0.1,
)
```
`start_potential`, `end_potential` and `scan_rate` will be overriden. 


All measurements have a `run` method that will run the experiment.

For measurements that have implementation on the side of
`thales_remote` (e.g `LinearSweepVoltammetry` or `CyclicVoltammetry`)
the reults of measurement will be **save on the side of
PC** that is running the server and connected to
the potentiostat. The results will be saved in the path defined by
`output_path` in `baseline.yaml`.

For measurements that don't have implementation on the side of
`thales_remote` (e.g `OpenCircuitPotential` or `Impedance`) the results
will be saved **by the python-script** into a csv file to the path defined by
`output_path` in `baseline.yaml`.

All those measurements are inheriting from `BaseManualMeasurements`
abstract class.

Also, for those measurements, you can access the results by accessing
`measured_data` attribute of the measurement object. For example:

```python
from thales.experiments import OpenCircuitPotential


experiment = OpenCircuitPotential(
    connection=connection,
    measurement_id='ocp_123')
experiment.run()

print(experiment.measured_data)
```