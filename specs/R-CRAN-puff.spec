%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  puff
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate and Visualize the Gaussian Puff Forward Atmospheric Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyselect 

%description
Simulate and run the Gaussian puff forward atmospheric model in sensor
(specific sensor coordinates) or grid (across the grid of a full oil and
gas operations site) modes, following Jia, M., Fish, R., Daniels, W.,
Sprinkle, B. and Hammerling, D. (2024)
<doi:10.26434/chemrxiv-2023-hc95q-v3>. Numerous visualization options,
including static and animated, 2D and 3D, and a site map generator based
on sensor and source coordinates.

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
