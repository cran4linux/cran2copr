%global packname  discoveR
%global packver   2.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Data Analysis System

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-highcharter 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinycustomloader 
BuildRequires:    R-CRAN-shinydashboardPlus 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-shiny 
Requires:         R-utils 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-config 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shinyjs 
Requires:         R-graphics 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-highcharter 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinycustomloader 
Requires:         R-CRAN-shinydashboardPlus 

%description
Performs an exploratory data analysis through a 'shiny' interface. It
includes basic methods such as the mean, median, mode, normality test,
among others. It also includes clustering techniques such as Principal
Components Analysis, Hierarchical Clustering and the K-Means Method.

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
