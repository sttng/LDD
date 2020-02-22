package bublible.shaders;

import bublible.Colors;
import bublible.Utils;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.core.shader.DiffuseShader;
import org.sunflow.image.Color;

public final class RubberShader implements Shader {

    // GLASS NEEDS TO BE ALWAYS DEFFINED FIRST ELSE IT WON'T WORK AT ALL!!!!!
    boolean b1, b2, ok = false;
    Color d = new Color(0.01f, 0.01f, 0.01f);
    Color c;
    ParameterList prmL;
    SunflowAPI sfA;

    private final String n1 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
    final DiffuseShader $n1 = new DiffuseShader();
    private final String n2 = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
    final PlasticShader $n2 = new PlasticShader();
    final float makeLighter = 0.03f;

    public RubberShader() {
    }

    public boolean update(ParameterList pl, SunflowAPI api) {
        if (!ok) {

            // one shot
            ok = true;

            c = pl.getColor("color", c);
            pl.clear(true);

            // DIFFUSE
            api.parameter("diffuse", new Color(c.r + makeLighter, c.g + makeLighter, c.b + makeLighter));
            b1 = $n1.update(pl, api);
            pl.clear(true);

            // PLASTIC
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
        Color ds = $n1.getRadiance(state);
        Color ps = $n2.getRadiance(state);
        Color rColor = Colors.blend(ds, ps, 0.5f);
        return rColor;
    }

    @Override
    public void scatterPhoton(ShadingState state, Color power) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated metho$n2, choose Tools | Templates.
    }

    @Override
    public float getReflectionValue() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated metho$n2, choose Tools | Templates.
    }
}
