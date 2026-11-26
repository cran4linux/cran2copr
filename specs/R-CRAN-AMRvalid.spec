%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AMRvalid
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Population-Aware Evaluation of Antimicrobial Resistance Predictions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-AMR >= 3.0.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-AMR >= 3.0.0
Requires:         R-stats 
Requires:         R-utils 

%description
Evaluates antimicrobial resistance phenotype predictions made by external
models and rule-based tools against phenotypic reference results,
accounting for the population structure of bacterial isolates. Provides a
documented data contract and input validation; classification and
probability metrics and antimicrobial susceptibility testing agreement
metrics (categorical agreement, very major, major and minor errors,
essential agreement) per species and antimicrobial; checks for overlap
between training and test isolates; performance by genomic distance to the
training data; cluster bootstrap intervals and paired model comparisons;
calibration; prevalence-adjusted predictive values; and reports aligned
with the TRIPOD+AI checklist (Collins et al. (2024)
<doi:10.1136/bmj-2023-078378>). Organism and antimicrobial identifiers use
the classes of the 'AMR' package. Models are not trained inside the
package.

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
