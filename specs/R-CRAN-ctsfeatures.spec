%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ctsfeatures
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Categorical Time Series

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
An implementation of several functions for feature extraction in
categorical time series datasets. Specifically, some features related to
marginal distributions and serial dependence patterns can be computed.
These features can be used to feed clustering and classification
algorithms for categorical time series, among others. The package also
includes some interesting datasets containing biological sequences.
Practitioners from a broad variety of fields could benefit from the
general framework provided by 'ctsfeatures'.

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
