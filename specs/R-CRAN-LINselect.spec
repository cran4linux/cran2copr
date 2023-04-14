%global __brp_check_rpaths %{nil}
%global packname  LINselect
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Selection of Linear Estimators

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-elasticnet 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-elasticnet 
Requires:         R-MASS 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-gtools 
Requires:         R-stats 

%description
Estimate the mean of a Gaussian vector, by choosing among a large
collection of estimators, following the method developed by Y. Baraud, C.
Giraud and S. Huet (2014) <doi:10.1214/13-AIHP539>. In particular it
solves the problem of variable selection by choosing the best predictor
among predictors emanating from different methods as lasso, elastic-net,
adaptive lasso, pls, randomForest. Moreover, it can be applied for
choosing the tuning parameter in a Gauss-lasso procedure.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
