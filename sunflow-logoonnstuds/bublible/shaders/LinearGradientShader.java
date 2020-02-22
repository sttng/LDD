package bublible.shaders;

import org.sunflow.core.shader.ConstantShader;
import bublible.Utils;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.core.shader.AmbientOcclusionShader;
import org.sunflow.core.shader.AnisotropicWardShader;
import org.sunflow.core.shader.DiffuseShader;
import org.sunflow.core.shader.GlassShader;
import org.sunflow.core.shader.MirrorShader;
import org.sunflow.core.shader.PhongShader;
import org.sunflow.core.shader.ShinyDiffuseShader;
import org.sunflow.image.Color;

// mat398
public final class LinearGradientShader implements Shader {

    // GLASS NEEDS TO BE ALWAYS DEFFINED FIRST ELSE IT WON'T WORK AT ALL!!!!!
    boolean b1, b2, ok = false;
    Color c1, c2;
    String direction, s1, s2;
    float offset, gap, extent, center, hit;

    private final String n1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
    private final String n2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
    Shader $n1, $n2;

    public boolean update(ParameterList pl, SunflowAPI api) {
        if (!ok) {

            // one shot
            ok = true;

            direction = pl.getString("direction", direction);
            s1 = pl.getString("shader1", s1);
            c1 = pl.getColor("color1", c1);
            s2 = pl.getString("shader2", s2);
            c2 = pl.getColor("color2", c2);
            offset = pl.getFloat("offset", offset);
            gap = pl.getFloat("gap", gap);
            pl.clear(true);

            switch (s1) {
                case "diffuse":
                    // DIFFUSE
                    String nD1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    DiffuseShader $nD1 = new DiffuseShader();
                    api.parameter("diffuse", c1);
                    b1 = $nD1.update(pl, api);
                    $n1 = $nD1;
                    break;
                case "shiny":
                    // SHINY
                    String nS1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    ShinyDiffuseShader $nS1 = new ShinyDiffuseShader();
                    api.parameter("diffuse", c1);
                    api.parameter("reflection", 0.05f);
                    b1 = $nS1.update(pl, api);
                    $n1 = $nS1;
                    break;
                case "plastic":
                    // PLASTIC
                    String nP1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    PlasticShader $nP1 = new PlasticShader();
                    api.parameter("color", c1);
                    b1 = $nP1.update(pl, api);
                    $n1 = $nP1;
                    break;
                case "trans":
                    // TRANSPARENT
                    String nT1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    GlassShader $nT1 = new GlassShader();
                    api.parameter("color", c1);
                    api.parameter("eta", 1.6f);
                    b1 = $nT1.update(pl, api);
                    $n1 = $nT1;
                    break;
                case "glass":
                    // GLASS
                    String nG1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    GlassShader $nG1 = new GlassShader();
                    api.parameter("color", c1);
                    api.parameter("eta", 1.6f);
                    api.parameter("absorbtion.distance", 100f);
                    api.parameter("absorbtion.color", c1);
                    b1 = $nG1.update(pl, api);
                    $n1 = $nG1;
                    break;
                case "pearl":
                    // PEARL
                    String nPRL1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    PearlShader $nPRL1 = new PearlShader();
                    api.parameter("color", c1);
                    b1 = $nPRL1.update(pl, api);
                    $n1 = $nPRL1;
                    break;
                case "phong":
                    // PHONG
                    String nQ1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    PhongShader $nQ1 = new PhongShader();
                    api.parameter("diffuse", c1);
                    api.parameter("specular", c1);
                    api.parameter("power", 300f);
                    api.parameter("samples", 10);
                    b1 = $nQ1.update(pl, api);
                    $n1 = $nQ1;
                    break;
                case "metallic":
                    // ANISOTROPIC
                    String nA1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    AnisotropicWardShader $nA1 = new AnisotropicWardShader();
                    api.parameter("diffuse", c1);
                    api.parameter("specular", Color.WHITE);
                    api.parameter("roughnessX", 0.05f);
                    api.parameter("roughnessY", 0.05f);
                    api.parameter("samples", 1);
                    b1 = $nA1.update(pl, api);
                    $n1 = $nA1;
                    break;
                case "mirror":
                    // MIRROR
                    String nM1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    MirrorShader $nM1 = new MirrorShader();
                    api.parameter("color", c1);
                    b1 = $nM1.update(pl, api);
                    $n1 = $nM1;
                    break;
                case "stainedmirror":
                    // STAINED MIRROR
                    String nBM1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    StainedMirrorShader $nBM1 = new StainedMirrorShader();
                    api.parameter("color", c1);
                    b1 = $nBM1.update(pl, api);
                    $n1 = $nBM1;
                    break;
                case "ambient":
                    // AMBIENT OCCLUSION MIRROR
                    String nAO = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    AmbientOcclusionShader $nAO = new AmbientOcclusionShader();
                    api.parameter("bright", c2);
                    api.parameter("dark", new Color(0f, 0f, 0f));
                    api.parameter("samples", 4);
                    api.parameter("maxdist", 1000.0f);
                    b1 = $nAO.update(pl, api);
                    $n1 = $nAO;
                    break;
                case "constant":
                default:
                    // CONSTANT
                    String nC1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    ConstantShader $nC1 = new ConstantShader();
                    api.parameter("color", c1);
                    b1 = $nC1.update(pl, api);
                    $n1 = $nC1;
                    break;
            }
            pl.clear(true);

            switch (s2) {
                case "diffuse":
                    // DIFFUSE
                    String nD2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    DiffuseShader $nD2 = new DiffuseShader();
                    api.parameter("diffuse", c2);
                    b2 = $nD2.update(pl, api);
                    $n2 = $nD2;
                    break;
                case "shiny":
                    // SHINY
                    String nS2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    ShinyDiffuseShader $nS2 = new ShinyDiffuseShader();
                    api.parameter("diffuse", c2);
                    api.parameter("reflection", 0.05f);
                    b2 = $nS2.update(pl, api);
                    $n2 = $nS2;
                    break;
                case "plastic":
                    // PLASTIC
                    String nP2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    PlasticShader $nP2 = new PlasticShader();
                    api.parameter("color", c2);
                    b2 = $nP2.update(pl, api);
                    $n2 = $nP2;
                    break;
                case "trans":
                    // TRANSPARENT
                    String nT2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    GlassShader $nT2 = new GlassShader();
                    api.parameter("color", c2);
                    api.parameter("eta", 1.6f);
                    b2 = $nT2.update(pl, api);
                    $n2 = $nT2;
                    break;
                case "glass":
                    // GLASS
                    String nG2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    GlassShader $nG2 = new GlassShader();
                    api.parameter("color", c2);
                    api.parameter("eta", 1.6f);
                    api.parameter("absorbtion.distance", 100f);
                    api.parameter("absorbtion.color", c2);
                    b2 = $nG2.update(pl, api);
                    $n2 = $nG2;
                    break;
                case "pearl":
                    // PEARL
                    String nPRL2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    PearlShader $nPRL2 = new PearlShader();
                    api.parameter("color", c1);
                    b2 = $nPRL2.update(pl, api);
                    $n2 = $nPRL2;
                    break;
                case "phong":
                    // PHONG
                    String nQ2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    PhongShader $nQ2 = new PhongShader();
                    api.parameter("diffuse", c1);
                    api.parameter("specular", c1);
                    api.parameter("power", 300f);
                    api.parameter("samples", 10);
                    b2 = $nQ2.update(pl, api);
                    $n2 = $nQ2;
                    break;
                case "metallic":
                    // ANISOTROPIC
                    String nA2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    AnisotropicWardShader $nA2 = new AnisotropicWardShader();
                    api.parameter("diffuse", c2);
                    api.parameter("specular", Color.WHITE);
                    api.parameter("roughnessX", 0.05f);
                    api.parameter("roughnessY", 0.05f);
                    api.parameter("samples", 1);
                    b2 = $nA2.update(pl, api);
                    $n2 = $nA2;
                    break;
                case "mirror":
                    // MIRROR
                    String nM2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    MirrorShader $nM2 = new MirrorShader();
                    api.parameter("color", c2);
                    b2 = $nM2.update(pl, api);
                    $n2 = $nM2;
                    break;
                case "stainedmirror":
                    // STAINED MIRROR
                    String nBM2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    StainedMirrorShader $nBM2 = new StainedMirrorShader();
                    api.parameter("color", c2);
                    b2 = $nBM2.update(pl, api);
                    $n2 = $nBM2;
                    break;
                case "ambient":
                    // AMBIENT OCCLUSION MIRROR
                    String nAO = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    AmbientOcclusionShader $nAO = new AmbientOcclusionShader();
                    api.parameter("bright", c2);
                    api.parameter("dark", new Color(0f, 0f, 0f));
                    api.parameter("samples", 4);
                    api.parameter("maxdist", 1000.0f);
                    b2 = $nAO.update(pl, api);
                    $n2 = $nAO;
                    break;
                case "constant":
                default:
                    // CONSTANT
                    String nC2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    ConstantShader $nC2 = new ConstantShader();
                    api.parameter("color", c2);
                    b2 = $nC2.update(pl, api);
                    $n2 = $nC2;
                    break;
            }
            pl.clear(true);

            return (b1 && b2);
        }
        return true;
    }

