%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  verification
%global packver   1.45
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.45
Release:          1%{?dist}%{?buildtag}
Summary:          Weather Forecast Verification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-CircStats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-CircStats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-dtw 
Requires:         R-graphics 
Requires:         R-stats 

%description
Utilities for verifying discrete, continuous and probabilistic forecasts,
and forecasts expressed as parametric distributions are included.

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
