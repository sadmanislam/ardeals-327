using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class helpers : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}

}


public class JsonHelper{

	public static T[] getJsonArray<T>(string json)
	{
		string newJson = "{\"array\": " + json + "}";
		Wrapper<T> wrapper = JsonUtility.FromJson<Wrapper<T>> (newJson);
		return wrapper.array;

	}
	
	[System.Serializable]
	public class Wrapper<T>
	{
		public T[] array;

	}
		
}


[System.Serializable]
public class RootObject
{
	public int id { get; set; }
	public string publisher { get; set; }
	public string description_small { get; set; }
	public string description_long { get; set; }
	public string main_attraction { get; set; }
	public string genre { get; set; }
	public string contact { get; set; }
	public string validity { get; set; }
	public string address { get; set; }
	public string city { get; set; }
	public string country { get; set; }
	public int longitude { get; set; }
	public int latitude { get; set; }
	public string thumbnail { get; set; }
	public int type { get; set; }
	public int category { get; set; }
	public int area { get; set; }
	public int user { get; set; }
}

[System.Serializable]
public class DealList
{
	public List<RootObject> Deals;

}