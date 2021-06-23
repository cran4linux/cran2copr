%global __brp_check_rpaths %{nil}
%global packname  FarmSelect
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Factor Adjusted Robust Model Selection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-fBasics 

%description
Implements a consistent model selection strategy for high dimensional
sparse regression when the covariate dependence can be reduced through
factor models. By separating the latent factors from idiosyncratic
components, the problem is transformed from model selection with highly
correlated covariates to that with weakly correlated variables. It is
appropriate for cases where we have many variables compared to the number
of samples. Moreover, it implements a robust procedure to estimate
distribution parameters wherever possible, hence being suitable for cases
when the underlying distribution deviates from Gaussianity. See the paper
on the 'FarmSelect' method, Fan et al.(2017) <arXiv:1612.08490>, for
detailed description of methods and further references.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
