%global packname  dCovTS
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Distance Covariance and Correlation for Time Series Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dcov 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rfast2 
Requires:         R-CRAN-dcov 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rfast2 

%description
Computing and plotting the distance covariance and correlation function of
a univariate or a multivariate time series. Both versions of biased and
unbiased estimators of distance covariance and correlation are provided.
Test statistics for testing pairwise independence are also implemented.
Some data sets are also included. References include: a) Edelmann Dominic,
Fokianos Konstantinos and Pitsillou Maria (2019). An Updated Literature
Review of Distance Correlation and Its Applications to Time Series.
International Statistical Review, 87(2): 237--262.
<doi:10.1111/insr.12294>. b) Fokianos Konstantinos and Pitsillou Maria
(2018). Testing independence for multivariate time series via the
auto-distance correlation matrix. Biometrika, 105(2): 337--352.
<doi:10.1093/biomet/asx082>. c) Fokianos Konstantinos and Pitsillou Maria
(2017). Consistent testing for pairwise dependence in time series.
Technometrics, 59(2): 262--270. <doi:10.1080/00401706.2016.1156024>. d)
Pitsillou Maria and Fokianos Konstantinos (2016). dCovTS: Distance
Covariance/Correlation for Time Series. R Journal, 8(2):324-340.
<doi:10.32614/RJ-2016-049>.

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
