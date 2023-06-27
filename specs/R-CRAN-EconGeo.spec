%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EconGeo
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Computing Key Indicators of the Spatial Distribution of Economic Activities

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-reshape 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-reshape 

%description
Computes a series of indices commonly used in the fields of economic
geography, economic complexity, and evolutionary economics to describe the
location, distribution, spatial organization, structure, and complexity of
economic activities. Functions include basic spatial indicators such as
the location quotient, the Krugman specialization index, the Herfindahl or
the Shannon entropy indices but also more advanced functions to compute
different forms of normalized relatedness between economic activities or
network-based measures of economic complexity. Most of the functions use
matrix calculus and are based on bipartite (incidence) matrices consisting
of region - industry pairs. These are described in Balland (2017)
<http://econ.geo.uu.nl/peeg/peeg1709.pdf>.

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
