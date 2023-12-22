%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dirttee
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Distributional Regression for Time to Event Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-expectreg >= 0.5
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-provenance 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-expectreg >= 0.5
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-provenance 
Requires:         R-CRAN-rlang 
Requires:         R-splines 
Requires:         R-CRAN-survival 

%description
Semiparametric distributional regression methods (expectile, quantile and
mode regression) for time-to-event variables with right-censoring; uses
inverse probability of censoring weights or accelerated failure time
models with auxiliary likelihoods. Expectile regression using inverse
probability of censoring weights has been introduced in Seipp et al.
(2021) ``Weighted Expectile Regression for Right-Censored Data''
<doi:10.1002/sim.9137>, mode regression for time-to-event variables has
been introduced in Seipp et al. (2022) ``Flexible Semiparametric Mode
Regression for Time-to-Event Data'' <doi:10.1177/09622802221122406>.

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
