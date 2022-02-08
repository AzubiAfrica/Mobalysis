import React from 'react'
// import './ChampBanner.css'
import 'animate.css'


const ChampionBanner = ({champion}) => {
    const imageStyle = {
        width:'100%',
        height:'260px',
        objectFit:'cover',
        border: 'none',
        borderRadius: '16px',
        boxShadow: '0px 2px 2px 1px #d0d0d0'
    }
    const sectionStyles ={
        position:'relative',
        top:'3.5rem'
    }
    return (
           
           <div className="champbanner mt-3 animate__animated animate__zoomIn" style={sectionStyles}>
               <img src={champion?.image_url} alt={champion?.name} style={imageStyle} loading='lazy' />
               <h3>{champion?.name}</h3> 
           </div>
         
    )
}

export default ChampionBanner
