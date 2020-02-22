package bublible;

import org.sunflow.SunflowAPI;
import org.sunflow.math.Matrix4;

// Transformation manipulations according to camera
public class World {

    /**
     * Applies camera rotation from LDD world to other objects so they facing
     * the camera exactly straight from the front.
     *
     * @param world2camera transformation camera matrix
     */
    public static void orientToCamera(Matrix4 world2camera) {
        float rotX, rotY, rotZ;
        if (world2camera.m00 == 1.0f) {
            rotX = (float) Math.toDegrees(0f);
            rotY = (float) Math.toDegrees((float) Math.atan2(world2camera.m02, world2camera.m23));
            rotZ = (float) Math.toDegrees(0f);
        } else if (world2camera.m00 == -1.0f) {
            rotX = (float) Math.toDegrees(0f);
            rotY = (float) Math.toDegrees((float) Math.atan2(world2camera.m02, world2camera.m23));
            rotZ = (float) Math.toDegrees(0f);
        } else {
            rotX = (float) Math.toDegrees((float) Math.asin(world2camera.m10));
            rotY = (float) Math.toDegrees((float) Math.atan2(-world2camera.m20, world2camera.m00));
            rotZ = (float) Math.toDegrees((float) Math.atan2(-world2camera.m12, world2camera.m11));
        }
        SunflowAPI.cameraRotX = (rotX < 0) ? 360 - Math.abs(rotX) : rotX;
        SunflowAPI.cameraRotY = (rotY < 0) ? 360 - (360 - Math.abs(rotY)) : 360 - rotY;
        SunflowAPI.cameraRotZ = (rotZ < 0) ? 360 - Math.abs(rotZ) : rotZ;
    }

    /**
     * Computes FDIST camera float value from brick's matrix
     *
     * @param camera camera matrix
     * @param brick brick LDD matrix
     * @return new float fdist value
     */
    public static float cameraFdistFromBrickMatrix(Matrix4 camera, Matrix4 brick) {

        float offset = 2.0f;
        float objX = brick.m03;
        float objZ = brick.m23;
        float camX = camera.m03;
        float camZ = camera.m23;

        float a = (float) Math.abs(objX - camX);
        float b = (float) Math.abs(objZ - camZ);
        float c = (float) Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2)) * offset;

        /*
         System.out.println("objX = " + objX);
         System.out.println("camX = " + camX);
         System.out.println("objZ = " + objZ);
         System.out.println("camZ = " + camZ);
         System.out.println("fdist = " + c);
         */
        return c;
    }
}
