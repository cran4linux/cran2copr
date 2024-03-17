%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mosaicCalc
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          R-Language Based Calculus Operations for Teaching

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mosaicCore >= 0.9.2
BuildRequires:    R-CRAN-metR >= 0.11.0
BuildRequires:    R-CRAN-mosaic 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggformula 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-orthopolynom 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Ryacas 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-mosaicCore >= 0.9.2
Requires:         R-CRAN-metR >= 0.11.0
Requires:         R-CRAN-mosaic 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggformula 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-orthopolynom 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Ryacas 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
Software to support the introductory *MOSAIC Calculus* textbook
<https://www.mosaic-web.org/MOSAIC-Calculus/>), one of many data- and
modeling-oriented educational resources developed by Project MOSAIC
(<https://www.mosaic-web.org/>). Provides symbolic and numerical
differentiation and integration, as well as support for applied linear
algebra (for data science), and differential equations/dynamics. Includes
grammar-of-graphics-based functions for drawing vector fields,
trajectories, etc. The software is suitable for general use, but intended
mainly for teaching calculus.

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
