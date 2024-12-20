%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cobs
%global packver   1.3-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          Constrained B-Splines (Sparse Matrix Based)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-quantreg >= 4.65
BuildRequires:    R-CRAN-SparseM >= 1.6
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-quantreg >= 4.65
Requires:         R-CRAN-SparseM >= 1.6
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-methods 

%description
Qualitatively Constrained (Regression) Smoothing Splines via Linear
Programming and Sparse Matrices.

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
