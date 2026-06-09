%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easyRasch2
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Psychometric Analysis with Rasch Measurement Theory

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-psychotools >= 0.7.3
BuildRequires:    R-CRAN-eRm 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-psychotools >= 0.7.3
Requires:         R-CRAN-eRm 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-mirt 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rlang 

%description
Streamlines reproducible Rasch measurement theory analyses for ordinal
item-response data, combining estimation routines from 'eRm',
'psychotools', 'mirt', 'iarm', and 'lavaan' with consistent diagnostic,
plotting, and reporting layers. Covers the four basic psychometric
criteria summarised by Christensen et al. (2021) <doi:10.1111/sms.13908>
-- unidimensionality, local independence, ordered response category
thresholds, and invariance across subgroups -- together with item fit,
targeting, reliability, category functioning, and descriptive
item-response plots. A distinguishing feature is the use of
simulation-based critical values to replace rule-of-thumb cutoffs for
conditional infit mean-square, Yen's Q3 local-dependence statistic, the
largest residual-PCA eigenvalue, and ordinal CFA fit indices. Outputs are
knitr::kable() tables and 'ggplot2' figures suitable for direct inclusion
in 'Quarto' and 'R Markdown' reports.

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
