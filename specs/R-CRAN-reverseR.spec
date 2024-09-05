%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reverseR
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Regression Stability to Significance Reversal

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-boot.pval 
BuildRequires:    R-CRAN-L1pack 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-isotree 
BuildRequires:    R-CRAN-robustbase 
Requires:         R-methods 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-boot.pval 
Requires:         R-CRAN-L1pack 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-isotree 
Requires:         R-CRAN-robustbase 

%description
Tests linear regressions for significance reversal through
leave-one(multiple)-out.

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
