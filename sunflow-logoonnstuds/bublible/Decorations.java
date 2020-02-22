package bublible;

import java.util.Arrays;
import java.util.HashMap;
import org.sunflow.math.Matrix4;

// Vectors manipulating methods
public class Decorations {

    private static boolean additionalDecorMapCreated = false;
    public static HashMap<String, Integer> decorMap = new HashMap<>();
    private static final String[] decorKnownTypes = {"2466p07", "2408p04", "2408p05",
        "2571", "3010p04", "3010p05", "3010p41", "3010p42", "3010p918", "3010p924",
        "3297p90", "3298p90", "3660p01", "3939p90", "3939p91", "4162pb012", "4760c01pb02",
        "4858p90", "4865p06", "6111pb011", "2340pb001", "3947", "61780tex02"};
    private static final String[] decorFacesA = {"2466p07", "2408p04", "2408p05",
        "2571", "3010p04", "3010p05", "3010p41", "3010p42", "3010p918", "3010p924", "3297p90",
        "3298p90", "3660p01", "3939p90", "3939p91", "4162pb012", "4858p90", "4865p06",
        "6111pb011"};
    private static final String[] decorFacesB = {"2340pb001", "3947"};
    private static final String[] decorFacesC = {};
    private static final String[] decorFacesD = {"4760c01pb02", "61780tex02"};

    /**
     * Adds new decoration layer to a brick.
     *
     * @param n brick designID
     * @return actual sequence number
     */
    public static int addDecorNameSequence(String n) {
        //
        if (!additionalDecorMapCreated) {
            for (String i : decorKnownTypes) {
                decorMap.put(i, 0);
            }
            additionalDecorMapCreated = true;
        }
        int i = decorMap.get(n);
        i++;
        decorMap.put(n, (int) i);
        return i;
    }

    /**
     * Returns number of faces for respective brick type.
     *
     * @param type
     * @return String array
     */
    public static int checkDecorFaces(String type) {
        int loops = 0;

        if (Arrays.asList(decorFacesA).contains(type)) {
            loops = 1;
        } else if (Arrays.asList(decorFacesB).contains(type)) {
            loops = 2;
        } else if (Arrays.asList(decorFacesC).contains(type)) {
            loops = 3;
        } else if (Arrays.asList(decorFacesD).contains(type)) {
            loops = 4;
        }

        return loops;
    }

