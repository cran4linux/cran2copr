%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eudract
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Creates Safety Results Summary in XML to Upload to EudraCT, or ClinicalTrials.gov

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-xslt 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-xslt 

%description
The remit of the European Clinical Trials Data Base (EudraCT
<https://eudract.ema.europa.eu/> ), or ClinicalTrials.gov
<https://clinicaltrials.gov/>, is to provide open access to summaries of
all registered clinical trial results; thus aiming to prevent
non-reporting of negative results and provide open-access to results to
inform future research. The amount of information required and the format
of the results, however, imposes a large extra workload at the end of
studies on clinical trial units. In particular, the
adverse-event-reporting component requires entering: each unique
combination of treatment group and safety event; for every such event
above, a further 4 pieces of information (body system, number of
occurrences, number of subjects, number exposed) for non-serious events,
plus an extra three pieces of data for serious adverse events (numbers of
causally related events, deaths, causally related deaths). This package
prepares the required statistics needed by EudraCT and formats them into
the precise requirements to directly upload an XML file into the web
portal, with no further data entry by hand.

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
