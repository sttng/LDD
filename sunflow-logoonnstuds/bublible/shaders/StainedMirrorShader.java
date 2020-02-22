package bublible.shaders;

import static bublible.Utils.rndRng;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Ray;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.image.Color;
import org.sunflow.math.Vector3;

public class StainedMirrorShader implements Shader {

    private Color color;
    private final int cislo = 10;
    private final int[] deleno = {cislo, cislo * -1};

    public StainedMirrorShader() {
        this.color = Color.WHITE;
    }

    public boolean update(ParameterList pl, SunflowAPI api) {
        color = pl.getColor("color", color);
        return true;
    }

    public Color getMaterialColor() {
        return color;
    }

    public Color getRadiance(ShadingState state) {
        if (!state.includeSpecular()) {
            return Color.BLACK;
        }
        state.faceforward();
        float cos = state.getCosND();
        float dn = 2 * cos;
        Vector3 refDir = new Vector3();

        refDir.x = (dn * state.getNormal().x) + state.getRay().getDirection().x + (float) Math.random() / (deleno[rndRng(0, 1)]);
        refDir.y = (dn * state.getNormal().y) + state.getRay().getDirection().y + (float) Math.random() / (deleno[rndRng(0, 1)]);
        refDir.z = (dn * state.getNormal().z) + state.getRay().getDirection().z + (float) Math.random() / (deleno[rndRng(0, 1)]);
        Ray refRay = new Ray(state.getPoint(), refDir);

        // compute Fresnel term
        cos = 1 - cos;
        float cos2 = cos * cos;
        float cos5 = cos2 * cos2 * cos;

        Color ret = Color.white();
        
        ret.sub(color);
        ret.mul(cos5);
        ret.add(color);
        return ret.mul(state.traceReflection(refRay, 0));
    }

    public void scatterPhoton(ShadingState state, Color power) {
        float avg = color.getAverage();
        double rnd = state.getRandom(0, 0, 1);
        if (rnd >= avg) {
            return;
        }
        state.faceforward();
        float cos = state.getCosND();
        power.mul(color).mul(1.0f / avg);
        // photon is reflected
        float dn = 2 * cos;
        Vector3 dir = new Vector3();
        dir.x = (dn * state.getNormal().x) + state.getRay().getDirection().x;
        dir.y = (dn * state.getNormal().y) + state.getRay().getDirection().y;
        dir.z = (dn * state.getNormal().z) + state.getRay().getDirection().z;
        state.traceReflectionPhoton(new Ray(state.getPoint(), dir), power);
    }

    @Override
    public float getReflectionValue() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
