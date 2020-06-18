%global packname  MCPModPack
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Simulation-Based Design and Analysis of Dose-Finding Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.1
Requires:         R-core >= 3.4.1
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppNumerical 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-devEMF 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppNumerical 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-devEMF 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 

%description
An efficient implementation of the MCPMod (Multiple Comparisons and
Modeling) method to support a simulation-based design and analysis of
dose-finding trials with normally distributed, binary and count endpoints
(Bretz et al. (2005) <doi:10.1111/j.1541-0420.2005.00344.x>).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/AnalysisApp
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/SimulationApp
%doc %{rlibdir}/%{packname}/template
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
