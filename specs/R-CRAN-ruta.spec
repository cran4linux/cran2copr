%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ruta
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Implementation of Unsupervised Neural Architectures

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-graphics >= 4.0.0
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-CRAN-R.utils >= 2.12.2
BuildRequires:    R-CRAN-keras >= 2.11.0
BuildRequires:    R-CRAN-tensorflow >= 2.11.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-utils 
Requires:         R-graphics >= 4.0.0
Requires:         R-stats >= 4.0.0
Requires:         R-CRAN-R.utils >= 2.12.2
Requires:         R-CRAN-keras >= 2.11.0
Requires:         R-CRAN-tensorflow >= 2.11.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-utils 

%description
Implementation of several unsupervised neural networks, from building
their architecture to their training and evaluation. Available networks
are auto-encoders including their main variants: sparse, contractive,
denoising, robust and variational, as described in Charte et al. (2018)
<doi:10.1016/j.inffus.2017.12.007>.

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
