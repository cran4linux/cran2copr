%global packname  eefAnalytics
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Analytical Methods for Evaluating Educational Interventions using Randomised Controlled Trials Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rstanarm 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-metafor 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-rstanarm 

%description
The eefAnalytics provides tools for analysing data from evaluations of
educational interventions using a randomised controlled trial designs. It
provides analytical tools to perform sensitivity analysis using different
methods(e.g. frequentist models with bootstrapping and permutations
options, Bayesian models). The functions contained in this package can be
used for simple individual randomised trials, cluster randomised trials
and multisite trials. The methods can also be used more widely beyond
education trials. This package can be used to evaluate other interventions
designs using Frequentist and Bayesian multilevel models.

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
