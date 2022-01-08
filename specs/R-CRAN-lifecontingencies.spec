%global __brp_check_rpaths %{nil}
%global packname  lifecontingencies
%global packver   1.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.8
Release:          1%{?dist}%{?buildtag}
Summary:          Financial and Actuarial Mathematics for Life Contingencies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-markovchain 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-utils 
Requires:         R-CRAN-markovchain 
Requires:         R-stats 

%description
Classes and methods that allow the user to manage life table, actuarial
tables (also multiple decrements tables). Moreover, functions to easily
perform demographic, financial and actuarial mathematics on life
contingencies insurances calculations are contained therein. See Spedicato
(2013) <doi:10.18637/jss.v055.i10>.

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
