%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  agricolaeplotr
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization of Design of Experiments from the 'agricolae' Package

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp >= 2.0.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-agricolae 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-FielDHub 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stplanr 
BuildRequires:    R-CRAN-ggspatial 
Requires:         R-CRAN-sp >= 2.0.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-agricolae 
Requires:         R-CRAN-raster 
Requires:         R-methods 
Requires:         R-CRAN-FielDHub 
Requires:         R-utils 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stplanr 
Requires:         R-CRAN-ggspatial 

%description
Visualization of Design of Experiments from the 'agricolae' package with
'ggplot2' framework The user provides an experiment design from the
'agricolae' package, calls the corresponding function and will receive a
visualization with 'ggplot2' based functions that are specific for each
design. As there are many different designs, each design is tested on its
type. The output can be modified with standard 'ggplot2' commands or with
other packages with 'ggplot2' function extensions.

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
