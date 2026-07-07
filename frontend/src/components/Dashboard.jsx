import Stats from "./Stats";
import Upload from "./Upload";
import DocumentList from "./DocumentList";
import Chat from "./Chat";

function Dashboard() {

    return (

        <div className="dashboard">

            <Stats />

            <Upload />

            <DocumentList />

            <Chat />

        </div>

    );

}

export default Dashboard;