%global __brp_check_rpaths %{nil}
%global packname  mlmts
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning Algorithms for Multivariate Time Series

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantspec 
BuildRequires:    R-CRAN-waveslim 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-TSclust 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-TSA 
BuildRequires:    R-CRAN-tsfeatures 
BuildRequires:    R-CRAN-tseriesChaos 
BuildRequires:    R-CRAN-freqdom 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-base 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-complexplus 
BuildRequires:    R-CRAN-MTS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-multiwave 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-TSdist 
BuildRequires:    R-CRAN-evolqg 
BuildRequires:    R-CRAN-geigen 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ClusterR 
BuildRequires:    R-CRAN-AID 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ranger 
Requires:         R-CRAN-quantspec 
Requires:         R-CRAN-waveslim 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-TSclust 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-TSA 
Requires:         R-CRAN-tsfeatures 
Requires:         R-CRAN-tseriesChaos 
Requires:         R-CRAN-freqdom 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-dtw 
Requires:         R-base 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-complexplus 
Requires:         R-CRAN-MTS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-multiwave 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-TSdist 
Requires:         R-CRAN-evolqg 
Requires:         R-CRAN-geigen 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-pspline 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-ClusterR 
Requires:         R-CRAN-AID 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ranger 

%description
An implementation of several machine learning algorithms for multivariate
time series. The package includes functions allowing the execution of
clustering, classification or outlier detection methods, among others. It
also incorporates a collection of multivariate time series datasets which
can be used to analyse the performance of new proposed algorithms.
Practitioners from a broad variety of fields could benefit from the
general framework provided by 'mlmts'.

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
