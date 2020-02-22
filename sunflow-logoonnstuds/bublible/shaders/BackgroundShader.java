package bublible.shaders;

import org.sunflow.core.shader.ConstantShader;
import bublible.Utils;
import static bublible.Utils.clamp;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.core.shader.AnisotropicWardShader;
import org.sunflow.core.shader.DiffuseShader;
import org.sunflow.core.shader.ShinyDiffuseShader;
import org.sunflow.image.Color;

// mat309
public final class BackgroundShader implements Shader {

    boolean b1, b2, ok = false;
    Color c;
    float r;
    String s;

    private final String n1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
    Shader $n1;
    private final String n2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
    final ConstantShader $n2 = new ConstantShader();

    public boolean update(ParameterList pl, SunflowAPI api) {
        if (!ok) {
            // one shot
            ok = true;

            c = pl.getColor("color", c);
            r = pl.getFloat("ratio", r);
            s = pl.getString("shading", s);
            pl.clear(true);

            //System.out.println("Background/baseplane shading = " + s);

            switch (s) {
                case "shiny":
                    // SHINY
                    String nS = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    ShinyDiffuseShader $nS = new ShinyDiffuseShader();
                    api.parameter("diffuse", c);
                    api.parameter("reflection", 0.05f);
                    b1 = $nS.update(pl, api);
                    $n1 = $nS;
                    break;
                case "plastic":
                    // PLASTIC
                    String nP = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    PlasticShader $nP = new PlasticShader();
                    api.parameter("color", c);
                    b1 = $nP.update(pl, api);
                    $n1 = $nP;
                    break;
                case "metallic":
                    // ANISOTROPIC
                    String nA = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    AnisotropicWardShader $nA = new AnisotropicWardShader();
                    api.parameter("diffuse", c);
                    api.parameter("specular", Color.WHITE);
                    api.parameter("roughnessX", 0.05f);
                    api.parameter("roughnessY", 0.05f);
                    api.parameter("samples", 1);
                    b1 = $nA.update(pl, api);
                    $n1 = $nA;
                    break;
                default:
                    // DIFFUSE
                    String nD = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
                    DiffuseShader $nD = new DiffuseShader();
                    api.parameter("diffuse", c);
                    b1 = $nD.update(pl, api);
                    $n1 = $nD;
                    break;
            }
            pl.clear(true);

            // CONSTANT
            api.parameter("color", c);
            b2 = $n2.update(pl, api);
            pl.clear(true);

            return (b1 && b2);
        }
        return true;
    }

    public Color getMaterialColor() {
        return c;
    }

    public Color getRadiance(ShadingState state) {
        return Color.blend($n1.getRadiance(state), $n2.getRadiance(state), clamp(r, 0f, 1f)).clamp(0f, 1f);
    }

    @Override
    public void scatterPhoton(ShadingState state, Color power) {
    }

    @Override
    public float getReflectionValue() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
