%global packname  visit
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Phase I Dose Escalation Study Design for Vaccines

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-parallel >= 3.2
BuildRequires:    R-CRAN-rstan >= 2.19.2
BuildRequires:    R-CRAN-StanHeaders >= 2.18.1.10
BuildRequires:    R-CRAN-BH >= 1.69.0.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-sqldf >= 0.4
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.5.0
BuildRequires:    R-methods 
Requires:         R-parallel >= 3.2
Requires:         R-CRAN-rstan >= 2.19.2
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-sqldf >= 0.4
Requires:         R-methods 

%description
A Bayesian Phase I cancer vaccine trial design is implemented in this
package. The design allows simultaneous evaluation of safety and
immunogenicity outcomes in the context of vaccine studies. See Wang (2019)
<DOI:10.1002/sim.8021> for the details of the Phase I cancer vaccine trial
design.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