    public Color getMaterialColor() {
        return Color.blend(c1, c2, offset);
    }

    public Color getRadiance(ShadingState state) {

        Color sA = $n1.getRadiance(state);
        Color sB = $n2.getRadiance(state);

        switch (direction) {
            case "y":
                // UP-DOWN
                extent = state.getInstance().getBounds().getExtents().y;
                center = state.getInstance().getBounds().getCenter().y;
                hit = state.getPoint().y;
                break;
            case "z":
                // FRONT-REAR
                extent = state.getInstance().getBounds().getExtents().z;
                center = state.getInstance().getBounds().getCenter().z;
                hit = state.getPoint().z;
                break;
            case "x":
            default:
                // LEFT-RIGHT
                extent = state.getInstance().getBounds().getExtents().x;
                center = state.getInstance().getBounds().getCenter().x;
                hit = state.getPoint().x;
                break;
        }
        center += offset * extent;

        // start gap
        float bot = center - extent * gap / 2f;

        // end gap
        float top = center + extent * gap / 2f;

        float fac = top - bot;

        // below the gap
        if (hit < bot) {
            return sA;
        }

        // above the gap
        if (hit > top) {
            return sB;
        }

        return Color.blend(sA, sB, (hit - bot) / fac);
    }

    @Override
    public void scatterPhoton(ShadingState state, Color power) {
    }

    @Override
    public float getReflectionValue() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
