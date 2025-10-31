%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RootscanR
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stitching and Analyzing Root Scans

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-parallel 
Requires:         R-CRAN-stringr 
Requires:         R-grid 
Requires:         R-CRAN-png 
Requires:         R-CRAN-abind 
Requires:         R-parallel 

%description
Minirhizotrons are widely used to observe and explore roots and their
growth. This package provides the means to stitch images and divide them
into depth layers. Please note that this R package was developed alongside
the following manuscript: Stitching root scans and extracting depth layer
information -- a workflow and practical examples, S. Kersting, L. Knüver,
and M. Fischer. The manuscript is currently in preparation and should be
citet as soon as it is available. This project was supported by the
project ArtIGROW, which is a part of the WIR!-Alliance ArtIFARM –
Artificial Intelligence in Farming funded by the German Federal Ministry
of Research, Technology and Space (No. 03WIR4805).

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
