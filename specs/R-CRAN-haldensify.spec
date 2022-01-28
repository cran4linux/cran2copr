%global __brp_check_rpaths %{nil}
%global packname  haldensify
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Highly Adaptive Lasso Conditional Density Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-origami >= 1.0.3
BuildRequires:    R-CRAN-hal9001 >= 0.4.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-origami >= 1.0.3
Requires:         R-CRAN-hal9001 >= 0.4.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-Rdpack 

%description
An algorithm for flexible conditional density estimation based on
application of pooled hazard regression to an artificial repeated measures
dataset constructed by discretizing the support of the outcome variable.
To facilitate non/semi-parametric estimation of the conditional density,
the highly adaptive lasso, a nonparametric regression function shown to
reliably estimate a large class of functions at a fast convergence rate,
is utilized. The pooled hazards data augmentation formulation implemented
was first described by Díaz and van der Laan (2011)
<doi:10.2202/1557-4679.1356>. To complement the conditional density
estimation utilities, tools for efficient nonparametric inverse
probability weighted (IPW) estimation of the causal effects of stochastic
shift interventions (modified treatment policies), directly utilizing the
density estimation technique for construction of the generalized
propensity score, are provided. These IPW estimators utilize
undersmoothing (sieve estimation) of the conditional density estimators in
order to achieve the non/semi-parametric efficiency bound.

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
