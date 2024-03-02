%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  expowo
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Mining of Plant Diversity and Distribution

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-flora 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-PupillometryR 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-utils 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-flora 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-PupillometryR 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-viridisLite 

%description
Produces diversity estimates and species lists with associated global
distribution for any vascular plant family and genus from 'Plants of the
World Online' database <https://powo.science.kew.org/>, by interacting
with the source code of each plant taxon page. It also creates global maps
of species richness, graphics of species discoveries and nomenclatural
changes over time.

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
