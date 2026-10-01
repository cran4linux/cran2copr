%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FARM
%global packver   0.1.5.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5.15
Release:          1%{?dist}%{?buildtag}
Summary:          Forward Angular Relevance Measure

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-utils 

%description
The original implementation of the Forward Angular Relevance Measure
(FARM). The algorithm relies on a forward alignment approach for compared
time series based on the dynamic time warping (DTW) principle. It
considers the differences between data point as source in a combined
distance metric that is used for series alignment. The algorithm returns a
global and a series of local relevance measures relying on correlation
coefficients. A normalization of time series is not part of the algorithm
but recommended for best results. The FARM method is introduced in:
Christen et al. (2023) <doi:10.48550/arXiv.2304.11028>.

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
