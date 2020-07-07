%global packname  robustlmm
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          3%{?dist}
Summary:          Robust Linear Mixed Effects Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-lme4 >= 1.1.9
BuildRequires:    R-Matrix >= 1.0.13
BuildRequires:    R-CRAN-robustbase >= 0.93
BuildRequires:    R-CRAN-Rcpp >= 0.12.2
BuildRequires:    R-CRAN-cubature > 1.3.8
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-lattice 
BuildRequires:    R-nlme 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-lme4 >= 1.1.9
Requires:         R-Matrix >= 1.0.13
Requires:         R-CRAN-robustbase >= 0.93
Requires:         R-CRAN-Rcpp >= 0.12.2
Requires:         R-CRAN-ggplot2 
Requires:         R-lattice 
Requires:         R-nlme 
Requires:         R-methods 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-fastGHQuad 

%description
A method to fit linear mixed effects models robustly. Robustness is
achieved by modification of the scoring equations combined with the Design
Adaptive Scale approach.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/xtraR
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
