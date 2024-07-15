%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HonestDiD
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Inference in Difference-in-Differences and Event Study Designs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolveAPI >= 5.5.2.0.17
BuildRequires:    R-CRAN-pracma >= 2.2.5
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-foreach >= 1.4.7
BuildRequires:    R-CRAN-tibble >= 1.3.4
BuildRequires:    R-CRAN-Matrix >= 1.2.17
BuildRequires:    R-CRAN-mvtnorm >= 1.1.3
BuildRequires:    R-CRAN-TruncatedNormal >= 1.0
BuildRequires:    R-CRAN-CVXR >= 0.99.6
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-matrixStats >= 0.63.0
BuildRequires:    R-CRAN-Rglpk >= 0.6.4
BuildRequires:    R-CRAN-latex2exp >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-lpSolveAPI >= 5.5.2.0.17
Requires:         R-CRAN-pracma >= 2.2.5
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-foreach >= 1.4.7
Requires:         R-CRAN-tibble >= 1.3.4
Requires:         R-CRAN-Matrix >= 1.2.17
Requires:         R-CRAN-mvtnorm >= 1.1.3
Requires:         R-CRAN-TruncatedNormal >= 1.0
Requires:         R-CRAN-CVXR >= 0.99.6
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-matrixStats >= 0.63.0
Requires:         R-CRAN-Rglpk >= 0.6.4
Requires:         R-CRAN-latex2exp >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-stats 
Requires:         R-CRAN-rlang 

%description
Provides functions to conduct robust inference in
difference-in-differences and event study designs by implementing the
methods developed in Rambachan & Roth (2023) <doi:10.1093/restud/rdad018>,
"A More Credible Approach to Parallel Trends" [Previously titled "An
Honest Approach..."]. Inference is conducted under a weaker version of the
parallel trends assumption. Uniformly valid confidence sets are
constructed based upon conditional confidence sets, fixed-length
confidence sets and hybridized confidence sets.

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
