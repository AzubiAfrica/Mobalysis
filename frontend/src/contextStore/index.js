import { createContext, useReducer } from "react";

export const Store = createContext("");

// const gState = {
//     tokens: { accessToken: "", refreshToken: "" },
//     organization: false,
//     userProfile: {},
//     totalCart: 0,
//     cart: [],
//     jobCateg: [],
//     resetcredentials: "",
//     forumPostEdit: false,
//     forumPost: [],
//     currentPost: {},
//     posts: []
//   };

const gState = {
    champions: [],
    championStatistics: {},
    loading: false,
    filters: {
      region: 1,
      tier: 1,
      fgm: 1,
      role: 1,
      duration: 1,
      champion: 'All'
    }
};

const reducer = (state, action) => {
  switch (action.type) {
    case "SET_LOADING":
      return { ...state, loading: action.payload };
    case "UPDATE_FILTERS":
        return { ...state, filters: action.payload };
    case "UPDATE_CHAMPIONS":
        return {...state, champions: action.payload, loading:false };
    case "UPDATE_CHAMPION_STATISTICS":
        return {...state, championStatistics: action.payload, loading:false };

    default:
      return state;
  }
};

export const ContextWrapper = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, gState);
  return (
    <Store.Provider value={{ state, dispatch }}>{children}</Store.Provider>
  );
};
