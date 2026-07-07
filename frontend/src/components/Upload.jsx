import { useState } from "react";
import api from "../api/api";

function Upload() {

    const [file, setFile] = useState(null);

    const [message, setMessage] = useState("");

    async function uploadFile() {

        if (!file) {

            alert("Choose a document first.");

            return;
        }

        const formData = new FormData();

        formData.append("file", file);

        try {

            const response = await api.post(
                "/upload/",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                }
            );

            setMessage(response.data.message);

        }

        catch {

            setMessage("Upload failed.");

        }

    }

    return (

        <div className="card">

            <h2>Upload Company Documents</h2>

            <p>
                Upload PDF, DOCX or TXT documents to build your knowledge base.
            </p>

            <input
                type="file"
                onChange={(e) => setFile(e.target.files[0])}
            />

            <button onClick={uploadFile}>

                Upload Document

            </button>

            <br /><br />

            <b>{message}</b>

        </div>

    );

}

export default Upload;