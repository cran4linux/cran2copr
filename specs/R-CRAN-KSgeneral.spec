%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KSgeneral
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Computing P-Values of the One-Sample K-S Test and the Two-Sample K-S and Kuiper Tests for (Dis)Continuous Null Distribution

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw-devel
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-dgof 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-dgof 

%description
Contains functions to compute p-values for the one-sample and two-sample
Kolmogorov-Smirnov (KS) tests and the two-sample Kuiper test for any fixed
critical level and arbitrary (possibly very large) sample sizes. For the
one-sample KS test, this package implements a novel, accurate and
efficient method named Exact-KS-FFT, which allows the pre-specified
cumulative distribution function under the null hypothesis to be
continuous, purely discrete or mixed. In the two-sample case, it is
assumed that both samples come from an unspecified (unknown) continuous,
purely discrete or mixed distribution, i.e. ties (repeated observations)
are allowed, and exact p-values of the KS and the Kuiper tests are
computed. Note, the two-sample Kuiper test is often used when data samples
are on the line or on the circle (circular data). To cite this package in
publication: (for the use of the one-sample KS test) Dimitrina S.
Dimitrova, Vladimir K. Kaishev, and Senren Tan. Computing the
Kolmogorov-Smirnov Distribution When the Underlying CDF is Purely
Discrete, Mixed, or Continuous. Journal of Statistical Software. 2020;
95(10): 1--42.  <doi:10.18637/jss.v095.i10>. (for the use of the
two-sample KS and Kuiper tests) Dimitrina S. Dimitrova, Yun Jia and
Vladimir K. Kaishev (2024). The R functions KS2sample and Kuiper2sample:
Efficient Exact Calculation of P-values of the Two-sample
Kolmogorov-Smirnov and Kuiper Tests. submitted.

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
