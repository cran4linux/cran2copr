%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sdcTable
%global packver   0.32.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.32.7
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Statistical Disclosure Control in Tabular Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    glpk-devel
BuildRequires:    gmp-devel
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Matrix >= 1.3.0
BuildRequires:    R-CRAN-sdcHierarchies >= 0.19.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-glpkAPI 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-SSBtools 
Requires:         R-CRAN-Matrix >= 1.3.0
Requires:         R-CRAN-sdcHierarchies >= 0.19.1
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-methods 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-glpkAPI 
Requires:         R-CRAN-progress 
Requires:         R-utils 
Requires:         R-CRAN-SSBtools 

%description
Methods for statistical disclosure control in tabular data such as primary
and secondary cell suppression as described for example in Hundepol et al.
(2012) <doi:10.1002/9781118348239> are covered in this package.

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
