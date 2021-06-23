%global __brp_check_rpaths %{nil}
%global packname  rivr
%global packver   1.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Steady and Unsteady Open-Channel Flow Computation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-Rcpp >= 1.0
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Rcpp >= 1.0
Requires:         R-utils 
Requires:         R-graphics 

%description
A tool for undergraduate and graduate courses in open-channel hydraulics.
Provides functions for computing normal and critical depths, steady-state
water surface profiles (e.g. backwater curves) and unsteady flow
computations (e.g. flood wave routing) as described in Koohafkan MC,
Younis BA (2015). "Open-channel computation with R." The R Journal, 7(2),
249–262. <doi: 10.32614/RJ-2015-034>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
