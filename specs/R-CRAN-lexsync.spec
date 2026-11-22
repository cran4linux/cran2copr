%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lexsync
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Lexical Optimisation and Hardware-Timed Experiment Generation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-readr >= 2.0.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.7
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-readr >= 2.0.0
Requires:         R-CRAN-jsonlite >= 1.8.7
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-digest 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
A cross-platform toolkit for lexical-corpus access (bundled English,
Spanish and Mandarin lexica and a registry of citable corpora), the
matching of stimuli on several dimensions at once, deterministic
pseudoword generation, counterbalancing and the automated generation of
experiments from a declarative trial-event model, for 'PsychoPy',
'OpenSesame' and the browser ('jsPsych'). The laboratory targets send
electroencephalography onset triggers on the screen refresh that shows the
stimulus. Several paradigms are supported (factorial word contrasts,
lexical decision, priming, self-paced reading and cued categorisation),
and each design is accompanied by a materials datasheet, readable by
machines and people, for reproducibility. A 'Python' package of the same
name has the same structure and functions.

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
