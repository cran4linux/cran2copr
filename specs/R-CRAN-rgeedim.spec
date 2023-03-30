%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rgeedim
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Search, Composite, and Download 'Google Earth Engine' Imagery with the 'Python' Module 'geedim'

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-jsonlite 

%description
Search, composite, and download 'Google Earth Engine' imagery with
'reticulate' bindings for the 'Python' module 'geedim' by Dugal Harris.
Read the 'geedim' documentation here: <https://geedim.readthedocs.io/>.
Wrapper functions are provided to make it more convenient to use 'geedim'
to download images larger than the 'Google Earth Engine' size limit
<https://developers.google.com/earth-engine/apidocs/ee-image-getdownloadurl>.
By default the "High Volume" API endpoint
<https://developers.google.com/earth-engine/cloud/highvolume> is used to
download data and this URL can be customized during initialization of the
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
