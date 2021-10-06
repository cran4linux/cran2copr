%global __brp_check_rpaths %{nil}
%global packname  rLiDAR
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          LiDAR Data Processing and Visualization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spatstat.geom 
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-geometry 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spatstat.geom 

%description
Set of tools for reading, processing and visualizing small set of LiDAR
(Light Detection and Ranging) data for forest inventory applications. More
details were published in Silva et al. (2016)
<doi:10.1080/07038992.2016.1196582>.

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
