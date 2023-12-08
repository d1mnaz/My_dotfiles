Vim�UnDo� ���S ۓ?�!��bEdz}�>fئF��ן   J   t          {doc.description && <p className="mt-0 text-xl text-slate-700 dark:text-slate-200">{post.description}</p>}   >   ^                       d�Zo    _�                             ����                                                                                                                                                                                                                                                                                                                                                             d�U�    �                .import { getTableOfContents } from "@/lib/toc"5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        d�U�    �                9import { DocsPageHeader } from "@/components/page-header"   .import { DocsPager } from "@/components/pager"   ;import { DashboardTableOfContents } from "@/components/toc"5�_�                           ����                                                                                                                                                                                                                                                                                                                                       
           V        d�U�    �                import "@/styles/mdx.css"5�_�                    '        ����                                                                                                                                                                                                                                                                                                                            '          *          V       d�Vz    �   &   '          (  const ogUrl = new URL(`${url}/api/og`)   A  ogUrl.searchParams.set("heading", doc.description ?? doc.title)   1  ogUrl.searchParams.set("type", "Documentation")   (  ogUrl.searchParams.set("mode", "dark")5�_�                    %        ����                                                                                                                                                                                                                                                                                                                            '          '          V       d�V|   	 �   $   %          %  const url = env.NEXT_PUBLIC_APP_URL5�_�      	              %        ����                                                                                                                                                                                                                                                                                                                            &          &          V       d�V}   
 �   $   %           5�_�      
           	   )        ����                                                                                                                                                                                                                                                                                                                            )           <           V        d�V�    �   (   )              openGraph: {         title: doc.title,   #      description: doc.description,         type: "article",   !      url: absoluteUrl(doc.slug),         images: [   	        {              url: ogUrl.toString(),             width: 1200,             height: 630,             alt: doc.title,   
        },         ],       },       twitter: {   "      card: "summary_large_image",         title: doc.title,   #      description: doc.description,   !      images: [ogUrl.toString()],       },5�_�   	              
   ;       ����                                                                                                                                                                                                                                                                                                                            )           )           V        d�V�    �   :   ;          4  const toc = await getTableOfContents(doc.body.raw)5�_�   
                 :        ����                                                                                                                                                                                                                                                                                                                            )           )           V        d�V�    �   9   :           5�_�                    <        ����                                                                                                                                                                                                                                                                                                                            <           H           V        d�V�    �   ;   K   =    �   <   =   =    �   ;   <          X    <main className="relative py-6 lg:gap-10 lg:py-10 xl:grid xl:grid-cols-[1fr_300px]">   .      <div className="mx-auto w-full min-w-0">   E        <DocsPageHeader heading={doc.title} text={doc.description} />   $        <Mdx code={doc.body.code} />   '        <hr className="my-4 md:my-6" />           <DocsPager doc={doc} />         </div>   /      <div className="hidden text-sm xl:block">   a        <div className="sticky top-16 -mt-10 max-h-[calc(var(--vh)-4rem)] overflow-y-auto pt-10">   0          <DashboardTableOfContents toc={toc} />           </div>         </div>       </main>5�_�                    <       ����                                                                                                                                                                                                                                                                                                                            <           J          V        d�V�    �   ;   K   =    �   ;   <   L      \        <main className="relative py-6 lg:gap-10 lg:py-10 xl:grid xl:grid-cols-[1fr_300px]">   4            <div className="mx-auto w-full min-w-0">   B                <article className="prose py-6 dark:prose-invert">   :                    <h1 className="mb-2">{post.title}</h1>                       {post.description && <p className="mt-0 text-xl text-slate-700 dark:text-slate-200">{post.description}</p>}   +                    <hr className="my-4" />   1                    <Mdx code={post.body.code} />                   </article>               </div>   5            <div className="hidden text-sm xl:block">   i                <div className="sticky top-16 -mt-10 max-h-[calc(var(--vh)-4rem)] overflow-y-auto pt-10">   ,                    DashboardTableOfContents                   </div>               </div>           </main>5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             d�Z2    �                import { env } from "@/env.mjs"5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             d�Z3    �                )import { absoluteUrl } from "@/lib/utils"5�_�                    =        ����                                                                                                                                                                                                                                                                                                                                                             d�ZH    �   <   >   J      0          <h1 className="mb-2">{post.title}</h1>5�_�                    =        ����                                                                                                                                                                                                                                                                                                                                                             d�ZI    �   <   >   J      ,          <h1 className="mb-2">{.title}</h1>�   =   >   J    5�_�                    =   !    ����                                                                                                                                                                                                                                                                                                                                                             d�ZJ    �   =   >   J    5�_�                    =   "    ����                                                                                                                                                                                                                                                                                                                                                             d�ZJ    �   =   >   J    5�_�                    =   #    ����                                                                                                                                                                                                                                                                                                                                                             d�ZJ     �   =   >   J    5�_�                    >       ����                                                                                                                                                                                                                                                                                                                                                             d�ZO    �   =   ?   J      u          {post.description && <p className="mt-0 text-xl text-slate-700 dark:text-slate-200">{post.description}</p>}5�_�                    @       ����                                                                                                                                                                                                                                                                                                                                                             d�ZR    �   ?   A   J      '          <Mdx code={post.body.code} />5�_�                    >   ^    ����                                                                                                                                                                                                                                                                                                                                                             d�Zm    �   =   ?   J      t          {doc.description && <p className="mt-0 text-xl text-slate-700 dark:text-slate-200">{post.description}</p>}5�_�                    >   _    ����                                                                                                                                                                                                                                                                                                                                                             d�Zm    �   >   ?   J    5�_�                     >   `    ����                                                                                                                                                                                                                                                                                                                                                             d�Zn    �   >   ?   J    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        d�U�    �              5�_�                             ����                                                                                                                                                                                                                                                                                                                                                  V        d�U�    �              5��