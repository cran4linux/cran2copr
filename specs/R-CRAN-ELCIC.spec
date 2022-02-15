%global __brp_check_rpaths %{nil}
%global packname  ELCIC
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Empirical Likelihood-Based Consistent Information Criterion

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-PoisNor 
BuildRequires:    R-CRAN-bindata 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-wgeesel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-PoisNor 
Requires:         R-CRAN-bindata 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-wgeesel 

%description
We developed a consistent and robust information criterion to conduct
model selection for semiparametric models. It is free of distribution
specification and powerful to locate the true model given large sample
size. This package provides several usage of ELCIC with applications in
generalized linear model (GLM), generalized estimating equation (GEE) for
longitudinal data, and weighted GEE (WGEE) for missing longitudinal data
under the mechanism of missing at random and drop-out. Chixaing Chen, Ming
Wang, Rongling Wu, Runze Li (2020) <doi:10.5705/ss.202020.0254>.

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
