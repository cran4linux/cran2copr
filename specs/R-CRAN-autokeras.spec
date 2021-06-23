%global __brp_check_rpaths %{nil}
%global packname  autokeras
%global packver   1.0.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.12
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to 'AutoKeras'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-stats 
Requires:         R-CRAN-keras 
Requires:         R-methods 
Requires:         R-CRAN-reticulate 
Requires:         R-stats 

%description
R Interface to 'AutoKeras' <https://autokeras.com/>. 'AutoKeras' is an
open source software library for Automated Machine Learning (AutoML). The
ultimate goal of AutoML is to provide easily accessible deep learning
tools to domain experts with limited data science or machine learning
background. 'AutoKeras' provides functions to automatically search for
architecture and hyperparameters of deep learning models.

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
