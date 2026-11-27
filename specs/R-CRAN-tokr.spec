%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tokr
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Process Models in the Plain-Text Language 'tok'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2

%description
Reads, checks, formats and exports process models written in 'tok', a
plain-text language for Business Process Model and Notation (BPMN) 2.0
processes with their Decision Model and Notation (DMN) decisions,
'Camunda' forms and simulation parameters. Models are checked against the
rules of BPMN 2.0, with diagnostics in English or Polish, and exported to
BPMN files with a diagram layout, Scalable Vector Graphics (SVG) pictures,
DMN and form files; they are drawn in the viewer and in 'R Markdown' and
'Quarto' documents through a 'knitr' engine. Processes are simulated as
discrete-event models, giving indicators, an event log for process mining
and a table of cases. The work is done by the 'Rust' engine of 'tok',
shared with its 'Python' package and command line tool.

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
