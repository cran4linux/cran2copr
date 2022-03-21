%global __brp_check_rpaths %{nil}
%global packname  KSgeneral
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Computing P-Values of the K-S Test for (Dis)Continuous Null Distribution

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw-devel >= 3.3.4
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-dgof 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-dgof 

%description
Computes a p-value of the one-sample two-sided (or one-sided, as a special
case) Kolmogorov-Smirnov (KS) statistic, for any fixed critical level, and
an arbitrary, possibly large sample size for a pre-specified purely
discrete, mixed or continuous cumulative distribution function (cdf) under
the null hypothesis. If a data sample is supplied, 'KSgeneral' computes
the p-value corresponding to the value of the KS test statistic computed
based on the user provided data sample. The package 'KSgeneral' implements
a novel, accurate and efficient method named Exact-KS-FFT, expressing the
p-value as a double-boundary non-crossing probability for a homogeneous
Poisson process, which is then efficiently computed using Fast Fourier
Transform (FFT). The package can also be used to compute and plot the
complementary cdf of the KS statistic which is known to depend on the
hypothesized distribution when the latter is discontinuous (i.e. purely
discrete or mixed). To cite this package in publication use: Dimitrina S.
Dimitrova, Vladimir K. Kaishev, and Senren Tan. Computing the
Kolmogorov-Smirnov Distribution When the Underlying CDF is Purely
Discrete, Mixed, or Continuous. Journal of Statistical Software. 2020;
95(10): 1--42. <doi:10.18637/jss.v095.i10>.

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
