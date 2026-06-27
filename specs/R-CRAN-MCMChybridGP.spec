%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MCMChybridGP
%global packver   7.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Hybrid Markov Chain Monte Carlo Using Gaussian Processes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rcpp 

%description
Hybrid Markov chain Monte Carlo (MCMC) for sampling from multimodal target
distributions when derivatives are unavailable. A Gaussian process
approximation is used to emulate derivatives, enabling efficient
exploration with parallel tempering. The method is described in Fielding,
Nott and Liong (2011) <doi:10.1198/TECH.2010.09195>. The research was
carried out as part of the Singapore-Delft Water Alliance Multi-Objective
Multi-Reservoir Management programme (R-264-001-272).

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
