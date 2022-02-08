import React, { useContext, useEffect, useState, useRef } from 'react'
import Filter from './Filter'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAngleLeft } from '@fortawesome/free-solid-svg-icons'
import { faSearch } from '@fortawesome/free-solid-svg-icons'
import { Link, NavLink } from 'react-router-dom'

const NavigationV1 = () => {
    const [backgroundColors,setbackgroundColor] = useState(false);

const changeBackground = () =>{
  if(window.scrollY >=30){
    setbackgroundColor(true);
  }else{
    setbackgroundColor(false);
  }
}
useEffect(()=>{
    changeBackground()
    window.addEventListener("scroll",changeBackground);
},[])
    return (
       
      <div className="filter-nav">
      <div className="row">
      <div className="col-lg-3"></div>
      <div className="col-lg-9">
      <div className={backgroundColors?'filter-section active':'filter-section'}>
                <div className="back-section">
                  <ol className="breadcrumb">
                    {/* <li className="breadcrumb-item"><Link to="/">
                      <FontAwesomeIcon icon={faAngleLeft} /> Back
                    </Link></li> */}
                    <li className="breadcrumb-item active" aria-current="page">Champions</li>
                  </ol>
                </div>
                <div className="search-section">
                  <Filter />
                </div>
              </div>
      </div>
      </div>
      </div>
    )
}

export default NavigationV1
