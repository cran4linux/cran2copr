%global packname  bkmrhat
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Chain Tools for Bayesian Kernel Machine Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-bkmr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-coda 
Requires:         R-CRAN-bkmr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-rstantools

%description
Bayesian kernel machine regression (from the 'bkmr' package) is a Bayesian
semi-parametric generalized linear model approach under identity and
probit links. There are a number of functions in this package that extend
Bayesian kernel machine regression fits to allow multiple-chain inference
and diagnostics, which leverage functions from the 'future', 'rstan', and
'coda' packages.  Reference: Bobb, J. F., Henn, B. C., Valeri, L., &
Coull, B. A. (2018). Statistical software for analyzing the health effects
of multiple concurrent exposures via Bayesian kernel machine regression. ;
<doi:10.1186/s12940-018-0413-y>.

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
