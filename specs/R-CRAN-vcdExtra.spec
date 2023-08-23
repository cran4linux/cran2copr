%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vcdExtra
%global packver   0.8-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.5
Release:          1%{?dist}%{?buildtag}
Summary:          'vcd' Extensions and Additions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-gnm >= 1.0.3
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ca 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-gnm >= 1.0.3
Requires:         R-CRAN-vcd 
Requires:         R-grid 
Requires:         R-CRAN-MASS 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ca 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-here 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 

%description
Provides additional data sets, methods and documentation to complement the
'vcd' package for Visualizing Categorical Data and the 'gnm' package for
Generalized Nonlinear Models. In particular, 'vcdExtra' extends mosaic,
assoc and sieve plots from 'vcd' to handle 'glm()' and 'gnm()' models and
adds a 3D version in 'mosaic3d'.  Additionally, methods are provided for
comparing and visualizing lists of 'glm' and 'loglm' objects. This package
is now a support package for the book, "Discrete Data Analysis with R" by
Michael Friendly and David Meyer.

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
