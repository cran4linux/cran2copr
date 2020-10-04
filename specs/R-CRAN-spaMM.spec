%global packname  spaMM
%global packver   3.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed-Effect Models, Particularly Spatial Models

License:          CeCILL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-ROI 
BuildRequires:    R-boot 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-proxy 
Requires:         R-nlme 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-ROI 
Requires:         R-boot 

%description
Inference based on mixed-effect models, including generalized linear mixed
models with spatial correlations and models with non-Gaussian random
effects (e.g., Beta). Various approximations of likelihood or restricted
likelihood are implemented, in particular Laplace approximation and
h-likelihood (Lee and Nelder 2001 <doi:10.1093/biomet/88.4.987>). Both
classical geostatistical models, and Markov random field models on
irregular grids (as considered in the 'INLA' package,
<http://www.r-inla.org>), can be fitted. Variation in residual variance
(heteroscedasticity) can itself be represented by a mixed-effect model.

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
