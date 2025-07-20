%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BeastJar
%global packver   10.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          10.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          JAR Dependency for MCMC Using 'BEAST'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava 
Requires:         R-CRAN-rJava 

%description
Provides JAR to perform Markov chain Monte Carlo (MCMC) inference using
the popular Bayesian Evolutionary Analysis by Sampling Trees 'BEAST X'
software library of Baele et al (2025) <doi:10.1038/s41592-025-02751-x>.
'BEAST X' supports auto-tuning Metropolis-Hastings, slice, Hamiltonian
Monte Carlo and Sequential Monte Carlo sampling for a large variety of
composable standard and phylogenetic statistical models using high
performance computing.  By placing the 'BEAST X' JAR in this package, we
offer an efficient distribution system for 'BEAST X' use by other R
packages using CRAN.

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
