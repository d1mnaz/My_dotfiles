Vim�UnDo� �s<]^)�Зbu*d`�~���b띷ዥh"��   	                                   d�ӗ    _�                             ����                                                                                                                                                                                                                                                                                                                                       	           V        d��%    �              	   "use client";   ;import React, { useState, MouseEventHandler } from "react";   import Link from "next/link";   import Image from "next/image";   &import MenuButton from "./MenuButton";   &import ActiveLink from "./ActiveLink";       'export function Navbar(): JSX.Element {   7  const [active, setActive] = useState<boolean>(false);5�_�                            ����                                                                                                                                                                                                                                                                                                                                      $           V        d��+    �                0  const handleClick: MouseEventHandler = () => {       setActive(!active);     };       
  return (       <>   N      <nav className="flex items-center flex-wrap p-3 mx-5 md:mx-20 lg:mx-24">           <Link href="/">             <Image               src="/logo.png"   a            className="fill-current text-black h-24 w-20 mr-2 cursor-pointer bg-white rounded-lg"               width={100}               height={100}               alt="ФВКР"             />           </Link>   0        <MenuButton handleClick={handleClick} />           <div   _          className={`${active ? "" : "hidden"} w-full lg:inline-flex lg:flex-grow lg:w-auto`}>   �          <ul className="flex flex-col w-full items-start lg:items-center lg:inline-flex lg:flex-row lg:ml-auto lg:w-auto lg:h-auto">   *            {PAGE_LINKS.map((link, i) => (   0              <ActiveLink link={link} key={i} />               ))}             </ul>           </div>         </nav>       </>     );   }5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V        d��0    �                  const PAGE_LINKS = [5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V        d��0    �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V        d��2     �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V        d��7    �               �                 +    { href: "/", title: "Главная" },   +    { href: "/about", title: "О нас" },   ;    { href: "/sportsmens", title: "Спортсмены" },   0    { href: "/coach", title: "Тренеры" },   -    { href: "/judges", title: "Судьи" },     ];5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V        d��u    �                export const PAGE_LINKS = [5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                 V        d��u    �             5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                 V        d��v    �             5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                 V        d��w   	 �             5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                 V        d��w   
 �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V        d��x     �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V        d�ӄ    �                #export default const PAGE_LINKS = [5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V        d�ӄ    �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V        d�ӆ     �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V        d�Ӊ    �               5�_�                            ����                                                                                                                                                                                                                                                                                                                            	          	           V        d�ӊ    �                  �               5�_�                    	        ����                                                                                                                                                                                                                                                                                                                            
          
           V        d�ӊ    �   	            5�_�                    	       ����                                                                                                                                                                                                                                                                                                                            
          
           V        d�Ӎ    �   	            5�_�                    	       ����                                                                                                                                                                                                                                                                                                                            
          
           V        d�ӎ    �   	            5�_�                    	       ����                                                                                                                                                                                                                                                                                                                            
          
           V        d�ӎ    �   	            5�_�                    	       ����                                                                                                                                                                                                                                                                                                                            
          
           V        d�ӏ    �   	            5�_�                    	       ����                                                                                                                                                                                                                                                                                                                            
          
           V        d�Ӑ    �   	            5�_�                    	       ����                                                                                                                                                                                                                                                                                                                            
          
           V        d�Ӓ    �   	            5�_�                    	       ����                                                                                                                                                                                                                                                                                                                            
          
           V        d�ӓ    �   	            5�_�                    	       ����                                                                                                                                                                                                                                                                                                                            
          
           V        d�Ӕ    �   	            5�_�                    	       ����                                                                                                                                                                                                                                                                                                                            
          
           V        d�ӕ    �   	            5�_�                    	       ����                                                                                                                                                                                                                                                                                                                            
          
           V        d�ӕ    �   	            5�_�                     	       ����                                                                                                                                                                                                                                                                                                                            
          
           V        d�Ӗ    �   	            5��