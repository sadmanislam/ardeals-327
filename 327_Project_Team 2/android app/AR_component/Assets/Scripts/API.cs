using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;
using System.Linq;
using System.Linq.Expressions;
using System;

public class API : MonoBehaviour {

	// Use this for initialization
	void Start () {
		StartCoroutine(GetDeals());
	}

	/*IEnumerator getWWW()
	{
		// First define the url, this should be a valid url
		string url = "http://localhost:8000/deal/info/?format=json";

		WWW www = new WWW(url);
		while (!www.isDone)
			yield return null;

		if (string.IsNullOrEmpty (www.error)) {
			//Debug.Log (www.text);
			if (www.isDone){
				string jsonResult = System.Text.Encoding.UTF8.GetString (www.bytes);
				Debug.Log (jsonResult);
				RootObject[] entities = JsonHelper.getJsonArray<RootObject> (jsonResult);
			}
		} else
			Debug.Log (www.error);

	}*/


	IEnumerator GetDeals()
	{
		string url = "http://localhost:8000/deal/info/?format=json";

		using (UnityWebRequest www = UnityWebRequest.Get (url)) {
			//www.chunkedTransfer = false;
			yield return www.Send ();
			if (www.isNetworkError || www.isHttpError) {
				Debug.Log (www.error);
			} else {
				if (www.isDone) {
					string jsonResult = System.Text.Encoding.UTF8.GetString (www.downloadHandler.data);
					Debug.Log (jsonResult);

					RootObject[] entities = JsonHelper.getJsonArray<RootObject> (jsonResult);


					//Debug.Log (entities.Select(1).ToString);
					//Debug.Log (entities [0].longitude);
					Console.WriteLine(entities[0].latitude);
				
				}
				//ddlCountries.options.AddRange(entities.
			}
		}

	}

	void Update(){

	}

}
