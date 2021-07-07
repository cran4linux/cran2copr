%global __brp_check_rpaths %{nil}
%global packname  FLightR
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Reconstruct Animal Paths from Solar Geolocation Loggers Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-bit 
BuildRequires:    R-CRAN-ggsn 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-CircStats 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-GeoLight 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-truncnorm 
Requires:         R-CRAN-bit 
Requires:         R-CRAN-ggsn 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-CircStats 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-GeoLight 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-maptools 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-nlme 
Requires:         R-parallel 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-truncnorm 

%description
Spatio-temporal locations of an animal are computed from annotated data
with a hidden Markov model via particle filter algorithm. The package is
relatively robust to varying degrees of shading. The hidden Markov model
is described in Movement Ecology (Rakhimberdiev et al., 2015)
<doi:10.1186/s40462-015-0062-5>, general package description is in the
Methods in Ecology and Evolution (Rakhimberdiev et al., 2017)
<doi:10.1111/2041-210X.12765> and package accuracy assessed in the Journal
of Avian Biology (Rakhimberdiev et al. 2016) <doi:10.1111/jav.00891>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
