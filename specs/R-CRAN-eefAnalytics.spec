%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eefAnalytics
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Analytical Methods for Evaluating Educational Interventions using Randomised Controlled Trials Designs

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-mvtnorm >= 1.1.2
BuildRequires:    R-CRAN-lme4 >= 1.1.0
BuildRequires:    R-CRAN-R2jags >= 0.7
BuildRequires:    R-CRAN-coda >= 0.19
BuildRequires:    R-CRAN-MCMCvis >= 0.15
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-mvtnorm >= 1.1.2
Requires:         R-CRAN-lme4 >= 1.1.0
Requires:         R-CRAN-R2jags >= 0.7
Requires:         R-CRAN-coda >= 0.19
Requires:         R-CRAN-MCMCvis >= 0.15
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 

%description
Analysing data from evaluations of educational interventions using a
randomised controlled trial design. Various analytical tools to perform
sensitivity analysis using different methods are supported (e.g.
frequentist models with bootstrapping and permutations options, Bayesian
models). The included commands can be used for simple randomised trials,
cluster randomised trials and multisite trials. The methods can also be
used more widely beyond education trials. This package can be used to
evaluate other intervention designs using Frequentist and Bayesian
multilevel models.

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
