window.onload = function() {
    const urlParams = new URLSearchParams(window.location.search);
    const careerPath = urlParams.get('careerpath');
    const resultDiv = document.getElementById('result');
  
    const careerPaths = {
      HCM: 'Health Care and Medicine: Explore careers in health care, including doctors, nurses, and medical researchers.',
      ET: 'Education and Training: Discover opportunities in education and training, from teaching to corporate training programs.',
      IT: 'Information Technology: Learn about careers in IT, such as software development, network administration, and cybersecurity.',
      EngT: 'Engineering and Technology: Investigate careers in engineering and technology, including mechanical, civil, and electrical engineering.',
      BF: 'Business and Finance: Find out about careers in business and finance, from accounting to investment banking.',
      AH: 'Art and Humanities: Explore careers in the arts and humanities, including roles in museums, theaters, and libraries.',
      L: 'Law: Learn about careers in law, including lawyers, paralegals, and legal analysts.'
    };
  
    if (careerPath in careerPaths) {
      resultDiv.textContent = careerPaths[careerPath];
    } else {
      resultDiv.textContent = 'Invalid career path selected.';
    }
  };
  