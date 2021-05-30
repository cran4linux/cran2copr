%global packname  dlookr
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Data Diagnosis, Exploration, Transformation

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-knitr >= 1.22
BuildRequires:    R-CRAN-corrplot >= 0.84
BuildRequires:    R-CRAN-hrbrthemes >= 0.8.0
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-extrafont >= 0.17
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-prettydoc 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RcmdrMisc 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-knitr >= 1.22
Requires:         R-CRAN-corrplot >= 0.84
Requires:         R-CRAN-hrbrthemes >= 0.8.0
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-extrafont >= 0.17
Requires:         R-CRAN-cli 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-prettydoc 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RcmdrMisc 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

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

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
