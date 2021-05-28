%global packname  CCWeights
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Perform Weighted Linear Regression for Calibration Curve

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-bs4Dash 
BuildRequires:    R-CRAN-fresh 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-bs4Dash 
Requires:         R-CRAN-fresh 
Requires:         R-CRAN-DT 
Requires:         R-tools 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-readr 

%description
Automated assessment and selection of weighting factors for accurate
quantification using linear calibration curve. In addition, a 'shiny' App
is provided, allowing users to analyze their data using an interactive
graphical user interface, without any programming requirements.

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
