%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LISTC
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pivot-Style Statistical Tables for Large-Scale Assessment Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-yaml 

%description
Turns assessment and survey sample data (demographics, scores, sampling
weights, ability estimates with individual item response theory standard
errors, replicate weights and plausible values) into fully customizable
pivot-style statistical tables in which every cell carries a
design-appropriate standard error. Provides weighted means, proportions
above cut scores, proficiency-level percentages and quantiles; sampling
variance via linearization, Woodruff (1952)
<doi:10.1080/01621459.1952.10483443> intervals for quantiles, or balanced
repeated replication and jackknife replicate weights including Fay's
method; measurement variance via delta-method propagation of individual
standard errors or Rubin (1987) <doi:10.1002/9780470316696> combination
across plausible values. Imports data from 'CSV', 'Excel', 'SPSS', 'SAS',
'Stata' and item response theory software person files ('Winsteps',
'ConQuest'); a configuration-file interface serves non-programmers and
automation; results export to formatted 'Excel', 'JSON' and standalone
'HTML' reports with rule-based plain-language interpretation.

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
