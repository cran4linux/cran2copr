%global packname  ggquickeda
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Quickly Explore Your Data Using 'ggplot2' and 'table1' Summary Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-shinyjs >= 1.1
BuildRequires:    R-CRAN-table1 >= 1.1
BuildRequires:    R-CRAN-shiny >= 1.0.4
BuildRequires:    R-CRAN-ggrepel >= 0.7.0
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggpmisc 
BuildRequires:    R-CRAN-ggstance 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shinyjqui 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-RPostgres 
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-shinyjs >= 1.1
Requires:         R-CRAN-table1 >= 1.1
Requires:         R-CRAN-shiny >= 1.0.4
Requires:         R-CRAN-ggrepel >= 0.7.0
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggpmisc 
Requires:         R-CRAN-ggstance 
Requires:         R-CRAN-ggpubr 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-markdown 
Requires:         R-methods 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shinyjqui 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-RPostgres 

%description
Quickly and easily perform exploratory data analysis by uploading your
data as a 'csv' file. Start generating insights using 'ggplot2' plots and
'table1' tables with descriptive stats, all using an easy-to-use point and
click 'Shiny' interface.

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
