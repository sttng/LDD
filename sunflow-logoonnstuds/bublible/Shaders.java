package bublible;

import static bublible.Utils.rndRng;
import bublible.shaders.ChromeShader;
import bublible.shaders.MetallicShader;
import bublible.shaders.PearlShader;
import bublible.shaders.PlasticShader;
import java.io.FileNotFoundException;
import org.sunflow.SunflowAPI;
import org.sunflow.core.Shader;
import org.sunflow.core.ShadingState;
import org.sunflow.core.Texture;
import org.sunflow.core.parser.SCParser;
import org.sunflow.core.primitive.Background;
import org.sunflow.core.shader.DiffuseShader;
import org.sunflow.core.shader.ShinyDiffuseShader;
import org.sunflow.core.shader.TexturedDiffuseShader;
import org.sunflow.image.Color;

// Additional shader functions
public class Shaders {

    private static Utils q;

    /**
     * Return mixture color output between color and texture.
     *
     * @param s ShadingState object
     * @param d material color
     * @param st alias for shader type in pure text format
     * @return mixed "color/texture" color output
     */
    public static Color getMixture(ShadingState s, Color d, String st) {

        //System.out.println("tex = " + s.getInstance().getTexture());
        /*if (st.equals("constant")) {
            Texture tex = s.getInstance().getTexture();
            if (tex == null) {
                return d;
            }
            return d;
        }*/
        
        // Background
        if(s.getNormal() == null){
            return d;
        }

        float x = s.getUV().x;
        float y = s.getUV().y;

        Texture tex = s.getInstance().getTexture();
        if (tex == null || x < 0 || y < 0 || x >= 1 || y >= 1) {
            return d;
        }

        int alpha = tex.getAlpha(x, y);
        if (alpha == 0) {
            return d;
        }

        Color texture = tex.getPixel(x, y);
        if (alpha == 255) {
            return texture;
        }

        float a = (float) alpha / 255f;
        return Color.add(Color.mul(a, texture), Color.mul(1f - a, d));
    }

    /**
     * Sets different graphic effects to final image output.
     *
     * @param state ShadingState object
     * @param shader actual shader being used
     */
    public static void imageFX(ShadingState state, Shader shader) {

        switch (SCParser.imagefx) {
            case "DarkLumina":
                state.setResult(shader.getRadiance(state).sub(shader.getMaterialColor()));
            case "ChildPainting":
                state.setResult(shader.getMaterialColor());
            case "PseudoNeon":
                state.setResult(shader.getRadiance(state).div(shader.getMaterialColor()));
            case "ShadedPainting":
                state.setResult(shader.getRadiance(state).add(shader.getMaterialColor()));
            case "BW":
                state.setResult(shader.getRadiance(state).mul(shader.getMaterialColor()).clamp(0f, 1f));
            case "TransBitsOnBlack":
                state.setResult(shader.getRadiance(state).sub(shader.getRadiance(state)));
            case "AcidSaturo":
                state.setResult(shader.getRadiance(state).sub(shader.getRadiance(state).opposite()));
            default:
                state.setResult(shader.getRadiance(state));
        }
    }

    /**
     * Creates the right material for decorated baseplates.
     *
     * @param api SUnflowAPI
     * @param tex texture
     * @param colr material color
     * @param name brick name
     * @throws java.io.FileNotFoundException
     */
    public static void exactDecoratedBP(SunflowAPI api, String tex, Color colr, String name) throws FileNotFoundException {
        api.parameter("diffuse", Color.blend(colr, Color.WHITE, 0.1f));
        if (tex == null) {
            api.shader(name + "BP", new DiffuseShader());
        } else {
            api.shader(name + "BP", new TexturedDiffuseShader());
        }
    }

    /**
     * Creates color variations of specific material.
     *
     * @param api SunflowAPI
     * @param shdr name of original shader
     * @param strength how strongly is that color change visible
     * @return name of newly created color variation material
     * @throws java.io.FileNotFoundException
     */
    public static String shaderColorVariations(SunflowAPI api, String shdr, float strength) throws FileNotFoundException {

        String newShader = shdr + "_var" + api.colVars;
        api.colVars++;
        Shader k = api.lookupShader(shdr);
        Color c = k.getMaterialColor();
        String ns = shdr;

        if (k instanceof ShinyDiffuseShader || k instanceof PlasticShader || k instanceof PearlShader || k instanceof ChromeShader || k instanceof MetallicShader) {

            float posneg = 1.0f;
            float v = 2000f;
            if (shdr.equals("mat1")) {
                posneg = -1.0f;
                v /= 4.0f;
            }
            float f = rndRng(0, 20);
            float d = v / strength;

            if (k instanceof ShinyDiffuseShader) {
                float r = k.getReflectionValue();
                api.parameter("diffuse", Colors.bleech((f / d) * posneg, c));
                api.parameter("reflection", r);
                api.shader(newShader, new ShinyDiffuseShader());
            } else if (k instanceof PlasticShader || k instanceof PearlShader || k instanceof ChromeShader || k instanceof MetallicShader) {
                api.parameter("color", Colors.bleech((f / d) * posneg, c));
                if (k instanceof PlasticShader) {
                    api.shader(newShader, new PlasticShader());
                } else if (k instanceof PearlShader) {
                    api.shader(newShader, new PearlShader());
                } else if (k instanceof ChromeShader) {
                    api.shader(newShader, new ChromeShader());
                } else if (k instanceof MetallicShader) {
                    api.shader(newShader, new MetallicShader());
                }
            }

            ns = newShader;
        }

        return ns;
    }
}
