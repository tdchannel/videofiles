/*
<meta id="slim"><![CDATA [
slim 2 appearance slim {
    instance surface textureManip textureManip {
        parameter float Kd {
            label "Diffuse"
            default 0.8
            range {0 10 0.01}
        }
        parameter color surfaceColor {
            label "Diffuse Color"
            default { 0.5 0.5 0.5 }
        }
        parameter string map {
            label "Texture Map"
            description "Choose a tx file"
            subtype texture
            default ""
        }
        parameter float useAlpha {
            subtype switch
            default 1
        }
        parameter float rotate {
            label "Rotate"
            default 0
            range {0 360 0.01}
        }
        parameter float flipS {
            label "Flip S"
            subtype switch
            default 0
        }
        parameter float flipT {
            label "Flip T"
            subtype switch
            default 0
        }
        parameter float repeatS {
            label "Repeat S"
            subtype integer
            default 1
        }
        parameter float repeatT {
            label "Repeat T"
            subtype integer
            default 1
        }
        parameter float offsetS {
            label "Offset S"
            default 0
        }
        parameter float offsetT {
            label "Offset T"
            default 0
        }
    }
}
]]></meta>
*/

#define rotate2d(x,y,rad,ox,oy,rx,ry) \
rx = ((x) - (ox)) * cos(rad) - ((y) - (oy)) * sin(rad) + (ox);\
ry = ((x) - (ox)) * sin(rad) + ((y) - (oy)) * cos(rad) + (oy)

surface textureManip(
                    float Kd = 0.8;
                    color surfaceColor = color(0.5);
                    string map = "";
                    uniform float useAlpha = 1;
                    uniform float rotate = 0;
                    uniform float flipS = 0;
                    uniform float flipT = 0;
                    uniform float repeatS = 1;
                    uniform float repeatT = 1;
                    uniform float offsetS = 0;
                    uniform float offsetT = 0;

                     )
{
    // local variables
    normal Nn = normalize(N);
    color sc = surfaceColor;
    color lc = color(0);

    if (map != "") {
        float ss =0;
        float tt = 0;
        // texture rotation
        rotate2d(s,t,radians(rotate),0.5, 0.5,ss,tt);

        // flip texture
        ss = flipS == 1 ? 1 - ss : ss;
        tt = flipT == 1 ? 1 - tt : tt;

        // texture repeat
        ss *= repeatS;
        tt *= repeatT;

        // texture offset
        ss += offsetS;
        tt += offsetT;

        lc = color texture(map,ss,tt);

        if (useAlpha == 1) {
            uniform float numChannels = 0;
            textureinfo(map,"channels",numChannels);

            if (numChannels == 4 ) {
                sc = mix (sc,lc,float texture(map[3],ss,tt));
            } else {
                sc = lc;
            }
        } else {
            sc = lc;
        }
    }
    
	Oi = Os;
	Ci = Oi * (sc * diffuse(Nn) * Kd);
}
