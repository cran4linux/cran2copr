%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  slendr
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Simulation Framework for Spatiotemporal Population Genetics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-gganimate 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-ijtiff 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-gganimate 
Requires:         R-CRAN-png 
Requires:         R-CRAN-ijtiff 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ape 

%description
A framework for simulating spatially explicit genomic data which leverages
real cartographic information for programmatic and visual encoding of
spatiotemporal population dynamics on real geographic landscapes.
Population genetic models are then automatically executed by the 'SLiM'
software by Haller et al. (2019) <doi:10.1093/molbev/msy228> behind the
scenes, using a custom built-in simulation 'SLiM' script. Additionally,
fully abstract spatial models not tied to a specific geographic location
are supported, and users can also simulate data from standard,
non-spatial, random-mating models. These can be simulated either with the
'SLiM' built-in back-end script, or using an efficient coalescent
population genetics simulator 'msprime' by Baumdicker et al. (2022)
<doi:10.1093/genetics/iyab229> with a custom-built 'Python' script bundled
with the R package. Simulated genomic data is saved in a tree-sequence
format and can be loaded, manipulated, and summarised using tree-sequence
functionality via an R interface to the 'Python' module 'tskit' by
Kelleher et al. (2019) <doi:10.1038/s41588-019-0483-y>. Complete model
configuration, simulation and analysis pipelines can be therefore
constructed without a need to leave the R environment, eliminating
friction between disparate tools for population genetic simulations and
data analysis.

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
