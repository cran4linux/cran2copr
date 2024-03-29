%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  brglm2
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bias Reduction in Generalized Linear Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-enrichwith 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-graphics 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-enrichwith 
Requires:         R-CRAN-numDeriv 

%description
Estimation and inference from generalized linear models based on various
methods for bias reduction and maximum penalized likelihood with powers of
the Jeffreys prior as penalty. The 'brglmFit' fitting method can achieve
reduction of estimation bias by solving either the mean bias-reducing
adjusted score equations in Firth (1993) <doi:10.1093/biomet/80.1.27> and
Kosmidis and Firth (2009) <doi:10.1093/biomet/asp055>, or the median
bias-reduction adjusted score equations in Kenne et al. (2017)
<doi:10.1093/biomet/asx046>, or through the direct subtraction of an
estimate of the bias of the maximum likelihood estimator from the maximum
likelihood estimates as in Cordeiro and McCullagh (1991)
<https://www.jstor.org/stable/2345592>. See Kosmidis et al (2020)
<doi:10.1007/s11222-019-09860-6> for more details. Estimation in all cases
takes place via a quasi Fisher scoring algorithm, and S3 methods for the
construction of of confidence intervals for the reduced-bias estimates are
provided. In the special case of generalized linear models for binomial
and multinomial responses (both ordinal and nominal), the adjusted score
approaches to mean and media bias reduction have been found to return
estimates with improved frequentist properties, that are also always
finite, even in cases where the maximum likelihood estimates are infinite
(e.g. complete and quasi-complete separation; see Kosmidis and Firth, 2020
<doi:10.1093/biomet/asaa052>, for a proof for mean bias reduction in
logistic regression).

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
