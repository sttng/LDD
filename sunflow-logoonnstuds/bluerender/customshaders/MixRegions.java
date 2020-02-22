package bluerender.customshaders;

import bublible.Utils;
import org.sunflow.SunflowAPI;
import org.sunflow.core.ParameterList;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.core.shader.GlassShader;
import org.sunflow.core.shader.DiffuseShader;
import org.sunflow.core.shader.MirrorShader;
import org.sunflow.image.Color;
import org.sunflow.math.Point3;

// mat398
public final class MixRegions implements Shader {

    // GLASS NEEDS TO BE ALWAYS DEFFINED FIRST ELSE IT WON'T WORK AT ALL!!!!!
    boolean b1, b2, b3, ok = false;
    Color c = new Color  ( 0.8392157f, 0.93333334f, 0.9647059f );
    
    private final String n1 = "n" + Utils.rndRng(0,100) + Utils.rndRng(0,100) + Utils.rndRng(0,100);
    final GlassShader $n1 = new GlassShader();
    private final String n2 = "n" + Utils.rndRng(0,100) + Utils.rndRng(0,100) + Utils.rndRng(0,100);
    final GlassShader $n2 = new GlassShader();
    private final String n3 = "n" + Utils.rndRng(0,100) + Utils.rndRng(0,100) + Utils.rndRng(0,100);
    final DiffuseShader $n3 = new DiffuseShader();
    
    
    DiffuseShader ds = new DiffuseShader();
    GlassShader gs = new GlassShader();
    MirrorShader ms = new MirrorShader();

    /*Point2D start = new Point2D.Float(0, 0);
    Point2D end = new Point2D.Float(50, 50);
    float[] dist = {0.0f, 0.2f, 1.0f};
    Color[] cols = {Color.RED, Color.WHITE, Color.BLUE};
    LinearGradientPaint p = new LinearGradientPaint(start, end, dist, cols);*/

    public boolean update(ParameterList pl, SunflowAPI api)
    {
        if (!ok)
        {
            // one shot
            ok = true;
            
            float flt;
            flt = (float) c.getRGB()[0];
            
            api.parameter( "color", c );
            api.parameter( "eta", 1.6f );
            api.parameter( "absorbtion.distance", 100f );
            api.parameter( "absorbtion.color", c );
            b1 = $n1.update(pl, api);
            pl.clear(true);
            
            api.parameter( "color", Color.WHITE );
            api.parameter( "eta", 1.6f );
            api.parameter( "absorbtion.distance", 100f );
            api.parameter( "absorbtion.color", Color.WHITE );
            b2 = $n2.update(pl, api);
            pl.clear(true);

            // DIFFUSE
            api.parameter( "diffuse", c );
            b3 = $n3.update(pl, api);
            pl.clear(true);
            
            return (b1 && b2 && b3);
        }
        return true;
    }

    public Color getMaterialColor(){
        return c.toLinear();
    }

    public Color getRadiance(ShadingState state) {
        
        Color gg = $n1.getRadiance(state);
        Color ggW = $n2.getRadiance(state);
        Color pp = $n3.getRadiance(state);
        /*Color rColor = Color.blend(gg, ggW, 0.2f);
        return rColor;*/
        
        Color rColor = new Color(0f, 0f, 0f);
        
        // size of the blending region
        float gap = 1.0f;
        
        // offset from object centre of the blend position
        float offset = -0.25f;
        
        float extenty = state.getInstance().getBounds().getExtents().y;
        float centery = state.getInstance().getBounds().getCenter().y;
        centery += offset * extenty;
        
        // start gap
        float bot = centery - extenty * gap/2f;
        
        // end gap
        float top = centery + extenty * gap/2f;
        
        float fac = top - bot;
        float hit = state.getPoint().y;
        
        // below the gap
        if (hit < bot)
        {
            rColor.set(ggW);
            return rColor;
        }
        
        // above the gap
        if (hit > top)
        {
            rColor.set(ggW);
            return rColor;
        }
        
        // in the gap
        Point3 p = new Point3(state.getPoint()); // save point
        Color m = new Color( ggW );
        
        // restore point
        state.getPoint().set(p);
        Color g = new Color( pp );
        //rColor.set(Color.blend(m, g, 0.1f ));
        rColor.set(Color.blend(m, g, (hit - bot) / fac ));
        return rColor;
    }

    @Override
    public void scatterPhoton(ShadingState state, Color power) {
    }

    @Override
    public float getReflectionValue() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}