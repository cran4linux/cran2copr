%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggmapcn
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Customizable China and Global Map Visualizations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 5.0.0
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-terra >= 1.7
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-tidyterra >= 0.6.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-grid 
Requires:         R-CRAN-curl >= 5.0.0
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-terra >= 1.7
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-tidyterra >= 0.6.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-digest 
Requires:         R-grid 

%description
A 'ggplot2' extension centered on map visualization of China and the
globe. Provides customizable projections, boundary styles, coordinate
grids, scale bars, and buffer zones for thematic maps, suitable for
spatial data analysis and cartographic visualization.

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
