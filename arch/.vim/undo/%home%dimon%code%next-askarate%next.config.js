Vim�UnDo� �u~C�㪯�fK7�(���T�;���&J�                                     e�    _�                        ,    ����                                                                                                                                                                                                                                                                                                                                                             e
�    �               �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e
�     �                )module.exports = withContentlayer(config)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e
�    �             �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        e
�    �                )module.exports = withContentlayer(config)   (/** @type {import('next').NextConfig} */   const config = {     reactStrictMode: true   }       9const { withContentlayer } = require('next-contentlayer')    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        e
�    �                (// module.exports = withMDX(nextConfig);5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        e�    �                   �               �                 :const { withContentlayer } = require("next-contentlayer");   (/** @type {import('next').NextConfig} */   const nextConfig = {       experimental: {           mdxRs: true,       },       reactStrictMode: true,       swcMinify: true,       rewrites: async () => {           return [               {   &                source: "/api/:path*",   @                destination: "http://127.0.0.1:8000/api/:path*",               },   
        ];       },   };   'const withMDX = require("@next/mdx")();   7module.exports = withContentlayer(withMDX(nextConfig));5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e
�    �              5��