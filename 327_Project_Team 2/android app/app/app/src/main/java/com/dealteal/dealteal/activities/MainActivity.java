package com.dealteal.dealteal.activities;


//import android.support.v4.app.Fragment;
import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.design.widget.NavigationView;
import android.support.multidex.MultiDex;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.MenuItem;

import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;
import com.dealteal.dealteal.R;
import com.dealteal.dealteal.adapters.RvAdapter;
import com.dealteal.dealteal.model.Deal;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private DrawerLayout mDrawerLayout ;
    private ActionBarDrawerToggle mToggle ;

    private final String JSON_URL =  "http://10.0.2.2:8000/deal/info/?format=json" ;

    private JsonArrayRequest request ;
    private RequestQueue requestQueue ;
    private List<Deal> lstDeal ;
    private RecyclerView recyclerView ;
    private RecyclerView.LayoutManager mLayoutManager;
    private RecyclerView.Adapter mAdapter;


    // Used to load the 'native-lib' library on application startup.
    static {
        System.loadLibrary("native-lib");
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
       // setContentView(R.layout.fragment_alldeals);

        lstDeal = new ArrayList<>();

        mDrawerLayout = (DrawerLayout) findViewById(R.id.drawer);
        mToggle = new ActionBarDrawerToggle(this,mDrawerLayout,R.string.open,R.string.close);
        mDrawerLayout.addDrawerListener(mToggle);
        mToggle.syncState();
        NavigationView nvDrawer = (NavigationView) findViewById(R.id.nv);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        setupDrawerContent(nvDrawer);

        recyclerView = (RecyclerView) findViewById(R.id.recyclerviewid);
        setuprecyclerview(lstDeal);

//        mLayoutManager = new LinearLayoutManager(this);
//        recyclerView.setLayoutManager(mLayoutManager);

//        mAdapter = new RvAdapter(this, lstDeal);
//        recyclerView.setAdapter(mAdapter);

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



            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

            }
        });

        requestQueue = Volley.newRequestQueue(MainActivity.this) ;
        requestQueue.add(request);


    }

    private void setuprecyclerview(List<Deal> lstDeal) {

        RvAdapter myadapter = new RvAdapter(this, lstDeal) ;
        //recyclerView.setLayoutManager(new LinearLayoutManager(this));
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        recyclerView.setAdapter(myadapter);

    }



    public void selectItemDrawer(MenuItem menuItem){

        //Fragment myFragment = new Fragment();
        android.support.v4.app.Fragment myFragment = null ;

        Class fragmentClass;
        switch (menuItem.getItemId()){
            case R.id.home:
                fragmentClass = Home.class;
                Intent intent = new Intent(this,MainActivity.class);
                break;
            case R.id.categories:
                fragmentClass = Categories.class;
                break;
            case R.id.alldeals:
                fragmentClass = Alldeals.class;
                break;
            case R.id.yourdeals:
                fragmentClass = Yourdeals.class;
                break;
            case R.id.about:
                fragmentClass = About.class;
                break;
            default:
                fragmentClass = Home.class;
        }

        try {
            //myFragment = (Fragment) fragmentClass.newInstance();
            myFragment = (android.support.v4.app.Fragment) fragmentClass.newInstance();

        }
        catch (Exception e){
            e.printStackTrace();
        }

        //FragmentManager fragmentManager = getSupportFragmentManager();
        android.support.v4.app.FragmentManager fragmentManager = getSupportFragmentManager();
      fragmentManager.beginTransaction().replace(R.id.flcontent,myFragment).commit();


        menuItem.setChecked(true);
        setTitle(menuItem.getTitle());
        mDrawerLayout.closeDrawers();

    }

    private void setupDrawerContent(NavigationView navigationView){

        navigationView.setNavigationItemSelectedListener(new NavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                selectItemDrawer(item);
                return true;
            }
        });

    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        if (mToggle.onOptionsItemSelected(item)){
            return true ;
        }
        return super.onOptionsItemSelected(item);
    }

    /**
     * A native method that is implemented by the 'native-lib' native library,
     * which is packaged with this application.
     */
   // public native String stringFromJNI();
}
