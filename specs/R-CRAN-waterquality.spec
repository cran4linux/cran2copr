%global packname  waterquality
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Satellite Derived Water Quality Detection Algorithms

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 

%description
The main purpose of waterquality is to quickly and easily convert
satellite-based reflectance imagery into one or many well-known water
quality algorithms designed for the detection of harmful algal blooms or
the following pigment proxies: chlorophyll-a, blue-green algae
(phycocyanin), and turbidity. Johansen et al. (2019)
<doi:10.21079/11681/35053>.

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
