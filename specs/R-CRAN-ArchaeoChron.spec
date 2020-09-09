%global packname  ArchaeoChron
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Modeling of Archaeological Chronologies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-ArchaeoPhases 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Bchron 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-ArchaeoPhases 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Bchron 

%description
Provides a list of functions for the Bayesian modeling of archaeological
chronologies. The Bayesian models are implemented in 'JAGS' ('JAGS' stands
for Just Another Gibbs Sampler. It is a program for the analysis of
Bayesian hierarchical models using Markov Chain Monte Carlo (MCMC)
simulation. See <http://mcmc-jags.sourceforge.net/> and "JAGS Version
4.3.0 user manual", Martin Plummer (2017)
<https://sourceforge.net/projects/mcmc-jags/files/Manuals/>.). The inputs
are measurements with their associated standard deviations and the study
period. The output is the MCMC sample of the posterior distribution of the
event date with or without radiocarbon calibration.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
