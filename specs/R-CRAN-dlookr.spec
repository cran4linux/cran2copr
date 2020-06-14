%global packname  dlookr
%global packver   0.3.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.13
Release:          2%{?dist}
Summary:          Tools for Data Diagnosis, Exploration, Transformation

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RcmdrMisc 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-prettydoc 
BuildRequires:    R-CRAN-smbinning 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-tinytex 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DMwR 
BuildRequires:    R-rpart 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-RcmdrMisc 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-prettydoc 
Requires:         R-CRAN-smbinning 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-tinytex 
Requires:         R-methods 
Requires:         R-CRAN-DMwR 
Requires:         R-rpart 

%description
A collection of tools that support data diagnosis, exploration, and
transformation. Data diagnostics provides information and visualization of
missing values and outliers and unique and negative values to help you
understand the distribution and quality of your data. Data exploration
provides information and visualization of the descriptive statistics of
univariate variables, normality tests and outliers, correlation of two
variables, and relationship between target variable and predictor. Data
transformation supports binning for categorizing continuous variables,
imputates missing values and outliers, resolving skewness. And it creates
automated reports that support these three tasks.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/report
%{rlibdir}/%{packname}/INDEX
