import React, { useState } from 'react';
import axios from 'axios';

const HashtagGetter = () => {
  const [text, setText] = useState('');
  const [hashtags, setHashtags] = useState([]);

  const handleGet = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8080/api/get-hashtags/', { text });
      setHashtags(response.data.hashtags);
    } catch (error) {
      console.error('Error getting hashtags:', error);
    }
  };

  return (
    <div>
      <h2>Get Hashtags</h2>
      <textarea value={text} onChange={(e) => setText(e.target.value)} />
      <button onClick={handleGet}>Get Hashtags</button>
      <p>Hashtags: {hashtags.join(', ')}</p>
    </div>
  );
};

export default HashtagGetter;
