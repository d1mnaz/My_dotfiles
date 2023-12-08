Vim�UnDo� �_q.4^p�ru��@���KWyK� M�0   M                 8       8   8   8    e��   4 _�                           ����                                                                                                                                                                                                                                                                                                                                                             e6    �      
   1    5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             e7    �         2       �   	   
   2    5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                             e7     �   
      3    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       eJ    �         3      +    <DocsPage toc={toc} footer={neighbour}>�         3    5�_�                            ����                                                                                                                                                                                                                                                                                                                                         *       v       e"_     �               3   8import { getPage, getPageUrl, tree } from '@/app/source'   0import { allDocs } from 'contentlayer/generated'   $import type { Metadata } from 'next'   -import { MDXContent } from 'next-docs-ui/mdx'   ,import { DocsPage } from 'next-docs-ui/page'   Iimport { findNeighbour, getTableOfContents } from 'next-docs-zeta/server'   *import { notFound } from 'next/navigation'   #import { Content } from './content'   <import { DashboardTableOfContents } from "@/components/toc";           $export default async function Page({     params   }: {     params: { slug?: string[] }   }) {   #  const page = getPage(params.slug)         if (page == null) {       notFound()     }       5  const toc = await getTableOfContents(page.body.raw)   @  const neighbour = findNeighbour(tree, getPageUrl(params.slug))       
  return (   @    <DocsPage toc={DashboardTableOfContents} footer={neighbour}>         <MDXContent>           <h1>{page.title}</h1>   )        <Content code={page.body.code} />         </MDXContent>       </DocsPage>     )   }       Mexport async function generateStaticParams(): Promise<{ slug: string[] }[]> {     return allDocs.map(page => ({       slug: page.slug.split('/')     }))   }       Oexport function generateMetadata({ params }: { params: { slug?: string[] } }) {   #  const page = getPage(params.slug)         if (page == null) return       
  return {       title: page.title,   !    description: page.description     } satisfies Metadata   }5�_�                       *    ����                                                                                                                                                                                                                                                                                                                                                             e"�    �         2      ,    <DocsPage toc={toc} footer={neighbour} >5�_�      	                 +    ����                                                                                                                                                                                                                                                                                                                                                             e"�    �         2    5�_�      
           	      2    ����                                                                                                                                                                                                                                                                                                                                                             e"�   	 �         2    5�_�   	              
      3    ����                                                                                                                                                                                                                                                                                                                                                             e"�   
 �         2    5�_�   
                    4    ����                                                                                                                                                                                                                                                                                                                                                             e"�    �         2    5�_�                       3    ����                                                                                                                                                                                                                                                                                                                                                             e"�    �         2    5�_�                       4    ����                                                                                                                                                                                                                                                                                                                                                             e"�    �         2    5�_�                       7    ����                                                                                                                                                                                                                                                                                                                                                             e"�    �         2    5�_�                       9    ����                                                                                                                                                                                                                                                                                                                                                             e"�     �         2    5�_�                       +    ����                                                                                                                                                                                                                                                                                                                               +          :       v   :    e"�    �         2      <    <DocsPage toc={toc} footer={neighbour} enabled={false} >5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e�R    �      #   2    �         2    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�[    �      
   6    �      	   6    5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             e�b    �      $   3    �          7      (                    {toc.length > 0 && (   G                        <h3 className="font-semibold">On this page</h3>                       )}   '                    <TOC items={toc} />5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       eʎ    �         7      ,    <DocsPage toc={toc} footer={neighbour} >5�_�                             ����                                                                                                                                                                                                                                                                                                                                       #          V       eʫ    �                       {toc.length > 0 && (   7        <h3 className="font-semibold">On this page</h3>         )}         <TOC items={toc} />5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V       eʭ    �      #   3    �         3    5�_�                            ����                                                                                                                                                                                                                                                                                                                                      $          V       e��    �      ,   -    �         -    �             
   "    <DocsPage footer={neighbour} >         <MDXContent>           <h1>{page.title}</h1>   )        <Content code={page.body.code} />         {toc.length > 0 && (   7        <h3 className="font-semibold">On this page</h3>         )}         <TOC items={toc} />         </MDXContent>       </DocsPage>5�_�                           ����                                                                                                                                                                                                                                                                                                                                       +   
       V       e��    �      ,   -    �         >      
        <>   U            <article className="flex flex-col gap-6 py-8 overflow-x-hidden lg:py-16">   >                <Breadcrumb pathname={pathname} tree={tree} />   D                <h1 className="text-4xl font-bold">{page.title}</h1>   '                <div className="prose">   8                    <MdxContent code={page.body.code} />                   </div>               </article>   N            <div className="relative flex flex-col gap-3 max-xl:hidden py-16">   o                <div className="sticky top-28 flex flex-col gap-3 overflow-auto max-h-[calc(100vh-4rem-3rem)]">   (                    {toc.length > 0 && (   G                        <h3 className="font-semibold">On this page</h3>                       )}   '                    <TOC items={toc} />                   </div>               </div>           </>5�_�                           ����                                                                                                                                                                                                                                                                                                                            ,           ,   
       V       e��    �                6        <Breadcrumb pathname={pathname} tree={tree} />5�_�                           ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�     �          =      .          <MdxContent code={page.body.code} />5�_�                           ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�     �          =      -          <dxContent code={page.body.code} />5�_�                           ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�    �          =      ,          <xContent code={page.body.code} />5�_�                    %   *    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�0    �   $   &   =      ;            <h3 className="font-semibold">On this page</h3>5�_�                    %   *    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�1    �   $   &   =      /            <h3 className="font-semibold"></h3>�   %   &   =    5�_�                     %   ,    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�2    �   %   &   =    5�_�      !               %   .    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�3    �   %   &   =    5�_�       "           !   %   /    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�3    �   %   &   =    5�_�   !   #           "   %   1    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�4     �   %   &   =    5�_�   "   $           #   %   /    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�5   ! �   %   &   =    5�_�   #   %           $   %   1    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�5   " �   %   &   =    5�_�   $   &           %   %   5    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�6   # �   %   &   =    5�_�   %   '           &   %   7    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�6   $ �   %   &   =    5�_�   &   (           '   %   8    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�6   % �   %   &   =    5�_�   '   )           (   %   :    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�7   & �   %   &   =    5�_�   (   *           )   %   @    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�8   ' �   %   &   =    5�_�   )   +           *   %   D    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�9   ( �   %   &   =    5�_�   *   ,           +   %   F    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�9   ) �   %   &   =    5�_�   +   -           ,   %   H    ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e�:     �   %   &   =    5�_�   ,   .           -   -        ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e˕   * �   -   ?   =    �   -   .   =    5�_�   -   /           .           ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       eˠ   + �         N    �         N    5�_�   .   0           /           ����                                                                                                                                                                                                                                                                                                                            ,           ,   
       V       eˮ   , �                -import { MDXContent } from 'next-docs-ui/mdx'5�_�   /   1           0           ����                                                                                                                                                                                                                                                                                                                            +           +   
       V       e˰   - �                ,import { DocsPage } from 'next-docs-ui/page'5�_�   0   2           1          ����                                                                                                                                                                                                                                                                                                                            *           *   
       V       e˷   . �         M      +          <Content code={page.body.code} />5�_�   1   3           2          ����                                                                                                                                                                                                                                                                                                                            *           *   
       V       e˷   / �         M    5�_�   2   4           3          ����                                                                                                                                                                                                                                                                                                                            *           *   
       V       e˸   0 �         M    5�_�   3   5           4          ����                                                                                                                                                                                                                                                                                                                            *           *   
       V       e˸     �         M    5�_�   4   6           5          ����                                                                                                                                                                                                                                                                                                                            *           *   
       V       e��   1 �         M      .          <MDXContent code={page.body.code} />5�_�   5   7           6          ����                                                                                                                                                                                                                                                                                                                            *           *   
       V       e��   2 �         M      .          <MdXContent code={page.body.code} />5�_�   6   8           7   3       ����                                                                                                                                                                                                                                                                                                                            *           *   
       V       e��   3 �   2   3                          a: SafeLink,5�_�   7               8           ����                                                                                                                                                                                                                                                                                                                            *           *   
       V       e��   4 �         L    �         L    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e*    �      	   1    �      	   1       5��