%global packname  blkbox
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Data Exploration with Multiple Machine Learning Algorithms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-bartMachine 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-kknn 
BuildRequires:    R-CRAN-pamr 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-tibble 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-bartMachine 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-kknn 
Requires:         R-CRAN-pamr 
Requires:         R-nnet 
Requires:         R-CRAN-party 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xgboost 
Requires:         R-parallel 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-tibble 

%description
Allows data to be processed by multiple machine learning algorithms at the
same time, enables feature selection of data by single a algorithm or
combinations of multiple. Easy to use tool for k-fold cross validation and
nested cross validation.

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
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
