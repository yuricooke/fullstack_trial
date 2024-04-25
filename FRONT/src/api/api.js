
const postUser = async (nome, email) => {
  const formData = new FormData();
  formData.append('nome', nome);
  formData.append('email', email);

  let url = 'http://127.0.0.1:5000/user';
  return fetch(url, {
    method: 'POST',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

export { postUser };



const getList = async () => {
  let url = "http://127.0.0.1:5000/hikes";
  return fetch(url, {
    method: "GET",
  })
    .then((response) => response.json())
    .then((data) => {
      return data.hikes;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

export { getList };

const postFavorite = async (userId, hikeId) => {
  console.log(`userId: ${userId}`);
  console.log(`hikeId: ${hikeId}`);
  
  let url = 'http://127.0.0.1:5000/favorite';
  return fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      user_id: userId,
      hike_id: hikeId,
    }),
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

export { postFavorite };










// /*
//   --------------------------------------------------------------------------------------
// METHOD: GET - /cores e /paletas
//  --------------------------------------------------------------------------------------
// */
// const getList = async () => {
//   let url = 'http://127.0.0.1:5000/cores';
//   fetch(url, {
//     method: 'GET',
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       data.cores.forEach(item => insertList(item.nome, item.hex))
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//     });
// }

// getList()

// const getPaletteList = async () => {
//   let url = 'http://127.0.0.1:5000/paletas';
//   fetch(url, {
//     method: 'GET',
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       data.paletas.forEach(item => insertPaletteList(item.nome, item.neutral, item.primary, item.accent))
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//     });
// }


// getPaletteList()

// /*
// --------------------------------------------------------------------------------------
// METHOD: POST - /cor e /paleta
// --------------------------------------------------------------------------------------
// */

// const postItem = async (colorName, colorValue) => {
//   const formData = new FormData();
//   formData.append('nome', colorName);
//   formData.append('hex', colorValue);

//   let url = 'http://127.0.0.1:5000/cor';
//   fetch(url, {
//     method: 'POST',
//     body: formData
//   })
//     .then((response) => response.json())
//     .catch((error) => {
//       console.error('Error:', error);
//     });
// }
// const postPaletteItem = async (paletteName, paletteNeutral, palettePrimary, paletteAccent) => {
//   const formData = new FormData();
//   formData.append('nome', paletteName);
//   formData.append('neutral', paletteNeutral);
//   formData.append('primary', palettePrimary);
//   formData.append('accent', paletteAccent);


//   let url = 'http://127.0.0.1:5000/paleta';
//   fetch(url, {
//     method: 'POST',
//     body: formData
//   })
//     .then((response) => response.json())
//     .catch((error) => {
//       console.error('Error:', error);
//     });
// }

// /*
// --------------------------------------------------------------------------------------
// METHOD: DELETE - /cor e /paleta
// --------------------------------------------------------------------------------------
// */
// const deleteItem = (item) => {
//   console.log(item)
//   let url = 'http://127.0.0.1:5000/cor?nome=' + item;
//   fetch(url, {
//     method: 'DELETE'
//   })
//     .then((response) => response.json())
//     .catch((error) => {
//       console.error('Error:', error);
//     });
// }

// const deletePaletteItem = (item) => {
//   console.log(`paleta ${item} removida`)
//   let url = 'http://127.0.0.1:5000/paleta?nome=' + item;
//   fetch(url, {
//     method: 'DELETE'
//   })
//     .then((response) => response.json())
//     .catch((error) => {
//       console.error('Error:', error);
//     });
// }
