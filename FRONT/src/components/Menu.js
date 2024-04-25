import React from "react";

import "./Components.css";

function Menu({ userName }) {

  return (
    <div className="menu_navbar pt-5">
      <div className="text-white">{userName}</div>
      <button
        className="btn btn-lg btn-dark rounded-pill btn-actions mt-3"
        title="Account"
      >
        <span className="material-symbols-outlined btn-user">person</span>
      </button>

      <button
        className="btn btn-lg btn-dark rounded-pill btn-actions mt-3"
        title="Account"
        type="button"
        data-bs-toggle="offcanvas"
        data-bs-target="#offcanvasExample"
        aria-controls="offcanvasExample"
      >
        <span className="material-symbols-outlined btn-user mt-2">favorite</span>
      </button>

      <div
        className="offcanvas offcanvas-end"
        tabindex="-1"
        id="offcanvasExample"
        aria-labelledby="offcanvasExampleLabel"

      >
        <div className="offcanvas-header">
          <h5 className="offcanvas-title" id="offcanvasExampleLabel">
            My favorite List
          </h5>
          <button
            type="button"
            className="btn-close text-reset"
            data-bs-dismiss="offcanvas"
            aria-label="Close"
          ></button>
        </div>
        <div className="offcanvas-body">
          <div>
            Favorite Cards
          </div>
        </div>
      </div>
    </div>
  );
}

export default Menu;
