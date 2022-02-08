import React from 'react'
import Conqueror from '../../images/Conqueror.png'
import 'bootstrap/dist/css/bootstrap.min.css'

const SituationalItems = () => {
    return (
        <React.Fragment>
        <div className="container">
            <div className="items-section">
            <div className="itemsheader">
            <h3>AATROX SITUATIONAL ITEMS</h3>
            <div className="sep"></div>
            <div className="situationalComp">
            <div className="sitautionImg">
            <div className="SIMG">
            <div><img src={Conqueror} alt="conq" width="40" height="40"/></div>
            </div>
            <div className="SIMG1">
            <div><img src={Conqueror} alt="conq" width="40" height="40"/></div>
            </div>
            <div className="SIMG1">
            <div><img src={Conqueror} alt="conq" width="40" height="40"/></div>
            </div>
            <div className="SIMG1">
            <div><img src={Conqueror} alt="conq" width="40" height="40"/></div>
            </div>
            </div>
            <div className="sitautionText">
            <div className="itemsheader blacktext">
            <h3>Black Clever</h3>
            </div>
            <p className="paraText">Pick Black Cleaver up when you're against enemies who will be building tank items.</p>
            
            </div>
            </div>
        </div>
            </div>
            </div>
        </React.Fragment>
    )
}

export default SituationalItems
