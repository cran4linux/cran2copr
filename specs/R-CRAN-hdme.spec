%global packname  hdme
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          High-Dimensional Regression with Measurement Error

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-glmnet >= 3.0.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-Rglpk >= 0.6.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-glmnet >= 3.0.0
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-Rglpk >= 0.6.1
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 

%description
Penalized regression for generalized linear models for measurement error
problems (aka. errors-in-variables). The package contains a version of the
lasso (L1-penalization) which corrects for measurement error (Sorensen et
al. (2015) <doi:10.5705/ss.2013.180>). It also contains an implementation
of the Generalized Matrix Uncertainty Selector, which is a version the
(Generalized) Dantzig Selector for the case of measurement error (Sorensen
et al. (2018) <doi:10.1080/10618600.2018.1425626>).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
