%global __brp_check_rpaths %{nil}
%global packname  relliptical
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Truncated Elliptical Family of Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-FuzzyNumbers.Ext.2 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Ryacas0 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-FuzzyNumbers.Ext.2 
Requires:         R-CRAN-matrixcalc 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Ryacas0 
Requires:         R-stats 

%description
It offers random numbers generation from members of the truncated
multivariate elliptical family of distribution such as the truncated
versions of the Normal, Student-t, Pearson VII, Slash, Logistic, among
others. Particular distributions can be provided by specifying the density
generating function. It also computes the first two moments (covariance
matrix as well) for some particular distributions. References used for
this package: Galarza, C. E., Matos, L. A., Castro, L. M., & Lachos, V. H.
(2022). Moments of the doubly truncated selection elliptical distributions
with emphasis on the unified multivariate skew-t distribution. Journal of
Multivariate Analysis, 189, 104944 <doi:10.1016/j.jmva.2021.104944>; Ho,
H. J., Lin, T. I., Chen, H. Y., & Wang, W. L. (2012). Some results on the
truncated multivariate t distribution. Journal of Statistical Planning and
Inference, 142(1), 25-40 <doi:10.1016/j.jspi.2011.06.006>; Valeriano, K.
A., Galarza, C. E., & Matos, L. A. (2021). Moments and random number
generation for the truncated elliptical family of distributions. arXiv
preprint <arXiv:2112.09319>.

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
