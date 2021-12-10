%global __brp_check_rpaths %{nil}
%global packname  gwpcormapper
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Geographically Weighted Partial Correlation Mapper

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-attempt 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-crosstalk 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-methods 
Requires:         R-CRAN-config 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-attempt 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geodist 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-crosstalk 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-leaflet 
Requires:         R-tools 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-pkgload 
Requires:         R-methods 

%description
An interactive mapping tool for geographically weighted correlation and
partial correlation. Geographically weighted partial correlation
coefficients are calculated following (Percival and Tsutsumida,
2017)<doi:10.1553/giscience2017_01_s36> and are described in greater
detail in (Tsutsumida et al., 2019)<doi:10.5194/ica-abs-1-372-2019> and
(Percival et al., 2021)<arXiv:2101.03491>.

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
