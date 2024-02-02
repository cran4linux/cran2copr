%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  klovan
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geostatistics Methods and Klovan Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-metR 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-metR 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyselect 

%description
A comprehensive set of geostatistical, visual, and analytical methods, in
conjunction with the expanded version of the acclaimed J.E. Klovan's
mining dataset, are included in 'klovan'. This makes the package an
excellent learning resource for Principal Component Analysis (PCA), Factor
Analysis (FA), kriging, and other geostatistical techniques. Originally
published in the 1976 book 'Geological Factor Analysis', the included
mining dataset was assembled by Professor J. E. Klovan of the University
of Calgary. Being one of the first applications of FA in the geosciences,
this dataset has significant historical importance. As a well-regarded and
published dataset, it is an excellent resource for demonstrating the
capabilities of PCA, FA, kriging, and other geostatistical techniques in
geosciences. For those interested in these methods, the 'klovan' datasets
provide a valuable and illustrative resource. Note that some methods
require the 'RGeostats' package. Please refer to the README or
Additional_repositories for installation instructions. This material is
based upon research in the Materials Data Science for Stockpile
Stewardship Center of Excellence (MDS3-COE), and supported by the
Department of Energy's National Nuclear Security Administration under
Award Number DE-NA0004104.

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
