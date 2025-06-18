%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rbcc
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Risk-Based Control Charts

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.00
Requires:         R-core >= 4.00
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-qcc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-PearsonDS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-qcc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-PearsonDS 
Requires:         R-methods 
Requires:         R-CRAN-pracma 

%description
Univariate and multivariate versions of risk-based control charts.
Univariate versions of control charts, such as the risk-based version of
X-bar, Moving Average (MA), Exponentially Weighted Moving Average Control
Charts (EWMA), and Cumulative Sum Control Charts (CUSUM) charts. The
risk-based version of the multivariate T2 control chart. Plot and summary
functions. Kosztyan et. al. (2016) <doi:10.1016/j.eswa.2016.06.019>.

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
