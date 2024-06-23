import React, { useState } from 'react';
import axios from 'axios';

const HashtagRemover = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');

  const handleRemove = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8080/api/remove-hashtags/', { text });
      setResult(response.data.cleaned_text);
    } catch (error) {
      console.error('Error removing hashtags:', error);
    }
  };

  return (
    <div>
      <h2>Remove Hashtags</h2>
      <textarea value={text} onChange={(e) => setText(e.target.value)} />
      <button onClick={handleRemove}>Remove Hashtags</button>
      <p>Result: {result}</p>
    </div>
  );
};

export default HashtagRemover;