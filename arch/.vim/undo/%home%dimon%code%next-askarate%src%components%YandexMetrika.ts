Vim�UnDo� LgS�	-xu%�_��7e�ׁZ�t�b��6���[   ^                                   d���    _�                             ����                                                                                                                                                                                                                                                                                                                                                             d���    �                   5�_�                    \       ����                                                                                                                                                                                                                                                                                                                                                             d���     �   \            5�_�                     \        ����                                                                                                                                                                                                                                                                                                                                                             d���    �      ]       �         \   X   =  return (boolValue === undefined ? defaultValue : boolValue)       ? "true"       : "false";   }       function YandexMetrikaTag({     yid,     clickmap=true,     trackLinks=true,     accurateTrackBounce=true,     webvisor=true,   }) {   (  /// Tag version of the Yandex Metrika.   H  /// Used when there is support for the JavaScript to fully track user.   ^  /// Will cause loading and injecting tag script, and activate Yandex Metrika by constructor.       D  // Tag options, see your Yandex Metrika recommendations for setup.   *  clickmap = convertParam(clickmap, true);   .  trackLinks = convertParam(trackLinks, true);   @  accurateTrackBounce = convertParam(accurateTrackBounce, true);   *  webvisor = convertParam(webvisor, true);       3  // Script that injects Yandex Metrika tag script.     const scriptInjectorHTML = `   X    (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};   ~    m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})   N    (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");     `;       
  return (       <script          dangerouslySetInnerHTML={{           __html: `   !            ${scriptInjectorHTML}                ym(${yid}, "init", {   %                clickmap:${clickmap},   )                trackLinks:${trackLinks},   ;                accurateTrackBounce:${accurateTrackBounce},   $                webvisor:${webvisor}               });         `,         }}       />     );   }       &function YandexMetrikaPixel({ yid }) {   *  /// Pixel version of the Yandex Metrika.   =  /// Used when there is no JavaScript on the target browser.   r  /// This will cause the Yandex Metrika to track user by calling loading of the pixel image (with target params).       &  // Target source to load pixel from.   :  const pixelSource = `https://mc.yandex.ru/watch/${yid}`;       0  /* eslint-disable @next/next/no-img-element */   
  return (       <noscript>         <div>           <img             src={pixelSource}   ;          style={{ position: "absolute", left: "-9999px" }}             alt=""   
        />         </div>       </noscript>     );   }       'export default function YandexMetrika({     yid,     clickmap=true,     trackLinks=true,     accurateTrackBounce=true,     webvisor=true,   }) {     /// Yandex Metrika service.   
  return (       <>         <YandexMetrikaTag           yid={yid}           clickmap={clickmap}           trackLinks={trackLinks}   1        accuracyTrackBounce={accurateTrackBounce}           webvisor={webvisor}         />   &      <YandexMetrikaPixel yid={yid} />       </>     );5��