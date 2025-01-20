%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  colorrepel
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Repel Visually Similar Colors for Colorblind Users in Various Plots

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-distances 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dqrng 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggalt 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-Polychrome 
Requires:         R-grDevices 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-distances 
Requires:         R-stats 
Requires:         R-CRAN-dqrng 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggalt 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-png 
Requires:         R-CRAN-Polychrome 

%description
Iterate and repel visually similar colors away in various 'ggplot2' plots.
When many groups are plotted at the same time on multiple axes, for
instance stacked bars or scatter plots, effectively ordering colors
becomes difficult. This tool iterates through color combinations to find
the best solution to maximize visual distinctness of nearby groups, so
plots are more friendly toward colorblind users. This is achieved by two
distance measurements, distance between groups within the plot, and CIELAB
color space distances between colors as described in Carter et al., (2018)
<doi:10.25039/TR.015.2018>.

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
