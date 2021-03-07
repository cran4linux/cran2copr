%global packname  rAmCharts4
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the JavaScript Library 'amCharts 4'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets >= 1.5.3
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-reactR 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-htmlwidgets >= 1.5.3
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-reactR 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-minpack.lm 
Requires:         R-tools 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Creates JavaScript charts. The charts can be included in 'Shiny' apps and
R markdown documents, or viewed from the R console and 'RStudio' viewer.
Based on the JavaScript library 'amCharts 4' and the R packages
'htmlwidgets' and 'reactR'. Currently available types of chart are:
vertical and horizontal bar chart, radial bar chart, stacked bar chart,
vertical and horizontal Dumbbell chart, line chart, scatter chart, range
area chart, gauge chart, boxplot chart, and pie chart.

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
