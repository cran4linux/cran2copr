%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CAs
%global packver   0.24-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.24.3
Release:          1%{?dist}%{?buildtag}
Summary:          Creating Covering Arrays

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caverify >= 0.2.0
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-DoE.base 
BuildRequires:    R-CRAN-sets 
BuildRequires:    R-CRAN-prepplot 
BuildRequires:    R-CRAN-primes 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-permutations 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-conf.design 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-combinat 
Requires:         R-CRAN-caverify >= 0.2.0
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-DoE.base 
Requires:         R-CRAN-sets 
Requires:         R-CRAN-prepplot 
Requires:         R-CRAN-primes 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-permutations 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-conf.design 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-combinat 

%description
Implements covering arrays, as proposed in Groemping (2025)
<doi:10.1109/ICSTW64639.2025.10962463>. Uniform and mixed-level covering
arrays are created and can be assessed for their coverage properties. The
mathematical background of the constructions is provided in the technical
reports Groemping (2026)
<https://www1.bht-berlin.de/FB_II/reports/Report-2026-001.pdf> for the
uniform arrays and Groemping (2025)
<https://www1.bht-berlin.de/FB_II/reports/Report-2025-001.pdf> for the
mixed-level constructions. The post-processing method by Nayeri, Colbourn,
and Konjevod (2013) <doi:10.1016/j.ejc.2012.07.017> is also provided. In
addition, there are preliminary tools for the creation of sequence
covering arrays.

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
