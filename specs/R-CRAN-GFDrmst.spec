%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GFDrmst
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple RMST-Based Tests in General Factorial Designs

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.53
BuildRequires:    R-CRAN-shinyjs >= 2.0.0
BuildRequires:    R-CRAN-plyr >= 1.8.6
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-shinythemes >= 1.1.2
BuildRequires:    R-CRAN-tippy >= 0.1.0
BuildRequires:    R-CRAN-GFDmcv 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinyMatrix 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS >= 7.3.53
Requires:         R-CRAN-shinyjs >= 2.0.0
Requires:         R-CRAN-plyr >= 1.8.6
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-shinythemes >= 1.1.2
Requires:         R-CRAN-tippy >= 0.1.0
Requires:         R-CRAN-GFDmcv 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinyMatrix 
Requires:         R-CRAN-mvtnorm 

%description
We implemented multiple tests based on the restricted mean survival time
(RMST) for general factorial designs as described in Munko et al. (2024)
<doi:10.1002/sim.10017>. Therefore, an asymptotic test, a groupwise
bootstrap test, and a permutation test are incorporated with a Wald-type
test statistic. The asymptotic and groupwise bootstrap test take the
asymptotic exact dependence structure of the test statistics into account
to gain more power. Furthermore, confidence intervals for RMST contrasts
can be calculated and plotted and a stepwise extension that can improve
the power of the multiple tests is available.

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
