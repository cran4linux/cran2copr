%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rivnet
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extract and Analyze Rivers from Elevation Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-parallelly >= 1.33.0
BuildRequires:    R-CRAN-OCNet >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-traudem >= 1.0.3
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-elevatr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-parallelly >= 1.33.0
Requires:         R-CRAN-OCNet >= 1.1.0
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-traudem >= 1.0.3
Requires:         R-CRAN-spam 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-elevatr 
Requires:         R-methods 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-fields 

%description
Seamless extraction of river networks from digital elevation models data.
The package allows analysis of digital elevation models that can be either
externally provided or downloaded from open source repositories (thus
interfacing with the 'elevatr' package). Extraction is performed via the
'D8' flow direction algorithm of TauDEM (Terrain Analysis Using Digital
Elevation Models), thus interfacing with the 'traudem' package. Resulting
river networks are compatible with functions from the 'OCNet' package. See
Carraro (2023) <doi:10.5194/hess-27-3733-2023> for a presentation of the
package.

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
