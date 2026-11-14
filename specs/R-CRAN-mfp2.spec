%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mfp2
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariable Fractional Polynomial Models with Extensions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-nnet 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 

%description
Fits multivariable fractional polynomial models with selection of
predictors and functional forms. The mfp2() function supports generalized
linear models, including Gamma and inverse-Gaussian regression;
negative-binomial, multinomial and ordinal regression; generalized
estimating equations for clustered data; Cox and parametric survival
models; and Fine-Gray competing-risks models. Extensions include
approximate cumulative distribution transformations for sigmoid-shaped
associations and spike-at-zero modelling for semi-continuous covariates.
The mfpi() function assesses interactions between a categorical grouping
variable and continuous, binary, or categorical predictors. Fractional
polynomial modelling is described by Royston and Altman (1994)
<doi:10.2307/2986270> and Royston and Sauerbrei (2008,
ISBN:978-0-470-02842-1). The approximate cumulative distribution extension
follows Royston (2014) <doi:10.1177/1536867X1401400206> and Royston and
Sauerbrei (2016) <doi:10.1177/1536867X1601600109>. Spike-at-zero modelling
follows Becher et al. (2012) <doi:10.1002/bimj.201100263>. Interaction
analyses follow Royston and Sauerbrei (2004) <doi:10.1002/sim.1815>,
Royston and Sauerbrei (2013) <doi:10.1002/sim.5813>, and Royston and
Sauerbrei (2014) <doi:10.1002/sim.6308>.

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
