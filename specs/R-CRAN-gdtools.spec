%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gdtools
%global packver   0.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for Graphical Rendering and Fonts Management

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cairo-devel
BuildRequires:    freetype-devel
BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-fontquiver >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-systemfonts >= 0.1.1
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-gfonts 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-fontquiver >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-systemfonts >= 0.1.1
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-gfonts 
Requires:         R-tools 
Requires:         R-CRAN-curl 

%description
Tools are provided to compute metrics of formatted strings and to check
the availability of a font. Another set of functions is provided to
support the collection of fonts from 'Google Fonts' in a cache. Their use
is simple within 'R Markdown' documents and 'shiny' applications but also
with graphic productions generated with the 'ggiraph', 'ragg' and
'svglite' packages or with tabular productions from the 'flextable'
package.

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
