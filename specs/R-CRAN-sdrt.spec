%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sdrt
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating the Sufficient Dimension Reduction Subspaces in Time Series

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-pracma 

%description
The sdrt() function is designed for estimating subspaces for Sufficient
Dimension Reduction (SDR) in time series, with a specific focus on the
Time Series Central Mean subspace (TS-CMS). The package employs the
Fourier transformation method proposed by Samadi and De Alwis (2023)
<doi:10.48550/arXiv.2312.02110> and the Nadaraya-Watson kernel smoother
method proposed by Park et al. (2009) <doi:10.1198/jcgs.2009.08076> for
estimating the TS-CMS. The package provides tools for estimating distances
between subspaces and includes functions for selecting model parameters
using the Fourier transformation method.

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
