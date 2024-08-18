%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Umatrix
%global packver   4.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization of Structures in High-Dimensional Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-tools 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-AdaptGauss 
BuildRequires:    R-CRAN-DataVisualizations 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-png 
Requires:         R-tools 
Requires:         R-grid 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-AdaptGauss 
Requires:         R-CRAN-DataVisualizations 

%description
By gaining the property of emergence through self-organization, the
enhancement of SOMs(self organizing maps) is called Emergent SOM (ESOM).
The result of the projection by ESOM is a grid of neurons which can be
visualised as a three dimensional landscape in form of the Umatrix.
Further details can be found in the referenced publications (see url).
This package offers tools for calculating and visualising the ESOM as well
as Umatrix, Pmatrix and UStarMatrix. All the functionality is also
available through graphical user interfaces implemented in 'shiny'. Based
on the recognized data structures, the method can be used to generate new
data.

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
