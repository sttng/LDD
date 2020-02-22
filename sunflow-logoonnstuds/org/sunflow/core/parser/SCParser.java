package org.sunflow.core.parser;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.Reader;
import java.io.StringReader;
import java.nio.ByteOrder;
import java.nio.FloatBuffer;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import org.codehaus.janino.ClassBodyEvaluator;
import org.codehaus.janino.CompileException;
import org.codehaus.janino.Scanner;
import org.codehaus.janino.Parser.ParseException;
import org.codehaus.janino.Scanner.ScanException;
import org.sunflow.SunflowAPI;
import org.sunflow.core.Camera;
import org.sunflow.core.PrimitiveList;
import org.sunflow.core.SceneParser;
import org.sunflow.core.Shader;
import org.sunflow.core.Tesselatable;
import org.sunflow.core.camera.FisheyeLens;
import org.sunflow.core.camera.OrthogonalLens;
import org.sunflow.core.camera.PinholeLens;
import org.sunflow.core.camera.SphericalLens;
import org.sunflow.core.camera.ThinLens;
import org.sunflow.core.light.DirectionalSpotlight;
import org.sunflow.core.light.ImageBasedLight;
import org.sunflow.core.light.PointLight;
import org.sunflow.core.light.SphereLight;
import org.sunflow.core.light.SunSkyLight;
import org.sunflow.core.light.TriangleMeshLight;
import org.sunflow.core.modifiers.BumpMappingModifier;
import org.sunflow.core.modifiers.NormalMapModifier;
import org.sunflow.core.primitive.Background;
import org.sunflow.core.primitive.BanchoffSurface;
import org.sunflow.core.primitive.CornellBox;
import org.sunflow.core.primitive.Hair;
import org.sunflow.core.primitive.JuliaFractal;
import org.sunflow.core.primitive.ParticleSurface;
import org.sunflow.core.primitive.Plane;
import org.sunflow.core.primitive.Sphere;
import org.sunflow.core.primitive.Torus;
import org.sunflow.core.primitive.TriangleMesh;
import org.sunflow.core.shader.AmbientOcclusionShader;
import org.sunflow.core.shader.AnisotropicWardShader;
import org.sunflow.core.shader.ConstantShader;
import org.sunflow.core.shader.DiffuseShader;
import org.sunflow.core.shader.GlassShader;
import org.sunflow.core.shader.IDShader;
import org.sunflow.core.shader.MirrorShader;
import org.sunflow.core.shader.PhongShader;
import org.sunflow.core.shader.ShinyDiffuseShader;
import org.sunflow.core.shader.TexturedAmbientOcclusionShader;
import org.sunflow.core.shader.TexturedDiffuseShader;
import org.sunflow.core.shader.TexturedPhongShader;
import org.sunflow.core.TextureCache;
import bublible.primitive.URamp;
import org.sunflow.core.shader.TexturedShinyDiffuseShader;
import org.sunflow.core.shader.TexturedWardShader;
import org.sunflow.core.shader.UberShader;
import org.sunflow.core.shader.ViewCausticsShader;
import org.sunflow.core.shader.ViewGlobalPhotonsShader;
import org.sunflow.core.shader.ViewIrradianceShader;
import org.sunflow.core.tesselatable.BezierMesh;
import org.sunflow.core.tesselatable.FileMesh;
import org.sunflow.core.tesselatable.Gumbo;
import org.sunflow.core.tesselatable.Teapot;
import org.sunflow.image.Color;
import org.sunflow.math.Matrix4;
import org.sunflow.math.Point3;
import org.sunflow.math.Vector3;
import org.sunflow.system.Parser;
import org.sunflow.system.Timer;
import org.sunflow.system.UI;
import org.sunflow.system.Parser.ParserException;
import org.sunflow.system.UI.Module;

import bublible.Bricks;
import bublible.Modifiers;
import bublible.Shaders;
import bublible.Utils;
import bublible.Vectors;
import bublible.Decorations;
import bublible.World;
import bublible.lights.KonstantLight;
import bublible.lights.RectangleLight;
import bublible.shaders.BackgroundShader;
import bublible.shaders.ChromeShader;
import bublible.shaders.GlowInDarkOpaqueShader;
import bublible.shaders.GlowInDarkWhiteShader;
import bublible.shaders.LampShader;
import bublible.shaders.LinearGradientShader;
import bublible.shaders.MetallicShader;
import bublible.shaders.MixShader;
import bublible.shaders.NeonShader;
import bublible.shaders.PearlShader;
import bublible.shaders.PlasticShader;
import bublible.shaders.RubberShader;
import bublible.shaders.StainedMirrorShader;
import bublible.shaders.TexturedPlasticShader;
import bublible.shaders.TransFlexHoseShader;
import bublible.shaders.TranslucentShader;
import bublible.shaders.TexturedConstantShader;
import bublible.shaders.TransparentShader;

/**
 * This class provides a static method for loading files in the Sunflow scene
 * file format.
 */
public class SCParser implements SceneParser {

    private Parser p;
    private int numLightSamples;
    private boolean w2c;
    private Camera c;
    private String brickseams = "on";
    private float brickseams_adjustGap = 0.000022f;
    private String logoonstuds = "on";
    private float logoonstuds_adjustLOS = 0f;
    private String grainyslopes = "on";
    private float grainyslopes_strength = 0.5f;
    public static String exactdecorbp = "on";
    private float exactdecorbp_strength = 0.002f;
    private static String rubberbricks = "on";
    private static String PNUT = "off";
    private static String brickinfo = "off";
    private static String cmdtolog = "off";
    public static String imagefx = "normal";
    private static String colorvariations = "on";
    private float colorvariations_strength = 1.0f;
    public static String credentials = "on";
    private Utils q;
    private final HashMap<String, String> map = new HashMap<>();
    private final List<String> cmdA = new ArrayList<>();
    private String brickName;
    private final Bricks m = new Bricks();
    private final Modifiers mods = new Modifiers();
    private final World world = new World();
    private final int uvsRow = 1;
    private final String brickTMP = "";
    private final String br = "\r\n";
    private final Shaders shaders = new Shaders();
    private final int var = 1;
    private Matrix4 cameraMatrix;
    public static Color bgColor;

    public SCParser() {
        TextureCache.flush();
    }

    public boolean parse(String filename, SunflowAPI api) {

        String localDir = new File(filename).getAbsoluteFile().getParentFile().getAbsolutePath();
        numLightSamples = 1;
        Timer timer = new Timer();
        timer.start();
        UI.printInfo(Module.API, "Parsing \"%s\" ...", filename);
        try {
            p = new Parser(filename);
            while (true) {
                String token = p.getNextToken();
                if (token == null) {
                    break;
                }
                switch (token) {
                    case "system":
                        UI.printInfo(Module.API, "Reading bublible's MOD settings ...");
                        parseSystemBlock(api);
                        break;
                    case "image":
                        UI.printInfo(Module.API, "Reading image settings ...");
                        parseImageBlock(api);
                        break;
                    case "background":
                        UI.printInfo(Module.API, "Reading background ...");
                        parseBackgroundBlock(api);
                        break;
                    case "accel":
                        UI.printInfo(Module.API, "Reading accelerator type ...");
                        p.getNextToken();
                        UI.printWarning(Module.API, "Setting accelerator type is not recommended - ignoring");
                        break;
                    case "filter":
                        UI.printInfo(Module.API, "Reading image filter type ...");
                        parseFilter(api);
                        break;
                    case "bucket":
                        UI.printInfo(Module.API, "Reading bucket settings ...");
                        api.parameter("bucket.size", p.getNextInt());
                        api.parameter("bucket.order", p.getNextToken());
                        api.options(SunflowAPI.DEFAULT_OPTIONS);
                        break;
                    case "photons":
                        UI.printInfo(Module.API, "Reading photon settings ...");
                        parsePhotonBlock(api);
                        break;
                    case "gi":
                        UI.printInfo(Module.API, "Reading global illumination settings ...");
                        parseGIBlock(api);
                        break;
                    case "lightserver":
                        UI.printInfo(Module.API, "Reading light server settings ...");
                        parseLightserverBlock(api);
                        break;
                    case "trace-depths":
                        UI.printInfo(Module.API, "Reading trace depths ...");
                        parseTraceBlock(api);
                        break;
                    case "camera":
                        parseCamera(api);
                        break;
                    case "shader":
                        if (!parseShader(api)) {
                            return false;
                        }
                        break;
                    case "modifier":
                        if (!parseModifier(api)) {
                            return false;
                        }
                        break;
                    case "override":
                        api.shaderOverride(p.getNextToken(), p.getNextBoolean());
                        break;
                    case "object":
                        parseObjectBlock(api);
                        break;
                    case "instance":
                        parseInstanceBlock(api);
                        break;
                    case "light":
                        parseLightBlock(api);
                        break;
                    case "texturepath": {
                        String path = p.getNextToken();
                        if (!new File(path).isAbsolute()) {
                            path = localDir + File.separator + path;
                        }
                        api.addTextureSearchPath(path);
                        break;
                    }
                    case "includepath": {
                        String path = p.getNextToken();
                        if (!new File(path).isAbsolute()) {
                            path = localDir + File.separator + path;
                        }
                        api.addIncludeSearchPath(path);
                        break;
                    }
                    case "include":
                        String file = p.getNextToken();
                        UI.printInfo(Module.API, "Including: \"%s\" ...", file);
                        api.parse(file);
                        break;
                    case "decor":
                        parseDecorBlock(api);
                        break;
                    default:
                        UI.printWarning(Module.API, "Unrecognized token %s", token);
                        break;
                }
            }
            p.close();
        } catch (ParserException e) {
            UI.printError(Module.API, "%s", e.getMessage());
            return false;
        } catch (FileNotFoundException e) {
            UI.printError(Module.API, "%s", e.getMessage());
            return false;
        } catch (IOException e) {
            UI.printError(Module.API, "%s", e.getMessage());
            return false;
        }
        timer.end();
        UI.printInfo(Module.API, "Done parsing.");
        UI.printInfo(Module.API, "Parsing time: %s", timer.toString());
        return true;
    }

