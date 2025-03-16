%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggvfields
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Vector Field Visualizations with 'ggplot2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-farver 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-grid 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-farver 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-deSolve 
Requires:         R-grid 
Requires:         R-utils 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-cli 

%description
A 'ggplot2' extension for visualizing vector fields in two-dimensional
space. Provides flexible tools for creating vector and stream field
layers, visualizing gradients and potential fields, and smoothing vector
and scalar data to estimate underlying patterns.

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
