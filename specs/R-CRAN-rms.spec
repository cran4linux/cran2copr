%global packname  rms
%global packver   5.1-3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1.3.1
Release:          1%{?dist}
Summary:          Regression Modeling Strategies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Hmisc >= 4.1.1
BuildRequires:    R-nlme >= 3.1.123
BuildRequires:    R-survival >= 2.40.1
BuildRequires:    R-CRAN-ggplot2 >= 2.2
BuildRequires:    R-CRAN-htmlTable >= 1.11.0
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-polspline 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-Hmisc >= 4.1.1
Requires:         R-nlme >= 3.1.123
Requires:         R-survival >= 2.40.1
Requires:         R-CRAN-ggplot2 >= 2.2
Requires:         R-CRAN-htmlTable >= 1.11.0
Requires:         R-lattice 
Requires:         R-CRAN-SparseM 
Requires:         R-methods 
Requires:         R-CRAN-quantreg 
Requires:         R-rpart 
Requires:         R-CRAN-polspline 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-htmltools 

%description
Regression modeling, testing, estimation, validation, graphics,
prediction, and typesetting by storing enhanced model design attributes in
the fit.  'rms' is a collection of functions that assist with and
streamline modeling.  It also contains functions for binary and ordinal
logistic regression models, ordinal models for continuous Y with a variety
of distribution families, and the Buckley-James multiple regression model
for right-censored responses, and implements penalized maximum likelihood
estimation for logistic and ordinary linear models.  'rms' works with
almost any regression model, but it was especially written to work with
binary or ordinal regression models, Cox regression, accelerated failure
time models, ordinary linear models, the Buckley-James model, generalized
least squares for serially or spatially correlated observations,
generalized linear models, and quantile regression.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
