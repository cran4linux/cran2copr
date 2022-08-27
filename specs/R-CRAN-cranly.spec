%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cranly
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Package Directives and Collaboration Networks in CRAN

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-tm 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-tm 

%description
Core visualizations and summaries for the CRAN package database. The
package provides comprehensive methods for cleaning up and organizing the
information in the CRAN package database, for building package directives
networks (depends, imports, suggests, enhances, linking to) and
collaboration networks, producing package dependence trees, and for
computing useful summaries and producing interactive visualizations from
the resulting networks and summaries. The resulting networks can be
coerced to 'igraph' <https://CRAN.R-project.org/package=igraph> objects
for further analyses and modelling.

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
