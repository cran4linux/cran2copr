%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tsqn
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Applications of the Qn Estimator to Time Series (Univariate and Multivariate)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-fracdiff 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-fracdiff 

%description
Time Series Qn is a package with applications of the Qn estimator of
Rousseeuw and Croux (1993) <doi:10.1080/01621459.1993.10476408> to
univariate and multivariate Time Series in time and frequency domains.
More specifically, the robust estimation of autocorrelation or
autocovariance matrix functions from Ma and Genton (2000, 2001)
<doi:10.1111/1467-9892.00203>, <doi:10.1006/jmva.2000.1942> and Cotta
(2017) <doi:10.13140/RG.2.2.14092.10883> are provided. The robust
pseudo-periodogram of Molinares et. al. (2009)
<doi:10.1016/j.jspi.2008.12.014> is also given. This packages also
provides the M-estimator of the long-memory parameter d based on the
robustification of the GPH estimator proposed by Reisen et al. (2017)
<doi:10.1016/j.jspi.2017.02.008>.

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
