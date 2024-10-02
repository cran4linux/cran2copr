%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geneHummus
%global packver   1.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          A Pipeline to Define Gene Families in Legumes and Beyond

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 3.3
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-rentrez >= 1.2.1
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-utils 
Requires:         R-CRAN-curl >= 3.3
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-rentrez >= 1.2.1
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-utils 

%description
A pipeline with high specificity and sensitivity in extracting proteins
from the RefSeq database (National Center for Biotechnology Information).
Manual identification of gene families is highly time-consuming and
laborious, requiring an iterative process of manual and computational
analysis to identify members of a given family. The pipelines implements
an automatic approach for the identification of gene families based on the
conserved domains that specifically define that family. See Die et al.
(2018) <doi:10.1101/436659> for more information and examples.

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
