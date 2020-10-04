%global packname  MVNBayesian
%global packver   0.0.8-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8.11
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Analysis Framework for MVN (Mixture) Distribution

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-plyr 
Requires:         R-stats 

%description
Tools of Bayesian analysis framework using the method suggested by Berger
(1985) <doi:10.1007/978-1-4757-4286-2> for multivariate normal (MVN)
distribution and multivariate normal mixture (MixMVN) distribution: a)
calculating Bayesian posteriori of (Mix)MVN distribution; b) generating
random vectors of (Mix)MVN distribution; c) Markov chain Monte Carlo
(MCMC) for (Mix)MVN distribution.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
