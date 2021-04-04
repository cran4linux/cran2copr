%global packname  viewshed3d
%global packver   4.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compute Viewshed in 3D Point Clouds of Ecosystems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-lidR 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-nabor 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-hyper.fit 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pkgcond 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-lidR 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-viridis 
Requires:         R-utils 
Requires:         R-CRAN-nabor 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-hyper.fit 
Requires:         R-stats 
Requires:         R-CRAN-pkgcond 

%description
A set of tools to compute viewshed in 3D from Terrestrial Laser Scanner
data and prepare the data prior to visibility estimation.

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
