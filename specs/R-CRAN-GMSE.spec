%global __brp_check_rpaths %{nil}
%global packname  GMSE
%global packver   1.0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Generalised Management Strategy Evaluation Simulator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-grDevices >= 4.0.0
BuildRequires:    R-graphics >= 4.0.0
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinycssloaders 
Requires:         R-grDevices >= 4.0.0
Requires:         R-graphics >= 4.0.0
Requires:         R-stats >= 4.0.0
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinycssloaders 

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
