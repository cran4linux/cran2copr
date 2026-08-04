%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sondage
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Survey Sampling Algorithms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0

%description
Fast implementations of survey sampling algorithms for single-stage
probability sampling from finite populations, written in C. Provides equal
probability methods (simple random sampling, systematic, Bernoulli),
unequal probability methods (conditional Poisson / maximum entropy,
Sampford, Brewer, systematic PPS, Pareto, sequential Poisson, Poisson,
Chromy's minimum replacement, multinomial), balanced sampling via the cube
method, and spatially balanced sampling via the local pivotal method and
spatially correlated Poisson sampling. All sampling functions return
design objects carrying sample indices, inclusion probabilities, and
design metadata. Generics compute joint inclusion probabilities, pairwise
expectations, and sampling covariances for variance estimation. Mostly
based on algorithms from Tillé (2006, <doi:10.1007/0-387-34240-0>).

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
