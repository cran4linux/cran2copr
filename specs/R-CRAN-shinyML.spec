%global __brp_check_rpaths %{nil}
%global packname  shinyML
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Compare Supervised Machine Learning Models Using Shiny App

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.0.3
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-argonDash 
BuildRequires:    R-CRAN-argonR 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-h2o 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-sparklyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-graphics 
Requires:         R-CRAN-shiny >= 1.0.3
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-argonDash 
Requires:         R-CRAN-argonR 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-h2o 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-sparklyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-lubridate 
Requires:         R-graphics 

%description
Implementation of a shiny app to easily compare supervised machine
learning model performances. You provide the data and configure each model
parameter directly on the shiny app. Different supervised learning
algorithms can be tested either on Spark or H2O frameworks to suit your
regression and classification tasks. Implementation of available machine
learning models on R has been done by Lantz (2013, ISBN:9781782162148).

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
