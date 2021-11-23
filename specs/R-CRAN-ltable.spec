%global __brp_check_rpaths %{nil}
%global packname  ltable
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Easy to Make (Lazy) Tables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-RcppGSL >= 0.3.9
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-RcppGSL >= 0.3.9
Requires:         R-methods 
Requires:         R-CRAN-clipr 
Requires:         R-graphics 
Requires:         R-stats 

%description
Constructs tables of counts and proportions out of data sets. It has
simplified syntax appealing for novice and even for advanced user under
time pressure. It is particularly suitable for exploratory data analysis
or presentation to single out most appropriate pieces of tabulated
information. The other important feature is possibility to insert tables
to Excel and Word documents. This version also features capacity of
log-linear and power analyses (original by Oleksandr Ocheredko
<doi:10.35566/isdsa2019c5>) for tabulated data with GSL.

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