    public boolean parse(Reader reader, SunflowAPI api) throws FileNotFoundException {

        numLightSamples = 1;
        Timer timer = new Timer();
        timer.start();
        UI.printInfo(Module.API, "Parsing \"%s\" ...", reader);
        try {
            p = new Parser(reader);
            while (true) {
                String token = p.getNextToken();
                if (token == null) {
                    break;
                }
                switch (token) {
                    case "system":
                        UI.printInfo(Module.API, "Reading bublible's MOD settings ...");
                        parseSystemBlock(api);
                        break;
                    case "image":
                        UI.printInfo(Module.API, "Reading image settings ...");
                        parseImageBlock(api);
                        break;
                    case "background":
                        UI.printInfo(Module.API, "Reading background ...");
                        parseBackgroundBlock(api);
                        break;
                    case "accel":
                        UI.printInfo(Module.API, "Reading accelerator type ...");
                        p.getNextToken();
                        UI.printWarning(Module.API, "Setting accelerator type is not recommended - ignoring");
                        break;
                    case "filter":
                        UI.printInfo(Module.API, "Reading image filter type ...");
                        parseFilter(api);
                        break;
                    case "bucket":
                        UI.printInfo(Module.API, "Reading bucket settings ...");
                        api.parameter("bucket.size", p.getNextInt());
                        api.parameter("bucket.order", p.getNextToken());
                        api.options(SunflowAPI.DEFAULT_OPTIONS);
                        break;
                    case "photons":
                        UI.printInfo(Module.API, "Reading photon settings ...");
                        parsePhotonBlock(api);
                        break;
                    case "gi":
                        UI.printInfo(Module.API, "Reading global illumination settings ...");
                        parseGIBlock(api);
                        break;
                    case "lightserver":
                        UI.printInfo(Module.API, "Reading light server settings ...");
                        parseLightserverBlock(api);
                        break;
                    case "trace-depths":
                        UI.printInfo(Module.API, "Reading trace depths ...");
                        parseTraceBlock(api);
                        break;
                    case "camera":
                        parseCamera(api);
                        break;
                    case "shader":
                        if (!parseShader(api)) {
                            return false;
                        }
                        break;
                    case "modifier":
                        if (!parseModifier(api)) {
                            return false;
                        }
                        break;
                    case "override":
                        api.shaderOverride(p.getNextToken(), p.getNextBoolean());
                        break;
                    case "object":
                        parseObjectBlock(api);
                        break;
                    case "instance":
                        parseInstanceBlock(api);
                        break;
                    case "light":
                        parseLightBlock(api);
                        break;
                    case "texturepath": {
                        String path = p.getNextToken();
                        if (!new File(path).isAbsolute()) {
                            throw new RuntimeException("No relative path plz");
                        }
                        api.addTextureSearchPath(path);
                        break;
                    }
                    case "includepath": {
                        String path = p.getNextToken();
                        if (!new File(path).isAbsolute()) {
                            throw new RuntimeException("No relative path plz");
                        }
                        api.addIncludeSearchPath(path);
                        break;
                    }
                    case "include":
                        String file = p.getNextToken();
                        UI.printInfo(Module.API, "Including: \"%s\" ...", file);
                        api.parse(file);
                        break;
                    case "decor":
                        parseDecorBlock(api);
                        break;
                    default:
                        UI.printWarning(Module.API, "Unrecognized token %s", token);
                        break;
                }
            }
            p.close();
        } catch (ParserException e) {
            UI.printError(Module.API, "%s", e.getMessage());
            return false;
        } catch (FileNotFoundException e) {
            UI.printError(Module.API, "%s", e.getMessage());
            return false;
        } catch (IOException e) {
            UI.printError(Module.API, "%s", e.getMessage());
            return false;
        }
        timer.end();
        UI.printInfo(Module.API, "Done parsing.");
        UI.printInfo(Module.API, "Parsing time: %s", timer.toString());
        Utils.bricksToCMD(cmdA);
        return true;
    }

    private void parseSystemBlock(SunflowAPI api) throws IOException, ParserException {
        p.checkNextToken("{");

        if (p.peekNextToken("brickseams")) {
            brickseams = p.getNextToken();
        }

        if (p.peekNextToken("brickseams_adjustGap")) {
            brickseams_adjustGap = p.getNextFloat();
        }

        if (p.peekNextToken("logoonstuds")) {
            logoonstuds = p.getNextToken();
        }

        if (p.peekNextToken("logoonstuds_adjustLOS")) {
            logoonstuds_adjustLOS = p.getNextFloat();
        }

        if (p.peekNextToken("grainyslopes")) {
            grainyslopes = p.getNextToken();
        }

        if (p.peekNextToken("grainyslopes_strength")) {
            grainyslopes_strength = p.getNextFloat();
        }

        if (p.peekNextToken("colorvariations")) {
            colorvariations = p.getNextToken();
        }

        if (p.peekNextToken("colorvariations_strength")) {
            colorvariations_strength = p.getNextFloat();
        }

        if (p.peekNextToken("exactdecorbp")) {
            exactdecorbp = p.getNextToken();
        }

        if (p.peekNextToken("exactdecorbp_strength")) {
            exactdecorbp_strength = p.getNextFloat();
        }

        if (p.peekNextToken("rubberbricks")) {
            rubberbricks = p.getNextToken();
        }

        if (p.peekNextToken("PNUT")) {
            PNUT = p.getNextToken();
        }

        if (p.peekNextToken("brickinfo")) {
            brickinfo = p.getNextToken();
        }

        if (p.peekNextToken("cmdtolog")) {
            cmdtolog = p.getNextToken();
        }

        if (p.peekNextToken("imagefx")) {
            imagefx = p.getNextToken();
        }

        if (p.peekNextToken("credentials")) {
            credentials = p.getNextToken();
        }

        p.checkNextToken("}");

        if (api.additionalVectorsWereCreated == 0) {
            api.additionalVectorsWereCreated = 1;
            Vectors.decorRectangle(api);
            Vectors.decor4858(api);
            Vectors.decor2340(api);
            Vectors.decor2340inv(api);
            Vectors.LOSobject(api);
            Vectors.craterBP(api);
        }

        if (api.grainsWereCreated == 0) {
            api.grainsWereCreated = 1;
            if (grainyslopes.equals("on")) {
                mods.Grains(api, grainyslopes_strength, exactdecorbp_strength);
            }
        }
    }

    private void parseImageBlock(SunflowAPI api) throws IOException, ParserException {
        p.checkNextToken("{");
        if (p.peekNextToken("resolution")) {
            int imageW = p.getNextInt();
            int imageH = p.getNextInt();
            Utils.setImageDimensions(imageW, imageH);
            api.parameter("resolutionX", imageW);
            api.parameter("resolutionY", imageH);
        }
        if (p.peekNextToken("aa")) {
            api.parameter("aa.min", p.getNextInt());
            api.parameter("aa.max", p.getNextInt());
        }
        if (p.peekNextToken("samples")) {
            api.parameter("aa.samples", p.getNextInt());
        }
        if (p.peekNextToken("contrast")) {
            api.parameter("aa.contrast", p.getNextFloat());
        }
        if (p.peekNextToken("filter")) {
            api.parameter("filter", p.getNextToken());
        }
        if (p.peekNextToken("jitter")) {
            api.parameter("aa.jitter", p.getNextBoolean());
        }
        if (p.peekNextToken("show-aa")) {
            UI.printWarning(Module.API, "Deprecated: show-aa ignored");
            p.getNextBoolean();
        }
        if (p.peekNextToken("output")) {
            UI.printWarning(Module.API, "Deprecated: output statement ignored");
            p.getNextToken();
        }
        api.options(SunflowAPI.DEFAULT_OPTIONS);
        p.checkNextToken("}");
    }

    private void parseBackgroundBlock(SunflowAPI api) throws IOException, ParserException {
        p.checkNextToken("{");
        p.checkNextToken("color");
        bgColor = parseColor();
        api.parameter("color", bgColor);
        api.shader("background.shader", new ConstantShader());
        api.geometry("background", new Background());
        api.parameter("shaders", "background.shader");
        api.instance("background.instance", "background");
        p.checkNextToken("}");
    }

    private void parseFilter(SunflowAPI api) throws IOException, ParserException {
        UI.printWarning(Module.API, "Deprecated keyword \"filter\" - set this option in the image block");
        String name = p.getNextToken();
        api.parameter("filter", name);
        api.options(SunflowAPI.DEFAULT_OPTIONS);
        boolean hasSizeParams = name.equals("box") || name.equals("gaussian") || name.equals("blackman-harris") || name.equals("sinc") || name.equals("triangle");
        if (hasSizeParams) {
            p.getNextFloat();
            p.getNextFloat();
        }
    }

    private void parsePhotonBlock(SunflowAPI api) throws ParserException, IOException {
        int numEmit = 0;
        boolean globalEmit = false;
        p.checkNextToken("{");
        if (p.peekNextToken("emit")) {
            UI.printWarning(Module.API, "Shared photon emit values are deprectated - specify number of photons to emit per map");
            numEmit = p.getNextInt();
            globalEmit = true;
        }
        if (p.peekNextToken("global")) {
            UI.printWarning(Module.API, "Global photon map setting belonds inside the gi block - ignoring");
            if (!globalEmit) {
                p.getNextInt();
            }
            p.getNextToken();
            p.getNextInt();
            p.getNextFloat();
        }
        p.checkNextToken("caustics");
        if (!globalEmit) {
            numEmit = p.getNextInt();
        }
        api.parameter("caustics.emit", numEmit);
        api.parameter("caustics", p.getNextToken());
        api.parameter("caustics.gather", p.getNextInt());
        api.parameter("caustics.radius", p.getNextFloat());
        api.options(SunflowAPI.DEFAULT_OPTIONS);
        p.checkNextToken("}");
    }

    private void parseGIBlock(SunflowAPI api) throws ParserException, IOException {
        p.checkNextToken("{");
        p.checkNextToken("type");
        if (p.peekNextToken("irr-cache")) {
            api.parameter("gi.engine", "irr-cache");
            p.checkNextToken("samples");
            api.parameter("gi.irr-cache.samples", p.getNextInt());
            p.checkNextToken("tolerance");
            api.parameter("gi.irr-cache.tolerance", p.getNextFloat());
            p.checkNextToken("spacing");
            api.parameter("gi.irr-cache.min_spacing", p.getNextFloat());
            api.parameter("gi.irr-cache.max_spacing", p.getNextFloat());
            // parse global photon map info
            if (p.peekNextToken("global")) {
                api.parameter("gi.irr-cache.gmap.emit", p.getNextInt());
                api.parameter("gi.irr-cache.gmap", p.getNextToken());
                api.parameter("gi.irr-cache.gmap.gather", p.getNextInt());
                api.parameter("gi.irr-cache.gmap.radius", p.getNextFloat());
            }
        } else if (p.peekNextToken("path")) {
            api.parameter("gi.engine", "path");
            p.checkNextToken("samples");
            api.parameter("gi.path.samples", p.getNextInt());
            if (p.peekNextToken("bounces")) {
                UI.printWarning(Module.API, "Deprecated setting: bounces - use diffuse trace depth instead");
                p.getNextInt();
            }
        } else if (p.peekNextToken("fake")) {
            api.parameter("gi.engine", "fake");
            p.checkNextToken("up");
            api.parameter("gi.fake.up", parseVector());
            p.checkNextToken("sky");
            api.parameter("gi.fake.sky", parseColor());
            p.checkNextToken("ground");
            api.parameter("gi.fake.ground", parseColor());
        } else if (p.peekNextToken("igi")) {
            api.parameter("gi.engine", "igi");
            p.checkNextToken("samples");
            api.parameter("gi.igi.samples", p.getNextInt());
            p.checkNextToken("sets");
            api.parameter("gi.igi.sets", p.getNextInt());
            if (!p.peekNextToken("b")) {
                p.checkNextToken("c");
            }
            api.parameter("gi.igi.c", p.getNextFloat());
            p.checkNextToken("bias-samples");
            api.parameter("gi.igi.bias_samples", p.getNextInt());
        } else if (p.peekNextToken("ambocc")) {
            api.parameter("gi.engine", "ambocc");
            p.checkNextToken("bright");
            api.parameter("gi.ambocc.bright", parseColor());
            p.checkNextToken("dark");
            api.parameter("gi.ambocc.dark", parseColor());
            p.checkNextToken("samples");
            api.parameter("gi.ambocc.samples", p.getNextInt());
            if (p.peekNextToken("maxdist")) {
                api.parameter("gi.ambocc.maxdist", p.getNextFloat());
            }
        } else if (p.peekNextToken("none") || p.peekNextToken("null")) {
            // disable GI
            api.parameter("gi.engine", "none");
        } else {
            UI.printWarning(Module.API, "Unrecognized gi engine type \"%s\" - ignoring", p.getNextToken());
        }
        api.options(SunflowAPI.DEFAULT_OPTIONS);
        p.checkNextToken("}");
    }

