%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cfcompare
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Compare DID, SDID, Matrix Completion and the Triply Robust Panel Estimator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 

%description
A comparison toolkit for binary-treatment panel causal inference. Runs
difference-in-differences (DID; two-way fixed effects), synthetic
difference-in-differences (SDID), synthetic control (SC), matrix
completion (MC), and the Triply RObust Panel (TROP) estimator of Athey,
Imbens, Qu and Viviano (2026) <doi:10.1002/jae.70061> on the same data,
and returns their average treatment effects on the treated (ATT) on a
single tidy schema with shared plots. TROP, DID and matrix completion are
implemented natively; SDID and SC are obtained through the 'synthdid'
package, and an alternative matrix-completion / interactive fixed-effects
estimator through 'gsynth'. The suggested packages 'synthdid' and
'augsynth' are not on CRAN; they can be installed from GitHub at
<https://github.com/synth-inference/synthdid> and
<https://github.com/ebenmichael/augsynth>, and every feature that needs
them is skipped with a message when they are absent. This is an
unofficial, independent implementation and is not affiliated with or
endorsed by the authors of the TROP estimator.

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
