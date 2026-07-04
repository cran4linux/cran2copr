%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cyclicwave
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cyclic Wave Analysis for Time-Series Clustering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-gsignal 
BuildRequires:    R-CRAN-waveslim 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-gsignal 
Requires:         R-CRAN-waveslim 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ggplot2 

%description
A modular toolkit for feature extraction and density-based clustering of
time-series data. It provides classical statistical, discrete wavelet,
Hilbert-based phase, and circular statistical features. The Hilbert-based
phase representation can support the analysis of periodic patterns, phase
relationships, and circular behavior in time-series data. The package
supports DBSCAN and OPTICS clustering, cluster evaluation, visualization,
data preparation, and comparison of multiple feature extraction and
clustering combinations. Methods are described in Karakaya and Purutcuoglu
(2026) <doi:10.15672/hujms.1821412> and Karakaya et al. (2026)
<doi:10.1007/978-3-032-17020-0_27>.

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
