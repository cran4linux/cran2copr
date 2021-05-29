%global packname  inferr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Inferential Statistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Select set of parametric and non-parametric statistical tests. 'inferr'
builds upon the solid set of statistical tests provided in 'stats' package
by including additional data types as inputs, expanding and restructuring
the test results. The tests included are t tests, variance tests,
proportion tests, chi square tests, Levene's test, McNemar Test, Cochran's
Q test and Runs test.

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
