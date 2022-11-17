%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  snSMART
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Small N Sequential Multiple Assignment Randomized Trial Methods

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.12
BuildRequires:    R-CRAN-condMVNorm >= 2020
BuildRequires:    R-CRAN-EnvStats >= 2.4.0
BuildRequires:    R-CRAN-pracma >= 2.3.3
BuildRequires:    R-CRAN-cubature >= 2.0.4.1
BuildRequires:    R-CRAN-geepack >= 1.3.1
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-truncdist >= 1.0.1
BuildRequires:    R-CRAN-HDInterval >= 0.2.0
BuildRequires:    R-CRAN-bayestestR >= 0.11.0
Requires:         R-CRAN-rjags >= 4.12
Requires:         R-CRAN-condMVNorm >= 2020
Requires:         R-CRAN-EnvStats >= 2.4.0
Requires:         R-CRAN-pracma >= 2.3.3
Requires:         R-CRAN-cubature >= 2.0.4.1
Requires:         R-CRAN-geepack >= 1.3.1
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-truncdist >= 1.0.1
Requires:         R-CRAN-HDInterval >= 0.2.0
Requires:         R-CRAN-bayestestR >= 0.11.0

%description
Consolidated data simulation, sample size calculation and analysis
functions for several snSMART (small sample sequential, multiple
assignment, randomized trial) designs under one library.  See Wei, B.,
Braun, T.M., Tamura, R.N. and Kidwell, K.M. "A Bayesian analysis of small
n sequential multiple assignment randomized trials (snSMARTs)." (2018)
Statistics in medicine, 37(26), pp.3723-3732 <doi:10.1002/sim.7900>.

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
