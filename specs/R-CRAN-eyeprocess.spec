%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eyeprocess
%global packver   0.11.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.1
Release:          1%{?dist}%{?buildtag}
Summary:          Harmonize Eye-Tracking, Pupillometry, Biometrics, and Psychometric Process Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Provides an extensible, vendor-neutral framework for importing,
validating, harmonizing, transforming, visualizing, and modelling
eye-tracking, pupillometry, behavioural, and biometric process data. The
package uses explicit timebase and coordinate-space registries, preserves
native fields and provenance, and offers first-class adapters for
Gazepoint Analysis and Gazepoint Biometrics exports alongside generic and
vendor-specific importers. Downstream tools support trial and area of
interest reconstruction, signal-quality auditing, feature derivation,
scanpath analysis, response-time and item-response workflows, and optional
psychometric modelling engines. An integrated Gazepoint workflow produces
quality-control evidence, media-trial reconstruction, plots,
analysis-ready process tables, item response theory (IRT)-ready response
structures, and reproducible reports. Brain Imaging Data Structure (BIDS)
interoperability for eye-tracking and validation-release infrastructure
support disk-backed storage, independent multi-vendor evidence, grouped
validation, simulation calibration, model-equivalence audits, and
explicitly experimental advanced psychometric process models.
Research-scale infrastructure adds deterministic resumable Monte Carlo
execution, atomic validation checkpoints, explicit advanced-model
promotion gates, independent multi-vendor evidence registries, stable
object contracts, partitioned disk-backed storage, optional probabilistic
engines, and a fully synthetic multimodal benchmark for reproducibility
testing. The measurement-intelligence programme adds probabilistic and
compositional area of interest (AOI) analysis, measurement-uncertainty
propagation, calibration and device-transportability audits, process
reliability, phase-amplitude pupil registration, informative-missingness
sensitivity, temporal and spatial process models, item-bank decision
optimization, fairness monitoring, conditional process reference
distributions, and evidence-provenance graphs.

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
