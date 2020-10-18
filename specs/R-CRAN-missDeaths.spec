%global packname  missDeaths
%global packver   2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Simulating and Analyzing Time to Event Data in the Presence of Population Mortality

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-relsurv 
BuildRequires:    R-CRAN-cmprsk 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mitools 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-CRAN-survival 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-relsurv 
Requires:         R-CRAN-cmprsk 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-mitools 

%description
Implements two methods: a nonparametric risk adjustment and a data
imputation method that use general population mortality tables to allow a
correct analysis of time to disease recurrence. Also includes a powerful
set of object oriented survival data simulation functions.

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
