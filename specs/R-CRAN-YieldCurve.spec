%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  YieldCurve
%global packver   5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Modelling and Estimation of the Yield Curve

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-xts 
Requires:         R-CRAN-xts 

%description
Modelling the yield curve with some parametric models. The models
implemented are: Nelson, C.R., and A.F. Siegel (1987) <doi:
10.1086/296409>, Diebold, F.X. and Li, C. (2006) <doi:
10.1016/j.jeconom.2005.03.005> and Svensson, L.E. (1994) <doi:
10.3386/w4871>. The package also includes the data of the term structure
of interest rate of Federal Reserve Bank and European Central Bank.

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
