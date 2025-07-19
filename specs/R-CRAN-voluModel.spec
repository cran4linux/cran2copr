%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  voluModel
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling Species Distributions in Three Dimensions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rangeBuilder >= 2.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-metR 
BuildRequires:    R-CRAN-modEvA 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-rangeBuilder >= 2.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggtext 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-metR 
Requires:         R-CRAN-modEvA 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-sf 

%description
Facilitates modeling species' ecological niches and geographic
distributions based on occurrences and environments that have a vertical
as well as horizontal component, and projecting models into
three-dimensional geographic space. Working in three dimensions is useful
in an aquatic context when the organisms one wishes to model can be found
across a wide range of depths in the water column. The package also
contains functions to automatically generate marine training model
training regions using machine learning, and interpolate and smooth
patchily sampled environmental rasters using thin plate splines. Davis
Rabosky AR, Cox CL, Rabosky DL, Title PO, Holmes IA, Feldman A, McGuire JA
(2016) <doi:10.1038/ncomms11484>. Nychka D, Furrer R, Paige J, Sain S
(2021) <doi:10.5065/D6W957CT>. Pateiro-Lopez B, Rodriguez-Casal A (2022)
<https://CRAN.R-project.org/package=alphahull>.

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
