import { useState } from "react";
import api from "../api/api";

function Chat() {

    const [question, setQuestion] = useState("");

    const [answer, setAnswer] = useState("");

    const [loading, setLoading] = useState(false);

    async function askQuestion() {

        if (question === "") return;

        setLoading(true);

        try {

            const response = await api.post("/chat/", {
                question
            });

            setAnswer(response.data.answer);

        }

        catch {

            setAnswer("Unable to generate answer.");

        }

        setLoading(false);

    }

    return (

        <div className="card">

            <h2>Customer Support Assistant</h2>

            <textarea

                rows="5"

                placeholder="Ask your question..."

                value={question}

                onChange={(e) => setQuestion(e.target.value)}

            />

            <button onClick={askQuestion}>

                Ask AI

            </button>

            <br /><br />

            {

                loading

                    ?

                    <p>Generating answer...</p>

                    :

                    <div>

                        <h3>Response</h3>

                        <p>{answer}</p>

                    </div>

            }

        </div>

    );

}

export default Chat;