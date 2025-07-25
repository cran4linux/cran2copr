%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  conformalbayes
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Jackknife(+) Predictive Intervals for Bayesian Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rstantools 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rstantools 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-matrixStats 

%description
Provides functions to construct finite-sample calibrated predictive
intervals for Bayesian models, following the approach in Barber et al.
(2021) <doi:10.1214/20-AOS1965>. These intervals are calculated
efficiently using importance sampling for the leave-one-out residuals. By
default, the intervals will also reflect the relative uncertainty in the
Bayesian model, using the locally-weighted conformal methods of Lei et al.
(2018) <doi:10.1080/01621459.2017.1307116>.

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
