import React from 'react'
// import './Bestchamp.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'animate.css'

const BestChamp = ({ summoners, champion }) => {

    return (
      <div className="role-section bestchamp">
        <div className="table-section table-responsive animate__animated animate__zoomIn animate__delay-4s">
        <div className="rate_header">
        <h3>{`Best ${champion?.name} Players`}</h3>
        </div>
            
            <div className='tableContainer'>
                <table className="table table-borderless table-striped table-primary rounded">
                    <thead>
                        <tr>
                            <th scope="col">Summoner</th>
                            <th scope="col">Tier</th>
                            <th scope="col">Winrate</th>
                            <th scope="col">Played</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            summoners && summoners.length > 0 &&
                            summoners.map((summoner, index) => {
                                return (
                                    <tr key={index+1}>
                                        <td><span>{summoner?.summoner}</span></td>
                                        <td><span>{summoner?.tier}</span></td>
                                        <td>{summoner?.winrate}</td>
                                        <td>{summoner?.played}</td>
                                    </tr>
                                );
                            })

                        }
                    </tbody>
                </table>
            </div>
        </div>
        </div>
       
    )
}

export default BestChamp
