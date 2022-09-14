%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sdmpredictors
%global packver   0.2.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.13
Release:          1%{?dist}%{?buildtag}
Summary:          Species Distribution Modelling Predictor Datasets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils >= 2.4.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-R.utils >= 2.4.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 

%description
Terrestrial and marine predictors for species distribution modelling from
multiple sources, including WorldClim <https://www.worldclim.org/>,,
ENVIREM <https://envirem.github.io/>, Bio-ORACLE <https://bio-oracle.org/>
and MARSPEC <http://www.marspec.org/>.

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
