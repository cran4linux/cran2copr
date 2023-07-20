%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fPASS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Power and Sample Size for Projection Test under Repeated Measures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-face 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-gamm4 
BuildRequires:    R-CRAN-gss 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-face 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-gamm4 
Requires:         R-CRAN-gss 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Computes the power and sample size (PASS) required to test for the
difference in the mean function between two groups under a repeatedly
measured longitudinal or sparse functional design. See the manuscript by
Koner and Luo (2023)
<https://salilkoner.github.io/assets/PASS_manuscript.pdf> for details of
the PASS formula and computational details. The details of the testing
procedure for univariate and multivariate response are presented in Wang
(2021) <doi:10.1214/21-EJS1802> and Koner and Luo (2023)
<arXiv:2302.05612> respectively.

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
