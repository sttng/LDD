package bublible.shaders;

import bublible.Colors;
import bublible.Shaders;
import static bublible.Utils.rndRng;
import java.util.Random;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Ray;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.core.Texture;
import org.sunflow.image.Color;
import org.sunflow.math.OrthoNormalBasis;
import org.sunflow.math.Vector3;

public final class ShinyBluredShader implements Shader {

    private Color c;
    private Color spec;
    private Texture colmap;
    private Texture specmap;
    private float colBlend;
    private float specBlend;
    private final float glossyness = 1f;
    private final int numSamples = 2;
    private final int cislo = 20;
    private final int[] deleno = {cislo, cislo * -1};
    Random rand = new Random();
    Color randC = new Color(rand.nextFloat(), rand.nextFloat(), rand.nextFloat());
    private final int i = 0;
    private final int iOffset = 1;
    //private final Color[] cA = {Color.BLUE, Color.CYAN, Color.GREEN, Color.MAGENTA, Color.RED, Color.YELLOW};

    public ShinyBluredShader() {
    }

    public boolean update(ParameterList pl, SunflowAPI api) {
        c = pl.getColor("color", c);
        spec = Colors.bleech(0.5f, c);
        return true;
    }

    public Color getMaterialColor() {
        return c;
    }

    public Color getDiffuse(ShadingState state) {
        return colmap == null ? Shaders.getMixture(state, c, "shinyblured") : Color.blend(Shaders.getMixture(state, c, "shinyblured"), colmap.getPixel(state.getUV().x, state.getUV().y), colBlend);
    }

    public Color getSpecular(ShadingState state) {
        return specmap == null ? Shaders.getMixture(state, spec, "shinyblured") : Color.blend(Shaders.getMixture(state, spec, "shinyblured"), specmap.getPixel(state.getUV().x, state.getUV().y), specBlend);
    }

    public Color getRadiance(ShadingState state) {
        // make sure we are on the right side of the material
        state.faceforward();
        // direct lighting
        state.initLightSamples();
        state.initCausticSamples();
        Color d = getDiffuse(state);
        Color lr = state.diffuse(d);
        if (!state.includeSpecular()) {
            return lr;
        }
        Color csp = state.specularPhong(getSpecular(state), 4 / glossyness, numSamples);

        float cos = state.getCosND();
        float dn = 2 * cos;
        // compute Fresnel term
        cos = 1 - cos;
        float cos2 = cos * cos;
        float cos5 = cos2 * cos2 * cos;

        Vector3 refDir = new Vector3();
        refDir.x = (dn * state.getNormal().x) + state.getRay().getDirection().x + (float) Math.random() / deleno[rndRng(0, 1)];
        refDir.y = (dn * state.getNormal().y) + state.getRay().getDirection().y + (float) Math.random() / deleno[rndRng(0, 1)];
        refDir.z = (dn * state.getNormal().z) + state.getRay().getDirection().z + (float) Math.random() / deleno[rndRng(0, 1)];
        Ray refRay = new Ray(state.getPoint(), refDir);
        //System.out.println("cos = " + cos);

        if (cos > 0f && cos < 0.1f) {
            csp.mul(Color.WHITE).clamp(0f, 1f);
        } else if (cos >= 0.1f && cos < 0.2f) {
            csp.mul((float) Math.random() * 2 * c.g / 2).clamp(0f, 1f);
        } else if (cos >= 0.2f && cos < 0.3f) {
            csp.mul((float) Math.random() * 2 * c.b / 2).clamp(0f, 1f);
        } else if (cos >= 0.3f && cos < 0.4f) {
            csp.mul((float) Math.random() * c.r).clamp(0f, 1f);
        } else if (cos >= 0.4f && cos < 0.5f) {
            csp.mul((float) Math.random() * c.g).clamp(0f, 1f);
        } else if (cos >= 0.5f && cos < 0.6f) {
            csp.mul((float) Math.random() * c.b).clamp(0f, 1f);
        }

        /*
         if (i < iOffset) {
         csp.mul(1f).clamp(0f, 1f);
         i++;
         } else if (i >= iOffset && i < iOffset * 2) {
         csp.add(c.mul(1f).clamp(0f, 1f)).clamp(0f, 1f);
         i++;
         } else if (i >= iOffset * 2 && i < iOffset * 10) {
         i++;
         } else {
         i = 0;
         }
         */
        return lr.add(csp).add(state.specularPhong(getSpecular(state), 4 / glossyness, numSamples)).clamp(0f, 1f);
    }

    public void scatterPhoton(ShadingState state, Color power) {
        Color diffuse, specular;
        // make sure we are on the right side of the material
        state.faceforward();
        diffuse = getDiffuse(state);
        specular = getSpecular(state);
        state.storePhoton(state.getRay().getDirection(), power, diffuse);
        float d = diffuse.getAverage();
        float r = specular.getAverage();
        double rnd = state.getRandom(0, 0, 1);
        if (rnd < d) {
            // photon is scattered
            power.mul(diffuse).mul(1.0f / d);
            OrthoNormalBasis onb = state.getBasis();
            double u = 2 * Math.PI * rnd / d;
            double v = state.getRandom(0, 1, 1);
            float s = (float) Math.sqrt(v);
            float s1 = (float) Math.sqrt(1.0 - v);
            Vector3 w = new Vector3((float) Math.cos(u) * s, (float) Math.sin(u) * s, s1);
            w = onb.transform(w, new Vector3());
            state.traceDiffusePhoton(new Ray(state.getPoint(), w), power);
        } else if (rnd < d + r) {
            if (glossyness == 0) {
                float cos = -Vector3.dot(state.getNormal(), state.getRay().getDirection());
                power.mul(diffuse).mul(1.0f / d);
                // photon is reflected
                float dn = 2 * cos;
                Vector3 dir = new Vector3();
                dir.x = (dn * state.getNormal().x) + state.getRay().getDirection().x;
                dir.y = (dn * state.getNormal().y) + state.getRay().getDirection().y;
                dir.z = (dn * state.getNormal().z) + state.getRay().getDirection().z;
                state.traceReflectionPhoton(new Ray(state.getPoint(), dir), power);
            } else {
                float dn = 2.0f * state.getCosND();
                // reflected direction
                Vector3 refDir = new Vector3();
                refDir.x = (dn * state.getNormal().x) + state.getRay().dx;
                refDir.y = (dn * state.getNormal().y) + state.getRay().dy;
                refDir.z = (dn * state.getNormal().z) + state.getRay().dz;
                power.mul(spec).mul(1.0f / r);
                OrthoNormalBasis onb = state.getBasis();
                double u = 2 * Math.PI * (rnd - r) / r;
                double v = state.getRandom(0, 1, 1);
                float s = (float) Math.pow(v, 1 / ((1.0f / glossyness) + 1));
                float s1 = (float) Math.sqrt(1 - s * s);
                Vector3 w = new Vector3((float) Math.cos(u) * s1, (float) Math.sin(u) * s1, s);
                w = onb.transform(w, new Vector3());
                state.traceReflectionPhoton(new Ray(state.getPoint(), w), power);
            }
        }
    }

    @Override
    public float getReflectionValue() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
