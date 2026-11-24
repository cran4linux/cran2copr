%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tm.hyslaw
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          'teal' Modules for Hy's Law Monitoring and Evaluation of Drug-Induced Serious Hepatotoxicity (eDISH) Plots

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-shinyjs >= 2.0.0
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-teal >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.5
BuildRequires:    R-CRAN-lifecycle >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-rtables >= 0.6.0
BuildRequires:    R-CRAN-teal.widgets >= 0.4.0
BuildRequires:    R-CRAN-shinyvalidate >= 0.1.0
BuildRequires:    R-CRAN-teal.picks >= 0.1.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-shinyjs >= 2.0.0
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-teal >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.5
Requires:         R-CRAN-lifecycle >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-rtables >= 0.6.0
Requires:         R-CRAN-teal.widgets >= 0.4.0
Requires:         R-CRAN-shinyvalidate >= 0.1.0
Requires:         R-CRAN-teal.picks >= 0.1.0

%description
Provides open-source 'teal' modules and reusable builders for exploratory
monitoring of Hy's Law (Hyman Zimmerman's observation that hepatocellular
injury with jaundice predicts severe drug-induced liver injury) from
Clinical Data Interchange Standards Consortium (CDISC) Analysis Data Model
(ADaM) subject-level analysis dataset (ADSL) and laboratory analysis
dataset (ADLB) records. Peak evaluation of Drug-Induced Serious
Hepatotoxicity (eDISH), modified evaluation of Drug-Induced Serious
Hepatotoxicity (mDISH; on-treatment peaks divided by baseline), and
cholestatic screening plots are produced, and concurrent alanine
aminotransferase (ALT) or aspartate aminotransferase (AST) plus bilirubin
elevations, with optional alkaline phosphatase (ALP) exclusion, are
classified without a study-specific drug-induced liver injury analysis
dataset (ADDILI). Table and plot builders can be called without launching
'shiny'. Hy's Law and eDISH criteria are discussed by Temple (2006)
<doi:10.1002/pds.1211>, the United States Food and Drug Administration
(2009) "Drug-Induced Liver Injury: Premarketing Clinical Evaluation"
<https://www.fda.gov/media/116737/download>, and Watkins et al. (2011)
<doi:10.2165/11586600-000000000-00000>. Baseline-scaled mDISH plots follow
the fold-baseline display in Lin et al. (2012) <doi:10.1007/BF03261982>.

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
