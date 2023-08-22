%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BIOMASS
%global packver   2.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Aboveground Biomass and Its Uncertainty in Tropical Forests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-proj4 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-CRAN-proj4 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-sp 

%description
Contains functions to estimate aboveground biomass/carbon and its
uncertainty in tropical forests. These functions allow to (1) retrieve and
to correct taxonomy, (2) estimate wood density and its uncertainty, (3)
construct height-diameter models, (4) manage tree and plot coordinates,
(5) estimate the aboveground biomass/carbon at the stand level with
associated uncertainty. To cite 'BIOMASS', please use citation("BIOMASS").
See more in the article of Réjou-Méchain et al. (2017)
<doi:10.1111/2041-210X.12753>.

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
