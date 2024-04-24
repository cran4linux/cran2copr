%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Amelia
%global packver   1.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Program for Missing Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.11
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11
Requires:         R-CRAN-foreign 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-rlang 

%description
A tool that "multiply imputes" missing data in a single cross-section
(such as a survey), from a time series (like variables collected for each
year in a country), or from a time-series-cross-sectional data set (such
as collected by years for each of several countries). Amelia II implements
our bootstrapping-based algorithm that gives essentially the same answers
as the standard IP or EMis approaches, is usually considerably faster than
existing approaches and can handle many more variables.  Unlike Amelia I
and other statistically rigorous imputation software, it virtually never
crashes (but please let us know if you find to the contrary!).  The
program also generalizes existing approaches by allowing for trends in
time series across observations within a cross-sectional unit, as well as
priors that allow experts to incorporate beliefs they have about the
values of missing cells in their data.  Amelia II also includes useful
diagnostics of the fit of multiple imputation models.  The program works
from the R command line or via a graphical user interface that does not
require users to know R.

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
