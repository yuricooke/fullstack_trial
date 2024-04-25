import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import Background from "../components/Background";
import HikeCard from "../components/HikeCard";
import Reviews from "../components/Reviews";

import Menu from "../components/Menu";
import Button from "../components/Button";

// import hikes from "../data/hikes.json"; // Importação dos hikes
import { getList } from "../api/api";
import { postFavorite } from "../api/api";

import "./HikeDetails.css";

import UserContext from "../api/UserContext";

export default function HikeDetails() {
  const navigate = useNavigate();
  const [hikeList, setHikeList] = useState([]);
  const [backgroundImage, setBackgroundImage] = useState("");
  const [selectedHike, setSelectedHike] = useState(null); // Initialize selectedHike as null or an empty object
  const { user } = React.useContext(UserContext);

  // useEffect to fetch hike list
  useEffect(() => {
    getList().then((hikes) => {
      setHikeList(hikes || []);
    });
  }, []);

  // useEffect to set background image and selected hike
  useEffect(() => {
    if (hikeList.length > 0) {
      setBackgroundImage(hikeList[0]?.imageUrl || "");
      setSelectedHike(hikeList[0] || {});
    }
  }, [hikeList]);

  const { id } = useParams();
  const parsedId = parseInt(id, 10);

  useEffect(() => {
    const foundHike = hikeList.find((hike) => hike.id === parsedId);
    if (foundHike) {
      setSelectedHike(foundHike);
      setBackgroundImage(foundHike.imageUrl || "");
    }
  }, [parsedId, hikeList]);

  if (!selectedHike) {
    console.log("Selected hike is loading");
    return <div>Loading...</div>;
  }

  if (!selectedHike || !selectedHike.title) {
    return <div>No title available</div>;
  }
  
  if (!selectedHike.title) {
    console.log("Project title is null or undefined");
    return <div>No title available</div>;
  }

  // console.log("Selected Hike:", selectedHike);

  // Filter hikes in the same continent as selectedHike
  const sameContinentHikes = hikeList.filter(
    (hike) =>
      hike.continent === selectedHike.continent && hike.id !== selectedHike.id
  );

  const handleFavoriteClick = async () => {
    if (!user || !user.id) {
      console.log("User is not logged in or user ID is not available");
      return;
    }

    try {
      const response = await postFavorite(user.id, selectedHike.id);

      if (!response.ok) {
        throw new Error("Failed to update favorites");
      }

      console.log("Hike added to favorites");
    } catch (error) {
      console.error("Failed to update favorites:", error);
    }
  };

  return (
    <>
      <div>
        <Background
          id="Hikes"
          className="Background"
          backgroundImage={`url(${backgroundImage})`}
        />
        <Menu userName={user ? user.nome : ""} /> {/* Pass user name to Menu */}
      </div>
      <div className="HikeDetails">
        <div className="mb-3">
          <Button
            label="Go Back!"
            icon="return"
            iconPosition="left"
            className="IconButton"
            onClick={() => navigate(`/Hikes`)}
          />
        </div>
        <div className="hikedetails_title">
          <div className="Great_Hikes">
            <img
              src="https://yuricooke.com/mvp/great_hikes.svg"
              alt="Great Hikes"
              width="50px"
            />
            <h3>Great Hikes</h3>
          </div>
          <div className="country">
            <span>{selectedHike.country}</span>
          </div>

          <div className="d-hikedetails_title--title">
            <h1 className="text-white">{selectedHike.title}</h1>
            <button
              className="btn btn-lg btn-dark shadow rounded-pill btn-actions"
              title="Favorite it"
              onClick={handleFavoriteClick}
            >
              <span class="material-symbols-outlined">favorite</span>
            </button>
            <button
              className="btn btn-lg btn-dark shadow rounded-pill btn-actions"
              title="Rate it"
            >
              <span class="material-symbols-outlined">star</span>
            </button>
            <button
              className="btn btn-lg btn-dark shadow rounded-pill btn-actions"
              title="Find groups"
            >
              <span class="material-symbols-outlined">groups</span>
            </button>
          </div>
        </div>
        <div className="hikedetails_card">
          <div className="row">
            <div className="col-lg-6 me-lg-5">
              <h4 className="mb-3">HIKING</h4>
              <p>{selectedHike.hikingExplained}</p>
              <h4 className="mb-3 mt-5">GALLERY</h4>
              <img
                className="img-fluid"
                src={selectedHike.imageUrl}
                alt={selectedHike.title}
              />
              <h4 className="mb-3 mt-5">EXPLORE +</h4>
              <div className="explore">
                <button className="btn btn-dark rounded-pill explore">
                  Official Site
                  <span class="material-symbols-outlined">computer</span>
                </button>
                <button className="btn btn-dark rounded-pill explore">
                  Maps<span class="material-symbols-outlined">map</span>
                </button>
                <button className="btn btn-dark rounded-pill explore">
                  Contact<span class="material-symbols-outlined">phone</span>
                </button>
              </div>
              <h4 className="mb-3 mt-5">FROM HIKERS</h4>

              <Reviews />
            </div>

            <div className="col-lg-5 ms-lg-5 ps-lg-5 border-start">
              <div className="d-flex align-items-start mb-5">
                <h4 className="mt-1 me-3">Location</h4>
              </div>
              <div className="gmp-map">
                <gmp-map
                  center={`${selectedHike.lat},${selectedHike.lng}`}
                  zoom="6"
                  map-id="DEMO_MAP_ID"
                >
                  <gmp-advanced-marker
                    position={`${selectedHike.lat},${selectedHike.lng}`}
                    title={selectedHike.title}
                  ></gmp-advanced-marker>
                </gmp-map>
              </div>
              <div className="d-flex flex-column justify-content-center mb-5">
                {/* <img
                  className="map-control img-fluid"
                  src={selectedHike.map}
                  alt={selectedHike.title}
                /> */}
                <button className="btn btn-dark w-25 align-self-end me-3 rounded-pill mt-3">
                  GPS Coordinates
                </button>
              </div>

              <h4>Hikes in {selectedHike.continent}</h4>

              <div>
                {/* Render HikeCard components for hikes in the same continent */}
                {sameContinentHikes.slice(0, 6).map((hike) => (
                  <HikeCard
                    key={hike.id}
                    image={hike.imageUrl}
                    title={hike.title}
                    continent={hike.continent}
                    country={hike.country}
                    onClick={() => navigate(`/Hikes/${hike.id}`)}
                  />
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
