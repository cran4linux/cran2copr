%global packname  Bayesrel
%global packver   0.7.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Reliability Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.4.6
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.4.6
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-Rdpack 

%description
Functionality for the most common single test reliability estimates:
Coefficient alpha, 'Guttman's' lambda-2/-4/-6, the Greatest lower bound
and coefficient omega. The Bayesian estimates are provided with credible
intervals. The frequentist estimates are provided with bootstrapped
confidence intervals The method for the Bayesian estimates, except for
omega, is sampling from the posterior inverse 'Wishart' for the covariance
matrix based measures (see 'Murphy', 2007,
<https://www.seas.harvard.edu/courses/cs281/papers/murphy-2007.pdf>. In
the case of omega it is 'Gibbs' Sampling from the joint conditional
distributions of a single factor model ('Lee', 2007,
<doi:10.1002/9780470024737>). The glb method uses adjusted code from the
'Rcsdp' package by 'Hector Corrada Bravo',
<https://CRAN.R-project.org/package=Rcsdp>. This process applies a
slightly adjusted solving algorithm from the 'CSDP' library by 'Brian
Borchers' <https://github.com/coin-or/Csdp/wiki>,
<doi.org/10.1080/10556789908805765>, but is wrapped in 'RcppArmadillo'.
Guttman's Lambda-4 is from 'Benton' (2015)
<doi:10.1007/978-3-319-07503-7_19>. The principal factor analysis for a
version of frequentist omega is from 'Schlegel' (2017)
<https://www.r-bloggers.com/2017/03/iterated-principal-factor-method-of-factor-analysis-with-r/>.
The analytic confidence interval of alpha is from 'Bonett' and 'Wright'
(2015) <doi:10.1002/job.1960>.

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
