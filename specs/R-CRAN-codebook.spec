%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  codebook
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Codebooks from Metadata Encoded in Dataset Attributes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-haven >= 2.3.0
BuildRequires:    R-CRAN-skimr >= 2.1.0
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-forcats >= 0.4.0
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rmdpartials 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-likert 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-labeling 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-future 
Requires:         R-CRAN-haven >= 2.3.0
Requires:         R-CRAN-skimr >= 2.1.0
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-forcats >= 0.4.0
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-rmdpartials 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-likert 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-labeling 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-future 

%description
Easily automate the following tasks to describe data frames: Summarise the
distributions, and labelled missings of variables graphically and using
descriptive statistics. For surveys, compute and summarise reliabilities
(internal consistencies, retest, multilevel) for psychological scales.
Combine this information with metadata (such as item labels and labelled
values) that is derived from R attributes. To do so, the package relies on
'rmarkdown' partials, so you can generate HTML, PDF, and Word documents.
Codebooks are also available as tables (CSV, Excel, etc.) and in JSON-LD,
so that search engines can find your data and index the metadata. The
metadata are also available at your fingertips via RStudio Addins.

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
