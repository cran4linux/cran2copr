%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  otsfeatures
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Ordinal Time Series Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-astsa 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Bolstad2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-astsa 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Bolstad2 

%description
An implementation of several functions for feature extraction in ordinal
time series datasets. Specifically, some of the features proposed by Weiss
(2019) <doi:10.1080/01621459.2019.1604370> can be computed. These features
can be used to perform inferential tasks or to feed machine learning
algorithms for ordinal time series, among others. The package also
includes some interesting datasets containing financial time series.
Practitioners from a broad variety of fields could benefit from the
general framework provided by 'otsfeatures'.

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
