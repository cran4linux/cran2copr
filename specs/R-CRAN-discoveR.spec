%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  discoveR
%global packver   3.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Data Analysis System

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-shinydashboardPlus >= 2.0.0
BuildRequires:    R-CRAN-shiny >= 1.7.4
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-loadeR 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-echarts4r 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinycustomloader 
Requires:         R-CRAN-shinydashboardPlus >= 2.0.0
Requires:         R-CRAN-shiny >= 1.7.4
Requires:         R-CRAN-DT 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-config 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-loadeR 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-echarts4r 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinycustomloader 

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
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
