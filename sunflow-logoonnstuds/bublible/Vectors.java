package bublible;

import org.sunflow.SunflowAPI;
import org.sunflow.core.parser.SCParser;
import org.sunflow.core.primitive.TriangleMesh;
import org.sunflow.core.tesselatable.FileMesh;

// Vectors manipulating methods
public class Vectors {

    private SCParser scp;

    /**
     * Draws simple 1x1 rectangle.
     *
     * @param api
     */
    public static void decorRectangle(SunflowAPI api) {
        // vertices
        float[] dataPoints = {0f, 0f, 0f, 0f, 1f, 0f, 1f, 1f, 0f, 1f, 0f, 0f};
        api.parameter("points", "point", "vertex", dataPoints);
        int[] dataTriangles = {0, 3, 2, 0, 2, 1};
        api.parameter("triangles", dataTriangles);
        // texture
        float[] dataUvs = {0f, 0f, 0f, 1f, 1f, 1f, 1f, 0f};
        api.parameter("uvs", "texcoord", "vertex", dataUvs);
        // apply it
        api.geometry("decorRectangle", new TriangleMesh());
    }

    /**
     * Draws simple 1x1 trapezium.
     *
     * @param api
     */
    public static void decor4858(SunflowAPI api) {
        // vertices
        float[] dataPoints = {0.25f, 0f, 0f, 0f, 1f, 0f, 1f, 1f, 0f, 0.75f, 0f, 0f};
        api.parameter("points", "point", "vertex", dataPoints);
        int[] dataTriangles = {0, 3, 2, 0, 2, 1};
        api.parameter("triangles", dataTriangles);
        // texture
        float[] dataUvs = {0.25f, 0f, 0f, 1f, 1f, 1f, 0.75f, 0f};
        api.parameter("uvs", "texcoord", "vertex", dataUvs);
        // apply it
        api.geometry("decor4858", new TriangleMesh());
    }

    /**
     * Draws decor mesh for brick 2340.
     *
     * @param api
     */
    public static void decor2340(SunflowAPI api) {
        // vertices
        float[] dataPoints = {0.2f, 0f, 0f,    0f, 1f, 0f,    0.4f, 1f, 0f,    1f, 0f, 0f};
        api.parameter("points", "point", "vertex", dataPoints);
        int[] dataTriangles = {0, 3, 2, 0, 2, 1};
        api.parameter("triangles", dataTriangles);
        // texture
        float[] dataUvs = {0.2f, 0f,    0f, 1f,    0.4f, 1f,    1f, 0f};
        api.parameter("uvs", "texcoord", "vertex", dataUvs);
        // apply it
        api.geometry("decor2340", new TriangleMesh());
    }

    /**
     * Draws inverse decor mesh for brick 2340.
     *
     * @param api
     */
    public static void decor2340inv(SunflowAPI api) {
        // vertices
        float[] dataPoints = {0f, 0f, 0f,    0.6f, 1f, 0f,    1f, 1f, 0f,    0.8f, 0f, 0f};
        api.parameter("points", "point", "vertex", dataPoints);
        int[] dataTriangles = {0, 3, 2, 0, 2, 1};
        api.parameter("triangles", dataTriangles);
        // texture
        float[] dataUvs = {0f, 0f,    0.6f, 1f,    1f, 1f,    0.8f, 0f};
        api.parameter("uvs", "texcoord", "vertex", dataUvs);
        // apply it
        api.geometry("decor2340inv", new TriangleMesh());
    }

    /**
     * Creates word "LEGO" vector for usage with brick studs.
     *
     * @param api
     */
    public static void LOSobject(SunflowAPI api) {
        api.parameter("filename", "bublible/obj/logoonstuds.obj");
        api.parameter("smooth_normals", true);
        api.geometry("logoonstuds", new FileMesh());
    }

