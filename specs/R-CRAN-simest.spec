%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simest
%global packver   0.4-1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Constrained Single Index Model Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-cobs 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-cobs 
Requires:         R-stats 
Requires:         R-graphics 

%description
Estimation of function and index vector in single index model ('sim') with
(and w/o) shape constraints including different smoothness conditions.
See, e.g., Kuchibhotla and Patra (2020) <doi:10.3150/19-BEJ1183>.

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
