%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  catalytic
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Applying Catalytic Priors in Statistical Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-invgamma 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-quadform 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-coda 
Requires:         R-CRAN-invgamma 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rstan 
Requires:         R-stats 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-quadform 
Requires:         R-CRAN-survival 
Requires:         R-methods 
Requires:         R-CRAN-rstantools

%description
To improve estimation accuracy and stability in statistical modeling,
catalytic prior distributions are employed, integrating observed data with
synthetic data generated from a simpler model's predictive distribution.
This approach enhances model robustness, stability, and flexibility in
complex data scenarios. The catalytic prior distributions are introduced
by 'Huang et al.' (2020, <doi:10.1073/pnas.1920913117>), Li and Huang
(2023, <doi:10.48550/arXiv.2312.01411>).

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
