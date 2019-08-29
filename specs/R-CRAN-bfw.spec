%global packname  bfw
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Bayesian Framework for Computational Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.47
BuildRequires:    R-CRAN-runjags >= 2.0.4.2
BuildRequires:    R-CRAN-coda >= 0.19.1
Requires:         R-MASS >= 7.3.47
Requires:         R-CRAN-runjags >= 2.0.4.2
Requires:         R-CRAN-coda >= 0.19.1

%description
Derived from the work of Kruschke (2015, <ISBN:9780124058880>), the
present package aims to provide a framework for conducting Bayesian
analysis using Markov chain Monte Carlo (MCMC) sampling utilizing the Just
Another Gibbs Sampler ('JAGS', Plummer, 2003,
<http://mcmc-jags.sourceforge.net/>). The initial version includes several
modules for conducting Bayesian equivalents of chi-squared tests, analysis
of variance (ANOVA), multiple (hierarchical) regression, softmax
regression, and for fitting data (e.g., structural equation modeling).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
