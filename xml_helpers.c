/*
 * xml_helpers.c -- Helper functions for the OCaml XML bindings.
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

#include "xml_helpers.h"

value
xml_string_option(value opt)
{
	CAMLparam1(opt);

	if (Is_long(opt))    /* None */
		CAMLreturn(0);
	else                 /* Some x */
		CAMLreturn(Field(opt, 0));
}
