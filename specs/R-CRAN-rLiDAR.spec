%global packname  rLiDAR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          LiDAR Data Processing and Visualization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-methods 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-bitops 
Requires:         R-methods 

%description
Set of tools for reading, processing and visualizing small set of LiDAR
(Light Detection and Ranging) data for forest inventory applications.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
