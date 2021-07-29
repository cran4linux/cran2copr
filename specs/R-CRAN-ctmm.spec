%global __brp_check_rpaths %{nil}
%global packname  ctmm
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Continuous-Time Movement Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Bessel 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-fasttime 
BuildRequires:    R-CRAN-Gmedian 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-manipulate 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Bessel 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-fasttime 
Requires:         R-CRAN-Gmedian 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-manipulate 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-statmod 
Requires:         R-stats 
Requires:         R-utils 

%description
Functions for identifying, fitting, and applying continuous-space,
continuous-time stochastic movement models to animal tracking data. The
package is described in Calabrese et al (2016)
<doi:10.1111/2041-210X.12559>, with models and methods based on those
introduced in Fleming & Calabrese et al (2014) <doi:10.1086/675504>,
Fleming et al (2014) <doi:10.1111/2041-210X.12176>, Fleming et al (2015)
<doi:10.1103/PhysRevE.91.032107>, Fleming et al (2015)
<doi:10.1890/14-2010.1>, Fleming et al (2016) <doi:10.1890/15-1607>, Péron
& Fleming et al (2016) <doi:10.1186/s40462-016-0084-7>, Fleming &
Calabrese (2017) <doi:10.1111/2041-210X.12673>, Péron et al (2017)
<doi:10.1002/ecm.1260>, Fleming et al (2017)
<doi:10.1016/j.ecoinf.2017.04.008>, Fleming et al (2018)
<doi:10.1002/eap.1704>, Winner & Noonan et al (2018)
<doi:10.1111/2041-210X.13027>, Fleming et al (2019)
<doi:10.1111/2041-210X.13270>, Noonan & Fleming et al (2019)
<doi:10.1186/s40462-019-0177-1>, Fleming et al (2020)
<doi:10.1101/2020.06.12.130195>, and Noonan et al (2021)
<doi:10.1111/2041-210X.13597>.

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
