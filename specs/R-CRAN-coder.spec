%global packname  coder
%global packver   0.13.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.5
Release:          1%{?dist}%{?buildtag}
Summary:          Deterministic Categorization of Items Based on External Code Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-decoder 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-decoder 
Requires:         R-CRAN-generics 
Requires:         R-methods 
Requires:         R-CRAN-tibble 

%description
Fast categorization of items based on external code data identified by
regular expressions. A typical use case considers patient with medically
coded data, such as codes from the International Classification of
Diseases ('ICD') or the Anatomic Therapeutic Chemical ('ATC')
classification system. Functions of the package relies on a triad of
objects: (1) case data with unit id:s and possible dates of interest; (2)
external code data for corresponding units in (1) and with optional dates
of interest and; (3) a classification scheme ('classcodes' object) with
regular expressions to identify and categorize relevant codes from (2). It
is easy to introduce new classification schemes ('classcodes' objects) or
to use default schemes included in the package. Use cases includes patient
categorization based on 'comorbidity indices' such as 'Charlson',
'Elixhauser', 'RxRisk V', or the 'comorbidity-polypharmacy' score (CPS),
as well as adverse events after hip and knee replacement surgery.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
