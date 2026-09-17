%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggmosaic2
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Mosaic Plots in the 'ggplot2' Framework, Extended

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9.3
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-withr >= 2.5.0
BuildRequires:    R-CRAN-productplots 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-plotly >= 4.9.3
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-withr >= 2.5.0
Requires:         R-CRAN-productplots 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-scales 

%description
Mosaic plots in the 'ggplot2' framework. Mosaic plot functionality is
provided in a single 'ggplot2' layer by calling the geom 'mosaic'. This
extends the now-defunct 'ggmosaic' package by allowing fitted loglinear
models which can be used to show patterns of association among variables
in frequency tables.

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
