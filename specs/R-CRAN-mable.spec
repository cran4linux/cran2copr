%global packname  mable
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum Approximate Bernstein/Beta Likelihood Estimation

License:          LGPL (>= 2.0, < 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-icenReg 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-tcltk 
Requires:         R-CRAN-survival 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-icenReg 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-tcltk 

%description
Fit data from a continuous population with a smooth density on finite
interval by an approximate Bernstein polynomial model which is a mixture
of certain beta distributions and find maximum approximate Bernstein
likelihood estimator of the unknown coefficients. Consequently, maximum
likelihood estimates of the unknown density, distribution functions, and
more can be obtained. If the support of the density is not the unit
interval then transformation can be applied. This is an implementation of
the methods proposed by the author of this package published in the
Journal of Nonparametric Statistics: Guan (2016)
<doi:10.1080/10485252.2016.1163349> and Guan (2017)
<doi:10.1080/10485252.2017.1374384>. For data with covariates, under some
semiparametric regression models such as Cox proportional hazards model
and the accelerated failure time model, the baseline survival function can
be estimated smoothly based on general interval censored data.

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
