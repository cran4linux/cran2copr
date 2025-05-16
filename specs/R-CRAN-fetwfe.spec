%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fetwfe
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fused Extended Two-Way Fixed Effects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix >= 1.6.0
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-grpreg 
Requires:         R-CRAN-Matrix >= 1.6.0
Requires:         R-CRAN-expm 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-grpreg 

%description
Calculates the fused extended two-way fixed effects (FETWFE) estimator for
unbiased and efficient estimation of difference-in-differences in panel
data with staggered treatment adoption. This estimator eliminates bias
inherent in conventional two-way fixed effects estimators, while also
employing a novel bridge regression regularization approach to improve
efficiency and yield valid standard errors. Provides flexible tuning
parameters (including user-specified or data-driven choices for penalty
parameters), detailed output including overall and cohort-specific
treatment effects with confidence intervals, and extensive diagnostic
tools. Also provides functions for generating simulated panel data
formatted for estimating FETWFE, and running and evaluating simulations.
See details in Faletto (2025) (<doi:10.48550/arXiv.2312.05985>).

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
