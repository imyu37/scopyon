import sys
import os
import numpy

from flip_handler   import FLIPConfigs, FLIPVisualizer
from effects_handler import PhysicalEffects

def test_flip(t0, t1) :

    # create FLIP imaging
    flip = FLIPConfigs()
    flip.set_LightSource(source_type='LASER', wave_length=532, imaging_flux=100e-6, bleaching_flux=100000e-3, \
                            bleaching_size=(30,30), bleaching_position=(512,512), bleaching_time=1.2, radius=400e-9)
    flip.set_Fluorophore(fluorophore_type='EGFP')
    flip.set_Pinhole(radius=28.8e-6)
    flip.set_Magnification(Mag=60)

    # PMT : Photon-counting mode
    flip.set_Detector(detector='PMT', mode="Photon-counting", image_size=(1024,1024), focal_point=(0.4,0.5,0.5), \
                    pixel_length=207.16e-9, scan_time=1.10, gain=1e+6, dyn_stages=11, pair_pulses=18e-9)
    flip.set_ADConverter(bit=12, offset=0, fullwell=4096)

#       # PMT : Anlalog mode
#       flip.set_Detector(detector='PMT', mode="Analog", image_size=(1024,1024), focal_point=(0.4,0.5,0.5), \
#                       pixel_length=207.16e-9, scan_time=1.15, gain=1e+6, dyn_stages=11, pair_pulses=18e-9)
#       flip.set_ADConverter(bit=12, offset=0, fullwell=4096)

#       # Output data
    flip.set_OutputData(image_file_dir='./numpys_flip_080000A_bleach')
    #flip.set_OutputData(image_file_dir='./numpys_flip_019656A_bleach')
    #flip.set_OutputData(image_file_dir='./numpys_flip_019656A_blink')
    #flip.set_OutputData(image_file_dir='./numpys_flip_000100A_bleach')

    # Input data
    #flip.set_InputData('/home/masaki/wrk/spatiocyte/models/beads_3D_019656A', start=t0, end=t1, observable="A")
    flip.set_InputData('/home/masaki/bioimaging_4public/data_flip_010000A_bleach', start=t0, end=t1, observable="A")
    #flip.set_InputData('/home/masaki/bioimaging_4public/data_flip_019656A_bleach', start=t0, end=t1, observable="A")
    #flip.set_InputData('/home/masaki/bioimaging_4public/data_flip_019656A_blink', start=t0, end=t1, observable="A")
    #flip.set_InputData('/home/masaki/bioimaging_4public/data_flip_000100A_bleach', start=t0, end=t1, observable="A")

    # create physical effects
    physics = PhysicalEffects()
    physics.set_background(mean=0)
    physics.set_fluorescence(quantum_yield=0.61, abs_coefficient=83400)
    physics.set_photobleaching(tau0=1e-3, alpha=0.73)
    #physics.set_photoactivation(turn_on_ratio=1000, activation_yield=1.0, frac_preactivation=0.00)
    #physics.set_photoblinking(t0_on=30e-6, a_on=0.58, t0_off=10e-6, a_off=0.48)

    # create image
    create = FLIPVisualizer(configs=flip, effects=physics)
    #create.rewrite_InputData(output_file_dir='./data_flip_19656A_bleach')
    #create.rewrite_InputData(output_file_dir='./data_flip_19656A_blink')
    create.output_frames(num_div=16)



if __name__ == "__main__":

    t0 = float(sys.argv[1])
    t1 = float(sys.argv[2])

    test_flip(t0, t1)