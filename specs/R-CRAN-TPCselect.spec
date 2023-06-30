%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TPCselect
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          1%{?dist}%{?buildtag}
Summary:          Variable Selection via Threshold Partial Correlation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-KernSmooth 
Requires:         R-stats 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-KernSmooth 

%description
A threshold partial correlation approach to selecting important variables
in linear models of L. and others (2017) at <doi:10.5705/ss.202015.0473>,
and in partial linear models of L. and others (2018) at
<doi:10.1016/j.jmva.2018.06.005>. This package also extends the PC-simple
algorithm of B. and others (2010) at <doi:10.1093/biomet/asq008> to
partial linear models.

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
