%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  traveltime
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Travel Times Over Space

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-malariaAtlas 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-malariaAtlas 
Requires:         R-CRAN-terra 

%description
Calculate travel time across a landscape from a set of user-specified
locations, over a friction surface describing the time taken to cross each
cell. Implements the least-cost travel time approach of Weiss et al.
(2018) <doi:10.1038/nature25181> and Weiss et al. (2020)
<doi:10.1038/s41591-020-1059-1>, and provides convenient access to their
global walking and motorised friction surfaces via the 'malariaAtlas'
package. Travel times are computed with 'terra'. See Ryan et al. (2025)
<doi:10.12688/gatesopenres.16356.1> for further details.

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
