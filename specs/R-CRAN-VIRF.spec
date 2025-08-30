%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VIRF
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of Volatility Impulse Response Function of Multivariate Time Series

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rmgarch 
BuildRequires:    R-CRAN-mgarchBEKK 
BuildRequires:    R-CRAN-gnm 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-BigVAR 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-matlib 
Requires:         R-stats 
Requires:         R-CRAN-rmgarch 
Requires:         R-CRAN-mgarchBEKK 
Requires:         R-CRAN-gnm 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-BigVAR 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-matlib 

%description
Computation of volatility impulse response function for multivariate time
series model using algorithm by Jin, Lin and Tamvakis (2012)
<doi:10.1016/j.eneco.2012.03.003>.

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
