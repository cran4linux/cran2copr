%global packname  HydeNet
%global packver   0.10.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.9
Release:          3%{?dist}
Summary:          Hybrid Bayesian Networks Using R and JAGS

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DiagrammeR >= 0.9.0
BuildRequires:    R-CRAN-pixiedust >= 0.6.1
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-DiagrammeR >= 0.9.0
Requires:         R-CRAN-pixiedust >= 0.6.1
Requires:         R-nnet 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rjags 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Facilities for easy implementation of hybrid Bayesian networks using R.
Bayesian networks are directed acyclic graphs representing joint
probability distributions, where each node represents a random variable
and each edge represents conditionality. The full joint distribution is
therefore factorized as a product of conditional densities, where each
node is assumed to be independent of its non-descendents given information
on its parent nodes. Since exact, closed-form algorithms are
computationally burdensome for inference within hybrid networks that
contain a combination of continuous and discrete nodes, particle-based
approximation techniques like Markov Chain Monte Carlo are popular. We
provide a user-friendly interface to constructing these networks and
running inference using the 'rjags' package. Econometric analyses (maximum
expected utility under competing policies, value of information) involving
decision and utility nodes are also supported.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/img
%{rlibdir}/%{packname}/INDEX
