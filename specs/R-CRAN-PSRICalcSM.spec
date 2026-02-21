%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PSRICalcSM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Plant Stress Response Index Calculator - Softmax Method

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch

%description
Implements the softmax aggregation method for calculating Plant Stress
Response Index (PSRI) from time-series germination data under
environmental stressors including prions, xenobiotics, osmotic stress,
heavy metals, and chemical contaminants. Provides zero-robust PSRI
computation through adaptive softmax weighting of germination components
(Maximum Stress-adjusted Germination, Maximum Rate of Germination,
complementary Mean Time to Germination, and Radicle Vigor Score),
eliminating the zero-collapse failure mode of the geometric mean approach
implemented in 'PSRICalc'. Includes perplexity-based temperature parameter
calibration and modular component functions for transparent germination
analysis. Built on the methodological foundation of the Osmotic Stress
Response Index (OSRI) framework developed by Walne et al. (2020)
<doi:10.1002/agg2.20087>. Note: This package implements methodology
currently under peer review. Please contact the author before publication
using this approach. Development followed an iterative human-machine
collaboration where all algorithmic design, statistical methodologies, and
biological validation logic were conceptualized, tested, and iteratively
refined by Richard A. Feiss through repeated cycles of running
experimental data, evaluating analytical outputs, and selecting among
candidate algorithms and approaches. AI systems (Anthropic Claude and
OpenAI GPT) served as coding assistants and analytical sounding boards
under continuous human direction. The selection of statistical methods,
evaluation of biological plausibility, and all final methodology decisions
were made by the human author. AI systems did not independently originate
algorithms, statistical approaches, or scientific methodologies.

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
