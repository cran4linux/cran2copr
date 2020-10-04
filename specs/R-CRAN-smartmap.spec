%global packname  smartmap
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}%{?buildtag}
Summary:          Smartly Create Maps from R Objects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-utils 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-sf 
Requires:         R-utils 

%description
Preview spatial data as 'leaflet' maps with minimal effort. smartmap is
optimized for interactive use and distinguishes itself from similar
packages because it does not need real spatial ('sp' or 'sf') objects an
input; instead, it tries to automatically coerce everything that looks
like spatial data to sf objects or leaflet maps. It - for example -
supports direct mapping of: a vector containing a single coordinate pair,
a two column matrix, a data.frame with longitude and latitude columns, or
the path or URL to a (possibly compressed) 'shapefile'.

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
