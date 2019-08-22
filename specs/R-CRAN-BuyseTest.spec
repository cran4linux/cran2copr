%global packname  BuyseTest
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}
Summary:          Generalized Pairwise Comparisons

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lava 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-CRAN-lava 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-utils 

%description
Implementation of the Generalized Pairwise Comparisons (GPC). GPC compare
two groups of observations (intervention vs. control group) regarding
several prioritized endpoints. The net benefit and win ratio statistics
can then be estimated and corresponding confidence intervals and p-values
can be estimated using resampling methods or the asymptotic U-statistic
theory. The software enables the use of thresholds of minimal importance
difference, stratification, and corrections to deal with right-censored
endpoints or missing values.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/Article-JSS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/Documentation
%doc %{rlibdir}/%{packname}/Issues
%doc %{rlibdir}/%{packname}/todo.org
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
