%global __brp_check_rpaths %{nil}
%global packname  RCGLS
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Download and Open Data Provided by the Copernicus Global Land Service

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 

%description
Download and open manifest files provided by the Copernicus Global Land
Service data <https://land.copernicus.eu/global/>. The manifest files are
available at: <https://land.copernicus.vgt.vito.be/manifest/>. Also see:
<https://land.copernicus.eu/global/access/>. Before you can download the
data, you will first need to register to create a username and password.

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
