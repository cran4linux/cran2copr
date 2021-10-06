%global __brp_check_rpaths %{nil}
%global packname  mgcViz
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Visualisations for Generalized Additive Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv >= 1.8.28
BuildRequires:    R-CRAN-qgam >= 1.2.3
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gamm4 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
Requires:         R-CRAN-mgcv >= 1.8.28
Requires:         R-CRAN-qgam >= 1.2.3
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gamm4 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 

%description
Extension of the 'mgcv' package, providing visual tools for Generalized
Additive Models that exploit the additive structure of such models, scale
to large data sets and can be used in conjunction with a wide range of
response distributions. The focus is providing visual methods for better
understanding the model output and for aiding model checking and
development beyond simple exponential family regression. The graphical
framework is based on the layering system provided by 'ggplot2'.

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
