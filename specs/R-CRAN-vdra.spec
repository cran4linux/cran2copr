%global __brp_check_rpaths %{nil}
%global packname  vdra
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Vertical Distributed Regression Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0

%description
Implements linear, logistic, and Cox regression on vertically partitioned
data across several data partners.  Data is not shared between data
partners or the analysis center and the computations can be considered
secure.  Three different protocols are implemented. 2-Party: two data
partners which communicate directly without an intermediate analysis
center; 2T-Party: two data partners communicate indirectly via an analysis
center, and KT-Party: two or more data partners plus an analysis center
are all allowed to communicate directly.  2-Party and 2^T-Party use a form
of secure multiplication as found in Karr, et. al. (2009)
"Privacy-Preserving Analysis of Vertically Partitioned Data Using Secure
Matrix Products" and Slavkovic et. al. (2007) "Secure Logistic Regression
of Horizontally and Vertically Partitioned Distributed Databases"
<doi:10.1109/ICDMW.2007.114>. Full details can be found in Samizo (In
preparation).

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
