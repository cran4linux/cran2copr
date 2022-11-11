%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sparseR
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Variable Selection under Ranked Sparsity Principles for Interactions and Polynomials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-recipes >= 1.0.0
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-recipes >= 1.0.0
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 

%description
An implementation of ranked sparsity methods, including penalized
regression methods such as the sparsity-ranked lasso, its non-convex
alternatives, and elastic net, as well as the sparsity-ranked Bayesian
Information Criterion. As described in Peterson and Cavanaugh (2022)
<doi:10.1007/s10182-021-00431-7>, ranked sparsity is a philosophy with
methods primarily useful for variable selection in the presence of prior
informational asymmetry, which occurs in the context of trying to perform
variable selection in the presence of interactions and/or polynomials.
Ultimately, this package attempts to facilitate dealing with cumbersome
interactions and polynomials while not avoiding them entirely. Typically,
models selected under ranked sparsity principles will also be more
transparent, having fewer falsely selected interactions and polynomials
than other methods.

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
