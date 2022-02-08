import React from 'react'
import noData from '../../images/no_data.svg'
import noDataOne from '../../images/no_data_one.svg'
const NoData = () => {
   
     const avatarSTyled = {
        //  display:'flex',
        //  justifyContent:'center',
        //  alignItems:'center',
        //  flexDirection:'column',
         width:'100%',
         display:'block'
     }
    return (
        <React.Fragment>
           
            <div className="avatarShow" style={avatarSTyled}>
            <div className="imgAvatar">
            <img src={noDataOne } alt="no data" width="100" height="100"/>
            </div>
             <h3 className="text-white-20 mt-2"> OOOPS!</h3>
             <p className="text-dark mt-2">Data Not Available</p>
            </div>
          
        </React.Fragment>
    )
}

export default NoData
