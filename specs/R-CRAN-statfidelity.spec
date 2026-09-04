%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  statfidelity
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Audit Statistical Fidelity of AI-Mediated Official Statistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides deterministic tools for auditing whether artificial intelligence
systems preserve the numerical, semantic, contextual, temporal,
geographic, unit, provenance, revision, transformation, and uncertainty
properties of official statistics. Structured reference statistics and
machine-generated claims can be compared with non-compensatory
critical-error rules, weakest-link and geometric fidelity summaries,
provenance graphs, and portable SHA-256 proof bundles. The package also
provides bounded connectors for official Eurostat, World Bank, OECD,
United Nations SDG, United Kingdom Office for National Statistics, and
United States Bureau of Labor Statistics application programming
interfaces, plus an extensible HTTPS JSON API registry with session-only
API-key support. Prompt perturbation, statistical red-team generation,
minimal-pair tests, and starter benchmark data support reproducible
evaluation of generative, retrieval-augmented, and agentic statistical
systems. An embedded alignment layer maps claim-level controls to relevant
activities of the Generic Statistical Business Process Model (GSBPM) 5.2,
including Analyse, Disseminate, Evaluate, Quality Management, and Metadata
Management. No specific model provider is required.

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