    private void parseLightserverBlock(SunflowAPI api) throws ParserException, IOException {
        p.checkNextToken("{");
        if (p.peekNextToken("shadows")) {
            UI.printWarning(Module.API, "Deprecated: shadows setting ignored");
            p.getNextBoolean();
        }
        if (p.peekNextToken("direct-samples")) {
            UI.printWarning(Module.API, "Deprecated: use samples keyword in area light definitions");
            numLightSamples = p.getNextInt();
        }
        if (p.peekNextToken("glossy-samples")) {
            UI.printWarning(Module.API, "Deprecated: use samples keyword in glossy shader definitions");
            p.getNextInt();
        }
        if (p.peekNextToken("max-depth")) {
            UI.printWarning(Module.API, "Deprecated: max-depth setting - use trace-depths block instead");
            int d = p.getNextInt();
            api.parameter("depths.diffuse", 1);
            api.parameter("depths.reflection", d - 1);
            api.parameter("depths.refraction", 0);
            api.parameter("depths.transshadow", 0.9f);
            api.options(SunflowAPI.DEFAULT_OPTIONS);
        }
        if (p.peekNextToken("global")) {
            UI.printWarning(Module.API, "Deprecated: global settings ignored - use photons block instead");
            p.getNextBoolean();
            p.getNextInt();
            p.getNextInt();
            p.getNextInt();
            p.getNextFloat();
        }
        if (p.peekNextToken("caustics")) {
            UI.printWarning(Module.API, "Deprecated: caustics settings ignored - use photons block instead");
            p.getNextBoolean();
            p.getNextInt();
            p.getNextFloat();
            p.getNextInt();
            p.getNextFloat();
        }
        if (p.peekNextToken("irr-cache")) {
            UI.printWarning(Module.API, "Deprecated: irradiance cache settings ignored - use gi block instead");
            p.getNextInt();
            p.getNextFloat();
            p.getNextFloat();
            p.getNextFloat();
        }
        p.checkNextToken("}");
    }

    private void parseTraceBlock(SunflowAPI api) throws ParserException, IOException {
        p.checkNextToken("{");
        if (p.peekNextToken("diff")) {
            api.parameter("depths.diffuse", p.getNextInt());
        }
        if (p.peekNextToken("refl")) {
            api.parameter("depths.reflection", p.getNextInt());
        }
        if (p.peekNextToken("refr")) {
            api.parameter("depths.refraction", p.getNextInt());
        }
        if (p.peekNextToken("transshadow")) {
            float abc = p.getNextFloat();
            api.parameter("depths.transshadow", abc);
            System.out.println("abc = " + abc);
        }
        p.checkNextToken("}");
        api.options(SunflowAPI.DEFAULT_OPTIONS);
    }

    private void parseCamera(SunflowAPI api) throws ParserException, IOException {
        p.checkNextToken("{");
        p.checkNextToken("type");
        String type = p.getNextToken();
        UI.printInfo(Module.API, "Reading %s camera ...", type);
        parseCameraTransform(api);
        String name = api.getUniqueName("camera");
        switch (type) {
            case "pinhole":
                p.checkNextToken("fov");
                api.parameter("fov", p.getNextFloat());
                p.checkNextToken("aspect");
                api.parameter("aspect", p.getNextFloat());
                api.camera(name, new PinholeLens());
                break;
            case "thinlens":
                p.checkNextToken("fov");
                api.parameter("fov", p.getNextFloat());
                p.checkNextToken("aspect");
                api.parameter("aspect", p.getNextFloat());

                p.checkNextToken("fdist");
                String fd = p.getNextToken();
                float f;
                if (fd.contains(",")) {
                    f = World.cameraFdistFromBrickMatrix(cameraMatrix, Matrix4.parseFrom4x3String(fd));
                } else {
                    f = Float.parseFloat(fd);
                }

                float ft = 0f;
                if (p.peekNextToken("ftune")) {
                    ft = p.getNextFloat();
                }
                api.parameter("ftune", ft);

                api.parameter("focus.distance", f);
                p.checkNextToken("lensr");
                api.parameter("lens.radius", p.getNextFloat());
                if (p.peekNextToken("sides")) {
                    api.parameter("lens.sides", p.getNextInt());
                }
                if (p.peekNextToken("rotation")) {
                    api.parameter("lens.rotation", p.getNextFloat());
                }
                api.camera(name, new ThinLens());
                break;
            case "spherical":
                // no extra arguments
                api.camera(name, new SphericalLens());
                break;
            case "orthogonal":
                // ??
                api.camera(name, new OrthogonalLens());
                break;
            case "fisheye":
                // no extra arguments
                api.camera(name, new FisheyeLens());
                break;
            default:
                UI.printWarning(Module.API, "Unrecognized camera type: %s", p.getNextToken());
                p.checkNextToken("}");
                return;
        }
        p.checkNextToken("}");
        if (name != null) {
            api.parameter("camera", name);
            api.options(SunflowAPI.DEFAULT_OPTIONS);
        }
    }

    private void parseCameraTransform(SunflowAPI api) throws ParserException, IOException {
        if (p.peekNextToken("steps")) {
            // motion blur camera
            int n = p.getNextInt();
            api.parameter("transform.steps", n);
            for (int i = 0; i < n; i++) {
                parseCameraMatrix(i, api);
            }
        } else {
            parseCameraMatrix(-1, api);
        }
    }

    private void parseCameraMatrix(int index, SunflowAPI api) throws IOException, ParserException {
        String offset = index < 0 ? "" : String.format("[%d]", index);
        if (p.peekNextToken("transform")) {
            // advanced camera
            cameraMatrix = parseMatrix("camera");
            api.parameter(String.format("transform%s", offset), cameraMatrix);
        } else {
            if (index >= 0) {
                p.checkNextToken("{");
            }
            // regular camera specification
            p.checkNextToken("eye");
            api.parameter(String.format("eye%s", offset), parsePoint());
            p.checkNextToken("target");
            api.parameter(String.format("target%s", offset), parsePoint());
            p.checkNextToken("up");
            api.parameter(String.format("up%s", offset), parseVector());
            if (index >= 0) {
                p.checkNextToken("}");
            }
        }
    }