    /**
     * Adds new decoration layer to a brick.
     *
     * @param matrix brick LDD matrix
     * @param type brick designID
     * @param loop actual decor face
     * @return
     */
    public static Matrix4 setAdditionalDecoration(String matrix, String type, int loop) {

        float sX, sY, sZ, tX, tY, tZ, r;
        Matrix4 m = Matrix4.IDENTITY;
        Matrix4 t;

        switch (type) {
            case "61780tex02":
                sX = 1f;
                sY = 1.3f;
                sZ = 1f;
                tX = -0.1f;
                tY = 0.62f;
                tZ = 0.351f;
                r = 0f;
                if (loop == 1) {
                    sX = -1f;
                    sY = 1.3f;
                    sZ = 1f;
                    tX = 0.9f;
                    tY = 0.62f;
                    tZ = -1.151f;
                } else if (loop == 2) {
                    sX = -1f;
                    sY = 1.3f;
                    sZ = 1f;
                    tX = -0.351f;
                    tY = 0.62f;
                    tZ = -0.9f;
                    r = 90f;
                } else if (loop == 3) {
                    sX = 1f;
                    sY = 1.3f;
                    sZ = 1f;
                    tX = 1.16f;
                    tY = 0.62f;
                    tZ = 0.1f;
                    r = 90f;
                }
                t = Matrix4.scale(sX, sY, sZ);
                m = t.multiply(m);
                t = Matrix4.rotateY((float) Math.toRadians(r));
                m = t.multiply(m);
                t = Matrix4.translation(tX, tY, tZ);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "2340pb001":
                sX = 5f;
                tX = -1.2f;
                tZ = 0.07738f;
                if (loop == 1) {
                    sX = -5f;
                    tX = 2.8f;
                    tZ = -0.07243f;
                }
                t = Matrix4.scale(sX, 3f, 1f);
                m = t.multiply(m);
                t = Matrix4.scale(0.8f);
                m = t.multiply(m);
                t = Matrix4.translation(tX, 0.32f, tZ);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "2466p07":
                t = Matrix4.scale(1.565f, 2.165f, 1f);
                m = t.multiply(m);
                t = Matrix4.translation(-0.385f, 1.82f, 2.004f);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "3010p04":
            case "3010p05":
            case "3010p41":
            case "3010p42":
            case "3010p918":
            case "3010p924":
                t = Matrix4.scale(3.18f, 0.95f, 1f);
                m = t.multiply(m);
                t = Matrix4.translation(-0.39f, 0f, 0.398f);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "3297p90":
                t = Matrix4.scale(3.2f, 1.756f, 1f);
                m = t.multiply(m);
                t = Matrix4.rotateX((float) Math.toRadians(-64.72f));
                m = t.multiply(m);
                t = Matrix4.translation(-0.39f, 0.20036f, 1.99f);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "3298p90":
                t = Matrix4.scale(1.6f, 1.756f, 1f);
                m = t.multiply(m);
                t = Matrix4.rotateX((float) Math.toRadians(-64.72f));
                m = t.multiply(m);
                t = Matrix4.translation(-0.39f, 0.20036f, 1.99f);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "3660p01":
                t = Matrix4.scale(1.58f, 1.15f, 1f);
                m = t.multiply(m);
                t = Matrix4.rotateX((float) Math.toRadians(45f));
                m = t.multiply(m);
                t = Matrix4.translation(-0.39f, 0f, 0.4f);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "3939p90":
            case "3939p91":
                t = Matrix4.scale(4.78f, 1.75f, 1f);
                m = t.multiply(m);
                t = Matrix4.rotateX((float) Math.toRadians(-64.72f));
                m = t.multiply(m);
                t = Matrix4.translation(-0.39f, 0.20036f, 1.99f);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "4162":
            case "4162pb012":
                t = Matrix4.scale(6.38f, 0.79f, 1f);
                m = t.multiply(m);
                t = Matrix4.rotateX((float) Math.toRadians(-90f));
                m = t.multiply(m);
                t = Matrix4.translation(-0.39f, 0.3115f, 0.39f);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "4865p06":
                t = Matrix4.scale(1.45f, 0.95f, 1f);
                m = t.multiply(m);
                t = Matrix4.translation(-0.32f, 0f, -0.398f);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "6111pb011":
                t = Matrix4.scale(7.97f, 0.95f, 1f);
                m = t.multiply(m);
                t = Matrix4.translation(-0.39f, 0f, 0.398f);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "3947":
                t = Matrix4.scale(4f);
                m = t.multiply(m);
                t = Matrix4.translation(12.4f, -0.201f, -12.7f);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "87552":
                t = Matrix4.scale(1.59f, 0.95f, 1f);
                m = t.multiply(m);
                t = Matrix4.translation(-0.39f, 0f, 0.401f);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "4858p90":
                t = Matrix4.scale(3.18f, 2.5f, 1f);
                m = t.multiply(m);
                t = Matrix4.rotateX((float) Math.toRadians(-72.55f));
                m = t.multiply(m);
                t = Matrix4.translation(-2.78f, 0.2035f, 2.79f);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "2408p04":
            case "2408p05":
                t = Matrix4.scale(4.79f, 4.5f, 1f);
                m = t.multiply(m);
                t = Matrix4.rotateX((float) Math.toRadians(-32f));
                m = t.multiply(m);
                t = Matrix4.translation(-0.39f, 4.8f, 0.4030001f);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "2571":
                t = Matrix4.scale(3.2f, 4.25f, 1f);
                m = t.multiply(m);
                t = Matrix4.translation(-0.4f, 0f, 0.4041f);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
            case "4760c01pb02":
                sX = 6.38f;
                sY = 1.95f;
                sZ = 1f;
                tX = -0.39f;
                tY = -1.645f;
                tZ = 0.4018f;
                r = 0f;
                if (loop == 1) {
                    sX = 3.18f;
                    sY = 1.95f;
                    sZ = 1f;
                    tX = 5.995f;
                    tY = -1.645f;
                    tZ = 0.4018f;
                    r = 90f;
                } else if (loop == 2) {
                    sX = -6.38f;
                    sY = 1f;
                    sZ = 1.95f;
                    tX = 5.99f;
                    tY = -1.645f;
                    tZ = -2.7887f;
                    r = 0f;
                } else if (loop == 3) {
                    sX = 3.18f;
                    sY = 1.95f;
                    sZ = 1f;
                    tX = -0.397f;
                    tY = -1.645f;
                    tZ = 0.4018f;
                    r = 90f;
                }
                t = Matrix4.scale(sX, sY, sZ);
                m = t.multiply(m);
                t = Matrix4.rotateY((float) Math.toRadians(r));
                m = t.multiply(m);
                t = Matrix4.translation(tX, tY, tZ);
                m = t.multiply(m);
                t = Matrix4.parseFrom4x3String(matrix);
                m = t.multiply(m);
                break;
        }
        return m;
    }
}
