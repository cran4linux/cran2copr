%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  divoRce
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Diagnosing Separation Phenomena in Latent Polyhedral Categorical Response Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rcdd 
Requires:         R-CRAN-rcdd 

%description
Utilities for checking and diagnosing separation phenomena (complete
separation, quasi-complete separation, overlap) for latent polyhedral
categorical response models including binary, nominal and ordinal data
models with link construction as baseline-category, adjacent-category,
cumulative, sequential (continuation-ratio), ordered stereotype and
arbitrary link error distribution (including logit, probit, cauchit,
cloglog, loglog, log amongst others) based on structure vectors as
described in Sablica, Hornik, Rusch (2026) <doi:10.48550/arXiv.2610.08100>
and Rusch, Sablica, Hornik (2026) <doi:10.48550/arXiv.2610.09951>. The
package functionality includes a check for separation and a check for
overlap with a linear program, a quick check for overlap, a sequential and
a parallel check for overlap based on subsamples, detailed separation
diagnostics such as identification of columns in the design
matrix/structure vector matrix that lead to separation, identification of
design matrix/structure vector matrix rows that lead to separation, the
dimension of the recession cone and the structure vectors that are
linearities. Calculations can be done with package 'rcdd' to employ
arbitrary precision and various other linear program solvers can also be
used via package 'ROI'. Implemented checks can be done before model
fitting based on outcome and design matrix or structure vector matrix or
via formula (pre-fit), or after model fitting for objects of class 'glm',
'multinom', 'polr', 'osm', 'clm', 'bracl', 'brmultinom'. Wrappers for
other classes can be easily constructed by third parties via pre-fit
functions.

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
