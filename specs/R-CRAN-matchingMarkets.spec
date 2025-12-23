%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  matchingMarkets
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Stable Matchings

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-RcppProgress >= 0.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-RcppProgress >= 0.2
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-lattice 
Requires:         R-parallel 
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-rJava 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements structural estimators to estimate preferences and correct for
the sample selection bias of observed outcomes in matching markets. This
includes one-sided matching of agents into groups (Klein, 2015)
<doi:10.17863/CAM.5812> as well as two-sided matching of students to
schools (Klein et al., 2024) <doi:10.1016/j.geb.2024.07.003>. The package
also contains algorithms to find stable matchings in the three most common
matching problems: the stable roommates problem (Irving, 1985)
<doi:10.1016/0196-6774(85)90033-1>, the college admissions problem (Gale
and Shapley, 1962) <doi:10.2307/2312726>, and the house allocation problem
(Shapley and Scarf, 1974) <doi:10.1016/0304-4068(74)90033-0>.

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
