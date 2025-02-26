using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.Interaction.Toolkit.AR;

public class ARHousePlacement : MonoBehaviour
{
    public GameObject housePrefab; // Assign a 3D house model in Unity
    private ARRaycastManager arRaycastManager;
    private GameObject spawnedHouse;
    private List<ARRaycastHit> hits = new List<ARRaycastHit>();

    void Start()
    {
        arRaycastManager = FindObjectOfType<ARRaycastManager>();
    }

    void Update()
    {
        if (Input.touchCount > 0)
        {
            Touch touch = Input.GetTouch(0);
            if (touch.phase == TouchPhase.Began)
            {
                PlaceHouse(touch.position);
            }
        }
    }

    void PlaceHouse(Vector2 touchPosition)
    {
        if (arRaycastManager.Raycast(touchPosition, hits, UnityEngine.XR.ARSubsystems.TrackableType.PlaneWithinPolygon))
        {
            Pose hitPose = hits[0].pose;
            
            if (spawnedHouse == null)
            {
                spawnedHouse = Instantiate(housePrefab, hitPose.position, hitPose.rotation);
            }
            else
            {
                spawnedHouse.transform.position = hitPose.position;
            }
        }
    }
}
