(*
 * Xml.ml -- OCaml bindings for libxml2.
 *
 * This file is part of ocaml-libxml2
 * 
 * Written and Copyright (c) 2005, 2007, 2008 by Marcel Kyas
 * <mkyas@users.berlios.de>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see
 * <http://www.gnu.org/licenses/>.
 *)

type doc

external from_file: string -> doc = "xml_doc_from_file"
(** Parse an XML document from a file.

    @param filename The name of the source file. *)

external to_file: doc -> string -> bool -> unit = "xml_doc_to_file"
