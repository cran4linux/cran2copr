%global packname  creditmodel
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Toolkit for Credit Modeling

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-pdp 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-glmnet 
Requires:         R-rpart 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-pdp 
Requires:         R-CRAN-cli 

%description
Provides a highly efficient R tool suite for Credit Modeling, Analysis and
Visualization. Contains infrastructure functionalities such as data
exploration and preparation, missing values treatment, outliers treatment,
variable derivation, variable selection, dimensionality reduction, grid
search for hyper parameters, data mining and visualization, model
evaluation, strategy analysis etc. This package is designed to make the
development of binary classification models (machine learning based models
as well as credit scorecard) simpler and faster.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
