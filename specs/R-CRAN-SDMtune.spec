%global packname  SDMtune
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Species Distribution Model Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-nnet >= 7.3.12
BuildRequires:    R-CRAN-randomForest >= 4.6.14
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-raster >= 2.9.5
BuildRequires:    R-CRAN-gbm >= 2.1.5
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-progress >= 1.2.2
BuildRequires:    R-CRAN-dismo >= 1.1.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-whisker >= 0.3
BuildRequires:    R-CRAN-rstudioapi >= 0.10
BuildRequires:    R-CRAN-maxnet >= 0.1.2
BuildRequires:    R-methods 
Requires:         R-nnet >= 7.3.12
Requires:         R-CRAN-randomForest >= 4.6.14
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-raster >= 2.9.5
Requires:         R-CRAN-gbm >= 2.1.5
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-progress >= 1.2.2
Requires:         R-CRAN-dismo >= 1.1.4
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-whisker >= 0.3
Requires:         R-CRAN-rstudioapi >= 0.10
Requires:         R-CRAN-maxnet >= 0.1.2
Requires:         R-methods 

%description
User-friendly framework that enables the training and the evaluation of
species distribution models (SDMs). The package implements functions for
data driven variable selection and model tuning and includes numerous
utilities to display the results. All the functions used to select
variables or to tune model hyperparameters have an interactive real-time
chart displayed in the 'RStudio' viewer pane during their execution.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/lib
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/templates
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
