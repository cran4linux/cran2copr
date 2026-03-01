%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KWELA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Adaptive 'RT-QuIC' Classification for Complex Matrices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Extends 'RT-QuIC' (Real-Time Quaking-Induced Conversion) statistical
analysis to complex environmental matrices through hierarchical adaptive
classification. 'KWELA' is named after a deity of the Fore people of Papua
New Guinea, among whom Kuru, a notable human prion disease, was
identified. Implements a 6-layer architecture: hard gate biological
constraints, per-well adaptive scoring, separation-aware combination,
Youden-optimized cutoffs, replicate consensus, and matrix instability
detection. Features dual-mode operation (diagnostic/research),
auto-profile selection (Standard/Sensitive/Matrix-Robust), RAF integration
for artifact detection, matrix-aware baseline correction, and multiple
consensus rules. Methods include energy distance (Szekely and Rizzo (2013)
<doi:10.1016/j.jspi.2013.03.018>), CRPS (Gneiting and Raftery (2007)
<doi:10.1198/016214506000001437>), SSMD (Zhang (2007)
<doi:10.1016/j.ygeno.2007.01.005>), and Jensen-Shannon divergence (Lin
(1991) <doi:10.1109/18.61115>). This package implements methodology
currently under peer review; please contact the author before publication
using this approach. Development followed an iterative human-machine
collaboration where all algorithmic design, statistical methodologies, and
biological validation logic were conceptualized, tested, and iteratively
refined by Richard A. Feiss through repeated cycles of running
experimental data, evaluating analytical outputs, and selecting among
candidate algorithms and approaches. AI systems ('Anthropic Claude' and
'OpenAI GPT') served as coding assistants and analytical sounding boards
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
