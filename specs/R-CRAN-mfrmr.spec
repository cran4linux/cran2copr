%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mfrmr
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Estimation, Diagnostics, and Generalizability for Many-Facet Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-cpp11 >= 0.5.4
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-generics 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-tools 
Requires:         R-utils 

%description
Estimates many-facet ordered-response measurement models (Rating Scale,
Partial Credit, and Generalized Many-Facet Rasch Models) including step
constraints, declarative category support, explanatory facet covariates,
and joint interactions via high-speed C++ Joint Maximum Likelihood,
Jeffreys-penalized Joint Maximum Likelihood with Block-Schur standard
errors, Gauss-Hermite and Laplace-adaptive Marginal Maximum Likelihood
(with expected a posteriori scoring, Warm's weighted likelihood
estimation, latent regression, and sandwich covariances), Conditional
Maximum Likelihood, and Laplace empirical Bayes Markov rater drift models.
Provides multi-threaded C++ batch estimation, connectivity audits prior to
estimation, fit diagnostics, Fair(M), Real SE, 'RajuSA-Welch' pairwise
bias and parallel split-element differential facet functioning,
color-vision-safe 'ggplot2' graphics, and Generalizability (G-Study) and
Decision (D-Study) planning including fast Henderson Method 1 ('urGENOVA')
estimation. Connects calibration, diagnostics, visualizations, and
Markdown, HTML, or Word report generation in one analysis workflow. See
Andrich (1978) <doi:10.1007/BF02293814>, Masters (1982)
<doi:10.1007/BF02296272>, Warm (1989) <doi:10.1007/BF02294627>, Raju
(1990) <doi:10.1177/014662169001400208>, Uto and Ueno (2020)
<doi:10.1007/s41237-020-00115-7>, and Brennan (2001, ISBN:9780387952826).

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
