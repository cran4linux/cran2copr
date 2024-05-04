%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reflectR
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Scoring of the Cognitive Reflection Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-stringr 

%description
A tool for researchers and psychologists to automatically code open-ended
responses to the Cognitive Reflection Test (CRT), a widely used class of
tests in cognitive science and psychology for assessing an individual's
propensity to override an incorrect gut response and engage in further
reflection to find a correct answer. This package facilitates the
standardization of Cognitive Reflection Test responses analysis across
large datasets in cognitive psychology, decision-making, and related
fields. By automating the coding process, it not only reduces manual
effort but also aims to reduce the variability introduced by subjective
interpretation of open-ended responses, contributing to a more consistent
and reliable analysis. 'reflectR' supports automatic coding and machine
scoring for the original English-language version of CRT (Frederick, 2005)
<doi:10.1257/089533005775196732>, as well as for CRT4 and CRT7, 4- and
7-item versions, respectively (Toplak et al., 2014)
<doi:10.1080/13546783.2013.844729>, for the CRT-long version built via
Item Response Theory by Primi and colleagues (2016)
<doi:10.1002/bdm.1883>, and for CRT-2 by Thomson & Oppenheimer (2016)
<doi:10.1017/s1930297500007622>. Note: While 'reflectR' draws inspiration
from the principles and scientific literature underlying the different
versions of the Cognitive Reflection Test, it has been independently
developed and does not hold any affiliation with any of the original
authors. The development of this package benefited significantly from the
kind insight and suggestion provided by Dr. Keela Thomson, whose
contribution is gratefully acknowledged. Additional gratitude is extended
to Dr. Paolo Giovanni Cicirelli, Prof. Marinella Paciello, Dr. Carmela
Sportelli, and Prof. Francesca D'Errico, whose contributions highlighted
the significant importance and practical relevance of this construct in
personality, social, and cognitive research.

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
