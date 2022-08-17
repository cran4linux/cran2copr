%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NSM3
%global packver   1.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.17
Release:          1%{?dist}%{?buildtag}
Summary:          Functions and Datasets to Accompany Hollander, Wolfe, and Chicken - Nonparametric Statistical Methods, Third Edition

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-agricolae 
BuildRequires:    R-CRAN-ash 
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-CRAN-BSDA 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-CRAN-fANCOVA 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-km.ci 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-Rfit 
BuildRequires:    R-CRAN-SemiPar 
BuildRequires:    R-CRAN-SuppDists 
BuildRequires:    R-CRAN-waveslim 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-partitions 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-agricolae 
Requires:         R-CRAN-ash 
Requires:         R-CRAN-binom 
Requires:         R-CRAN-BSDA 
Requires:         R-CRAN-coin 
Requires:         R-CRAN-fANCOVA 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-km.ci 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-np 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-Rfit 
Requires:         R-CRAN-SemiPar 
Requires:         R-CRAN-SuppDists 
Requires:         R-CRAN-waveslim 

%description
Designed to replace the tables which were in the back of the first two
editions of Hollander and Wolfe - Nonparametric Statistical Methods.
Exact procedures are performed when computationally possible.  Monte Carlo
and Asymptotic procedures are performed otherwise.  For those procedures
included in the base packages, our code simply provides a wrapper to
standardize the output with the other procedures in the package.

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
