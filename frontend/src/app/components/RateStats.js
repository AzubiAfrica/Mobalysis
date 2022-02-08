import React from 'react'

const RateStats = ({champion}) => {
    return (
        <React.Fragment>
            <div className="role-section ratestats table-responsive">
            <div className="rate_header">
            <h3>Stats</h3>
            </div>
                <div className='tableContainer'>
                    <table className="table table-borderless table-responsive table-striped table-rounded table-primary">
                        <thead>
                            <tr>

                                <th scope="col-4">Rate</th>
                                <th scope="col-4">Percent</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    Win Rate
                                </td>
                                <td>
                                    {champion?.win_rate}%
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    Pick Rate
                                </td>
                                <td>
                                {champion?.pick_rate}%
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    Ban Rate
                                </td>
                                <td>
                                {champion?.ban_rate}%
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    Pentas
                                </td>
                                <td>
                                    {champion?.pentasMatch || 0}
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    KDA
                                </td>
                                <td>
                            <span  className="pick">{champion?.kills}</span> /
                            <span className="win">{champion?.deaths}</span> /
                            <span className="ban">{champion?.assists}</span>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            {
                /*
                
                <div className="list-group">
                <div className="list-group-item active disabled">
                <span className="rate">Tier</span>
                <span className="rate">B</span>
                {
                   // <FontAwesomeIcon icon={faCaretUp} style={{color:'green'}}/>
                }
                
               </div>
                <div className="list-group-item">
                 <span className="rate">Win rate</span>
                 <span className="percent">47%</span>
                 {
                    // <FontAwesomeIcon icon={faCaretUp} style={{color:'green'}}/>
                 }
                 
                </div>
                <div className="list-group-item">
                <span className="rate">Pick rate</span>
                <span className="percent">4.7%</span>
                {
                    // <FontAwesomeIcon icon={faCaretDown} style={{color:'red'}}/>
                }
               
                </div>
                <div className="list-group-item">
                <span className="rate">Ban rate</span>
                <span className="percent">2.7%</span>
                {
                    // <FontAwesomeIcon icon={faCaretDown} style={{color:'red'}}/>
                }
                
                </div>
                <div className="list-group-item">
                <span className="rate">Pentas/Match</span>
                <span className="percent">0</span>  
                </div>
                <div className="list-group-item">
                <span className="rate">KDA</span>
                <span className="percent">5.6/4.8/5.8</span>
                </div>
                </div>
                */
            }
        </React.Fragment>
    )
}

export default RateStats
