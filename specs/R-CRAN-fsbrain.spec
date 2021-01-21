%global packname  fsbrain
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Managing and Visualizing Brain Surface Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-freesurferformats >= 0.1.14
BuildRequires:    R-CRAN-pkgfilecache >= 0.1.1
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-squash 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-magick 
Requires:         R-CRAN-freesurferformats >= 0.1.14
Requires:         R-CRAN-pkgfilecache >= 0.1.1
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-squash 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-magick 

%description
Provides high-level access to neuroimaging data from standard software
packages like 'FreeSurfer' <http://freesurfer.net/> on the level of
subjects and groups. Load morphometry data, surfaces and brain
parcellations based on atlases. Mask data using labels, load data for
specific atlas regions only, and visualize data and statistical results
directly in 'R'.

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
