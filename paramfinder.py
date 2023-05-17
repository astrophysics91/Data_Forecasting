import re as re

class params:
    
    def __init__(self):
        pass
    
    def call_parameters(name):
        call=(open(name).read())
        call=re.sub(r'\t', ' ', call)
        call=call.split('\n')

        param_array=np.zeros(0)
        for i in range(0,len(call)):
            each_line=np.array(call[i].split(' ')) 
            each_line=each_line[each_line!='']
            if each_line[0]=='CLK':
                break
            else:
                pass
            param_array=np.append(param_array,each_line)
        return param_array
    
    def param_finder(array,param):
        param_idx=np.where(array==param)
        param_name=array[param_idx]

        param_val=array[param_idx[0]+1]
        param_err=array[param_idx[0]+3]
        if param=='RAJ' or param=='DECJ': 
            if param=='RAJ':
                head='h'
                head_sub='d'
                param_idx_sub=np.where(array=='DECJ')
                param_name_sub=array[param_idx_sub]
                param_val_sub=array[param_idx_sub[0]+1]
                param_err_sub=array[param_idx_sub[0]+3]
            if param=='DECJ':
                head='d'
                head_sub='h'
                param_idx_sub=np.where(array=='RAJ')
                param_name_sub=array[param_idx_sub]
                param_val_sub=array[param_idx_sub[0]+1]
                param_err_sub=array[param_idx_sub[0]+3]

            coord=''
            err_part=''
            locator=0

            for i in param_val[0]:
                if i==':': 
                    if locator==0:
                        i=head

                    locator=locator+1
                if locator<=1:
                    coord=coord+i
                if locator>1:
                    err_part=err_part+i

            upper=float(err_part[1:])+float(param_err[0])
            lower=float(err_part[1:])-float(param_err[0])

            coord_upper=coord+'m'+str(upper)
            coord_lower=coord+'m'+str(lower)

            coord_sub=''
            err_part_sub=''
            locator_sub=0
            
            for i in param_val_sub[0]:
                if i==':': 
                    if locator_sub==0:
                        i=head_sub
                    locator_sub=locator_sub+1
                if locator_sub<=1:
                    coord_sub=coord_sub+i
                if locator_sub>1:
                    err_part_sub=err_part_sub+i


            sub_part=float(err_part_sub[1:])
            coord_sub=coord_sub+'m'+str(sub_part)
             

            if param=='RAJ':
                coord_lw= SkyCoord(coord_upper, coord_sub, frame='icrs')
                coord_up= SkyCoord(coord_lower, coord_sub, frame='icrs')  
                mean=(coord_lw.galactic.frame.l.deg+coord_up.galactic.frame.l.deg)/2
                err=(mean-coord_lw.galactic.frame.l.deg)

            if param=='DECJ':
                coord_lw= SkyCoord(coord_sub, coord_upper, frame='icrs')
                coord_up= SkyCoord(coord_sub, coord_lower, frame='icrs')            
                mean=(coord_lw.galactic.frame.b.deg+coord_up.galactic.frame.b.deg)/2
                err=(mean-coord_lw.galactic.frame.b.deg)

            param_val=mean
            param_err=err
                
        else:
            param_val=float(param_val[0])
            param_err=float(param_err[0])
      
        return param_name,param_val


