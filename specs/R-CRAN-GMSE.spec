%global packname  GMSE
%global packver   0.6.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0.4
Release:          2%{?dist}
Summary:          Generalised Management Strategy Evaluation Simulator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-grDevices >= 3.4.0
BuildRequires:    R-graphics >= 3.4.0
BuildRequires:    R-stats >= 3.4.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
Requires:         R-grDevices >= 3.4.0
Requires:         R-graphics >= 3.4.0
Requires:         R-stats >= 3.4.0
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 

%description
Integrates game theory and ecological theory to construct
social-ecological models that simulate the management of populations and
stakeholder actions. These models build off of a previously developed
management strategy evaluation (MSE) framework to simulate all aspects of
management: population dynamics, manager observation of populations,
manager decision making, and stakeholder responses to management
decisions. The newly developed generalised management strategy evaluation
(GMSE) framework uses genetic algorithms to mimic the decision-making
process of managers and stakeholders under conditions of change,
uncertainty, and conflict. Simulations can be run using gmse(),
gmse_apply(), and gmse_gui() functions.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
