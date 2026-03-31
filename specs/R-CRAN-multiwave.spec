%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multiwave
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Multivariate Long-Memory Models Parameters

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-signal 
Requires:         R-CRAN-signal 

%description
Computation of an estimation of the long-memory parameters and the
long-run covariance matrix using a multivariate model (Lobato (1999)
<doi:10.1016/S0304-4076(98)00038-4>; Shimotsu (2007)
<doi:10.1016/j.jeconom.2006.01.003>). Two semi-parametric methods are
implemented: a Fourier based approach (Shimotsu (2007)
<doi:10.1016/j.jeconom.2006.01.003>) and a wavelet based approach (Achard
and Gannaz (2016) <doi:10.1111/jtsa.12170>; Achard and Gannaz (2024)
<doi:10.1111/jtsa.12719>). Real and complex wavelets are implemented.

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
