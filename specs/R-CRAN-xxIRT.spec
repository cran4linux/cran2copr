%global packname  xxIRT
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          2%{?dist}
Summary:          Item Response Theory and Computer-Based Testing in R

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glpkAPI 
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glpkAPI 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 

%description
A suite of psychometric analysis tools for research and operation,
including: (1) computation of probability, information, and likelihood for
the 3PL, GPCM, and GRM; (2) parameter estimation using joint or marginal
likelihood estimation method; (3) simulation of computerized adaptive
testing using built-in or customized algorithms; (4) assembly and
simulation of multistage testing. The full documentation and tutorials are
at <https://github.com/xluo11/xxIRT>.

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
