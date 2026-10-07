%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  zuhtml
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parse 'HTML' with a Bundled 'Gumbo' Parser

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1

%description
Parses real-world 'HTML' with a bundled copy of the 'Gumbo' parser
(<https://codeberg.org/gumbo-parser/gumbo-parser>), which follows the
'WHATWG' parsing algorithm, so that no system library is required.
Documents become immutable trees navigated with a documented subset of
'CSS' selectors. Attributes, text, lists, tables, links, forms and page
metadata ('JSON-LD', microdata) are extracted into ordinary character
vectors, lists and data frames, and nodes convert to 'Markdown'. Input is
a string, raw bytes, a file, a URL or a connection, and raw input is
decoded as browsers decode it, from a byte-order mark or a '<meta>'
declaration. Parsing is bounded by limits on input size, native memory and
nesting depth.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