    /**
     * Creates crater baseplate object from external .obj file.
     *
     * @param api
     */
    public static void craterBP(SunflowAPI api) {
        api.parameter("filename", "bublible/obj/3947g0.obj");
        api.parameter("smooth_normals", true);
        api.geometry("3947_studs", new FileMesh());

        api.parameter("filename", "bublible/obj/3947g1.obj");
        api.parameter("smooth_normals", true);
        api.geometry("3947_crater", new FileMesh());
    }

    /**
     * Adds new UV mapping for slope part of the brick. This is useful for
     * creating grainy surface on slope bricks as seen in real LEGO bricks.
     *
     * @param n brick designID
     * @param uvs original bricks UV mappings array
     * @return newly updated UV mappings array
     */
    public static float[] addSlopeUVS(String n, float[] uvs) {
        float[] tmp = uvs.clone();
        float[] u = {5.9604645E-8f, 0.0f, 0.99999976f, 1.0f, -2.9802322E-8f, 1.0f, 1.0f, 5.9604645E-8f};
        int[] offsets = new int[]{0};
        switch (n) {
            case "3046":
                offsets = new int[]{0, 3};
                break;
            case "3048":
            case "15571":
                offsets = new int[]{1, 5, 10};
                break;
            case "3297":
                offsets = new int[]{4};
                break;
            case "3300":
            case "3299":
                offsets = new int[]{4, 11};
                break;
            case "3043":
                offsets = new int[]{4, 12, 22};
                break;
            case "3044":
                offsets = new int[]{4, 22};
                break;
            case "3298":
                offsets = new int[]{5};
                break;
            case "3685":
                offsets = new int[]{5, 33};
                break;
            case "4161":
                offsets = new int[]{6};
                break;
            case "4861":
                offsets = new int[]{7, 23, 48};
                break;
            case "30363":
                offsets = new int[]{9};
                break;
            case "3042":
                offsets = new int[]{9, 17, 26};
                break;
            case "3675":
                offsets = new int[]{9, 42};
                break;
            case "3045":
                offsets = new int[]{15, 42};
                break;
            case "3049":
                offsets = new int[]{22, 43};
                break;
            case "4871":
                offsets = new int[]{23, 69};
                break;
            case "4286":
                offsets = new int[]{24};
                break;
            case "4460":
            case "30499":
                offsets = new int[]{25};
                break;
            case "52501":
                offsets = new int[]{25, 62};
                break;
            case "32083":
                offsets = new int[]{33, 49};
                break;
            case "2875":
                offsets = new int[]{36};
                break;
            case "3676":
                offsets = new int[]{36, 64};
                break;
            case "3038":
            case "2449":
                offsets = new int[]{37};
                break;
            case "4854":
                offsets = new int[]{38, 75};
                break;
            case "92946":
                offsets = new int[]{40};
                break;
            case "3660":
                //44
                offsets = new int[]{42};
                break;
            case "60477":
            case "4445":
                offsets = new int[]{45};
                break;
            case "18759":
                offsets = new int[]{46, 70};
                break;
            case "3665":
                offsets = new int[]{46};
                break;
            case "99301":
                offsets = new int[]{47, 54};
                break;
            case "2341":
                offsets = new int[]{49, 73};
                break;
            case "15647":
                offsets = new int[]{57, 73};
                break;
            case "72454":
                offsets = new int[]{95, 106};
                break;
            case "30183":
                //120,158
                offsets = new int[]{120, 158};
                break;
            case "30390":
                offsets = new int[]{129, 145};
                break;
            case "60219":
                offsets = new int[]{223, 267};
                break;
            case "30249":
                offsets = new int[]{36};
                break;
            case "4509":
                offsets = new int[]{9, 25};
                break;
            case "3037":
                offsets = new int[]{25};
                break;
            case "4858":
                //offsets = new int[]{170, 188};
                break;
            /*case "4287":
             //98
             offsets = new int[]{52,64,68,92,106,106,232};
             break;*/
            default:
                offsets = new int[]{0};
                break;
        }

        for (int i = 0; i < offsets.length; i++) {
            System.arraycopy(u, 0, tmp, offsets[i], 8);
        }
        return tmp;
    }
}
