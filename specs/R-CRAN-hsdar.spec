%global packname  hsdar
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Manage, Analyse and Simulate Hyperspectral Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildRequires:    R-CRAN-raster >= 2.5.8
BuildRequires:    R-CRAN-rgdal >= 1.1.10
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-Boruta 
Requires:         R-CRAN-raster >= 2.5.8
Requires:         R-CRAN-rgdal >= 1.1.10
Requires:         R-CRAN-signal 
Requires:         R-methods 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-Boruta 

%description
Transformation of reflectance spectra, calculation of vegetation indices
and red edge parameters, spectral resampling for hyperspectral remote
sensing, simulation of reflectance and transmittance using the leaf
reflectance model PROSPECT and the canopy reflectance model PROSAIL.

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
