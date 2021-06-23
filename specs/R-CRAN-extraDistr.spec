%global __brp_check_rpaths %{nil}
%global packname  extraDistr
%global packver   1.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Additional Univariate and Multivariate Distributions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Density, distribution function, quantile function and random generation
for a number of univariate and multivariate distributions. This package
implements the following distributions: Bernoulli, beta-binomial,
beta-negative binomial, beta prime, Bhattacharjee, Birnbaum-Saunders,
bivariate normal, bivariate Poisson, categorical, Dirichlet,
Dirichlet-multinomial, discrete gamma, discrete Laplace, discrete normal,
discrete uniform, discrete Weibull, Frechet, gamma-Poisson, generalized
extreme value, Gompertz, generalized Pareto, Gumbel, half-Cauchy,
half-normal, half-t, Huber density, inverse chi-squared, inverse-gamma,
Kumaraswamy, Laplace, location-scale t, logarithmic, Lomax, multivariate
hypergeometric, multinomial, negative hypergeometric, non-standard beta,
normal mixture, Poisson mixture, Pareto, power, reparametrized beta,
Rayleigh, shifted Gompertz, Skellam, slash, triangular, truncated
binomial, truncated normal, truncated Poisson, Tukey lambda, Wald,
zero-inflated binomial, zero-inflated negative binomial, zero-inflated
Poisson.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
