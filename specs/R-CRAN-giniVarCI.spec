%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  giniVarCI
%global packver   0.0.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Gini Indices, Variances and Confidence Intervals for Finite and Infinite Populations

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-stats 

%description
Estimates the Gini index and computes variances and confidence intervals
for finite and infinite populations, using different methods; also
computes Gini index for continuous probability distributions, draws
samples from continuous probability distributions with Gini indices set by
the user; uses 'Rcpp'. References: Muñoz et al. (2023)
<doi:10.1177/00491241231176847>. Álvarez et al. (2021)
<doi:10.3390/math9243252>. Giorgi and Gigliarano (2017)
<doi:10.1111/joes.12185>. Langel and Tillé (2013)
<doi:10.1111/j.1467-985X.2012.01048.x>.

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
