%global packname  care
%global packver   1.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.10
Release:          2%{?dist}
Summary:          High-Dimensional Regression and CAR Score Variable Selection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor >= 1.6.8
BuildRequires:    R-stats 
Requires:         R-CRAN-corpcor >= 1.6.8
Requires:         R-stats 

%description
Implements the regression approach of Zuber and Strimmer (2011)
"High-dimensional regression and variable selection using CAR scores"
SAGMB 10: 34, <DOI:10.2202/1544-6115.1730>. CAR scores measure the
correlation between the response and the Mahalanobis-decorrelated
predictors.  The squared CAR score is a natural measure of variable
importance and provides a canonical ordering of variables. This package
provides functions for estimating CAR scores, for variable selection using
CAR scores, and for estimating corresponding regression coefficients. Both
shrinkage as well as empirical estimators are available.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
