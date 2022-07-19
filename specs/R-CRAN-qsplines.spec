%global __brp_check_rpaths %{nil}
%global packname  qsplines
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quaternions Splines

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-onion 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-onion 
Requires:         R-CRAN-shiny 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 

%description
Provides routines to create some quaternions splines: Barry-Goldman
algorithm, De Casteljau algorithm, and Kochanek-Bartels algorithm. The
implementations are based on the Python library 'splines'. Quaternions
splines allow to construct spherical curves. References: Barry and Goldman
<doi:10.1145/54852.378511>, Kochanek and Bartels
<doi:10.1145/800031.808575>.

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
