%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ustats
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to Python Tools for Computing Higher-Order U-Statistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.41
Requires:         R-CRAN-reticulate >= 1.41

%description
Provides an R interface to the Python package 'u-stats'
<https://pypi.org/project/u-stats/> for efficient computation of
higher-order U-statistics using Einstein summation notation, implementing
the methods of Chen, Zhang, and Liu (2025)
<doi:10.48550/arXiv.2508.12627>. The package automatically converts R
objects to 'NumPy' or 'PyTorch' tensors via 'reticulate' and supports GPU
acceleration when 'PyTorch' with 'CUDA' is available. Python dependencies
are declared via 'reticulate' and can be installed automatically on first
use. Designed for large-scale statistical estimation where numerical
stability and performance are critical.

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
