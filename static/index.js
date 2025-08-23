// Function to create and append an article
function createArticle(title, imgSrc, imgAlt, text, publishedDateTime, customClass = '', imgClass = '') {
  const article = document.createElement('article');
  if (customClass) article.classList.add(customClass.split(','));

  const header = document.createElement('header');
  const h2 = document.createElement('h2');
  h2.textContent = title;
  header.appendChild(h2);

  const p = document.createElement('p');
  const img = document.createElement('img');
  img.src = imgSrc;
  img.alt = imgAlt;
  if (imgClass) img.classList.add(imgClass.split(','))
  p.appendChild(img);
  p.appendChild(document.createElement('br'));
  p.appendChild(document.createTextNode(text));

  const footer = document.createElement('footer');
  const pubP = document.createElement('p');
  pubP.textContent = `Publicado: ${publishedDateTime}`;
  footer.appendChild(pubP);

  article.appendChild(header);
  article.appendChild(p);
  article.appendChild(footer);

  document.getElementById('news-container').appendChild(article);
}

// Add all your articles here
createArticle(
  'Bienvenido a BrunNews!',
  'https://i.pinimg.com/736x/89/bf/a7/89bfa758bb284213368de4541d9e0e54.jpg',
  'Que buen servicio',
  'Las mejores noticias (En realidad son solo memes)',
  'Que buen servicio',
  'bienvenida',
  'que-buen-servicio'
);

createArticle(
  'Eso brad',
  'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjc0dmJsMGg2bnJmaDN3amNxN283NTUwZnR5MXg2OGM3NDdxNmxlaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RJddmVhFR04GisOuII/giphy.webp',
  'Alien bailongo',
  'Estatua de la libertad remplazada por un alien bailongo',
  '30.2.1600 6:66 am'
);

createArticle(
  'José 😡',
  'https://i.pinimg.com/736x/5e/a1/4e/5ea14e9b8352d04308f76d36efadba40.jpg',
  'José >:(',
  'José 😡',
  'José.😡.1807 10:61'
);

createArticle(
  'Se cayo el porton (si se que es IA pero esta chistoso igual)',
  'https://i.pinimg.com/736x/54/d8/96/54d8964d04ebf0d83e5d790f83e64abc.jpg',
  'Se cayo el porton',
  'Se cayo el porton 😭😭😭😭😭😭',
  '23.😭.1992 12:😭'
);

createArticle(
  'Imagenes de ultima momento de como escapo el alien bailongo',
  'https://media2.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZWVoaTdodGU3cmJtMDczYnV5dmR4NW94amY0MjkyNHc4czZuYXlicCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/UVBdBXssTeRW9eOnSm/200.webp',
  'alien balingo escapando del area 51',
  '',
  '23.12.1992 12:30'
);

createArticle(
  'Recuerdas el se me cayo el porton?',
  'https://i.pinimg.com/736x/19/bb/f8/19bbf8d615e1683637136dabf36ece0a.jpg',
  'Se me cayo el porton reaccion',
  'Ya le sacaron reaccion a mi porton',
  '25.25.2525 25:25'
);

createArticle(
  'Sata andagi!',
  'https://i.pinimg.com/736x/1a/e0/f1/1ae0f10e96107daf40adc5aa7d5092bf.jpg',
  '"Se dice Oaxaca!"',
  '"Se dice Oaxaca!"',
  'oh my gah'
)

createArticle(
  '"Prefiero ir a el refugio para gente sin hogar que agarrar la pala" -- El lema de los programadores Ada lovelace',
  'https://i.pinimg.com/736x/36/74/67/36746718b5ddbf9329b25b697df4bea7.jpg',
  'Si mas momos de Azumanga daio',
  'Si mas momos de Azumanga daio y que?',
  'Osaka where the f*ck did you got a seal?'
)
