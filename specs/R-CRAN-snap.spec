%global __brp_check_rpaths %{nil}
%global packname  snap
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Neural Application

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-CORElearn 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-CORElearn 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-reticulate 

%description
A simple wrapper to easily design vanilla deep neural networks using
'Tensorflow'/'Keras' backend for regression, classification and
multi-label tasks, with some tweaks and tricks (skip shortcuts, embedding,
feature selection and anomaly detection).

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
