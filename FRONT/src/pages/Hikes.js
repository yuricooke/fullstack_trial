import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Menu from "../components/Menu";
import Background from "../components/Background";
import Carousel from "../components/Carousel";
import HikeCard from "../components/HikeCard";
import { getList } from "../api/api";
import UserContext from "../api/UserContext";

import "./Hikes.css";

export default function Hikes() {
  const navigate = useNavigate();
  const [hikeList, setHikeList] = useState([]);
  const [backgroundImage, setBackgroundImage] = useState("");
  const [selectedHike, setSelectedHike] = useState({});
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

  // Function to handle hike selection
  const handleBoxClick = (hike) => {
    setBackgroundImage(hike.imageUrl || "");
    setSelectedHike(hike);
  };

  return (
    <div className="Hikes">
      <Background id="Hikes" backgroundImage={`url(${backgroundImage})`} />
      <Menu userName={user ? user.nome : ""} /> {/* Pass user name to Menu */}

      <div className="row justify-content-end">
        <div className="col-lg-6 fixed-top Hikes_Content">
          <div className="Great_Hikes">
            <img
              src="https://yuricooke.com/mvp/great_hikes.svg"
              alt="Great Hikes"
              width="110px"
            />
            <h1>Great Hikes</h1>
          </div>
          <div className="Location">
            <p className="my-3">
              {selectedHike.continent} <span className="mx-3">|</span>{" "}
              {selectedHike.country}
            </p>
          </div>
          <div className="my-3 Info">
            <h2>{selectedHike.title}</h2>
            <p
              dangerouslySetInnerHTML={{
                __html: selectedHike.description,
              }}
            />
          </div>

          <div>
            <button
              className="btn btn-success rounded-pill explore"
              onClick={() => navigate(`/Hikes/${selectedHike.id}`)}
            >
              <span class="material-symbols-outlined">hiking</span> Let's hike!
            </button>
          </div>
        </div>
        <div className="col-lg-5 Carousel">
          <Carousel>
            {hikeList.map((hike) => (
              <HikeCard
                key={hike.id}
                image={hike.imageUrl}
                title={hike.title}
                continent={hike.continent}
                country={hike.country}
                onClick={() => handleBoxClick(hike)}
              />
            ))}
          </Carousel>
        </div>
      </div>
    </div>
  );
}
