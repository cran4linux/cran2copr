%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyrules
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities to Retrieve Rulelists from Model Fits, Filter, Prune, Reorder and Predict on Unseen Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.2
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-checkmate >= 2.3.1
BuildRequires:    R-CRAN-glue >= 1.7.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-partykit >= 1.2.2
BuildRequires:    R-CRAN-data.table >= 1.14.6
BuildRequires:    R-CRAN-rlang >= 1.1.3
BuildRequires:    R-CRAN-MetricsWeighted >= 1.0.3
BuildRequires:    R-CRAN-pheatmap >= 1.0.12
BuildRequires:    R-CRAN-DescTools >= 0.99.54
BuildRequires:    R-CRAN-proxy >= 0.4.27
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-tidytable >= 0.11.0
BuildRequires:    R-CRAN-generics >= 0.1.3
Requires:         R-CRAN-cli >= 3.6.2
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-checkmate >= 2.3.1
Requires:         R-CRAN-glue >= 1.7.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-partykit >= 1.2.2
Requires:         R-CRAN-data.table >= 1.14.6
Requires:         R-CRAN-rlang >= 1.1.3
Requires:         R-CRAN-MetricsWeighted >= 1.0.3
Requires:         R-CRAN-pheatmap >= 1.0.12
Requires:         R-CRAN-DescTools >= 0.99.54
Requires:         R-CRAN-proxy >= 0.4.27
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-tidytable >= 0.11.0
Requires:         R-CRAN-generics >= 0.1.3

%description
Provides a framework to work with decision rules. Rules can be extracted
from supported models, augmented with (custom) metrics using validation
data, manipulated using standard dataframe operations, reordered and
pruned based on a metric, predict on unseen (test) data. Utilities
include; Creating a rulelist manually, Exporting a rulelist as a SQL case
statement and so on. The package offers two classes; rulelist and ruleset
based on dataframe.

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
