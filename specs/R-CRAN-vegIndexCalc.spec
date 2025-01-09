%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vegIndexCalc
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Vegetation Indices (VIs) Calculation for Remote Sensing Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
It provides a comprehensive toolkit for calculating a suite of common
vegetation indices (VIs) derived from remote sensing imagery. VIs are
essential tools used to quantify vegetation characteristics, such as
biomass, leaf area index (LAI) and photosynthetic activity, which are
essential parameters in various ecological, agricultural, and
environmental studies. Applications of this package include biomass
estimation, crop monitoring, forest management, land use and land cover
change analysis and climate change studies. For method details see,
Deb,D.,Deb,S.,Chakraborty,D.,Singh,J.P.,Singh,A.K.,Dutta,P.and
Choudhury,A.(2020)<doi:10.1080/10106049.2020.1756461>. Utilizing this R
package, users can effectively extract and analyze critical information
from remote sensing imagery, enhancing their comprehension of vegetation
dynamics and their importance in global ecosystems. The package includes
the function vegetation_indices().

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
