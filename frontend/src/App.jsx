import "./App.css";

import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import Dashboard from "./components/Dashboard";

function App() {
    return (
        <div className="app">
            <Navbar />

            <div className="container">

                <Sidebar />

                <Dashboard />

            </div>
        </div>
    );
}

export default App;