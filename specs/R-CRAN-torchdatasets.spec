%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  torchdatasets
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Ready to Use Extra Datasets for Torch

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-torch >= 0.5.0
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-pins 
BuildRequires:    R-CRAN-torchvision 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-utils 
Requires:         R-CRAN-torch >= 0.5.0
Requires:         R-CRAN-fs 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-pins 
Requires:         R-CRAN-torchvision 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-withr 
Requires:         R-utils 

%description
Provides datasets in a format that can be easily consumed by torch
'dataloaders'. Handles data downloading from multiple sources, caching and
pre-processing so users can focus only on their model implementations.

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
