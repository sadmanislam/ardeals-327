package com.dealteal.dealteal.activities;

import android.content.Context;
import android.media.Image;
import android.net.Uri;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;
import com.dealteal.dealteal.R;
import com.dealteal.dealteal.model.Deal;
import com.dealteal.dealteal.adapters.RvAdapter;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;


/**
 * A simple {@link Fragment} subclass.
 * Activities that contain this fragment must implement the
 * {@link Alldeals.OnFragmentInteractionListener} interface
 * to handle interaction events.
 * Use the {@link Alldeals#newInstance} factory method to
 * create an instance of this fragment.
 */
public class Alldeals extends Fragment {

    private final String JSON_URL =  "http://10.0.2.2:8000/deal/info/?format=json" ;

    private JsonArrayRequest request ;
    private RequestQueue requestQueue ;
    private List<Deal> lstDeal ;
    private RecyclerView recyclerView ;

//                                                                                                        // TODO: Rename parameter arguments, choose names that match
//                                                                                                        // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
//                                                                                                        private static final String ARG_PARAM1 = "param1";
//                                                                                                        private static final String ARG_PARAM2 = "param2";
//
//                                                                                                        // TODO: Rename and change types of parameters
//                                                                                                        private String mParam1;
//                                                                                                        private String mParam2;
//
//                                                                                                        private OnFragmentInteractionListener mListener;

                                                                                                        public Alldeals() {
                                                                                                            // Required empty public constructor
                                                                                                        }

//                                                                                                        /**
//                                                                                                         * Use this factory method to create a new instance of
//                                                                                                         * this fragment using the provided parameters.
//                                                                                                         *
//                                                                                                         * @param param1 Parameter 1.
//                                                                                                         * @param param2 Parameter 2.
//                                                                                                         * @return A new instance of fragment Alldeals.
//                                                                                                         */
//                                                                                                        // TODO: Rename and change types and number of parameters
//                                                                                                        public static Alldeals newInstance(String param1, String param2) {
//                                                                                                            Alldeals fragment = new Alldeals();
//                                                                                                            Bundle args = new Bundle();
//                                                                                                            args.putString(ARG_PARAM1, param1);
//                                                                                                            args.putString(ARG_PARAM2, param2);
//                                                                                                            fragment.setArguments(args);
//                                                                                                            return fragment;
//                                                                                                        }

//    @Override
//    public void onCreate(Bundle savedInstanceState) {
//        super.onCreate(savedInstanceState);
////        if (getArguments() != null) {
////            mParam1 = getArguments().getString(ARG_PARAM1);
////            mParam2 = getArguments().getString(ARG_PARAM2);
////        }
//
//        recyclerView = getView().findViewById(R.id.recyclerviewid) ;
//
//    }

//    @Override
//    public void onViewCreated(View view, Bundle savedInstanceState) {
//        super.onViewCreated(view, savedInstanceState);
//
//        lstDeal = new ArrayList<>() ;
//       // view.findViewById(R.id.recyclerviewid).setOnClickListener(this);
//        recyclerView = view.findViewById(R.id.recyclerviewid);
//        //recyclerView.setOnClickListener(this);
//        jsonrequest();
//
//
//     }

     @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        //View view = inflater.inflate(R.layout.fragment_alldeals,container,false);
        //ImageView imageView = (ImageView) view.findViewById(R.id.thumbnail);
        //return view;
         return inflater.inflate(R.layout.fragment_alldeals,container, false);
    }
    @Override
    public void onActivityCreated(Bundle savedInstanceState) {

        super.onActivityCreated(savedInstanceState);

        lstDeal = new ArrayList<>() ;
        View view = getView();
        recyclerView = view.findViewById(R.id.recyclerviewid);

        jsonrequest();

    }


     private void jsonrequest(){

     request = new JsonArrayRequest(JSON_URL, new Response.Listener<JSONArray>() {
         @Override
         public void onResponse(JSONArray response) {

             JSONObject jsonObject = null ;

             for (int i = 0; i < response.length(); i++){

                 try {
                     jsonObject = response.getJSONObject(i) ;
                     Deal deal = new Deal() ;
                     deal.setPublisher(jsonObject.getString("publisher"));
                     deal.setCategory(jsonObject.getString("category"));
                     deal.setDescription_small(jsonObject.getString("description_small"));
                     deal.setArea(jsonObject.getString("area"));
                     deal.setDeal_logo(jsonObject.getString("deal_logo"));
                     lstDeal.add(deal);

                 } catch (JSONException e) {
                     e.printStackTrace();
                 }


             }

            setuprecyclerview(lstDeal);

         }
     }, new Response.ErrorListener() {
         @Override
         public void onErrorResponse(VolleyError error) {

         }
     });

     requestQueue = Volley.newRequestQueue(getActivity().getApplicationContext()) ;
     requestQueue.add(request);


     }

    private void setuprecyclerview(List<Deal> lstDeal) {

        RvAdapter myadapter = new RvAdapter(getActivity(), lstDeal) ;
        //recyclerView.setLayoutManager(new LinearLayoutManager(this));
        recyclerView.setLayoutManager(new LinearLayoutManager(getActivity().getApplicationContext()));

        recyclerView.setAdapter(myadapter);

    }



//    // TODO: Rename method, update argument and hook method into UI event
//    public void onButtonPressed(Uri uri) {
//        if (mListener != null) {
//            mListener.onFragmentInteraction(uri);
//        }
//    }

//    @Override
//    public void onAttach(Context context) {
//        super.onAttach(context);
//
//    }
//
//    @Override
//    public void onDetach() {
//        super.onDetach();
//        mListener = null;
//    }
//
//        /**
//     * This interface must be implemented by activities that contain this
//     * fragment to allow an interaction in this fragment to be communicated
//     * to the activity and potentially other fragments contained in that
//     * activity.
//     * <p>
//     * See the Android Training lesson <a href=
//     * "http://developer.android.com/training/basics/fragments/communicating.html"
//     * >Communicating with Other Fragments</a> for more information.
//     */
//    public interface OnFragmentInteractionListener {
//        // TODO: Update argument type and name
//        void onFragmentInteraction(Uri uri);
//    }
}
