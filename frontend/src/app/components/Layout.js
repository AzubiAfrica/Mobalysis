import React from 'react';
import Navigation from './Navigation';
import NavigationV1 from './NavigationV1';
import Filter from './Filter'

const Layout = ({ children }) => {
	return (
		<div className="container">
			<main>
            <Navigation />
            {children}
            </main>
		</div>
	);
};

export default Layout;
