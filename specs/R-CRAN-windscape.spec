%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  windscape
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model Landscape Connectivity by Wind

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-terra >= 1.8.42
BuildRequires:    R-CRAN-gdistance 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-terra >= 1.8.42
Requires:         R-CRAN-gdistance 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Model landscape connectivity by wind for ecological and evolutionary
analyses. Summarize long time series of gridded wind data, downloaded from
reanalyses or supplied by the user, into wind roses describing directional
conductance between neighboring grid cells. Model dispersal through them
with least-cost path and random walk algorithms, to map windsheds around
sites and estimate pairwise connectivity among them, test hypotheses
relating wind to ecological data, and visualize wind and connectivity with
'ggplot2'. The approach builds on Kling and Ackerly (2020)
<doi:10.1038/s41558-020-0848-3> and Kling and Ackerly (2021)
<doi:10.1073/pnas.2017317118>.

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
