%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TrueWAP
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          True Range-Weighted Average Price ('TrueWAP')

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.2
Requires:         R-core >= 4.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.8.14
BuildRequires:    R-CRAN-TTR >= 0.24.4
Requires:         R-CRAN-zoo >= 1.8.14
Requires:         R-CRAN-TTR >= 0.24.4

%description
This groundbreaking technical indicator directly integrates volatility
into price averaging by weighting median range-bound prices using the True
Range.  Unlike conventional metrics such as TWAP (Time-Weighted Average
Price), which focuses solely on time, or VWAP (Volume-Weighted Average
Price), which emphasizes volume, 'TrueWAP' captures fluctuating market
behavior by reflecting true price movement within high/low performance
boundaries.

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
