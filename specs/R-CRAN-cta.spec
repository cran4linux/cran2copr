%global __brp_check_rpaths %{nil}
%global packname  cta
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Contingency Table Analysis Based on ML Fitting of MPH Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-intervals 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-methods 
Requires:         R-CRAN-intervals 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-limSolve 
Requires:         R-methods 

%description
Contingency table analysis is performed based on maximum likelihood (ML)
fitting of multinomial-Poisson homogeneous (MPH) and homogeneous linear
predictor (HLP) models. See Lang (2004) <doi:10.1214/aos/1079120140> and
Lang (2005) <doi:10.1198/016214504000001042> for MPH and HLP models.
Objects computed include model goodness-of-fit statistics; likelihood-
based (cell- and link-specific) residuals; and cell probability and
expected count estimates along with standard errors. This package can also
compute test-inversion--e.g. Wald, profile likelihood, score,
power-divergence--confidence intervals for contingency table estimands,
when table probabilities are potentially subject to equality constraints.
For test-inversion intervals, see Lang (2008) <doi:10.1002/sim.3391> and
Zhu (2020) <doi:10.17077/etd.005331>.

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
