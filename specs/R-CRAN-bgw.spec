%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bgw
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Bunch-Gay-Welsch Statistical Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0

%description
Performs statistical estimation and inference-related computations by
accessing and executing modified versions of 'Fortran' subroutines
originally published in the Association for Computing Machinery (ACM)
journal Transactions on Mathematical Software (TOMS) by Bunch, Gay and
Welsch (1993) <doi:10.1145/151271.151279>. The acronym 'BGW' (from the
authors' last names) will be used when making reference to technical
content (e.g., algorithm, methodology) that originally appeared in ACM
TOMS. A key feature of BGW is that it exploits the special structure of
statistical estimation problems within a trust-region-based optimization
approach to produce an estimation algorithm that is much more effective
than the usual practice of using optimization methods and codes originally
developed for general optimization. The 'bgw' package bundles 'R' wrapper
(and related) functions with modified 'Fortran' source code so that it can
be compiled and linked in the 'R' environment for fast execution. This
version implements a function ('bgw_mle.R') that performs maximum
likelihood estimation (MLE) for a user-provided model object that computes
probabilities (a.k.a. probability densities). The original motivation for
producing this package was to provide fast, efficient, and reliable MLE
for discrete choice models that can be called from the 'Apollo' choice
modelling 'R' package ( see <https://www.apollochoicemodelling.com>).
Starting with the release of Apollo 3.0, BGW is the default estimation
package. However, estimation can also be performed using BGW in a
stand-alone fashion without using 'Apollo' (as shown in simple examples
included in the package). Note also that BGW capabilities are not limited
to MLE, and future extension to other estimators (e.g., nonlinear least
squares, generalized method of moments, etc.) is possible. The 'Fortran'
code included in 'bgw' was modified by one of the original BGW authors
(Bunch) under his rights as confirmed by direct consultation with the ACM
Intellectual Property and Rights Manager.  See
<https://authors.acm.org/author-resources/author-rights>. The main
requirement is clear citation of the original publication (see above).

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
