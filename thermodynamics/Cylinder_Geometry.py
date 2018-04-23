#This file calculates the cylinder geometry given the top dead center volume the sweept volume and the bore and stroke
#and the location within the engine cylce given the crank angle Depictions of the geometry and equations can by found in
#Internal Combustion Engine Fundementals, Heywood, page 43.
import numpy as np



class Cylinder_Geometry:
    # The geometry of the cylnder is a function of the given variables
    # The angle theta has a resolution of 1/10th of a degree
    #volumes are in cubic centimeters and lengths are in mm by convention

    def __init__(self,bore,stroke,tdc_volume,swept_volume, connecting_rod_length,crank_angle):
        #This init function converts all the base geometeries into arrays using numpy.array(), this is done
        #for speed
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

        for theta in theta_c:
            s=(a * np.cos(theta)) + (np.sqrt(l ** 2 - a ** 2 * (np.sin(theta)) ** 2))
            cylinder_volume= v_c+((np.pi*(b**2))/4.0)*(l+a-s)
        return cylinder_volume

    def compression_ratio(self):

        compression_ratio= (self.tdc_volume+self.swept_volume)/self.tdc_volume

        return compression_ratio
    def piston_velocity(self,n):
        #this function is used to define both the average velocity of the piston
        #aswell as the actual velocity of the piston
        theta_c = np.deg2rad(self.crank_angle)
        ave_pist_velocity=2*L*n

        for theta in theta_c:
            actual_pist_velocity= ave_pist_velocity*(np.pi*0.5*np.sin(theta_c))*(1+(np.cos(theta_c)/np.sqrt(self.connectrod_crankrad**2-(np.sin(theta_c)))))

        return ave_pist_velocity, actual_psit_velocity






if __name__=="__main__":

    cylinder_geometry(1,2,3,4)