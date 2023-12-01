%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Racmacs
%global packver   1.2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Antigenic Cartography Macros

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-brotli 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rmarchingcubes 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-RcppEnsmallen 
BuildRequires:    R-CRAN-rapidjsonr 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-brotli 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rmarchingcubes 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-rlang 

%description
A toolkit for making antigenic maps from immunological assay data, in
order to quantify and visualize antigenic differences between different
pathogen strains as described in Smith et al. (2004)
<doi:10.1126/science.1097211> and used in the World Health Organization
influenza vaccine strain selection process. Additional functions allow for
the diagnostic evaluation of antigenic maps and an interactive viewer is
provided to explore antigenic relationships amongst several strains and
incorporate the visualization of associated genetic information.

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
