%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  highriskzone
%global packver   1.4.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.9
Release:          1%{?dist}%{?buildtag}
Summary:          Determining and Evaluating High-Risk Zones

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat >= 1.54.0
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-polyclip 
Requires:         R-CRAN-spatstat >= 1.54.0
Requires:         R-CRAN-fields 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-polyclip 

%description
Functions for determining and evaluating high-risk zones and simulating
and thinning point process data, as described in 'Determining high risk
zones using point process methodology - Realization by building an R
package' Seibold (2012)
<http://highriskzone.r-forge.r-project.org/Bachelorarbeit.pdf> and
'Determining high-risk zones for unexploded World War II bombs by using
point process methodology', Mahling et al. (2013)
<doi:10.1111/j.1467-9876.2012.01055.x>.

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
