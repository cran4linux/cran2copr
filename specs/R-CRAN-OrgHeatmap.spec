%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OrgHeatmap
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization Tool for Human Organ Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-ggpolypath >= 0.3.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-ggpolypath >= 0.3.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grDevices 

%description
A tool for visualizing numerical data (such as gene expression levels) on
human organ maps. It supports custom color schemes, organ system
filtering, and optional bar charts for quantitative comparison. The
package integrates organ coordinate data to plot anatomical contours and
map data values to specific organs, facilitating intuitive visualization
of biological data distribution. The underlying method was described in
the preprint by Zhou et al. (2022) <doi:10.1101/2022.09.07.506938>.

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
