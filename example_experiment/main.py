from autothalix.measurements import CyclicVoltammetry, LinearSweepVoltammetry, OpenCircuitPotential, Impedance
from autothalix.utils import initialize_experiment
import os
from autothalix.logging import logger

run_name = 'example_name'
zennium_connection, zahner_zennium = initialize_experiment()

logger.info('Any additional information')  # you can write any comments like that
ocp1 = OpenCircuitPotential(wr_connection=zahner_zennium,
                            seconds=10,
                            measurement_id='ocp1')
ocp1.output_path = os.path.join(ocp1.output_path, run_name)
ocp1.run()
ocp_last = ocp1.measured_data['potential_V'][-1]

imp1 = Impedance(wr_connection=zahner_zennium, measurement_id='imp1')
imp1.output_path = os.path.join(imp1.output_path, run_name)
imp1.run()
imp_last = imp1.measured_data['impedance_Ohm'][-1]

cv1 = CyclicVoltammetry(wr_connection=zahner_zennium,
                        start_potential=ocp_last,
                        upper_reversing_potential=0.4,
                        lower_reversing_potential=ocp_last,
                        cycles=0.5,
                        end_potential=ocp_last,
                        ohmic_drop=imp_last,
                        measurement_id='cv1')
cv1.output_path = os.path.join(cv1.output_path, run_name)
cv1.run()