import { FETCH_SUBWAY } from '../actions/index';

const initialState = {
    subwayList: [],
};


export default function (state = initialState, action) {
    switch(action.type) {
        case FETCH_SUBWAY:
            return { ...state, subwayList: action.payload.data };
        default:
            return state;
    }
}