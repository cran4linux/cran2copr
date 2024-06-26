%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  frequentistSSDBinary
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Screened Selection Design with Binary Endpoints

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-clinfun 
BuildRequires:    R-CRAN-ph2mult 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-clinfun 
Requires:         R-CRAN-ph2mult 

%description
A study based on the screened selection design (SSD) is an exploratory
phase II randomized trial with two or more arms but without concurrent
control. The primary aim of the SSD trial is to pick a desirable treatment
arm (e.g., in terms of the response rate) to recommend to the subsequent
randomized phase IIb (with the concurrent control) or phase III. The
proposed designs can “partially” control or provide the empirical type I
error/false positive rate by an optimal algorithm (implemented by the
optimal_2arm_binary() or optimal_3arm_binary() function) for each arm. All
the design needed components (sample size, operating characteristics) are
supported.

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
