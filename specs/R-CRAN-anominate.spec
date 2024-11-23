%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  anominate
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Alpha-NOMINATE Ideal Point Estimator

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-wnominate 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-MCMCpack 
Requires:         R-stats 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-wnominate 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-MCMCpack 

%description
Provides functions to estimate and interpret the alpha-NOMINATE ideal
point model developed in Carroll et al. (2013, <doi:10.1111/ajps.12029>).
alpha-NOMINATE extends traditional spatial voting frameworks by allowing
for a mixture of Gaussian and quadratic utility functions, providing
flexibility in modeling political actors' preferences. The package uses
Markov Chain Monte Carlo (MCMC) methods for parameter estimation,
supporting robust inference about individuals' ideological positions and
the shape of their utility functions. It also contains functions to
simulate data from the model and to calculate the probability of a vote
passing given the ideal points of the legislators/voters and the estimated
location of the choice alternatives.

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
