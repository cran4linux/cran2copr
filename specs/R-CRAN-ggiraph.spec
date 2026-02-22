%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggiraph
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          1%{?dist}%{?buildtag}
Summary:          Make 'ggplot2' Graphics Interactive

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libpng-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-htmlwidgets >= 1.5
BuildRequires:    R-CRAN-systemfonts >= 1.3.1
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-CRAN-gdtools >= 0.5.0
BuildRequires:    R-CRAN-S7 >= 0.2.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-htmlwidgets >= 1.5
Requires:         R-CRAN-systemfonts >= 1.3.1
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-CRAN-gdtools >= 0.5.0
Requires:         R-CRAN-S7 >= 0.2.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-grid 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-vctrs 

%description
Create interactive 'ggplot2' graphics using 'htmlwidgets'.

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
