%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  galamm
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Additive Latent and Mixed Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-gratia 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-reformulas 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-gratia 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-memoise 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-reformulas 
Requires:         R-stats 

%description
Estimates generalized additive latent and mixed models using maximum
marginal likelihood, as defined in Sorensen et al. (2023)
<doi:10.1007/s11336-023-09910-z>, which is an extension of Rabe-Hesketh
and Skrondal (2004)'s unifying framework for multilevel latent variable
modeling <doi:10.1007/BF02295939>. Efficient computation is done using
sparse matrix methods, Laplace approximation, and automatic
differentiation. The framework includes generalized multilevel models with
heteroscedastic residuals, mixed response types, factor loadings,
smoothing splines, crossed random effects, and combinations thereof.
Syntax for model formulation is close to 'lme4' (Bates et al. (2015)
<doi:10.18637/jss.v067.i01>) and 'PLmixed' (Rockwood and Jeon (2019)
<doi:10.1080/00273171.2018.1516541>).

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
