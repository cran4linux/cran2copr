%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fishboot
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrap-Based Methods for the Study of Fish Stocks and Aquatic Populations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-TropFishR 
BuildRequires:    R-CRAN-fishmethods 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-TropFishR 
Requires:         R-CRAN-fishmethods 

%description
A suite of bootstrap-based models and tools for analyzing fish stocks and
aquatic populations. Designed for ecologists and fisheries scientists, it
supports data from length-frequency distributions, tag-and-recapture
studies, and hard structure readings (e.g., otoliths). See Schwamborn et
al., 2019 <doi:10.1016/j.ecolmodel.2018.12.001> for background. The
package includes functions for bootstrapped fitting of growth curves and
plotting.

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
