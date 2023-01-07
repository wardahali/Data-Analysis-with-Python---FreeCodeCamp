import numpy as np

def calculate(list):
  if(len(list)==9):
       #convert list to 3x3 matrix
    array=np.array(list)
    array=array.reshape(3,3)
       #calculate mean
    mean0=np.mean(array, axis=0).tolist()
    mean1=np.mean(array, axis=1).tolist()
    mean_f=np.mean(array).tolist()
    mean=[mean0,mean1, mean_f]
      #calculate min
    min0=np.min(array, axis=0).tolist()
    min1=np.min(array, axis=1).tolist()
    min_f=np.min(array).tolist()
    min=[min0,min1, min_f]  
      #calculate max
    max0=np.max(array, axis=0).tolist()
    max1=np.max(array, axis=1).tolist()
    max_f=np.max(array).tolist()
    max=[max0,max1, max_f] 
      #calculate sum
    sum0=np.sum(array, axis=0).tolist()
    sum1=np.sum(array, axis=1).tolist()
    sum_f=np.sum(array).tolist()
    sum=[sum0,sum1, sum_f] 
      #calculate variance
    var0=np.var(array, axis=0).tolist()
    var1=np.var(array, axis=1).tolist()
    var_f=np.var(array).tolist()
    var=[var0,var1, var_f] 
      #calculate standard deviation
    std0=np.std(array, axis=0).tolist()
    std1=np.std(array, axis=1).tolist()
    std_f=np.std(array).tolist()
    std=[std0,std1, std_f] 

    calculate={
        'mean': mean,
        'variance': var,
        'standard deviation': std,
        'max': max,
        'min': min,
        'sum': sum
    }
    return  calculate
  else:
       raise ValueError("List must contain nine numbers.")

         


  

    #return calculations