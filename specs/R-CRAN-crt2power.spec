%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crt2power
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Designing Cluster-Randomized Trials with Two Co-Primary Outcomes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-stats >= 3.6.2
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-devtools >= 2.4.5
BuildRequires:    R-CRAN-tidyverse >= 2.0.0
BuildRequires:    R-CRAN-rootSolve >= 1.8.2.3
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-knitr >= 1.43
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-mvtnorm >= 1.2
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-tableone >= 0.13.2
Requires:         R-stats >= 3.6.2
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-devtools >= 2.4.5
Requires:         R-CRAN-tidyverse >= 2.0.0
Requires:         R-CRAN-rootSolve >= 1.8.2.3
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-knitr >= 1.43
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-mvtnorm >= 1.2
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-tableone >= 0.13.2

%description
Provides methods for powering cluster-randomized trials with two
co-primary outcomes using five key design techniques. Includes functions
for calculating required sample size and statistical power. For more
details on methodology, see Li et al. (2020) <doi:10.1111/biom.13212>,
Pocock et al. (1987) <doi:10.2307/2531989>, Vickerstaff et al. (2019)
<doi:10.1186/s12874-019-0754-4>, and Yang et al. (2022)
<doi:10.1111/biom.13692>.

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
