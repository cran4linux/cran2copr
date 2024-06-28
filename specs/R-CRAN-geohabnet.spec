%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geohabnet
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Geographical Risk Analysis Based on Habitat Connectivity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-yaml >= 2.3.7
BuildRequires:    R-CRAN-igraph >= 2.0.3
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-memoise >= 2.0.1
BuildRequires:    R-CRAN-terra >= 1.7.29
BuildRequires:    R-CRAN-geosphere >= 1.5.18
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-future >= 1.33.0
BuildRequires:    R-CRAN-beepr >= 1.3
BuildRequires:    R-CRAN-patchwork >= 1.2.0
BuildRequires:    R-CRAN-future.apply >= 1.11.0
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-easycsv >= 1.0.8
BuildRequires:    R-CRAN-geodata >= 0.6.2
BuildRequires:    R-CRAN-viridisLite >= 0.4.2
BuildRequires:    R-CRAN-rnaturalearth >= 0.3.3
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-tools 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-yaml >= 2.3.7
Requires:         R-CRAN-igraph >= 2.0.3
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-memoise >= 2.0.1
Requires:         R-CRAN-terra >= 1.7.29
Requires:         R-CRAN-geosphere >= 1.5.18
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-future >= 1.33.0
Requires:         R-CRAN-beepr >= 1.3
Requires:         R-CRAN-patchwork >= 1.2.0
Requires:         R-CRAN-future.apply >= 1.11.0
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-easycsv >= 1.0.8
Requires:         R-CRAN-geodata >= 0.6.2
Requires:         R-CRAN-viridisLite >= 0.4.2
Requires:         R-CRAN-rnaturalearth >= 0.3.3
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-tools 
Requires:         R-methods 

%description
The geohabnet package is designed to perform a geographically or spatially
explicit risk analysis of habitat connectivity. Xing et al (2021)
<doi:10.1093/biosci/biaa067> proposed the concept of cropland connectivity
as a risk factor for plant pathogen or pest invasions. As the functions in
geohabnet were initially developed thinking on cropland connectivity,
users are recommended to first be familiar with the concept by looking at
the Xing et al paper. In a nutshell, a habitat connectivity analysis
combines information from maps of host density, estimates the relative
likelihood of pathogen movement between habitat locations in the area of
interest, and applies network analysis to calculate the connectivity of
habitat locations. The functions of geohabnet are built to conduct a
habitat connectivity analysis relying on geographic parameters (spatial
resolution and spatial extent), dispersal parameters (in two commonly used
dispersal kernels: inverse power law and negative exponential models), and
network parameters (link weight thresholds and network metrics). The
functionality and main extensions provided by the functions in geohabnet
to habitat connectivity analysis are a) Capability to easily calculate the
connectivity of locations in a landscape using a single function, such as
sensitivity_analysis() or msean(). b) As backbone datasets, the geohabnet
package supports the use of two publicly available global datasets to
calculate cropland density. The backbone datasets in the geohabnet package
include crop distribution maps from Monfreda, C., N. Ramankutty, and J. A.
Foley (2008) <doi:10.1029/2007gb002947> "Farming the planet: 2. Geographic
distribution of crop areas, yields, physiological types, and net primary
production in the year 2000, Global Biogeochem. Cycles, 22, GB1022" and
International Food Policy Research Institute (2019)
<doi:10.7910/DVN/PRFF8V> "Global Spatially-Disaggregated Crop Production
Statistics Data for 2010 Version 2.0, Harvard Dataverse, V4". Users can
also provide any other geographic dataset that represents host density. c)
Because the geohabnet package allows R users to provide maps of host
density (as originally in Xing et al (2021)), host landscape density
(representing the geographic distribution of either crops or wild
species), or habitat distribution (such as host landscape density adjusted
by climate suitability) as inputs, we propose the term habitat
connectivity. d) The geohabnet package allows R users to customize
parameter values in the habitat connectivity analysis, facilitating
context-specific (pathogen- or pest-specific) analyses. e) The geohabnet
package allows users to automatically visualize maps of the habitat
connectivity of locations resulting from a sensitivity analysis across all
customized parameter combinations. The primary function is sean() and
sensitivity analysis(). Most functions in geohabnet provide as three main
outcomes: i) A map of mean habitat connectivity across parameters selected
by the user, ii) a map of variance of habitat connectivity across the
selected parameters, and iii) a map of the difference between the ranks of
habitat connectivity and habitat density. Each function can be used to
generate these maps as 'final' outcomes. Each function can also provide
intermediate outcomes, such as the adjacency matrices built to perform the
analysis, which can be used in other network analysis. Refer to article at
<https://garrettlab.github.io/HabitatConnectivity/articles/analysis.html>
to see examples of each function and how to access each of these outcome
types. To change parameter values, the file called parameters.yaml stores
the parameters and their values, can be accessed using get_parameters()
and set new parameter values with set_parameters(). Users can modify up to
ten parameters.

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
