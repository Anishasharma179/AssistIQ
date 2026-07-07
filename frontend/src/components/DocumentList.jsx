import { useEffect, useState } from "react";
import api from "../api/api";

function DocumentList() {

    const [documents, setDocuments] = useState([]);

    useEffect(() => {

        loadDocuments();

    }, []);

    const loadDocuments = async () => {

        const response = await api.get("/documents/");

        setDocuments(response.data);

    };

    return (

        <div className="card">

            <h2>Uploaded Documents</h2>

            <table>

                <thead>

                    <tr>

                        <th>ID</th>
                        <th>Filename</th>
                        <th>Type</th>

                    </tr>

                </thead>

                <tbody>

                    {documents.map((doc) => (

                        <tr key={doc.id}>

                            <td>{doc.id}</td>
                            <td>{doc.filename}</td>
                            <td>{doc.filetype}</td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default DocumentList;