    private boolean parseShader(SunflowAPI api) throws ParserException, IOException {
        p.checkNextToken("{");
        p.checkNextToken("name");
        String name = p.getNextToken();
        UI.printInfo(Module.API, "Reading shader: %s ...", name);
        p.checkNextToken("type");
        if (p.peekNextToken("diffuse")) {
            if (p.peekNextToken("diff")) {
                api.parameter("diffuse", parseColor());
                api.shader(name, new DiffuseShader());
            } else if (p.peekNextToken("texture")) {
                api.parameter("texture", p.getNextToken());
                api.shader(name, new TexturedDiffuseShader());
            } else {
                UI.printWarning(Module.API, "Unrecognized option in diffuse shader block: %s", p.getNextToken());
            }
        } else if (p.peekNextToken("constant")) {
            // backwards compatibility -- peek only
            if (p.peekNextToken("color")) {
                api.parameter("color", parseColor());
                api.shader(name, new ConstantShader());
            } else if (p.peekNextToken("texture")) {
                api.parameter("texture", p.getNextToken());
                api.shader(name, new TexturedConstantShader());
            } else {
                UI.printWarning(Module.API, "Unrecognized option in constant shader block: %s", p.getNextToken());
            }
        } else if (p.peekNextToken("custom")) {
            p.checkNextToken("class");
            String cls = p.getNextToken();
            Shader s;
            try {
                s = (Shader) Class.forName(cls).newInstance();
                api.shader(name, s);
            } catch (ClassNotFoundException | InstantiationException | IllegalAccessException e) {
                throw new RuntimeException(e);
            }
        } else if (p.peekNextToken("phong")) {
            String tex = null;
            if (p.peekNextToken("texture")) {
                api.parameter("texture", tex = p.getNextToken());
            } else {
                p.checkNextToken("diff");
                api.parameter("diffuse", parseColor());
            }
            p.checkNextToken("spec");
            api.parameter("specular", parseColor());
            api.parameter("power", p.getNextFloat());
            if (p.peekNextToken("samples")) {
                api.parameter("samples", p.getNextInt());
            }
            if (tex != null) {
                api.shader(name, new TexturedPhongShader());
            } else {
                api.shader(name, new PhongShader());
            }
        } else if (p.peekNextToken("amb-occ") || p.peekNextToken("amb-occ2")) {
            String tex = null;
            if (p.peekNextToken("diff") || p.peekNextToken("bright")) {
                api.parameter("bright", parseColor());
            } else if (p.peekNextToken("texture")) {
                api.parameter("texture", tex = p.getNextToken());
            }
            if (p.peekNextToken("dark")) {
                api.parameter("dark", parseColor());
                p.checkNextToken("samples");
                api.parameter("samples", p.getNextInt());
                p.checkNextToken("dist");
                api.parameter("maxdist", p.getNextFloat());
            }
            if (tex == null) {
                api.shader(name, new AmbientOcclusionShader());
            } else {
                api.shader(name, new TexturedAmbientOcclusionShader());
            }
        } else if (p.peekNextToken("mirror")) {
            p.checkNextToken("refl");
            api.parameter("color", parseColor());
            api.shader(name, new MirrorShader());
        } else if (p.peekNextToken("glass")) {
            p.checkNextToken("eta");
            api.parameter("eta", p.getNextFloat());
            p.checkNextToken("color");
            api.parameter("color", parseColor());
            if (p.peekNextToken("absorbtion.distance")) {
                api.parameter("absorbtion.distance", p.getNextFloat());
            }
            if (p.peekNextToken("absorbtion.color")) {
                api.parameter("absorbtion.color", parseColor());
            }
            api.shader(name, new GlassShader());
        } else if (p.peekNextToken("shiny")) {
            String tex = null;
            if (p.peekNextToken("texture")) {
                api.parameter("texture", tex = p.getNextToken());
            }
            p.checkNextToken("diff");
            Color colr = parseColor();
            api.parameter("diffuse", colr);
            p.checkNextToken("refl");
            float rfl = p.getNextFloat();
            api.parameter("reflection", rfl);
            if (tex == null) {
                api.shader(name, new ShinyDiffuseShader());
            } else {
                api.shader(name, new TexturedShinyDiffuseShader());
            }

            if (rubberbricks.equals("on")) {
                api.parameter("color", colr);
                api.shader(name + "R", new RubberShader());
            }

            if (exactdecorbp.equals("on")) {
                Shaders.exactDecoratedBP(api, tex, colr, name);
            }

        } else if (p.peekNextToken("plastic")) {
            p.checkNextToken("color");
            Color colr = parseColor();
            api.parameter("color", colr);

            String tex = null;
            if (p.peekNextToken("texture")) {
                api.parameter("texture", tex = p.getNextToken());
            }
            if (tex == null) {
                api.shader(name, new PlasticShader());
            } else {
                api.shader(name, new TexturedPlasticShader());
            }

            if (rubberbricks.equals("on")) {
                api.parameter("color", colr);
                api.shader(name + "R", new RubberShader());
            }

            if (exactdecorbp.equals("on")) {
                Shaders.exactDecoratedBP(api, tex, colr, name);
            }

        } else if (p.peekNextToken("neon")) {
            p.checkNextToken("color");
            api.parameter("color", parseColor());
            api.shader(name, new NeonShader());

        } else if (p.peekNextToken("transparent")) {
            api.shader(name, new TransparentShader());

        } else if (p.peekNextToken("rubber")) {
            p.checkNextToken("color");
            api.parameter("color", parseColor());
            api.shader(name, new RubberShader());

        } else if (p.peekNextToken("GlowInDarkWhite")) {
            api.shader(name, new GlowInDarkWhiteShader());

        } else if (p.peekNextToken("GlowInDarkOpaque")) {
            api.shader(name, new GlowInDarkOpaqueShader());

        } else if (p.peekNextToken("pearl")) {
            p.checkNextToken("color");
            api.parameter("color", parseColor());
            api.shader(name, new PearlShader());

        } else if (p.peekNextToken("metallic")) {
            p.checkNextToken("color");
            api.parameter("color", parseColor());
            api.shader(name, new MetallicShader());

        } else if (p.peekNextToken("chrome")) {
            p.checkNextToken("color");
            api.parameter("color", parseColor());
            api.shader(name, new ChromeShader());

        } else if (p.peekNextToken("background")) {
            p.checkNextToken("shading");
            api.parameter("shading", p.getNextToken());
            p.checkNextToken("color");
            api.parameter("color", parseColor());
            p.checkNextToken("ratio");
            api.parameter("ratio", p.getNextFloat());
            api.shader(name, new BackgroundShader());

        } else if (p.peekNextToken("gradient-linear")) {
            p.checkNextToken("direction");
            api.parameter("direction", p.getNextToken());
            p.checkNextToken("shader1");
            api.parameter("shader1", p.getNextToken());
            p.checkNextToken("color1");
            api.parameter("color1", parseColor());
            p.checkNextToken("shader2");
            api.parameter("shader2", p.getNextToken());
            p.checkNextToken("color2");
            api.parameter("color2", parseColor());
            p.checkNextToken("offset");
            api.parameter("offset", p.getNextFloat());
            p.checkNextToken("gap");
            api.parameter("gap", p.getNextFloat());
            api.shader(name, new LinearGradientShader());

        } else if (p.peekNextToken("mix")) {
            p.checkNextToken("shader1");
            api.parameter("shader1", p.getNextToken());
            p.checkNextToken("color1");
            api.parameter("color1", parseColor());
            p.checkNextToken("shader2");
            api.parameter("shader2", p.getNextToken());
            p.checkNextToken("color2");
            api.parameter("color2", parseColor());
            p.checkNextToken("ratio");
            api.parameter("ratio", p.getNextFloat());
            api.shader(name, new MixShader());

        } else if (p.peekNextToken("stainedmirror")) {
            p.checkNextToken("color");
            api.parameter("color", parseColor());
            api.shader(name, new StainedMirrorShader());

        } else if (p.peekNextToken("transflexhose")) {
            p.checkNextToken("color");
            api.parameter("color", parseColor());
            api.shader(name, new TransFlexHoseShader());

        } else if (p.peekNextToken("translucent")) {
            p.checkNextToken("color");
            api.parameter("color", parseColor());
            api.shader(name, new TranslucentShader());

        } else if (p.peekNextToken("ward")) {
            String tex = null;
            if (p.peekNextToken("texture")) {
                api.parameter("texture", tex = p.getNextToken());
            } else {
                p.checkNextToken("diff");
                api.parameter("diffuse", parseColor());
            }
            p.checkNextToken("spec");
            api.parameter("specular", parseColor());
            p.checkNextToken("rough");
            api.parameter("roughnessX", p.getNextFloat());
            api.parameter("roughnessY", p.getNextFloat());
            if (p.peekNextToken("samples")) {
                api.parameter("samples", p.getNextInt());
            }
            if (tex != null) {
                api.shader(name, new TexturedWardShader());
            } else {
                api.shader(name, new AnisotropicWardShader());
            }
        } else if (p.peekNextToken("view-caustics")) {
            api.shader(name, new ViewCausticsShader());
        } else if (p.peekNextToken("view-irradiance")) {
            api.shader(name, new ViewIrradianceShader());
        } else if (p.peekNextToken("view-global")) {
            api.shader(name, new ViewGlobalPhotonsShader());
        } else if (p.peekNextToken("lamp")) {
            p.peekNextToken("color");
            api.parameter("color", parseColor());
            p.peekNextToken("power");
            api.parameter("power", p.getNextFloat());
            api.shader(name, new LampShader());
        } else if (p.peekNextToken("janino")) {
            String code = p.getNextCodeBlock();
            try {
                Shader shader = (Shader) ClassBodyEvaluator.createFastClassBodyEvaluator(new Scanner(null, new StringReader(code)), Shader.class, ClassLoader.getSystemClassLoader());
                api.shader(name, shader);
            } catch (CompileException e) {
                UI.printDetailed(Module.API, "Compiling: %s", code);
                UI.printError(Module.API, "%s", e.getMessage());
                return false;
            } catch (ParseException | ScanException e) {
                UI.printDetailed(Module.API, "Compiling: %s", code);
                UI.printError(Module.API, "%s", e.getMessage());
                return false;
            } catch (IOException e) {
                UI.printDetailed(Module.API, "Compiling: %s", code);
                UI.printError(Module.API, "%s", e.getMessage());
                return false;
            }
        } else if (p.peekNextToken("id")) {
            api.shader(name, new IDShader());
        } else if (p.peekNextToken("uber")) {
            if (p.peekNextToken("diff")) {
                api.parameter("diffuse", parseColor());
            }
            if (p.peekNextToken("diff.texture")) {
                api.parameter("diffuse.texture", p.getNextToken());
            }
            if (p.peekNextToken("diff.blend")) {
                api.parameter("diffuse.blend", p.getNextFloat());
            }
            if (p.peekNextToken("refl") || p.peekNextToken("spec")) {
                api.parameter("specular", parseColor());
            }
            if (p.peekNextToken("texture")) {
                // deprecated
                UI.printWarning(Module.API, "Deprecated uber shader parameter \"texture\" - please use \"diffuse.texture\" and \"diffuse.blend\" instead");
                api.parameter("diffuse.texture", p.getNextToken());
                api.parameter("diffuse.blend", p.getNextFloat());
            }
            if (p.peekNextToken("spec.texture")) {
                api.parameter("specular.texture", p.getNextToken());
            }
            if (p.peekNextToken("spec.blend")) {
                api.parameter("specular.blend", p.getNextFloat());
            }
            if (p.peekNextToken("glossy")) {
                api.parameter("glossyness", p.getNextFloat());
            }
            if (p.peekNextToken("samples")) {
                api.parameter("samples", p.getNextInt());
            }
            api.shader(name, new UberShader());
        } else {
            UI.printWarning(Module.API, "Unrecognized shader type: %s", p.getNextToken());
        }
        p.checkNextToken("}");
        return true;
    }

    private boolean parseModifier(SunflowAPI api) throws ParserException, IOException {
        p.checkNextToken("{");
        p.checkNextToken("name");
        String name = p.getNextToken();
        UI.printInfo(Module.API, "Reading modifier: %s ...", name);
        p.checkNextToken("type");
        if (p.peekNextToken("bump")) {
            p.checkNextToken("texture");
            api.parameter("texture", p.getNextToken());
            p.checkNextToken("scale");
            api.parameter("scale", p.getNextFloat());
            api.modifier(name, new BumpMappingModifier());
        } else if (p.peekNextToken("normalmap")) {
            p.checkNextToken("texture");
            api.parameter("texture", p.getNextToken());
            api.modifier(name, new NormalMapModifier());
        } else {
            UI.printWarning(Module.API, "Unrecognized modifier type: %s", p.getNextToken());
        }
        p.checkNextToken("}");
        return true;
    }

