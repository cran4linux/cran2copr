%global packname  purgeR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Inbreeding-Purging Estimation in Pedigreed Populations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-foreach >= 1.5.1
BuildRequires:    R-CRAN-progress >= 1.2.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-doSNOW >= 1.0.19
BuildRequires:    R-CRAN-RcppProgress >= 0.4.2
BuildRequires:    R-parallel 
Requires:         R-CRAN-foreach >= 1.5.1
Requires:         R-CRAN-progress >= 1.2.2
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-doSNOW >= 1.0.19
Requires:         R-CRAN-RcppProgress >= 0.4.2
Requires:         R-parallel 

%description
Inbreeding-purging analysis of pedigreed populations, including the
computation of the inbreeding coefficient, partial, ancestral and purged
inbreeding coefficients, and measures of the opportunity of purging
related to the individual reduction of inbreeding load. In addition,
functions to calculate the effective population size and other parameters
relevant to population genetics are included. Caballero A. and Toro M.A.
(2000) <doi:10.1017/s0016672399004449>. García-Dorado A., Wang J. and
López-Cortegano E. (2016) <doi:10.1534/g3.116.032425>. Gulisija D. and
Crow J.F. (2007) <doi:10.1111/j.1558-5646.2007.00088.x>. Gutiérrez J.P.,
Cervantes I., Goyache F. (2009) <doi:10.1111/j.1439-0388.2009.00810.x>.
López-Cortegano E., Bersabé D., Wang J., García-Dorado A. (2018)
<doi:10.1038/s41437-017-0045-y>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
