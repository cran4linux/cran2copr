%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robustsur
%global packver   0.0-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Estimation for Seemingly Unrelated Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-robreg3S 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-GSE 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-robreg3S 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-GSE 

%description
Data sets are often corrupted by outliers. When data are multivariate
outliers can be classified as case-wise or cell-wise. The latters are
particularly challenge to handle. We implement a robust estimation
procedure for Seemingly Unrelated Regression Models which is able to cope
well with both type of outliers. Giovanni Saraceno, Fatemah Alqallaf,
Claudio Agostinelli (2021) <arXiv:2107.00975>.

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
