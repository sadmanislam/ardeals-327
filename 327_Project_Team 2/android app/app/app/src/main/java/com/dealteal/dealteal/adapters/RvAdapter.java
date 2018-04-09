package com.dealteal.dealteal.adapters;

import android.content.Context;
import android.content.Intent;
import android.media.Image;
import android.support.annotation.NonNull;
import android.support.multidex.MultiDex;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;
import com.bumptech.glide.request.RequestOptions;
import com.dealteal.dealteal.R;
import com.dealteal.dealteal.activities.Alldeals;
import com.dealteal.dealteal.model.Deal;

import org.w3c.dom.Text;

import java.util.List;

public class RvAdapter extends RecyclerView.Adapter<RvAdapter.MyViewHolder>{

    private Context mContext ;
    private List<Deal> mData ;
    RequestOptions option;


    public RvAdapter(Context mContext, List<Deal> mData) {
        //this.mContext = mContext;
        this.mContext = mContext;
        this.mData = mData;


        //glide req

        option = new RequestOptions().centerCrop().placeholder(R.drawable.loading_shape).error(R.drawable.loading_shape);
    }


    @Override
    public RvAdapter.MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {

        View view ;
        LayoutInflater inflater = LayoutInflater.from(mContext) ;
        view = inflater.inflate(R.layout.deal_row_item,parent,false) ;
        return new MyViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull RvAdapter.MyViewHolder holder, int position) {

        holder.deal_publisher.setText(mData.get(position).getPublisher());
        holder.deal_category.setText(mData.get(position).getCategory());
        holder.deal_details.setText(mData.get(position).getDescription_small());
        holder.deal_area.setText(mData.get(position).getArea());

        //load img

        Glide.with(mContext).load(mData.get(position).getDeal_logo()).apply(option).into(holder.img_thumbnail);


    }

    @Override
    public int getItemCount() {
        return mData.size();
    }


    public static class MyViewHolder extends RecyclerView.ViewHolder{

        TextView deal_publisher;
        TextView deal_category;
        TextView deal_details;
        TextView deal_area;
        ImageView img_thumbnail;



        public MyViewHolder(View itemView){
            super(itemView);

            deal_publisher = itemView.findViewById(R.id.publisher);
            deal_category = itemView.findViewById(R.id.category);
            deal_details = itemView.findViewById(R.id.description_small);
            deal_area = itemView.findViewById(R.id.area);
            img_thumbnail = itemView.findViewById(R.id.thumbnail);


        }
    }
}