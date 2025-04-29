%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MDSMap
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          High Density Genetic Linkage Mapping using Multidimensional Scaling

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-princurve >= 2.0.2
BuildRequires:    R-CRAN-smacof >= 1.9.0
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-reshape 
Requires:         R-CRAN-princurve >= 2.0.2
Requires:         R-CRAN-smacof >= 1.9.0
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-reshape 

%description
Estimate genetic linkage maps for markers on a single chromosome (or in a
single linkage group) from pairwise recombination fractions or intermarker
distances using weighted metric multidimensional scaling. The methods are
suitable for autotetraploid as well as diploid populations. Options for
assessing the fit to a known map are also provided. Methods are discussed
in detail in Preedy and Hackett (2016) <doi:10.1007/s00122-016-2761-8>.

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
