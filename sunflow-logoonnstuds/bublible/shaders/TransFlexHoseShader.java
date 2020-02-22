package bublible.shaders;

import bublible.Utils;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.core.shader.GlassShader;
import org.sunflow.image.Color;

// 
public final class TransFlexHoseShader implements Shader {

    // GLASS NEEDS TO BE ALWAYS DEFFINED FIRST ELSE IT WON'T WORK AT ALL!!!!!
    boolean b1, b2, ok, okb = false;
    Color c;
    float offset, gap, extent, center, hit;
    Shader $n1, $n2;

    public boolean update(ParameterList pl, SunflowAPI api) {
        if (!ok) {

            // one shot
            ok = true;

            c = pl.getColor("color", c);
            offset = 0f;
            gap = 0.3f;
            pl.clear(true);

            // GLASS
            String nG = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
            GlassShader $nG = new GlassShader();
            api.parameter("color", c);
            api.parameter("eta", 1.6f);
            api.parameter("absorbtion.distance", 100f);
            api.parameter("absorbtion.color", c);
            b1 = $nG.update(pl, api);
            $n1 = $nG;
            pl.clear(true);

            // TRANS-CLEAR
            String nT = "n" + Utils.rndRng(0, 100) + Utils.rndRng(0, 100) + Utils.rndRng(0, 100);
            GlassShader $nT = new GlassShader();
            api.parameter("color", new Color(0.96666664f, 0.96666664f, 0.96666664f));
            api.parameter("eta", 1.6f);
            b2 = $nT.update(pl, api);
            $n2 = $nT;
            pl.clear(true);

            return (b1 && b2);
        }
        return true;
    }

    public Color getMaterialColor() {
        return c;
    }

    public Color getRadiance(ShadingState state) {

        Color farba = $n1.getRadiance(state);
        Color transclear = $n2.getRadiance(state);

        extent = state.getInstance().getBounds().getExtents().y;
        center = state.getInstance().getBounds().getCenter().y;
        hit = state.getPoint().y;
        center += offset * extent;

        // start gap
        float bot = center - extent * gap / 2f;

        // end gap
        float top = center + extent * gap / 2f;

        float fac = top - bot;

        // sides
        if (hit < bot || hit > top) {
            return transclear;
        }

        return farba;
    }

    @Override
    public void scatterPhoton(ShadingState state, Color power) {
    }

    @Override
    public float getReflectionValue() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
