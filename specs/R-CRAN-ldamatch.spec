%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ldamatch
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Selection of Statistically Similar Research Groups

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RUnit 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-iterpc 
BuildRequires:    R-CRAN-kSamples 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-RUnit 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-iterpc 
Requires:         R-CRAN-kSamples 
Requires:         R-stats 
Requires:         R-CRAN-car 
Requires:         R-CRAN-gmp 
Requires:         R-utils 
Requires:         R-methods 

%description
Select statistically similar research groups by backward selection using
various robust algorithms, including a heuristic based on linear
discriminant analysis, multiple heuristics based on the test statistic,
and parallelized exhaustive search.

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
