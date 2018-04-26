#This file calculates the cylinder geometry given the top dead center volume the sweept volume and the bore and stroke
#and the location within the engine cylce given the crank angle Depictions of the geometry and equations can by found in
#Internal Combustion Engine Fundementals, Heywood, page 43.
import numpy as np
from matplotlib import pyplot

class Cylinder_Geometry:
    # The geometry of the cylnder is a function of the given variables
    # The angle theta has a resolution of 1/10th of a degree
    #volumes are in cubic centimeters and lengths are in mm by convention

    def __init__(self,compression_ratio = 12.75 ,bore=9.5,stroke=6.34,tdc_volume=0,swept_volume=449.9, connecting_rod_length=15.0,crank_angle=np.arange(0,720,0.1)):
        #This init function converts all the base geometeries into arrays using numpy.array(), this is done
        #for speed
        self.compression_ratio=compression_ratio
        self.bore=np.array(bore)
        self.stroke=np.array(stroke)
        self.tdc_volume=np.array(tdc_volume)
        self.swept_volume=np.array(swept_volume)
        self.crank_radius=np.array(stroke/2.0)
        self.connecting_rod_length=np.array(connecting_rod_length)
        self.crank_angle=np.array(crank_angle)
        self.connectrod_crankrad= np.array(connecting_rod_length/(stroke*0.5))


    def cylinder_volume_func(self):

        theta_c = np.deg2rad(self.crank_angle)
        a=self.crank_radius
        l=self.connecting_rod_length
        b=self.bore
        v_c=self.tdc_volume
        c=Cylinder_Geometry()
        if v_c == 0:
            v_c = c.tdc_volume_calc()
        cylinder_volume=range(0,len(theta_c))
        for i,theta in enumerate(theta_c):
            s=(a * np.cos(theta)) + (np.sqrt(l ** 2 - (a ** 2) * (np.sin(theta)) ** 2))

            cylinder_volume[i]= v_c+((np.pi*(b**2))/4.0)*(l+a-s)
        return cylinder_volume

    def tdc_volume_calc(self):
        tdc_volume=self.swept_volume/(self.compression_ratio-1)
        return tdc_volume
    def compression_ratio(self):

        compression_ratio= (self.tdc_volume+self.swept_volume)/self.tdc_volume

        return compression_ratio
    def piston_velocity(self,n):
        #this function is used to define both the average velocity of the piston
        #aswell as the actual velocity of the piston
        theta_c = np.deg2rad(self.crank_angle)
        ave_pist_velocity=2*self.stroke*n

        for theta in theta_c:
            actual_pist_velocity= ave_pist_velocity*(np.pi*0.5*np.sin(theta_c))*(1+(np.cos(theta_c)/np.sqrt(self.connectrod_crankrad**2-(np.sin(theta_c)))))

        return ave_pist_velocity, actual_pist_velocity






if __name__=="__main__":

    c=Cylinder_Geometry()
    tdcv= c.tdc_volume_calc()
    print tdcv

    cylinder_volume=c.cylinder_volume_func()
    print cylinder_volume

    pyplot.plot(cylinder_volume)
    pyplot.show


