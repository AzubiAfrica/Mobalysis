import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'

const ProgressBar = ({percentage,width,color}) => {
     const styleWidth = {
         width:`${width}`
     }
     const styleFont = {
         fontSize:'12px',
         fontWeight:'300'
     }

    return (
        <React.Fragment>
        <div className="progress">
        <div className={`progress-bar ${color}`} style={styleWidth}
         role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
         <h6 style={styleFont}>{percentage}</h6>
        </React.Fragment>
    )
}

export default ProgressBar
