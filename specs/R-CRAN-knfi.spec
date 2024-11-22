%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  knfi
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Korean National Forest Inventory Database

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-BiodiversityR 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cellranger 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-drat 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-BiodiversityR 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-cellranger 
Requires:         R-stats 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-drat 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-scales 

%description
Understanding the current status of forest resources is essential for
monitoring changes in forest ecosystems and generating related statistics.
In South Korea, the National Forest Inventory (NFI) surveys over 4,500
sample plots nationwide every five years and records 70 items, including
forest stand, forest resource, and forest vegetation surveys. Many
researchers use NFI as the primary data for research, such as biomass
estimation or analyzing the importance value of each species over time and
space, depending on the research purpose. However, the large volume of
accumulated forest survey data from across the country can make it
challenging to manage and utilize such a vast dataset. To address this
issue, we developed an R package that efficiently handles large-scale NFI
data across time and space. The package offers a comprehensive workflow
for NFI data analysis. It starts with data processing, where read_nfi()
function reconstructs NFI data according to the researcher's needs while
performing basic integrity checks for data quality.Following this, the
package provides analytical tools that operate on the verified data. These
include functions like summary_nfi() for summary statistics,
diversity_nfi() for biodiversity analysis, iv_nfi() for calculating
species importance value, and biomass_nfi() and cwd_biomass_nfi() for
biomass estimation. Finally, for visualization, the tsvis_nfi() function
generates graphs and maps, allowing users to visualize forest ecosystem
changes across various spatial and temporal scales. This integrated
approach and its specialized functions can enhance the efficiency of
processing and analyzing NFI data, providing researchers with insights
into forest ecosystems. The NFI Excel files (.xlsx) are not included in
the R package and must be downloaded separately. Users can access these
NFI Excel files by visiting the Korea Forest Service Forestry Statistics
Platform
<https://kfss.forest.go.kr/stat/ptl/article/articleList.do?curMenu=11694&bbsId=microdataboard>
to download the annual NFI Excel files, which are bundled in .zip
archives. Please note that this website is only available in Korean, and
direct download links can be found in the notes section of the read_nfi()
function.

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
