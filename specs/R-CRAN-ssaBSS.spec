%global packname  ssaBSS
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stationary Subspace Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-JADE >= 2.0.2
BuildRequires:    R-CRAN-tsBSS >= 0.5.3
BuildRequires:    R-CRAN-ICtest >= 0.3.4
BuildRequires:    R-CRAN-BSSprep 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-JADE >= 2.0.2
Requires:         R-CRAN-tsBSS >= 0.5.3
Requires:         R-CRAN-ICtest >= 0.3.4
Requires:         R-CRAN-BSSprep 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
Stationary subspace analysis (SSA) is a blind source separation (BSS)
variant where stationary components are separated from non-stationary
components. Several SSA methods for multivariate time series are provided
here (Flumian et al. (2021); Hara et al. (2010)
<doi:10.1007/978-3-642-17537-4_52>) along with functions to simulate time
series with time-varying variance and autocovariance (Patilea and
Raissi(2014) <doi:10.1080/01621459.2014.884504>).

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
