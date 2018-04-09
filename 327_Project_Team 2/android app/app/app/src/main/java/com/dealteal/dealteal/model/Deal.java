package com.dealteal.dealteal.model;

public class Deal {

    private int id;
    private String publisher;
    private String description_small;
    private String description_long;
    private String keyword1;
    private String keyword2;
    private String keyword3;
    private String contact;
    private String validity;
        private String location;
    private Double latitude;
    private Double longitude;
    private String deal_logo;
    private String category;
    private String area;
    private String user;


    public Deal(){

    }

    public Deal(int id, String publisher, String description_small, String description_long, String keyword1, String keyword2, String keyword3,
                String contact, String validity, String location, Double latitude, Double longitude, String deal_logo, String category, String area, String user) {
        this.id = id;
        this.publisher = publisher;
        this.description_small = description_small;
        this.description_long = description_long;
        this.keyword1 = keyword1;
        this.keyword2 = keyword2;
        this.keyword3 = keyword3;
        this.contact = contact;
        this.validity = validity;
        this.location = location;
        this.latitude = latitude;
        this.longitude = longitude;
        this.deal_logo = deal_logo;
        this.category = category;
        this.area = area;
        this.user = user;
    }

    public int getId() {
        return id;
    }

    public String getPublisher() {
        return publisher;
    }

    public String getDescription_small() {
        return description_small;
    }

    public String getDescription_long() {
        return description_long;
    }

    public String getKeyword1() {
        return keyword1;
    }

    public String getKeyword2() {
        return keyword2;
    }

    public String getKeyword3() {
        return keyword3;
    }

    public String getContact() {
        return contact;
    }

    public String getValidity() {
        return validity;
    }

    public String getLocation() {
        return location;
    }

    public Double getLatitude() {
        return latitude;
    }

    public Double getLongitude() {
        return longitude;
    }

    public String getDeal_logo() {
        return deal_logo;
    }

    public String getCategory() {
        return category;
    }

    public String getArea() {
        return area;
    }

    public String getUser() {
        return user;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }

    public void setDescription_small(String description_small) {
        this.description_small = description_small;
    }

    public void setDescription_long(String description_long) {
        this.description_long = description_long;
    }

    public void setKeyword1(String keyword1) {
        this.keyword1 = keyword1;
    }

    public void setKeyword2(String keyword2) {
        this.keyword2 = keyword2;
    }

    public void setKeyword3(String keyword3) {
        this.keyword3 = keyword3;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }

    public void setValidity(String validity) {
        this.validity = validity;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public void setLatitude(Double latitude) {
        this.latitude = latitude;
    }

    public void setLongitude(Double longitude) {
        this.longitude = longitude;
    }

    public void setDeal_logo(String deal_logo) {
        this.deal_logo = deal_logo;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public void setArea(String area) {
        this.area = area;
    }

    public void setUser(String user) {
        this.user = user;
    }
}
