%global packname  BaBooN
%global packver   0.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Bootstrap Predictive Mean Matching - Multiple andSingle Imputation for Discrete Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-MASS 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-Hmisc 
Requires:         R-MASS 
Requires:         R-nnet 
Requires:         R-CRAN-coda 

%description
Included are two variants of Bayesian Bootstrap Predictive Mean Matching
to multiply impute missing data. The first variant is a
variable-by-variable imputation combining sequential regression and
Predictive Mean Matching (PMM) that has been extended for unordered
categorical data. The Bayesian Bootstrap allows for generating
approximately proper multiple imputations. The second variant is also
based on PMM, but the focus is on imputing several variables at the same
time. The suggestion is to use this variant, if the missing-data pattern
resembles a data fusion situation, or any other missing-by-design pattern,
where several variables have identical missing-data patterns. Both
variants can be run as 'single imputation' versions, in case the analysis
objective is of a purely descriptive nature.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
