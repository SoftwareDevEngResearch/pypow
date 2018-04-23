#This file calculates the cylinder geometry given the top dead center volume the sweept volume and the bore and stroke
#and the location within the engine cylce given the crank angle Depictions of the geometry and equations can by found in
#Internal Combustion Engine Fundementals, Heywood, page 43.
import numpy as np

def cylinder_geometry(bore,stroke,tdc_volume,swept_volume,crank_radius,connecting_rod_length,crank_angle):
    # The geometry of the cylnder is a function of the given variables
    # The angle theta has a resolution of 1/10th of a degree
    #volumes are in cubic centimeters and lengths are in mm by convention

    theta_c=np.array(crank_angle)
    a=np.array(crank_radius)
    l=np.array(connecting_rod_length)
    b=np.array(bore)


    compression_ratio= (tdc_volume+swept_volume)/tdc_volume

    for theta in theta_c:
        s=(a*np.cos(theta))+(np.sqrt(l**2-a**2*(np.sin(theta))**2))
        cylinder_volume= tdc_volume+((np.pi*(b**2))/4.0)*(l+a-s)








if__name__=="__main__":
    cylinder_geometry(1,2,3,4)