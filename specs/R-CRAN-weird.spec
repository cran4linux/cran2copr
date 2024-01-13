%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  weird
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions and Data Sets for "That's Weird: Anomaly Detection Using R" by Rob J Hyndman

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-cli >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-aplpack 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-stray 
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-cli >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-aplpack 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-evd 
Requires:         R-grDevices 
Requires:         R-CRAN-interp 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-stray 

%description
All functions and data sets required for the examples in the book Hyndman
(2024) "That's Weird: Anomaly Detection Using R"
<https://OTexts.com/weird/>. All packages needed to run the examples are
also loaded.

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
