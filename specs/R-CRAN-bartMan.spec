%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bartMan
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Visualisations for BART Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-DendSer 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggiraph 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rrapply 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidybayes 
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidytreatment 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-BART 
BuildRequires:    R-CRAN-bartMachine 
BuildRequires:    R-CRAN-dbarts 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-DendSer 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggiraph 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggraph 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rrapply 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-tidybayes 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidytreatment 
Requires:         R-utils 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-BART 
Requires:         R-CRAN-bartMachine 
Requires:         R-CRAN-dbarts 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-vctrs 

%description
Investigating and visualising Bayesian Additive Regression Tree (BART)
(Chipman, H. A., George, E. I., & McCulloch, R. E. 2010)
<doi:10.1214/09-AOAS285> model fits.  We construct conventional plots to
analyze a model’s performance and stability as well as create new
tree-based plots to analyze variable importance, interaction, and tree
structure.  We employ Value Suppressing Uncertainty Palettes (VSUP) to
construct heatmaps that display variable importance and interactions
jointly using colour scale to represent posterior uncertainty.  Our
visualisations are designed to work with the most popular BART R packages
available, namely 'BART' Rodney Sparapani and Charles Spanbauer and Robert
McCulloch 2021 <doi:10.18637/jss.v097.i01>, 'dbarts' (Vincent Dorie 2023)
<https://CRAN.R-project.org/package=dbarts>, and 'bartMachine' (Adam
Kapelner and Justin Bleich 2016) <doi:10.18637/jss.v070.i04>.

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
