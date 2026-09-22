%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DMAR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Design, Measurement, and Analysis in R (DMAR)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-generics 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Methods for design, measurement, and analysis, with the aim of being user
friendly yet methodologically sound. 'DMAR' (pronounced "Dee-Mar")
implements many advanced and nonstandard methods and makes them available
for straightforward use, with interfaces, defaults, and documentation that
are consistent across the package and grounded in the methodological
literature, in support of sound and reproducible results. The package
emphasizes effect size estimation with confidence intervals; sample size
planning through accuracy in parameter estimation (AIPE) and power
analysis (including composite power for designs whose conclusions require
several results to hold at once), with minimum risk, sequential, and
equivalence frameworks; reliability, agreement, and measurement more
broadly, from coefficient omega with confidence intervals to measurement
invariance; factor analysis and structural equation modeling, in which
constructs, latent variables measured by multiple indicators, are modeled
directly, with confirmatory factor analysis, convergent and discriminant
validity, and sample size planning for structural equation models;
mediation analysis, from the simple mediation model with bootstrap
intervals to likelihood ratio tests of arbitrary indirect effects by
model-based constrained optimization (MBCO), with multiple groups and the
probing of moderated mediation; equivalence and noninferiority testing;
meta-analysis; repeated measures, multivariate, ANOVA, and ANCOVA designs;
and inference grounded in model comparison throughout. Measurement is
approached from a psychometric perspective, and although many of the
methods grew up in human-centered research, they apply broadly across the
empirical sciences. Much of what is implemented traces to the author's
methodological work, interests, and collaborations. 'DMAR' is a more
modern, more general, and greatly expanded reimagining of the 'MBESS'
package (Kelley, 2007a, <doi:10.18637/jss.v020.i08>; 2007b,
<doi:10.3758/BF03192993>), which has been on CRAN for more than two
decades and remains available there in stable form. Most functions accept
either raw data or the summary statistics typically reported in published
articles, so an analysis can be reproduced from a paper without the
original data, which is useful both for extending a published analysis and
for meta-analytic work. The estimation, inference, and planning functions
return one consistently formatted data frame per function that composes
with the broader R ecosystem, and confidence intervals are reported
alongside effect sizes throughout, as best practice recommends.
Researchers who have data and a question but who are not R experts will
find the package approachable, while methodologists gain access to
advanced and nonstandard methods, including tables of critical values not
available elsewhere.

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
