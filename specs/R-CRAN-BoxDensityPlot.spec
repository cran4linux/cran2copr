%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BoxDensityPlot
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Trait Density and Boxplot Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grid 
BuildRequires:    R-tools 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-readxl 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grid 
Requires:         R-tools 

%description
Reads wide-format phenotypic data (one row per genotype or sample, one
column per trait) from CSV or 'Excel' files, reshapes it to long format,
and produces faceted figures that combine a mirrored density curve with a
boxplot for each trait. Density curves can be drawn on the left, right, or
both sides of the box, and figures can be saved automatically at
publication resolution.

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
