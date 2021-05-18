%global packname  anipaths
%global packver   0.10.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.1
Release:          1%{?dist}%{?buildtag}
Summary:          Animation of Multiple Trajectories with Uncertainty

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-crawl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-animation 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-mgcv 
Requires:         R-grDevices 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-crawl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 

%description
Animation of observed trajectories using spline-based interpolation (see
for example, Buderman, F. E., Hooten, M. B., Ivan, J. S. and Shenk, T. M.
(2016), <doi:10.1111/2041-210X.12465> "A functional model for
characterizing long-distance movement behaviour". Methods Ecol Evol).
Intended to be used exploratory data analysis, and perhaps for preparation
of presentations.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
