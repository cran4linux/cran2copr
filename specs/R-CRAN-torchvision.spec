%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  torchvision
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Models, Datasets and Transformations for Images

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-torch >= 0.5.0
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-zeallot 
Requires:         R-CRAN-torch >= 0.5.0
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rappdirs 
Requires:         R-utils 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-tiff 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-png 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-zeallot 

%description
Provides access to datasets, models and preprocessing facilities for deep
learning with images. Integrates seamlessly with the 'torch' package and
it's 'API' borrows heavily from 'PyTorch' vision package.

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
