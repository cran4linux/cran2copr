%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  corrViz
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualise Correlations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-DendSer 
BuildRequires:    R-CRAN-gganimate 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-circlize 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-DendSer 
Requires:         R-CRAN-gganimate 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-circlize 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-shiny 

%description
An investigative tool designed to help users visualize correlations
between variables in their datasets. This package aims to provide an easy
and effective way to explore and visualize these correlations, making it
easier to interpret and communicate results.

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
