%global packname  cvms
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Cross-Validation for Model Selection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.84
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-MuMIn >= 1.43.6
BuildRequires:    R-CRAN-pROC >= 1.14.0
BuildRequires:    R-CRAN-data.table >= 1.12
BuildRequires:    R-CRAN-lme4 >= 1.1.21
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-broom >= 0.5.2
BuildRequires:    R-CRAN-mltools >= 0.3.5
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-caret >= 6.0.84
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-MuMIn >= 1.43.6
Requires:         R-CRAN-pROC >= 1.14.0
Requires:         R-CRAN-data.table >= 1.12
Requires:         R-CRAN-lme4 >= 1.1.21
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-broom >= 0.5.2
Requires:         R-CRAN-mltools >= 0.3.5
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-lifecycle 

%description
Cross-validate one or multiple regression and classification models and
get relevant evaluation metrics in a tidy format. Validate the best model
on a test set and compare it to a baseline evaluation. Alternatively,
evaluate predictions from an external model. Currently supports regression
and classification (binary and multiclass). Described in chp. 5 of
Jeyaraman, B. P., Olsen, L. R., & Wambugu M. (2019, ISBN: 9781838550134).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
