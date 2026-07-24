%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rchime
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Detect and Remove Chimeras from Amplicon Sequence Analysis Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildRequires:    R-CRAN-strollur >= 0.1.3
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-RcppThread 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppXsimd 
Requires:         R-CRAN-strollur >= 0.1.3
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-RcppThread 
Requires:         R-utils 

%description
Detect and remove chimeras from your amplicon sequence analysis using
reference-based or de novo approaches. The 'rchime' package implements the
'VSEARCH' algorithms described in Rognes et al. (2016)
<doi:10.7717/peerj.2584>. 'VSEARCH' builds on the work of Edgar,R.C. et
al. (2011) <doi:10.1093/bioinformatics/btr381>.

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
