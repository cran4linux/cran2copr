%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  projectLSA
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          R Shiny Application for Latent Structure Analysis with a Graphical User Interface

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggiraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-poLCA 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-semPlot 
BuildRequires:    R-CRAN-semptools 
BuildRequires:    R-CRAN-semTools 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyLPA 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggiraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-poLCA 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-semPlot 
Requires:         R-CRAN-semptools 
Requires:         R-CRAN-semTools 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyLPA 
Requires:         R-CRAN-viridisLite 

%description
Provides an interactive Shiny-based toolkit for conducting latent
structure analyses, including Latent Profile Analysis (LPA), Latent Class
Analysis (LCA), Latent Trait Analysis (LTA/IRT), Exploratory Factor
Analysis (EFA), Confirmatory Factor Analysis (CFA), and Structural
Equation Modeling (SEM). The implementation is grounded in established
methodological frameworks: LPA is supported through 'tidyLPA' (Rosenberg
et al., 2018) <doi:10.21105/joss.00978>, LCA through 'poLCA' (Linzer &
Lewis, 2011), LTA/IRT via 'mirt' (Chalmers, 2012)
<doi:10.18637/jss.v048.i06>, and EFA via 'psych' (Revelle, 2025). SEM and
CFA functionalities build upon the 'lavaan' framework (Rosseel, 2012)
<doi:10.18637/jss.v048.i02>. Users can upload datasets or use built-in
examples, fit models, compare fit indices, visualize results, and export
outputs without programming.

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
