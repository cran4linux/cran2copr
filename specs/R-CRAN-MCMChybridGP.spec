%global __brp_check_rpaths %{nil}
%global packname  MCMChybridGP
%global packver   5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Hybrid Markov Chain Monte Carlo using Gaussian Processes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
Hybrid Markov chain Monte Carlo (MCMC) to simulate from a multimodal
target distribution.  A Gaussian process approximation makes this possible
when derivatives are unknown. The Package serves to minimize the number of
function evaluations in Bayesian calibration of computer models using
parallel tempering.  It allows replacement of the true target distribution
in high temperature chains, or complete replacement of the target.
Methods used are described in, "Efficient MCMC schemes for computationally
expensive posterior distributions", Fielding et al. (2011)
<doi:10.1198/TECH.2010.09195>. The research presented in this work was
carried out as part of the Singapore-Delft Water Alliance Multi-Objective
Multi-Reservoir Management research programme (R-264-001-272).

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
