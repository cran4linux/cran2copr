%global __brp_check_rpaths %{nil}
%global packname  PopGenReport
%global packver   3.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          A Simple Framework to Analyse Population and Landscape Genetic Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-adegenet >= 2.0.0
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-RgoogleMaps 
BuildRequires:    R-CRAN-gap 
BuildRequires:    R-CRAN-calibrate 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-pegas 
BuildRequires:    R-CRAN-genetics 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-gdistance 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-mmod 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-raster 
Requires:         R-CRAN-adegenet >= 2.0.0
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-RgoogleMaps 
Requires:         R-CRAN-gap 
Requires:         R-CRAN-calibrate 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dismo 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-pegas 
Requires:         R-CRAN-genetics 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-gdistance 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-mmod 
Requires:         R-CRAN-GGally 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-raster 

%description
Provides beginner friendly framework to analyse population genetic data.
Based on 'adegenet' objects it uses 'knitr' to create comprehensive
reports on spatial genetic data. For detailed information how to use the
package refer to the comprehensive tutorials or visit
<http://www.popgenreport.org/>.

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