    private void parseObjectBlock(SunflowAPI api) throws ParserException, IOException {
        p.checkNextToken("{");
        String name;
        String nazov;
        boolean noInstance = false;
        Matrix4 transform = null;
        String[] shaderzz = null;
        String[] modifiers = null;
        if (p.peekNextToken("noinstance")) {
            // this indicates that the geometry is to be created,
            // but not instanced into the scene
            noInstance = true;
        } else {
            // these are the parameters to be passed to the instance
            if (p.peekNextToken("shaders")) {
                int n = p.getNextInt();
                shaderzz = new String[n];
                for (int i = 0; i < n; i++) {
                    shaderzz[i] = p.getNextToken();
                }
            } else {
                p.checkNextToken("shader");
                shaderzz = new String[]{p.getNextToken()};
            }
            if (p.peekNextToken("modifiers")) {
                int n = p.getNextInt();
                modifiers = new String[n];
                for (int i = 0; i < n; i++) {
                    modifiers[i] = p.getNextToken();
                }
            } else if (p.peekNextToken("modifier")) {
                modifiers = new String[]{p.getNextToken()};
            }
            if (p.peekNextToken("transform")) {
                transform = parseMatrix("object");
            }
        }
        if (p.peekNextToken("accel")) {
            api.parameter("accel", p.getNextToken());
        }
        p.checkNextToken("type");
        String type = p.getNextToken();
        if (p.peekNextToken("name")) {
            name = p.getNextToken();
        } else {
            name = api.getUniqueName(type);
        }

        switch (type) {
            // --------------- LEGO BRICK OBJECT/GEOMETRY ---------------
            case "mesh": {
                nazov = name.split("_")[0];
                int numVertices = p.getNextInt();
                int numTriangles = p.getNextInt();
                float[] points = new float[numVertices * 3];
                float[] normals = new float[numVertices * 3];
                float[] uvs = new float[numVertices * 2];

                for (int i = 0; i < numVertices; i++) {
                    p.checkNextToken("v");
                    points[3 * i + 0] = p.getNextFloat();
                    points[3 * i + 1] = p.getNextFloat();
                    points[3 * i + 2] = p.getNextFloat();
                    normals[3 * i + 0] = p.getNextFloat();
                    normals[3 * i + 1] = p.getNextFloat();
                    normals[3 * i + 2] = p.getNextFloat();
                    uvs[2 * i + 0] = p.getNextFloat();
                    uvs[2 * i + 1] = p.getNextFloat();
                }

                int[] triangles = new int[numTriangles * 3];
                for (int i = 0; i < numTriangles; i++) {
                    p.checkNextToken("t");
                    triangles[i * 3 + 0] = p.getNextInt();
                    triangles[i * 3 + 1] = p.getNextInt();
                    triangles[i * 3 + 2] = p.getNextInt();
                }

                if (grainyslopes.equals("on")) {
                    if (Arrays.asList(m.checkGrainySlopes()).contains(nazov)) {
                        if (nazov.equals("3039") || nazov.equals("3040")) {
                        } else {
                            uvs = Vectors.addSlopeUVS(nazov, uvs);
                        }
                    }
                }

                // create geometry
                api.parameter("triangles", triangles);
                api.parameter("points", "point", "vertex", points);
                api.parameter("normals", "vector", "vertex", normals);
                api.parameter("uvs", "texcoord", "vertex", uvs);
                api.geometry(name, new TriangleMesh());

                // put info about the mesh for CMD window
                if (PNUT.equals("on")) {
                    if (name.split("_")[1].equals("1")) {
                        Utils.w(" ");
                        Utils.w("------------------------------");
                        Utils.w(name + " POINTS: " + points.length / 3);
                        Utils.w("==============");
                        String s = "";
                        int j = 0;
                        for (int i = 0; i < points.length; i++) {
                            s += Float.toString(points[i]) + " ";
                            if (j == 2) {
                                s += br;
                                j = 0;
                            } else {
                                j++;
                            }
                        }
                        Utils.w(s);

                        Utils.w(" ");
                        Utils.w("------------------------------");
                        Utils.w(name + " TRIANGLES: " + triangles.length / 3);
                        Utils.w("==============");
                        String sB = "";
                        int k = 0;
                        for (int mc = 0; mc < triangles.length; mc++) {
                            sB += Float.toString(triangles[mc]) + " ";
                            if (k == 2) {
                                sB += br;
                                k = 0;
                            } else {
                                k++;
                            }
                        }
                        Utils.w(sB);

                        Utils.w(" ");
                        Utils.w("------------------------------");
                        Utils.w(name + " NORMALS: " + normals.length / 3);
                        Utils.w("==============");
                        String sC = "";
                        int r = 0;
                        for (int pc = 0; pc < normals.length; pc++) {
                            sC += Float.toString(normals[pc]) + " ";
                            if (r == 2) {
                                sC += br;
                                r = 0;
                            } else {
                                r++;
                            }
                        }
                        Utils.w(sC);

                        Utils.w(" ");
                        Utils.w("------------------------------");
                        Utils.w(name + " UVS: " + uvs.length / 2);
                        Utils.w("==============");
                        String sD = "";
                        int tt = 0;
                        for (int ss = 0; ss < uvs.length; ss++) {
                            sD += Float.toString(uvs[ss]) + " ";
                            if (tt == 1) {
                                sD += br;
                                tt = 0;
                            } else {
                                tt++;
                            }
                        }
                        Utils.w(sD);
                    }
                }

                if (brickinfo.equals("on")) {
                    brickName = name;
                    cmdA.add(brickName + ":::BRICK:::" + name);
                    cmdA.add(brickName + ":::VERTICES:::" + numVertices);
                    cmdA.add(brickName + ":::TRIANGLES:::" + numTriangles);
                }

                break;
                // ---------------------------------------------------------------------
            }
            case "flat-mesh": {
                UI.printWarning(Module.API, "Deprecated object type: flat-mesh");
                UI.printInfo(Module.API, "Reading flat mesh: %s ...", name);
                int numVertices = p.getNextInt();
                int numTriangles = p.getNextInt();
                float[] points = new float[numVertices * 3];
                float[] uvs = new float[numVertices * 2];
                for (int i = 0; i < numVertices; i++) {
                    p.checkNextToken("v");
                    points[3 * i + 0] = p.getNextFloat();
                    points[3 * i + 1] = p.getNextFloat();
                    points[3 * i + 2] = p.getNextFloat();
                    p.getNextFloat();
                    p.getNextFloat();
                    p.getNextFloat();
                    uvs[2 * i + 0] = p.getNextFloat();
                    uvs[2 * i + 1] = p.getNextFloat();
                }
                int[] triangles = new int[numTriangles * 3];
                for (int i = 0; i < numTriangles; i++) {
                    p.checkNextToken("t");
                    triangles[i * 3 + 0] = p.getNextInt();
                    triangles[i * 3 + 1] = p.getNextInt();
                    triangles[i * 3 + 2] = p.getNextInt();
                }       // create geometry
                api.parameter("triangles", triangles);
                api.parameter("points", "point", "vertex", points);
                api.parameter("uvs", "texcoord", "vertex", uvs);
                api.geometry(name, new TriangleMesh());
                break;
            }
            case "sphere":
                UI.printInfo(Module.API, "Reading sphere ...");
                api.geometry(name, new Sphere());
                if (transform == null && !noInstance) {
                    // legacy method of specifying transformation for spheres
                    p.checkNextToken("c");
                    float x = p.getNextFloat();
                    float y = p.getNextFloat();
                    float z = p.getNextFloat();
                    p.checkNextToken("r");
                    float radius = p.getNextFloat();
                    api.parameter("transform", Matrix4.translation(x, y, z).multiply(Matrix4.scale(radius)));
                    api.parameter("shaders", shaderzz);
                    if (modifiers != null) {
                        api.parameter("modifiers", modifiers);
                    }
                    api.instance(name + ".instance", name);
                    noInstance = true; // disable future auto-instancing because
                    // instance has already been created
                }
                break;
            case "banchoff":
                UI.printInfo(Module.API, "Reading banchoff ...");
                api.geometry(name, new BanchoffSurface());
                break;
            case "torus":
                UI.printInfo(Module.API, "Reading torus ...");
                p.checkNextToken("r");
                api.parameter("radiusInner", p.getNextFloat());
                api.parameter("radiusOuter", p.getNextFloat());
                api.geometry(name, new Torus());
                break;
            case "plane":
                UI.printInfo(Module.API, "Reading plane ...");
                p.checkNextToken("p");
                api.parameter("center", parsePoint());
                if (p.peekNextToken("n")) {
                    api.parameter("normal", parseVector());
                } else {
                    p.checkNextToken("p");
                    api.parameter("point1", parsePoint());
                    p.checkNextToken("p");
                    api.parameter("point2", parsePoint());
                }
                api.geometry(name, new Plane());
                break;
            case "uramp":
                UI.printInfo(Module.API, "Reading plane ...");
                p.checkNextToken("p");
                api.parameter("center", parsePoint());
                if (p.peekNextToken("n")) {
                    api.parameter("normal", parseVector());
                } else {
                    p.checkNextToken("p");
                    api.parameter("point1", parsePoint());
                    p.checkNextToken("p");
                    api.parameter("point2", parsePoint());
                }
                api.geometry(name, new URamp());
                break;
            case "cornellbox":
                UI.printInfo(Module.API, "Reading cornell box ...");
                if (transform != null) {
                    UI.printWarning(Module.API, "Instancing is not supported on cornell box -- ignoring transform");
                }
                p.checkNextToken("corner0");
                api.parameter("corner0", parsePoint());
                p.checkNextToken("corner1");
                api.parameter("corner1", parsePoint());
                p.checkNextToken("left");
                api.parameter("leftColor", parseColor());
                p.checkNextToken("right");
                api.parameter("rightColor", parseColor());
                p.checkNextToken("top");
                api.parameter("topColor", parseColor());
                p.checkNextToken("bottom");
                api.parameter("bottomColor", parseColor());
                p.checkNextToken("back");
                api.parameter("backColor", parseColor());
                p.checkNextToken("emit");
                api.parameter("radiance", parseColor());
                if (p.peekNextToken("samples")) {
                    api.parameter("samples", p.getNextInt());
                }
                new CornellBox().init(name, api);
                noInstance = true; // instancing is handled natively by the init
                // method
                break;
            case "generic-mesh":
                UI.printInfo(Module.API, "Reading generic mesh: %s ... ", name);
                // parse vertices
                p.checkNextToken("points");
                int np = p.getNextInt();
                api.parameter("points", "point", "vertex", parseFloatArray(np * 3));
                // parse triangle indices
                p.checkNextToken("triangles");
                int nt = p.getNextInt();
                api.parameter("triangles", parseIntArray(nt * 3));
                // parse normals
                p.checkNextToken("normals");
                if (p.peekNextToken("vertex")) {
                    api.parameter("normals", "vector", "vertex", parseFloatArray(np * 3));
                } else if (p.peekNextToken("facevarying")) {
                    api.parameter("normals", "vector", "facevarying", parseFloatArray(nt * 9));
                } else {
                    p.checkNextToken("none");
                }   // parse texture coordinates
                p.checkNextToken("uvs");
                if (p.peekNextToken("vertex")) {
                    api.parameter("uvs", "texcoord", "vertex", parseFloatArray(np * 2));
                } else if (p.peekNextToken("facevarying")) {
                    api.parameter("uvs", "texcoord", "facevarying", parseFloatArray(nt * 6));
                } else {
                    p.checkNextToken("none");
                }
                if (p.peekNextToken("face_shaders")) {
                    api.parameter("faceshaders", parseIntArray(nt));
                }
                api.geometry(name, new TriangleMesh());
                break;
            case "hair":
                UI.printInfo(Module.API, "Reading hair curves: %s ... ", name);
                p.checkNextToken("segments");
                api.parameter("segments", p.getNextInt());
                p.checkNextToken("width");
                api.parameter("widths", p.getNextFloat());
                p.checkNextToken("points");
                api.parameter("points", "point", "vertex", parseFloatArray(p.getNextInt()));
                api.geometry(name, new Hair());
                break;
            case "janino-tesselatable":
                UI.printInfo(Module.API, "Reading procedural primitive: %s ... ", name);
                String code = p.getNextCodeBlock();
                try {
                    Tesselatable tess = (Tesselatable) ClassBodyEvaluator.createFastClassBodyEvaluator(new Scanner(null, new StringReader(code)), Tesselatable.class, ClassLoader.getSystemClassLoader());
                    api.geometry(name, tess);
                } catch (CompileException e) {
                    UI.printDetailed(Module.API, "Compiling: %s", code);
                    UI.printError(Module.API, "%s", e.getMessage());
                    noInstance = true;
                } catch (ParseException | ScanException e) {
                    UI.printDetailed(Module.API, "Compiling: %s", code);
                    UI.printError(Module.API, "%s", e.getMessage());
                    noInstance = true;
                } catch (IOException e) {
                    UI.printDetailed(Module.API, "Compiling: %s", code);
                    UI.printError(Module.API, "%s", e.getMessage());
                    noInstance = true;
                }
                break;
            case "teapot": {
                UI.printInfo(Module.API, "Reading teapot: %s ... ", name);
                boolean hasTesselationArguments = false;
                if (p.peekNextToken("subdivs")) {
                    api.parameter("subdivs", p.getNextInt());
                    hasTesselationArguments = true;
                }
                if (p.peekNextToken("smooth")) {
                    api.parameter("smooth", p.getNextBoolean());
                    hasTesselationArguments = true;
                }
                if (hasTesselationArguments) {
                    api.geometry(name, (Tesselatable) new Teapot());
                } else {
                    api.geometry(name, (PrimitiveList) new Teapot());
                }
                break;
            }
            case "gumbo": {
                UI.printInfo(Module.API, "Reading gumbo: %s ... ", name);
                boolean hasTesselationArguments = false;
                if (p.peekNextToken("subdivs")) {
                    api.parameter("subdivs", p.getNextInt());
                    hasTesselationArguments = true;
                }
                if (p.peekNextToken("smooth")) {
                    api.parameter("smooth", p.getNextBoolean());
                    hasTesselationArguments = true;
                }
                if (hasTesselationArguments) {
                    api.geometry(name, (Tesselatable) new Gumbo());
                } else {
                    api.geometry(name, (PrimitiveList) new Gumbo());
                }
                break;
            }
            case "julia":
                UI.printInfo(Module.API, "Reading julia fractal: %s ... ", name);
                if (p.peekNextToken("q")) {
                    api.parameter("cw", p.getNextFloat());
                    api.parameter("cx", p.getNextFloat());
                    api.parameter("cy", p.getNextFloat());
                    api.parameter("cz", p.getNextFloat());
                }
                if (p.peekNextToken("iterations")) {
                    api.parameter("iterations", p.getNextInt());
                }
                if (p.peekNextToken("epsilon")) {
                    api.parameter("epsilon", p.getNextFloat());
                }
                api.geometry(name, new JuliaFractal());
                break;
            case "particles":
            case "dlasurface":
                if (type.equals("dlasurface")) {
                    UI.printWarning(Module.API, "Deprecated object type: \"dlasurface\" - please use \"particles\" instead");
                }
                p.checkNextToken("filename");
                String filename = p.getNextToken();
                boolean littleEndian = false;
                if (p.peekNextToken("little_endian")) {
                    littleEndian = true;
                }
                UI.printInfo(Module.USER, "Loading particle file: %s", filename);
                File file = new File(filename);
                FileInputStream stream = new FileInputStream(filename);
                MappedByteBuffer mapa = stream.getChannel().map(FileChannel.MapMode.READ_ONLY, 0, file.length());
                if (littleEndian) {
                    mapa.order(ByteOrder.LITTLE_ENDIAN);
                }
                FloatBuffer buffer = mapa.asFloatBuffer();
                float[] data = new float[buffer.capacity()];
                for (int i = 0; i < data.length; i++) {
                    data[i] = buffer.get(i);
                }
                stream.close();
                api.parameter("particles", "point", "vertex", data);
                if (p.peekNextToken("num")) {
                    api.parameter("num", p.getNextInt());
                } else {
                    api.parameter("num", data.length / 3);
                }
                p.checkNextToken("radius");
                api.parameter("radius", p.getNextFloat());
                api.geometry(name, new ParticleSurface());
                break;
            case "file-mesh":
                UI.printInfo(Module.API, "Reading file mesh: %s ... ", name);
                p.checkNextToken("filename");
                api.parameter("filename", p.getNextToken());
                if (p.peekNextToken("smooth_normals")) {
                    api.parameter("smooth_normals", p.getNextBoolean());
                }
                api.geometry(name, new FileMesh());
                break;
            case "bezier-mesh": {
                UI.printInfo(Module.API, "Reading bezier mesh: %s ... ", name);
                p.checkNextToken("n");
                int nu, nv;
                api.parameter("nu", nu = p.getNextInt());
                api.parameter("nv", nv = p.getNextInt());
                if (p.peekNextToken("wrap")) {
                    api.parameter("uwrap", p.getNextBoolean());
                    api.parameter("vwrap", p.getNextBoolean());
                }
                p.checkNextToken("points");
                float[] points = new float[3 * nu * nv];
                for (int i = 0; i < points.length; i++) {
                    points[i] = p.getNextFloat();
                }
                api.parameter("points", "point", "vertex", points);
                if (p.peekNextToken("subdivs")) {
                    api.parameter("subdivs", p.getNextInt());
                }
                if (p.peekNextToken("smooth")) {
                    api.parameter("smooth", p.getNextBoolean());
                }
                api.geometry(name, (Tesselatable) new BezierMesh());
                break;
            }
            default:
                UI.printWarning(Module.API, "Unrecognized object type: %s", p.getNextToken());
                noInstance = true;
                break;
        }
        if (!noInstance) {
            // create instance
            api.parameter("shaders", shaderzz);
            if (modifiers != null) {
                api.parameter("modifiers", modifiers);
            }
            if (transform != null) {
                api.parameter("transform", transform);
            }
            api.instance(name + ".instance", name);
        }
        p.checkNextToken("}");
    }

