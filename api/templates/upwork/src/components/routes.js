import React from 'react'
import { Route,Switch } from 'react-router-dom';
import Home from './Home.js'


function BaseRouter () {
    return (
        <Switch>
            <Route key="1" exact path="/home"component={Home} /> 
        </Switch>
    )
}

export default BaseRouter;
