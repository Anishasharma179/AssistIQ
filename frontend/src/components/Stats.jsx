import { useEffect, useState } from "react";
import api from "../api/api";

function Stats() {

    const [stats, setStats] = useState({
        documents: 0,
        chunks: 0,
        questions: 0
    });

    useEffect(() => {
        loadStats();
    }, []);

    async function loadStats() {

        try {

            const response = await api.get("/stats");

            setStats(response.data);

        } catch {

            console.log("Unable to load stats.");

        }

    }

    return (

        <div className="stats-grid">

            <div className="stat-card">
                <h2>{stats.documents}</h2>
                <p>Documents</p>
            </div>

            <div className="stat-card">
                <h2>{stats.chunks}</h2>
                <p>Knowledge Chunks</p>
            </div>

            <div className="stat-card">
                <h2>{stats.questions}</h2>
                <p>Questions</p>
            </div>

        </div>

    );

}

export default Stats;