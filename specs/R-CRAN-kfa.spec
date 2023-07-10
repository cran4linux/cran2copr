%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kfa
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          K-Fold Cross Validation for Factor Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.6.9
BuildRequires:    R-CRAN-flextable >= 0.6.3
BuildRequires:    R-CRAN-semTools >= 0.5.5
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-simstandard 
Requires:         R-CRAN-lavaan >= 0.6.9
Requires:         R-CRAN-flextable >= 0.6.3
Requires:         R-CRAN-semTools >= 0.5.5
Requires:         R-CRAN-caret 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-officer 
Requires:         R-parallel 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-simstandard 

%description
Provides functions to identify plausible and replicable factor structures
for a set of variables via k-fold cross validation. The process combines
the exploratory and confirmatory factor analytic approach to scale
development (Flora & Flake, 2017) <doi:10.1037/cbs0000069> with a cross
validation technique that maximizes the available data (Hastie,
Tibshirani, & Friedman, 2009) <isbn:978-0-387-21606-5>. Also available are
functions to determine k by drawing on power analytic techniques for
covariance structures (MacCallum, Browne, & Sugawara, 1996)
<doi:10.1037/1082-989X.1.2.130>, generate model syntax, and summarize
results in a report.

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
