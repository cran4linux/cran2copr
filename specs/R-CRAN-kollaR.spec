%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kollaR
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Event Classification, Visualization and Analysis of Eye Tracking Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-scales 

%description
Functions for analysing eye tracking data, including event detection,
visualizations and area of interest (AOI) based analyses. The package
includes implementations of the IV-T, I-DT, adaptive velocity threshold,
and Identification by two means clustering (I2MC) algorithms. See separate
documentation for each function. The principles underlying I-VT and I-DT
algorithms are described in Salvucci & Goldberg
(2000,doi{10.1145/355017.355028}). Two-means clustering is described in
Hessels et al. (2017, doi{10.3758/s13428-016-0822-1}). The adaptive
velocity threshold algorithm is described in Nyström & Holmqvist
(2010,doi{10.3758/BRM.42.1.188}). See a demonstration in the URL.

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
