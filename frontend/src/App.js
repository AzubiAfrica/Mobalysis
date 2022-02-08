import React from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import { ContextWrapper } from "./contextStore";
import ChampionsV1 from './app/layouts/ChampionsV1';
import ChampionStatsV1 from './app/layouts/ChampionStatsV1';
import Layout from './app/components/Layout'



function App() {
 
  return (
    <ContextWrapper>
      <Router>
        <Layout>
        {
          // <Navigation/> 
        }
          <Switch>
            <Route exact path="/" component={ChampionsV1} />
            <Route exact path="/championstats/:id" component={ChampionStatsV1} />
          </Switch>
        </Layout>
      </Router>
    </ContextWrapper>
  );
}

export default App
