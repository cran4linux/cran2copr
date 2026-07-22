%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LLMRagent
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reproducible Language-Model Agents for Research

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-LLMR >= 0.8.10
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-utils 
Requires:         R-CRAN-LLMR >= 0.8.10
Requires:         R-CRAN-R6 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-callr 
Requires:         R-utils 

%description
An 'R' interface built on 'LLMR' creates large language model (LLM) agents
for use as reproducible and governed research instruments. Agents pair a
model configuration with optional persona instructions. Stateful exchanges
retain conversational memory, and native 'R' functions can serve as tools
within declared budgets. Several agents can hold a turn-taking
conversation over a shared transcript, and factorial experiments across
such designs run in parallel. Model calls and tool activity are captured
in a run object, so the research record extends beyond generated text. A
study manifest hashes the design and computational apparatus without
treating sampled replies as part of its identity, and a hash-sealed
archive preserves it alongside transcripts and call records. Tool policies
record declared side effects and can limit call counts or result sizes;
calls marked for human review pause before execution. Robustness checks
assess sensitivity to prompt or model changes, while calibration against
human labels corrects estimates drawn from imperfect model labels.

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