    private void parseInstanceBlock(SunflowAPI api) throws ParserException, IOException {

        p.checkNextToken("{");
        p.checkNextToken("name");
        String name = p.getNextToken();
        UI.printInfo(Module.API, "Reading instance: %s ...", name);
        p.checkNextToken("geometry");
        String geoname = p.getNextToken();
        String teksture = null;

        w2c = false;
        if (p.peekNextToken("w2c")) {
            w2c = true;
        }

        p.checkNextToken("transform");
        Matrix4 m4 = parseMatrix("instance");
        Matrix4 m4TMP = m4;

        if (brickseams.equals("on")) {
            m4 = m.SimpleBrickSeams(api, geoname, m4, brickseams_adjustGap);
        }

        //api.parameter("transform", m4);
        if (brickinfo.equals("on")) {
            cmdA.add(name + ":::SCALE:::x=" + m4.m00 + ", y=" + m4.m11 + ", z=" + m4.m22);
            cmdA.add(name + ":::POSITION:::x=" + m4.m30 + ", y=" + m4.m31 + ", z=" + m4.m32);
        }

        if (p.peekNextToken("texture")) {
            teksture = p.getNextToken();
            //api.parameter("texture", teksture);
            if (brickinfo.equals("on")) {
                cmdA.add(name + ":::TEXTURE:::" + teksture);
            }
        }

        String[] shaderz;
        String shdr = null;
        if (p.peekNextToken("shaders")) {
            int n = p.getNextInt();
            shaderz = new String[n];
            for (int i = 0; i < n; i++) {
                shaderz[i] = p.getNextToken();
            }
        } else {
            p.checkNextToken("shader");
            shdr = p.getNextToken();
            if (geoname.contains("_")) {
                String[] g = geoname.split("_");

                // LEGO BRICKS
                if (g[0].matches("[0-9]+") && g[0].length() >= 4) {
                    // ---------------------- GRAIN BP -------------------------
                    if (Arrays.asList(m.checkGrainyBP32x32()).contains(g[0])
                            || Arrays.asList(m.checkGrainyBP16x16()).contains(g[0])
                            && api.lookupShader(shdr) instanceof ShinyDiffuseShader
                            && exactdecorbp.equals("on")) {
                        shdr = shdr + "BP";
                        // -------------------- RUBBER PARTS -----------------------
                    } else if (Arrays.asList(m.checkRubberParts()).contains(g[0])
                            && rubberbricks.equals("on")) {
                        shdr = shdr + "R";
                        // -------------------- COLOR VARIATIONS -----------------------
                    } else if (colorvariations.equals("on")) {
                        shdr = Shaders.shaderColorVariations(api, shdr, colorvariations_strength);
                    }
                }
            }
            shaderz = new String[]{shdr};
        }

        if (brickinfo.equals("on")) {
            cmdA.add(name + ":::MATERIAL:::" + shdr);
        }

        String[] modifiers = null;
        String mdfr = null;
        if (p.peekNextToken("modifiers")) {
            int n = p.getNextInt();
            modifiers = new String[n];
            for (int i = 0; i < n; i++) {
                modifiers[i] = p.getNextToken();
            }
        } else if (p.peekNextToken("modifier")) {
            mdfr = p.getNextToken();
            modifiers = new String[]{mdfr};
        }

        if (brickinfo.equals("on")) {
            cmdA.add(name + ":::MODIFIER:::" + mdfr);
            cmdA.add(name + ":::GEOMETRY:::" + geoname);
            cmdA.add(name + ":::INSTANCE NAME:::" + name);
        }

        // -------------------- BEGINNING OF ALL INSTANCE APIs -----------------------
        //api.parameter("w2c", w2c);
        api.parameter("transform", m4);
        api.parameter("texture", teksture);
        api.parameter("shaders", shaderz);

        if (modifiers != null) {
            api.parameter("modifiers", modifiers);
        }

        if (grainyslopes.equals("on")) {
            mdfr = m.GrainySlopes(api, geoname);
            if (mdfr != null) {
                modifiers = new String[]{mdfr};
                api.parameter("modifiers", modifiers);
            }
        }

        api.instance(name, geoname);

        // ADDITIONAL "REPAIRED" SLOPES UVs
        if (geoname.contains("4858")) {

            Matrix4 m4858 = Matrix4.IDENTITY;
            Matrix4 t4858;

            // SCALE
            t4858 = Matrix4.scale(3.18f, 2.5f, 1f);
            m4858 = t4858.multiply(m4858);

            // ROTATION
            t4858 = Matrix4.rotateX((float) Math.toRadians(-72.55f));
            m4858 = t4858.multiply(m4858);

            // POSITION
            //t4858 = Matrix4.translation(m4.m03 - 2.78f, m4.m13 + 0.2f, m4.m23 + 2.79f);
            t4858 = Matrix4.translation(-2.78f, 0.209f, 2.79f);
            m4858 = t4858.multiply(m4858);

            // ORIGINAL BRICK MATRIX
            t4858 = new Matrix4(m4.asRowMajor(), true);
            m4858 = t4858.multiply(m4858);

            api.parameter("transform", m4858);
            api.parameter("texture", teksture);
            api.parameter("shaders", shaderz);
            String[] mods = new String[]{"modGrainySlopes4858"};
            api.parameter("modifiers", mods);
            api.instance("instance_" + name, "decor4858");
        }

        if (logoonstuds.equals("on")) {
            m.LogoOnStuds(api, geoname, shdr, m4, logoonstuds_adjustLOS);
        }

        p.checkNextToken("}");
    }

