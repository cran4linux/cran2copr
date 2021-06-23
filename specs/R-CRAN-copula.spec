%global __brp_check_rpaths %{nil}
%global packname  copula
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Dependence with Copulas

License:          GPL (>= 3) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-stabledist >= 0.6.4
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-ADGofTest 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-stabledist >= 0.6.4
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats4 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-ADGofTest 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-pspline 
Requires:         R-CRAN-numDeriv 

%description
Classes (S4) of commonly used elliptical, Archimedean, extreme-value and
other copula families, as well as their rotations, mixtures and
asymmetrizations. Nested Archimedean copulas, related tools and special
functions. Methods for density, distribution, random number generation,
bivariate dependence measures, Rosenblatt transform, Kendall distribution
function, perspective and contour plots. Fitting of copula models with
potentially partly fixed parameters, including standard errors. Serial
independence tests, copula specification tests (independence,
exchangeability, radial symmetry, extreme-value dependence,
goodness-of-fit) and model selection based on cross-validation. Empirical
copula, smoothed versions, and non-parametric estimators of the Pickands
dependence function.

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
