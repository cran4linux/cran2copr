%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RTransferEntropy
%global packver   0.2.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.21
Release:          1%{?dist}%{?buildtag}
Summary:          Measuring Information Flow Between Time Series with Shannon and Renyi Transfer Entropy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-future >= 1.19.0
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-future >= 1.19.0
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-Rcpp 

%description
Measuring information flow between time series with Shannon and Rényi
transfer entropy. See also Dimpfl and Peter (2013)
<doi:10.1515/snde-2012-0044> and Dimpfl and Peter (2014)
<doi:10.1016/j.intfin.2014.03.004> for theory and applications to
financial time series. Additional references can be found in the theory
part of the vignette.

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
