Vim�UnDo� `���i��!<O�&��s� ��xj�|{ �                                     e
�    _�                     	        ����                                                                                                                                                                                                                                                                                                                                                             e
�    �   	          �   	   
       5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       e
�    �                   �               �                 )import { getPageUrl } from '@/app/source'   0import { allDocs } from 'contentlayer/generated'   7import { createSearchAPI } from 'next-docs-zeta/server'       2export const { GET } = createSearchAPI('simple', {   !  indexes: allDocs.map(page => ({       title: page.title,       content: page.body.raw,       url: getPageUrl(page.slug)   '    structuredData: page.structuredData     }))   })5��