%global __brp_check_rpaths %{nil}
%global packname  corpcor
%global packver   1.6.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.10
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Estimation of Covariance and (Partial) Correlation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Implements a James-Stein-type shrinkage estimator for the covariance
matrix, with separate shrinkage for variances and correlations. The
details of the method are explained in Schafer and Strimmer (2005)
<DOI:10.2202/1544-6115.1175> and Opgen-Rhein and Strimmer (2007)
<DOI:10.2202/1544-6115.1252>.  The approach is both computationally as
well as statistically very efficient, it is applicable to "small n, large
p" data, and always returns a positive definite and well-conditioned
covariance matrix. In addition to inferring the covariance matrix the
package also provides shrinkage estimators for partial correlations and
partial variances. The inverse of the covariance and correlation matrix
can be efficiently computed, as well as any arbitrary power of the
shrinkage correlation matrix.  Furthermore, functions are available for
fast singular value decomposition, for computing the pseudoinverse, and
for checking the rank and positive definiteness of a matrix.

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
