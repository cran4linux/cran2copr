%global packname  Bayesrel
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          2%{?dist}%{?buildtag}
Summary:          Bayesian Reliability Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-Rcsdp 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-Rcsdp 
Requires:         R-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-Rdpack 

%description
Functionality for the most common single test reliability estimates is
provided: Coefficient alpha, 'Guttman's' lambda-2/-4/-6, the greatest
lower bound and coefficient omega. The Bayesian estimates are provided
with credible intervals. The frequentist estimates are provided with
bootstrapped confidence intervals The method for the Bayesian estimates,
except for omega, is sampling from the posterior inverse 'Wishart' for the
covariance matrix based measures. See 'Murphy' (2007)
<https://www.seas.harvard.edu/courses/cs281/papers/murphy-2007.pdf>. In
the case of omega it is 'Gibbs' Sampling from the joint conditional
distributions of a single factor model. See 'Lee' (2007,
<doi:10.1002/9780470024737>). The glb method is adjusted code from the
'Rcsdp' package by 'Hector Corrada Bravo',
<https://CRAN.R-project.org/package=Rcsdp>; lambda-4 is from 'Benton'
(2015) <doi:10.1007/978-3-319-07503-7_19>; the principal factor analysis
for the frequentist omega is from 'Schlegel' (2017)
<https://www.r-bloggers.com/iterated-principal-factor-method-of-factor-analysis-with-r/>;
and the analytic alpha interval is from 'Bonett' and 'Wright' (2014)
<doi:10.1002/job.1960>.

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

%files
%{rlibdir}/%{packname}
