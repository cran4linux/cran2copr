%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dynamAedes
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Unified Mechanistic Model for the Population Dynamics of Invasive Aedes Mosquitoes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-drc 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-drc 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-sp 

%description
Generalised model for population dynamics of invasive Aedes mosquitoes.
Rationale and model structure are described here: Da Re et al. (2021)
<doi:10.1016/j.ecoinf.2020.101180> and Da Re et al. (2022)
<doi:10.1101/2021.12.21.473628>.

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
