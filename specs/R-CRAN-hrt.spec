%global packname  hrt
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Heteroskedasticity Robust Testing

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-CompQuadForm 

%description
Functions for testing affine hypotheses on the regression coefficient
vector in regression models with heteroskedastic errors: (i) a function
for computing various test statistics (in particular using HC0-HC4
covariance estimators based on unrestricted or restricted residuals); (ii)
a function for numerically approximating the size of a test based on such
test statistics and a user-supplied critical value; and, most importantly,
(iii) a function for determining size-controlling critical values for such
test statistics and a user-supplied significance level (also incorporating
a check of conditions under which such a size-controlling critical value
exists). The three functions are based on results in Poetscher and
Preinerstorfer (2021) "Valid Heteroskedasticity Robust Testing"
<arXiv:2104.12597>.

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
