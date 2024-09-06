%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  keras3
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to 'Keras'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tensorflow >= 2.16.0
BuildRequires:    R-CRAN-tfruns >= 1.5.2
BuildRequires:    R-CRAN-reticulate >= 1.36.0
BuildRequires:    R-CRAN-generics >= 0.0.1
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-zeallot 
BuildRequires:    R-CRAN-fastmap 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-tensorflow >= 2.16.0
Requires:         R-CRAN-tfruns >= 1.5.2
Requires:         R-CRAN-reticulate >= 1.36.0
Requires:         R-CRAN-generics >= 0.0.1
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-zeallot 
Requires:         R-CRAN-fastmap 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 

%description
Interface to 'Keras' <https://keras.io>, a high-level neural networks API.
'Keras' was developed with a focus on enabling fast experimentation,
supports both convolution based networks and recurrent networks (as well
as combinations of the two), and runs seamlessly on both CPU and GPU
devices.

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
