%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  powerPLS
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Power Analysis for PLS Classification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-compositions 
BuildRequires:    R-CRAN-FKSUM 
BuildRequires:    R-CRAN-nipals 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-simukde 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-caret 
Requires:         R-CRAN-compositions 
Requires:         R-CRAN-FKSUM 
Requires:         R-CRAN-nipals 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-simukde 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-caret 

%description
It estimates power and sample size for Partial Least Squares-based methods
described in Andreella, et al., (2024), <doi:10.48550/arXiv.2403.10289>.

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