    private void parseDecorBlock(SunflowAPI api) throws ParserException, IOException {
        p.checkNextToken("{");

        String bublibleDecorPath = "bublible/img/d/bublible_";

        p.checkNextToken("type");
        String type = p.getNextToken();
        UI.printInfo(Module.API, "Reading additional decoration: %s ...", type);

        String teksture;
        if (p.peekNextToken("texture")) {
            teksture = p.getNextToken();
        } else {
            teksture = bublibleDecorPath + type + ".png";
        }

        p.checkNextToken("lddbrick");
        String lddbrick = p.getNextToken();

        String shdr;
        p.checkNextToken("shader");
        shdr = p.getNextToken();
        String[] shadersz = new String[]{shdr};

        String[] modifiers = null;
        String bc = type.split("p")[0];
        if (Arrays.asList(m.checkGrainySlopes()).contains(bc)) {
            modifiers = new String[]{"modGrainySlopes" + bc};
        }

        int nr = Decorations.checkDecorFaces(type);
        int brickTypeCount = Decorations.addDecorNameSequence(type);
        for (int loop = 0; loop < nr; loop++) {
            //api.parameter("w2c", false);
            api.parameter("shaders", shadersz);
            if (modifiers != null) {
                api.parameter("modifiers", modifiers);
            }
            // CRATER BASEPLATE
            if (type.equals("3947")) {
                String tp;
                if (loop == 0) {
                    tp = type + "_studs";
                } else {
                    tp = type + "_crater";
                }

                Matrix4 m4 = Decorations.setAdditionalDecoration(lddbrick, type, loop);
                api.parameter("transform", m4);
                api.instance("instance_" + tp + "_" + brickTypeCount + "_" + (loop + 1), tp);

                if (logoonstuds.equals("on")) {
                    m.LogoOnStuds(api, tp, shdr, m4, logoonstuds_adjustLOS);
                }
                // ALL THE OTHER "ORDINARY" BRICKS
            } else {
                String tkstr = teksture;
                String delim = ".png";
                if (type.equals("61780tex02")) {
                    tkstr = teksture.split(delim)[0] + "_" + loop + delim;
                } else if (type.equals("2340pb001") && loop == 1) {
                    tkstr = bublibleDecorPath + type + "inv.png";
                } else if ((type.equals("4760c01pb02") && loop == 1) || (type.equals("4760c01pb02") && loop == 3)) {
                    tkstr = bublibleDecorPath + "blank.png";
                }
                api.parameter("texture", tkstr);

                api.parameter("transform", Decorations.setAdditionalDecoration(lddbrick, type, loop));
                switch (type) {
                    case "4858p90":
                        api.instance("instance_" + type + "_" + brickTypeCount + "_" + (loop + 1), "decor4858");
                        break;
                    case "2340pb001":
                        String decorTyp = "decor2340";
                        if (loop == 1) {
                            decorTyp = "decor2340inv";
                        }
                        api.instance("instance_" + type + "_" + brickTypeCount + "_" + (loop + 1), decorTyp);
                        break;
                    default:
                        api.instance("instance_" + type + "_" + brickTypeCount + "_" + (loop + 1), "decorRectangle");
                        break;
                }
            }
        }

        p.checkNextToken("}");
    }

    private void parseLightBlock(SunflowAPI api) throws ParserException, IOException {
        p.checkNextToken("{");
        p.checkNextToken("type");
        if (p.peekNextToken("mesh")) {
            UI.printWarning(Module.API, "Deprecated light type: mesh");
            p.checkNextToken("name");
            String name = p.getNextToken();
            UI.printInfo(Module.API, "Reading light mesh: %s ...", name);
            p.checkNextToken("emit");
            api.parameter("radiance", parseColor());
            int samples = numLightSamples;
            if (p.peekNextToken("samples")) {
                samples = p.getNextInt();
            } else {
                UI.printWarning(Module.API, "Samples keyword not found - defaulting to %d", samples);
            }
            api.parameter("samples", samples);
            int numVertices = p.getNextInt();
            int numTriangles = p.getNextInt();
            float[] points = new float[3 * numVertices];
            int[] triangles = new int[3 * numTriangles];
            for (int i = 0; i < numVertices; i++) {
                p.checkNextToken("v");
                points[3 * i + 0] = p.getNextFloat();
                points[3 * i + 1] = p.getNextFloat();
                points[3 * i + 2] = p.getNextFloat();
                // ignored
                p.getNextFloat();
                p.getNextFloat();
                p.getNextFloat();
                p.getNextFloat();
                p.getNextFloat();
            }
            for (int i = 0; i < numTriangles; i++) {
                p.checkNextToken("t");
                triangles[3 * i + 0] = p.getNextInt();
                triangles[3 * i + 1] = p.getNextInt();
                triangles[3 * i + 2] = p.getNextInt();
            }
            api.parameter("points", "point", "vertex", points);
            api.parameter("triangles", triangles);
            TriangleMeshLight mesh = new TriangleMeshLight();
            mesh.init(name, api);
        } else if (p.peekNextToken("point")) {
            UI.printInfo(Module.API, "Reading point light ...");
            Color pow;
            if (p.peekNextToken("color")) {
                pow = parseColor();
                p.checkNextToken("power");
                float po = p.getNextFloat();
                pow.mul(po);
            } else {
                UI.printWarning(Module.API, "Deprecated color specification - please use color and power instead");
                p.checkNextToken("power");
                pow = parseColor();
            }
            api.parameter("power", pow);

            w2c = false;
            if (p.peekNextToken("w2c")) {
                w2c = true;
            }

            if (p.peekNextToken("p")) {
                api.parameter("center", parsePoint());
            } else if (p.peekNextToken("transform")) {
                api.parameter("center", parseMatrix("light").transformP(new Point3(0, 0, 0)));
            }

            api.light(api.getUniqueName("pointlight"), new PointLight());
        } else if (p.peekNextToken("spherical")) {
            UI.printInfo(Module.API, "Reading spherical light ...");
            p.checkNextToken("color");
            Color pow = parseColor();

            String tp = "constant";
            if (p.peekNextToken("balltype")) {
                tp = p.getNextToken();
            }
            api.parameter("balltype", tp);

            Color bc = pow;
            if (p.peekNextToken("ballcolor")) {
                bc = parseColor();
            }
            api.parameter("ballcolor", bc);

            p.checkNextToken("radiance");
            pow.mul(p.getNextFloat());
            api.parameter("radiance", pow);

            w2c = false;
            if (p.peekNextToken("w2c")) {
                w2c = true;
            }

            if (p.peekNextToken("center")) {
                api.parameter("center", parsePoint());
            } else if (p.peekNextToken("transform")) {
                api.parameter("center", parseMatrix("light").transformP(new Point3(0, 0, 0)));
            }

            p.checkNextToken("radius");
            api.parameter("radius", p.getNextFloat());
            p.checkNextToken("samples");
            api.parameter("samples", p.getNextInt());

            boolean noball = false;
            if (p.peekNextToken("noball")) {
                noball = true;
            }
            api.parameter("noball", noball);

            SphereLight light = new SphereLight();
            light.init(api.getUniqueName("spherelight"), api);
        } else if (p.peekNextToken("directional")) {
            UI.printInfo(Module.API, "Reading directional light ...");
            Point3 s = new Point3(0, 0, 0);

            w2c = false;
            if (p.peekNextToken("w2c")) {
                w2c = true;
            }

            if (p.peekNextToken("source")) {
                s = parsePoint();
                api.parameter("source", s);
            } else if (p.peekNextToken("sourcetransform")) {
                s = parseMatrix("light").transformP(new Point3(0, 0, 0));
                api.parameter("source", s);
            }
            Point3 t = new Point3(0, 0, 0);
            if (p.peekNextToken("target")) {
                t = parsePoint();
            } else if (p.peekNextToken("targettransform")) {
                t = parseMatrix("light").transformP(new Point3(0, 0, 0));
            }
            api.parameter("dir", Point3.sub(t, s, new Vector3()));
            p.checkNextToken("radius");
            api.parameter("radius", p.getNextFloat());
            p.checkNextToken("emit");
            Color e = parseColor();
            if (p.peekNextToken("intensity")) {
                e.mul((float) p.getNextFloat());
            } else {
                UI.printWarning(Module.API, "Deprecated color specification - please use emit and intensity instead");
            }
            api.parameter("radiance", e);
            api.light(api.getUniqueName("dirlight"), new DirectionalSpotlight());
        } else if (p.peekNextToken("ibl")) {
            UI.printInfo(Module.API, "Reading image based light ...");
            p.checkNextToken("image");
            api.parameter("texture", p.getNextToken());
            p.checkNextToken("center");
            api.parameter("center", parseVector());
            p.checkNextToken("up");
            api.parameter("up", parseVector());
            p.checkNextToken("lock");
            api.parameter("fixed", p.getNextBoolean());
            int samples = numLightSamples;
            if (p.peekNextToken("samples")) {
                samples = p.getNextInt();
            } else {
                UI.printWarning(Module.API, "Samples keyword not found - defaulting to %d", samples);
            }
            api.parameter("samples", samples);
            int power = 1;
            if (p.peekNextToken("power")) {
                power = p.getNextInt();
            } else {
                UI.printWarning(Module.API, "IBL Light: Power keyword not found - defaulting to %d", power);
            }
            api.parameter("power", power);
            ImageBasedLight ibl = new ImageBasedLight();
            ibl.init(api.getUniqueName("ibl"), api);
        } else if (p.peekNextToken("meshlight")) {
            p.checkNextToken("name");
            String name = p.getNextToken();
            UI.printInfo(Module.API, "Reading meshlight: %s ...", name);
            p.checkNextToken("emit");
            Color e = parseColor();
            if (p.peekNextToken("radiance")) {
                e.mul((float) p.getNextFloat());
            } else {
                UI.printWarning(Module.API, "Deprecated color specification - please use emit and radiance instead");
            }
            api.parameter("radiance", e);
            int samples = numLightSamples;
            if (p.peekNextToken("samples")) {
                samples = p.getNextInt();
            } else {
                UI.printWarning(Module.API, "Samples keyword not found - defaulting to %d", samples);
            }
            api.parameter("samples", samples);
            // parse vertices
            p.checkNextToken("points");
            int np = p.getNextInt();
            api.parameter("points", "point", "vertex", parseFloatArray(np * 3));
            // parse triangle indices
            p.checkNextToken("triangles");
            int nt = p.getNextInt();
            api.parameter("triangles", parseIntArray(nt * 3));
            TriangleMeshLight mesh = new TriangleMeshLight();
            mesh.init(name, api);
        } else if (p.peekNextToken("sunsky")) {
            /*p.checkNextToken("up");
             api.parameter("up", parseVector());
             p.checkNextToken("east");
             api.parameter("east", parseVector());
             p.checkNextToken("sundir");
             api.parameter("sundir", parseVector());
             p.checkNextToken("turbidity");
             api.parameter("turbidity", p.getNextFloat());
             if (p.peekNextToken("samples")) {
             api.parameter("samples", p.getNextInt());
             }*/

            Vector3 up = new Vector3(0f, 1f, 0f);
            if (p.peekNextToken("up")) {
                up = parseVector();
            }
            api.parameter("up", up);

            Vector3 east = new Vector3(1f, 0f, 0f);
            if (p.peekNextToken("east")) {
                east = parseVector();
            }
            api.parameter("east", east);

            Vector3 sundir = new Vector3(1f, 1f, 1f);
            if (p.peekNextToken("sundir")) {
                sundir = parseVector();
            }
            api.parameter("sundir", sundir);

            float turbidity = 7f;
            if (p.peekNextToken("turbidity")) {
                turbidity = p.getNextFloat();
            }
            api.parameter("turbidity", turbidity);

            int samples = 64;
            if (p.peekNextToken("samples")) {
                samples = p.getNextInt();
            }
            api.parameter("samples", samples);

            SunSkyLight sunsky = new SunSkyLight();
            sunsky.init(api.getUniqueName("sunsky"), api);

        } else if (p.peekNextToken("konstant")) {

            Vector3 up = new Vector3(0f, 1f, 0f);
            if (p.peekNextToken("up")) {
                up = parseVector();
            }
            api.parameter("up", up);

            Vector3 east = new Vector3(1f, 0f, 0f);
            if (p.peekNextToken("east")) {
                east = parseVector();
            }
            api.parameter("east", east);

            Vector3 sundir = new Vector3(1f, 1f, 1f);
            if (p.peekNextToken("sundir")) {
                sundir = parseVector();
            }
            api.parameter("sundir", sundir);

            float turbidity = 7f;
            if (p.peekNextToken("turbidity")) {
                turbidity = p.getNextFloat();
            }
            api.parameter("turbidity", turbidity);

            int samples = 64;
            if (p.peekNextToken("samples")) {
                samples = p.getNextInt();
            }
            api.parameter("samples", samples);

            float power = 0f;
            if (p.peekNextToken("power")) {
                power = p.getNextFloat();
            }
            api.parameter("power", power);

            float shadow = 1f;
            if (p.peekNextToken("shadow")) {
                shadow = p.getNextFloat();
            }
            api.parameter("shadow", shadow);

            boolean addLongShadows = true;
            if (p.peekNextToken("addLongShadows")) {
                addLongShadows = p.getNextBoolean();
            }
            api.parameter("addLongShadows", addLongShadows);

            boolean autoColor = true;
            if (p.peekNextToken("autoColor")) {
                autoColor = p.getNextBoolean();
            }
            api.parameter("autoColor", autoColor);

            KonstantLight konstant = new KonstantLight();
            konstant.init(api.getUniqueName("konstant"), api);

        } else if (p.peekNextToken("rectangle")) {
            p.checkNextToken("color");
            Color e = parseColor();
            p.checkNextToken("radiance");
            e.mul((float) p.getNextFloat());
            api.parameter("radiance", e);

            w2c = false;
            if (p.peekNextToken("w2c")) {
                w2c = true;
            }

            Matrix4 meshUpdate = null;
            if (p.peekNextToken("transform")) {
                meshUpdate = parseMatrix("light");
            }

            api.parameter("points", "point", "vertex", parseMeshlightFloatArray(meshUpdate));
            int[] tris = {0, 1, 2, 0, 2, 3};
            api.parameter("triangles", tris);

            boolean noball = false;
            if (p.peekNextToken("noball")) {
                noball = true;
            }
            api.parameter("noball", noball);

            RectangleLight mesh = new RectangleLight();
            mesh.init(api);

        } else {
            UI.printWarning(Module.API, "Unrecognized object type: %s", p.getNextToken());
        }
        p.checkNextToken("}");
    }

