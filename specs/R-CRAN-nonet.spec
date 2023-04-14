%global __brp_check_rpaths %{nil}
%global packname  nonet
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Weighted Average Ensemble without Training Labels

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.78
BuildRequires:    R-CRAN-pROC >= 1.13.0
BuildRequires:    R-CRAN-rlist >= 0.4.6.1
BuildRequires:    R-CRAN-rlang >= 0.2.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-caret >= 6.0.78
Requires:         R-CRAN-pROC >= 1.13.0
Requires:         R-CRAN-rlist >= 0.4.6.1
Requires:         R-CRAN-rlang >= 0.2.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-purrr 

%description
It provides ensemble capabilities to supervised and unsupervised learning
models predictions without using training labels. It decides the relative
weights of the different models predictions by using best models
predictions as response variable and rest of the mo. User can decide the
best model, therefore, It provides freedom to user to ensemble models
based on their design solutions.

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
