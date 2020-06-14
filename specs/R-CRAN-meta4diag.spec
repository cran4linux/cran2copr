%global packname  meta4diag
%global packver   2.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.8
Release:          2%{?dist}
Summary:          Meta-Analysis for Diagnostic Test Studies

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-caTools 
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-caTools 

%description
Bayesian inference analysis for bivariate meta-analysis of diagnostic test
studies using integrated nested Laplace approximation with INLA. A purpose
built graphic user interface is available. The installation of R package
INLA is compulsory for successful usage. The INLA package can be obtained
from <http://www.r-inla.org>. We recommend the testing version, which can
be downloaded by running: install.packages("INLA",
repos=c(getOption("repos"),
INLA="https://inla.r-inla-download.org/R/testing"), dep=TRUE).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/image
%doc %{rlibdir}/%{packname}/meta4diagGUI
%doc %{rlibdir}/%{packname}/txt
%{rlibdir}/%{packname}/INDEX
