%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  groupedHyperframe
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Grouped Hyper Data Frame: An Extension of Hyper Data Frame

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5
Requires:         R-core >= 4.5
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-GET 
BuildRequires:    R-CRAN-SpatialPack 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-geomtextpath 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.random 
Requires:         R-CRAN-cli 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-GET 
Requires:         R-CRAN-SpatialPack 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-geomtextpath 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.random 

%description
An S3 class 'groupedHyperframe' that inherits from hyper data frame. Batch
processes on point-pattern hyper column. Aggregation of
function-value-table hyper column(s) and numeric hyper column(s) over a
nested grouping structure.

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
