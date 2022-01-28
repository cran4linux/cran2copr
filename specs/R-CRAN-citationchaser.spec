%global __brp_check_rpaths %{nil}
%global packname  citationchaser
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Perform Forward and Backwards Chasing in Evidence Syntheses

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-maditr 
BuildRequires:    R-CRAN-MESS 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-maditr 
Requires:         R-CRAN-MESS 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-data.table 

%description
In searching for research articles, we often want to obtain lists of
references from across studies, and also obtain lists of articles that
cite a particular study. In systematic reviews, this supplementary search
technique is known as 'citation chasing': forward citation chasing looks
for all records citing one or more articles of known relevance; backward
citation chasing looks for all records referenced in one or more articles.
Traditionally, this process would be done manually, and the resulting
records would need to be checked one-by-one against included studies in a
review to identify potentially relevant records that should be included in
a review. This package contains functions to automate this process by
making use of the Lens.org API. An input article list can be used to
return a list of all referenced records, and/or all citing records in the
Lens.org database (consisting of PubMed, PubMed Central, CrossRef,
Microsoft Academic Graph and CORE; <https://www.lens.org>).

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
