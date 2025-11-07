%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  refineR
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reference Interval Estimation using Real-World Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ash 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-ash 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Indirect method for the estimation of reference intervals (RIs) using
Real-World Data ('RWD') and methods for comparing and verifying RIs.
Estimates RIs by applying advanced statistical methods to routine
diagnostic test measurements, which include both pathological and
non-pathological samples, to model the distribution of non-pathological
samples. This distribution is then used to derive reference intervals and
support RI verification, i.e., deciding if a specific RI is suitable for
the local population. The package also provides functions for printing and
plotting algorithm results. See ?refineR for a detailed description of
features. Version 1.0 of the algorithm is described in 'Ammer et al.
(2021)' <doi:10.1038/s41598-021-95301-2>. Additional guidance is in 'Ammer
et al. (2023)' <doi:10.1093/jalm/jfac101>. The verification method is
described in 'Beck et al. (2025)' <doi:10.1515/cclm-2025-0728>.

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
