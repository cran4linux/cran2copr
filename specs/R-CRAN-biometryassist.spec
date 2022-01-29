%global __brp_check_rpaths %{nil}
%global packname  biometryassist
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Assist Design and Analysis of Agronomic Experiments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-agricolae 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-farver 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-predictmeans 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-agricolae 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-farver 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-interp 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-predictmeans 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-withr 

%description
Provides functions to aid in the design and analysis of agronomic and
agricultural experiments through easy access to documentation and helper
functions, especially for users who are learning these concepts.

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
