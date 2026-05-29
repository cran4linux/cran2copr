%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  evacpath
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Least-Cost Pedestrian Evacuation Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-leastcostpath 
BuildRequires:    R-utils 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-leastcostpath 
Requires:         R-utils 

%description
Tools for road-constrained, least-cost pedestrian evacuation modeling. The
package provides reusable functions for preparing hazard zones, generating
road-based evacuation origin points, identifying escape/safety points,
creating slope-based conductance surfaces, calculating least-cost distance
to safety, and converting distance outputs into evacuation-time polygons.
It is designed to support workflows like tsunami evacuation modeling while
remaining adaptable to other regions and hazards. Tsunami-specific helpers
support separate land-only hazard zones, water-combined escape zones,
road-aware escape boundaries, and study-area inset cropping for quality
assurance and quality control. Methods build on Cordero et al. (2025)
<doi:10.1007/s44367-025-00018-y>, Lewis (2021)
<doi:10.1007/s10816-021-09522-w>, and Joseph Lewis's 'leastcostpath'
package (2023) <https://CRAN.R-project.org/package=leastcostpath>.

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
