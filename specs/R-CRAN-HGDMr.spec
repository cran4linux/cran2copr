%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HGDMr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hysteretic and Gatekeeping Depressions Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-stats 

%description
Implementation of the Hysteretic and Gatekeeping Depressions Model (HGDM)
which calculates variable connected/contributing areas and resulting
discharge volumes in prairie basins dominated by depressions ("slough" or
"potholes"). The small depressions are combined into a single "meta"
depression which explicitly models the hysteresis between the storage of
water and the connected/contributing areas of the depressions. The largest
(greater than 5%% of the total depressional area) depression (if it exists)
is represented separately to model its gatekeeping, i.e. the blocking of
upstream flows until it is filled. The methodolgy is described in detail
in Shook and Pomeroy (2025, <doi:10.1016/j.jhydrol.2025.132821>).

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
