%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GGoutlieR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Identify Individuals with Unusual Geo-Genetic Patterns

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-FastKNN 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
Requires:         R-stats4 
Requires:         R-CRAN-FastKNN 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 

%description
Identify and visualize individuals with unusual association patterns of
genetics and geography using the approach of Chang and Schmid (2023)
<doi:10.1101/2023.04.06.535838>. It detects potential outliers that
violate the isolation-by-distance assumption using the K-nearest neighbor
approach. You can obtain a table of outliers with statistics and visualize
unusual geo-genetic patterns on a geographical map. This is useful for
landscape genomics studies to discover individuals with unusual geography
and genetics associations from a large biological sample.

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
