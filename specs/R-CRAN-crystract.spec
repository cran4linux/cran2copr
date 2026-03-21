%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crystract
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Crystallographic Information File (CIF) Data Processing Tools

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-geometry 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-geometry 

%description
Provides a suite of functions to parse Crystallographic Information Files
(.cif), extracting essential data such as chemical formulas, unit cell
parameters, atomic coordinates, and symmetry operations. It also includes
tools to calculate interatomic distances, identify bonded pairs using
various algorithms (minimum_distance, brunner_nn_reciprocal, econ_nn,
crystal_nn), determine nearest neighbor counts, and calculate bond angles.
The package is designed to facilitate the preparation of crystallographic
data for further analysis, including machine learning applications in
materials science. Methods are described in: Brunner (1977)
<doi:10.1107/S0567739477000461>; Hoppe (1979)
<doi:10.1524/zkri.1979.150.14.23>; O'Keeffe (1979)
<doi:10.1107/S0567739479001765>; Shannon (1976)
<doi:10.1107/S0567739476001551>; Pan et al. (2021)
<doi:10.1021/acs.inorgchem.0c02996>; Pauling (1960, ISBN:978-0801403330).

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
