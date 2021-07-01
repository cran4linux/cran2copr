%global __brp_check_rpaths %{nil}
%global packname  snap
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Neural Application

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-keras >= 2.3.0.0
BuildRequires:    R-CRAN-tensorflow >= 2.2.0
BuildRequires:    R-CRAN-CORElearn >= 1.54.2
BuildRequires:    R-CRAN-readr >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-reticulate >= 1.18
BuildRequires:    R-CRAN-dbscan >= 1.1.5
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-tictoc >= 1.0.1
BuildRequires:    R-CRAN-forcats >= 0.5.0
BuildRequires:    R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-keras >= 2.3.0.0
Requires:         R-CRAN-tensorflow >= 2.2.0
Requires:         R-CRAN-CORElearn >= 1.54.2
Requires:         R-CRAN-readr >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-reticulate >= 1.18
Requires:         R-CRAN-dbscan >= 1.1.5
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-tictoc >= 1.0.1
Requires:         R-CRAN-forcats >= 0.5.0
Requires:         R-CRAN-purrr >= 0.3.4

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
