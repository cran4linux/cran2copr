%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pandocfilters
%global packver   0.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Pandoc Filters for R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-utils 

%description
The document converter 'pandoc' <https://pandoc.org/> is widely used in
the R community. One feature of 'pandoc' is that it can produce and
consume JSON-formatted abstract syntax trees (AST). This allows to
transform a given source document into JSON-formatted AST, alter it by so
called filters and pass the altered JSON-formatted AST back to 'pandoc'.
This package provides functions which allow to write such filters in
native R code. Although this package is inspired by the Python package
'pandocfilters' <https://github.com/jgm/pandocfilters/>, it provides
additional convenience functions which make it simple to use the
'pandocfilters' package as a report generator. Since 'pandocfilters'
inherits most of it's functionality from 'pandoc' it can create documents
in many formats (for more information see <https://pandoc.org/>) but is
also bound to the same limitations as 'pandoc'.

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
