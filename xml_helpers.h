/*
 * xml_helpers.h -- Helper functions for the OCaml XML bindings.
 *
 * This file is part of ocaml-libxml2
 *
 * Written and Copyright (c) 2005, 2007, 2008 by
 * Marcel Kyas <mkyas@users.berlios.de>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#ifndef INCLUDED_XML_HELPERS_H
#define INCLUDED_XML_HELPERS_H

#include <caml/mlvalues.h>
#include <caml/memory.h>
#include <caml/alloc.h>
#include <caml/fail.h>
#include <caml/custom.h>

#include <libxml/parser.h>
#include <libxml/tree.h>

value xml_string_option(value opt);

#define XmlDoc_val(v) (*(xmlDocPtr*) Data_custom_val(v))

value xml_doc_new(xmlDocPtr doc);

#define XsltTransformCtxt_val(v) \
	(*(xsltTransformContextPtr*) Data_custom_val(v))

#endif
