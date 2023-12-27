// FileUploader.js
import React, { useState} from 'react';
import * as websockets from 'isomorphic-ws';

export const Conexion = () => {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
  };

  const handleSendClick = async () => {
    if (file) {
      const serverUri = 'ws://localhost:5555';
      const websocket = new websockets.default(serverUri);
      const fileReader = new FileReader();

      fileReader.onload = (event) => {
        const data = event.target.result;
        websocket.send(data);
      };

      fileReader.readAsArrayBuffer(file);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleSendClick}>Enviar</button>
    </div>
  );
};

