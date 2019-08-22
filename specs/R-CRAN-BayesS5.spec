%global packname  BayesS5
%global packver   1.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.31
Release:          1%{?dist}
Summary:          Bayesian Variable Selection Using Simplified Shotgun StochasticSearch with Screening (S5)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-CRAN-abind 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-snowfall 
Requires:         R-CRAN-abind 

%description
In p >> n settings, full posterior sampling using existing Markov chain
Monte Carlo (MCMC) algorithms is highly inefficient and often not feasible
from a practical perspective. To overcome this problem, we propose a
scalable stochastic search algorithm that is called the Simplified Shotgun
Stochastic Search (S5) and aimed at rapidly explore interesting regions of
model space and finding the maximum a posteriori(MAP) model. Also, the S5
provides an approximation of posterior probability of each model
(including the marginal inclusion probabilities).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
