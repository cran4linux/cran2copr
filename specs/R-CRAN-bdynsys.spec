%global packname  bdynsys
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Bayesian Dynamical System Model

License:          GNU General Public License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-Formula 
Requires:         R-MASS 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-matrixStats 

%description
The package bdynsys for panel/longitudinal data combines methods to model
changes in up to four indicators over times as a function of the
indicators themselves and up to three predictors using ordinary
differential equations (ODEs) with polynomial terms that allow to model
complex and nonlinear effects. A Bayesian model selection approach is
implemented. The package provides also visualisation tools to plot phase
portraits of the dynamic system, showing the complex co-evolution of two
indicators over time with the possibility to highlight trajectories for
specified entities (e.g. countries, individuals). Furthermore the
visualisation tools allow for making predictions of the trajectories of
specified entities with respect to the indicators.

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
