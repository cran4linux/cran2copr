%global packname  HLMdiag
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          Diagnostic Tools for Hierarchical (Multilevel) Linear Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-CRAN-ggplot2 >= 0.9.2
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-RLRsim 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 0.9.2
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-RLRsim 
Requires:         R-mgcv 

%description
A suite of diagnostic tools for hierarchical (multilevel) linear models.
The tools include not only leverage and traditional deletion diagnostics
(Cook's distance, covratio, covtrace, and MDFFITS) but also convenience
functions and graphics for residual analysis. Models can be fit using
either lmer in the 'lme4' package or lme in the 'nlme' package, but only
two-level models fit using lme are currently supported.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
