import React from 'react'
// import './Bestchamp.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import Role from '../../images/role.png'
// import pickrate from '../../images/pick.png'
// import winrate from '../../images/win.png'
import DonutChart from "../charts/DonutChart";


const RolesPerformance = ({ rolePerformance }) => {

    const avatarStyles = {
        verticalAlign: "middle",
        width: "2rem",
        height: "2rem",
        borderRadius: "50%",
    };

    const margin = {
        left: 10,
        top: 10,
        right: 10,
        bottom: 10
    };

    const svg = [100, 80];

    const size = [150, 150];

    return (
        <div className="role-section bestRole table-responsive rounded">
        <div className="rate_header">
        <h3>Roles</h3>
        </div>
            <div className="tableContainer">
                <table className="table table-borderless table-striped table-primary border border-1 rounded">
                    <thead>
                        <tr>

                            <th scope="col-4">Role</th>
                            <th scope="col-4">Winrate</th>
                            <th scope="col-4">Pickrate</th>

                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><img src={rolePerformance && rolePerformance["bot"]?.position_icon_url} alt="Bot" style={avatarStyles} /> <span>Bot</span></td>
                            <td><DonutChart data={rolePerformance && rolePerformance["bot"]?.win_rate}
                                size={size} svg={svg} margin={margin} color="blue"/>
                            </td>
                            <td><DonutChart data={rolePerformance && rolePerformance["bot"]?.pick_rate}
                                size={size} svg={svg} margin={margin} color="green"/>
                            </td>
                        </tr>
                        <tr>
                            <td><img src={rolePerformance && rolePerformance["mid"]?.position_icon_url} alt="Mid" style={avatarStyles} /> <span>Mid</span></td>
                            <td><DonutChart data={rolePerformance && rolePerformance["mid"]?.win_rate}
                                size={size} svg={svg} margin={margin} color="blue"/>
                            </td>
                            <td><DonutChart data={rolePerformance && rolePerformance["mid"]?.pick_rate}
                                size={size} svg={svg} margin={margin} color="green"/>
                            </td>
                        </tr>
                        <tr>
                            <td><img src={rolePerformance && rolePerformance["top"]?.position_icon_url} alt="Top" style={avatarStyles} /> <span>Top</span></td>
                            <td><DonutChart data={rolePerformance && rolePerformance["top"]?.win_rate}
                                size={size} svg={svg} margin={margin} color="blue"/>
                            </td>
                            <td><DonutChart data={rolePerformance && rolePerformance["top"]?.pick_rate}
                                size={size} svg={svg} margin={margin} color="green"/>
                            </td>
                        </tr>
                        <tr>
                            <td><img src={rolePerformance && rolePerformance["support"]?.position_icon_url} alt="Support" style={avatarStyles} /> <span>Support</span></td>
                            <td><DonutChart data={rolePerformance && rolePerformance["support"]?.win_rate}
                                size={size} svg={svg} margin={margin} color="blue"/>
                            </td>
                            <td><DonutChart data={rolePerformance && rolePerformance["support"]?.pick_rate}
                                size={size} svg={svg} margin={margin} color="green"/>
                            </td>
                        </tr>
                        <tr>
                            <td><img src={rolePerformance && rolePerformance["jungler"]?.position_icon_url} alt="Jungler" style={avatarStyles} /> <span>Jungler</span></td>
                            <td><DonutChart data={rolePerformance && rolePerformance["jungler"]?.win_rate}
                                size={size} svg={svg} margin={margin} color="blue"/>
                            </td>
                            <td><DonutChart data={rolePerformance && rolePerformance["jungler"]?.pick_rate}
                                size={size} svg={svg} margin={margin} color="green"/>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    )
}

export default RolesPerformance
