%global packname  saemix
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Stochastic Approximation Expectation Maximization (SAEM)Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 

%description
The SAEMIX package implements the Stochastic Approximation EM algorithm
for parameter estimation in (non)linear mixed effects models. The SAEM
algorithm: - computes the maximum likelihood estimator of the population
parameters, without any approximation of the model (linearisation,
quadrature approximation,...), using the Stochastic Approximation
Expectation Maximization (SAEM) algorithm, - provides standard errors for
the maximum likelihood estimator - estimates the conditional modes, the
conditional means and the conditional standard deviations of the
individual parameters, using the Hastings-Metropolis algorithm. Several
applications of SAEM in agronomy, animal breeding and PKPD analysis have
been published by members of the Monolix group
(<http://group.monolix.org/>).

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/userguide_saemix.pdf
%{rlibdir}/%{packname}/INDEX
