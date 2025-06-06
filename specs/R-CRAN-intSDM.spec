%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  intSDM
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Reproducible Integrated Species Distribution Models Across Norway using 'INLA'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-inlabru >= 2.3.1
BuildRequires:    R-CRAN-PointedSDMs >= 2.1.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-geodata 
BuildRequires:    R-CRAN-fmesher 
BuildRequires:    R-CRAN-giscoR 
BuildRequires:    R-CRAN-blockCV 
BuildRequires:    R-CRAN-rgbif 
BuildRequires:    R-CRAN-tidyterra 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-inlabru >= 2.3.1
Requires:         R-CRAN-PointedSDMs >= 2.1.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-geodata 
Requires:         R-CRAN-fmesher 
Requires:         R-CRAN-giscoR 
Requires:         R-CRAN-blockCV 
Requires:         R-CRAN-rgbif 
Requires:         R-CRAN-tidyterra 
Requires:         R-CRAN-units 

%description
Integration of disparate datasets is needed in order to make efficient use
of all available data and thereby address the issues currently threatening
biodiversity. Data integration is a powerful modeling framework which
allows us to combine these datasets together into a single model, yet
retain the strengths of each individual dataset. We therefore introduce
the package, 'intSDM': an R package designed to help ecologists develop a
reproducible workflow of integrated species distribution models, using
data both provided from the user as well as data obtained freely online.
An introduction to data integration methods is discussed in Issac,
Jarzyna, Keil, Dambly, Boersch-Supan, Browning, Freeman, Golding,
Guillera-Arroita, Henrys, Jarvis, Lahoz-Monfort, Pagel, Pescott, Schmucki,
Simmonds and O’Hara (2020) <doi:10.1016/j.tree.2019.08.006>.

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
