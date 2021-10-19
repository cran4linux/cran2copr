%global __brp_check_rpaths %{nil}
%global packname  abmR
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Agent-Based Models in R

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-table1 
BuildRequires:    R-CRAN-googledrive 
BuildRequires:    R-CRAN-swfscMisc 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-gtsummary 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-rnaturalearthdata 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tmap 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rgeos 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-table1 
Requires:         R-CRAN-googledrive 
Requires:         R-CRAN-swfscMisc 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-gtsummary 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-rnaturalearthdata 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tmap 
Requires:         R-CRAN-raster 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-rgeos 

%description
Supplies tools for running agent-based models (ABM) in R, as discussed in
Gochanour et al. (2021) <doi:10.1101/2021.09.15.460374> The package
contains two movement functions, each of which is based on the
Ornstein-Uhlenbeck (OU) model (Ornstein & Uhlenbeck, 1930)
<doi:10.1103/PhysRev.36.823>. It also contains several visualization and
data summarization functions to facilitate the presentation of simulation
results.

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
