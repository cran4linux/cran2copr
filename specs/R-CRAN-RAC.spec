%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RAC
%global packver   1.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          R Package for Aqua Culture

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 

%description
Solves the individual bioenergetic balance for different aquaculture sea
fish (Sea Bream and Sea Bass; Brigolin et al., 2014
<doi:10.3354/aei00093>) and shellfish (Mussel and Clam; Brigolin et al.,
2009 <doi:10.1016/j.ecss.2009.01.029>; Solidoro et al., 2000
<doi:10.3354/meps199137>). Allows for spatialized model runs and
population simulations.

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
