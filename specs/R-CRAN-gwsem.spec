%global packname  gwsem
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Genome-Wide Structural Equation Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-OpenMx >= 2.0
BuildRequires:    R-CRAN-BH >= 1.69.0.1
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-qqman 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-OpenMx >= 2.0
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-qqman 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-lifecycle 

%description
Melds genome-wide association tests with structural equation modeling
(SEM) using 'OpenMx'. This package contains low-level C/C++ code to
rapidly read genetic data encoded in U.K. Biobank or 'plink' formats.
Prebuilt modeling options include one and two factor models. Alternately,
analyses may utilize arbitrary, user-provided SEMs.  See Verhulst, Maes, &
Neale (2017) <doi:10.1007/s10519-017-9842-6> for details. An updated
manuscript is in preparation.

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