    private Color parseColor() throws IOException, ParserException {
        Color col = null;
        if (p.peekNextToken("{")) {
            String space = p.getNextToken();
            //Color c = null;
            if (space.equals("sRGB nonlinear")) {
                float r = p.getNextFloat();
                float g = p.getNextFloat();
                float b = p.getNextFloat();
                col = new Color(r, g, b);
                col.toLinear();
            } else if (space.equals("sRGB linear")) {
                float r = p.getNextFloat();
                float g = p.getNextFloat();
                float b = p.getNextFloat();
                col = new Color(r, g, b);
            } else if (space.length() == 6) {
                //System.out.println("space = " + space);
                col = new Color(space);
            } else {
                UI.printWarning(Module.API, "Unrecognized color space: %s", space);
            }
            p.checkNextToken("}");
            return col;
        } else {
            float r = p.getNextFloat();
            float g = p.getNextFloat();
            float b = p.getNextFloat();
            return new Color(r, g, b);
            //c = new Color(r, g, b);
        }
        //return Color.blend(c, Color.BLACK, rndRng(0, 100)/10);
    }

    private Point3 parsePoint() throws IOException {
        float x = p.getNextFloat();
        float y = p.getNextFloat();
        float z = p.getNextFloat();
        return new Point3(x, y, z);
    }

    private Vector3 parseVector() throws IOException {
        float x = p.getNextFloat();
        float y = p.getNextFloat();
        float z = p.getNextFloat();
        return new Vector3(x, y, z);
    }

    private int[] parseIntArray(int size) throws IOException {
        int[] data = new int[size];
        for (int i = 0; i < size; i++) {
            data[i] = p.getNextInt();
        }
        return data;
    }

    private float[] parseFloatArray(int size) throws IOException {
        float[] data = new float[size];
        for (int i = 0; i < size; i++) {
            data[i] = p.getNextFloat();
        }
        return data;
    }

    private float[] parseMeshlightFloatArray(Matrix4 u) throws IOException {
        //float pX = 0, pY = 0, pZ = 0f;
        float[] v = {0f, 0f, 0f, 0f, 1f, 0f, 1f, 1f, 0f, 1f, 0f, 0f};
        float[] data = new float[v.length];
        int p3 = 0;
        for (int i = 0; i < v.length; i++) {
            if (p3 < 2) {
                p3++;
            } else if (p3 == 2) {

                data[i - 2] = (u.m00 * v[i - 2]) + (u.m01 * v[i - 1]) + (u.m02 * v[i]) + u.m03;
                data[i - 1] = (u.m10 * v[i - 2]) + (u.m11 * v[i - 1]) + (u.m12 * v[i]) + u.m13;
                data[i] = (u.m20 * v[i - 2]) + (u.m21 * v[i - 1]) + (u.m22 * v[i]) + u.m23;

                p3 = 0;
            }
        }
        return data;
    }

    private Matrix4 parseMatrix(String typ) throws IOException, ParserException {
        if (p.peekNextToken("row")) {
            return new Matrix4(parseFloatArray(16), true);
        } else if (p.peekNextToken("col")) {
            return new Matrix4(parseFloatArray(16), false);
        } else {
            Matrix4 matrix = Matrix4.IDENTITY;
            p.checkNextToken("{");
            while (!p.peekNextToken("}")) {
                Matrix4 t = null;
                if (p.peekNextToken("lddbrick")) {
                    t = Matrix4.parseFrom4x3String((String) p.getNextToken());
                } else if (p.peekNextToken("row")) {
                    t = new Matrix4(parseFloatArray(16), true);
                    if (brickinfo.equals("on")) {
                        cmdA.add(brickName + ":::ROW:::" + t);
                    }
                } else if (p.peekNextToken("col")) {
                    t = new Matrix4(parseFloatArray(16), false);
                    if (brickinfo.equals("on")) {
                        cmdA.add(brickName + ":::COL:::" + t);
                    }
                } else if (p.peekNextToken("translate")) {
                    float x = p.getNextFloat();
                    float y = p.getNextFloat();
                    float z = p.getNextFloat();
                    t = (w2c && (typ.equals("light") || typ.equals("instance"))) ? Matrix4.rotateY((float) Math.toRadians(SunflowAPI.cameraRotY)).multiply(Matrix4.translation(x, y, z)) : Matrix4.translation(x, y, z);
                } else if (p.peekNextToken("scaleu")) {
                    t = Matrix4.scale((float) p.getNextFloat());
                } else if (p.peekNextToken("scale")) {
                    float x = p.getNextFloat();
                    float y = p.getNextFloat();
                    float z = p.getNextFloat();
                    t = Matrix4.scale(x, y, z);
                } else if (p.peekNextToken("rotatex")) {
                    t = Matrix4.rotateX((float) Math.toRadians((float) p.getNextFloat()));
                } else if (p.peekNextToken("rotatey")) {
                    t = Matrix4.rotateY((float) Math.toRadians((float) p.getNextFloat()));
                } else if (p.peekNextToken("rotatez")) {
                    t = Matrix4.rotateZ((float) Math.toRadians((float) p.getNextFloat()));
                } else if (p.peekNextToken("rotate")) {
                    float x = p.getNextFloat();
                    float y = p.getNextFloat();
                    float z = p.getNextFloat();
                    t = Matrix4.rotate(x, y, z, (float) Math.toRadians((float) p.getNextFloat()));
                } else {
                    UI.printWarning(Module.API, "Unrecognized transformation type: %s", p.getNextToken());
                }
                if (t != null) {
                    matrix = t.multiply(matrix);
                }
            }
            return matrix;
        }
    }

    public static String checkAttributeStatus(String var) {
        switch (var) {
            case "cmdtolog":
                return cmdtolog;
            case "brickinfo":
                return brickinfo;
            case "exactdecorbp":
                return exactdecorbp;
            case "rubberbricks":
                return rubberbricks;
            default:
                return null;
        }
    }
}
