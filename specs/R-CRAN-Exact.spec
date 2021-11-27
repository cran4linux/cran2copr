%global __brp_check_rpaths %{nil}
%global packname  Exact
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Unconditional Exact Test

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rootSolve 

%description
Performs unconditional exact tests and power calculations for 2x2
contingency tables. For comparing two independent proportions, performs
Barnard's test (1945) <doi:10.1038/156177a0> using the original CSM test
(Barnard, 1947 <doi:10.1093/biomet/34.1-2.123>), using Fisher's p-value
referred to as Boschloo's test (1970)
<doi:10.1111/j.1467-9574.1970.tb00104.x>, or using a Z-statistic (Suissa
and Shuster, 1985, <doi:10.2307/2981892>). For comparing two binary
proportions, performs unconditional exact test using McNemar's Z-statistic
(Berger and Sidik, 2003, <doi:10.1191/0962280203sm312ra>), using McNemar's
conditional p-value, using McNemar's Z-statistic with continuity
correction, or using CSM test.  Calculates confidence intervals for the
difference in proportion. This package interacts with pre-computed data
available through the ExactData R package, which is available in a 'drat'
repository. Install the ExactData R package from GitHub at
<https://pcalhoun1.github.io/drat/>. The ExactData R package is
approximately 25 MB.

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
