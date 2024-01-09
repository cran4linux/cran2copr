%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geodimension
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Definition of Geographic Dimensions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-snakecase 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-snakecase 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 

%description
The geographic dimension plays a fundamental role in multidimensional
systems. To define a geographic dimension in a star schema, we need a
table with attributes corresponding to the levels of the dimension.
Additionally, we will also need one or more geographic layers to represent
the data using this dimension. The goal of this package is to support the
definition of geographic dimensions from layers of geographic information
related to each other. It makes it easy to define relationships between
layers and obtain the necessary data from them.

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
