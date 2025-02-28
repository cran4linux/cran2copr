%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mobsim
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Simulation and Scale-Dependent Analysis of Biodiversity Changes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-sads >= 0.4.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-sads >= 0.4.1
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-vegan 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 

%description
Simulation, analysis and sampling of spatial biodiversity data (May,
Gerstner, McGlinn, Xiao & Chase 2017) <doi:10.1111/2041-210x.12986>. In
the simulation tools user define the numbers of species and individuals,
the species abundance distribution and species aggregation. Functions for
analysis include species rarefaction and accumulation curves, species-area
relationships and the distance decay of similarity.

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
