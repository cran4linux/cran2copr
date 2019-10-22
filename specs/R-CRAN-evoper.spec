%global packname  evoper
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Evolutionary Parameter Estimation for 'Repast Simphony' Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rrepast 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RNetLogo 
Requires:         R-CRAN-rrepast 
Requires:         R-methods 
Requires:         R-CRAN-futile.logger 
Requires:         R-boot 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-data.table 
Requires:         R-utils 
Requires:         R-CRAN-RNetLogo 

%description
The EvoPER, Evolutionary Parameter Estimation for Individual-based Models
is an extensible package providing optimization driven parameter
estimation methods using metaheuristics and evolutionary computation
techniques (Particle Swarm Optimization, Simulated Annealing, Ant Colony
Optimization for continuous domains, Tabu Search, Evolutionary Strategies,
...)  which could be more efficient and require, in some cases, fewer
model evaluations than alternatives relying on experimental design.
Currently there are built in support for models developed with 'Repast
Simphony' Agent-Based framework (<https://repast.github.io/>) and with
NetLogo (<https://ccl.northwestern.edu/netlogo/>) which are the most used
frameworks for Agent-based modeling.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
