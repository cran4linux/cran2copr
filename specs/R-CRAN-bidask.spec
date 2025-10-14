%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bidask
%global packver   2.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Estimation of Bid-Ask Spreads from Open, High, Low, and Close Prices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-data.table 

%description
Implements the efficient estimator of bid-ask spreads from open, high,
low, and close prices described in Ardia, Guidotti, & Kroencke (JFE, 2024)
<doi:10.1016/j.jfineco.2024.103916>. It also provides an implementation of
the estimators described in Roll (JF, 1984)
<doi:10.1111/j.1540-6261.1984.tb03897.x>, Corwin & Schultz (JF, 2012)
<doi:10.1111/j.1540-6261.2012.01729.x>, and Abdi & Ranaldo (RFS, 2017)
<doi:10.1093/rfs/hhx084>.

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
