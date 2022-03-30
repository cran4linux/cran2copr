%global __brp_check_rpaths %{nil}
%global packname  SKAT
%global packver   2.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          SNP-Set (Sequence) Kernel Association Test

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-SPAtest 
BuildRequires:    R-CRAN-RSpectra 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-SPAtest 
Requires:         R-CRAN-RSpectra 

%description
Functions for kernel-regression-based association tests including Burden
test, SKAT and SKAT-O. These methods aggregate individual SNP score
statistics in a SNP set and efficiently compute SNP-set level p-values.
Methods available in this package include SKAT described in Micheal Wu,
Seunggeun Lee et al. (2011) <doi:10.1016/j.ajhg.2011.05.029>, SKAT-O in
Seunggeun Lee et al. (2012) <doi:10.1093/biostatistics/kxs014>, combined
test of rare and common variants in Iuliana Ionita-Laza and Seunggeun Lee
et al. (2013) <doi:10.1016/j.ajhg.2013.04.015>, efficient resampling for
binary traits in Seunggeun Lee et al. (2016)
<doi:10.1093/biostatistics/kxv033>, and robust test for binary traits in
Zhangchen Zhao et al. (2020) <doi:10.1016/j.ajhg.2019.11.012>.

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
