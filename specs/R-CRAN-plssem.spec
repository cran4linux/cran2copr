%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plssem
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Complex Partial Least Squares Structural Equation Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-modsem >= 1.0.17
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-reformulas 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-FNN 
Requires:         R-CRAN-modsem >= 1.0.17
Requires:         R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-reformulas 
Requires:         R-parallel 
Requires:         R-CRAN-FNN 

%description
Estimate complex Structural Equation Models (SEMs) by fitting Partial
Least Squares Structural Equation Modeling (PLS-SEM) and Partial Least
Squares consistent Structural Equation Modeling (PLSc-SEM) specifications
that handle categorical data, non-linear relations, and multilevel
structures. The implementation follows Lohmöller (1989) for the classic
PLS-SEM algorithm, Dijkstra and Henseler (2015) for consistent PLSc-SEM,
Dijkstra et al., (2014) for nonlinear PLSc-SEM, and Schuberth, Henseler,
Dijkstra (2018) for ordinal PLS-SEM and PLSc-SEM. Additional extensions
are under development. The MC-OrdPLSc algorithm, used to handle ordinal
interaction models is detailed in Slupphaug et al., (2026). References:
Lohmöller, J.-B. (1989, ISBN:9783790803002). "Latent Variable Path
Modeling with Partial Least Squares." Dijkstra, T. K., & Henseler, J.
(2015). <doi:10.1016/j.jmva.2015.06.002>. "Consistent partial least
squares path modeling." Dijkstra, T. K., & Schermelleh-Engel, K. (2014).
<doi:10.1016/j.csda.2014.07.008>. "Consistent partial least squares for
nonlinear structural equation models." Schuberth, F., Henseler, J., &
Dijkstra, T. K. (2018). <doi:10.1007/s11135-018-0767-9>. "Partial least
squares path modeling using ordinal categorical indicators." Slupphaug, K.
Mehmetoglu, M. & Mittner, M. (2026). <doi:10.31234/osf.io/fwzj6_v1>.
"Consistent Estimates from Biased Estimators: Monte-Carlo Consistent
Partial Least Squares for Latent Interaction Models with Ordinal
Indicators."

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
