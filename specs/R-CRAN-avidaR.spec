%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  avidaR
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Computational Biologist’s Toolkit To Get Data From 'avidaDB'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 5.0.2
BuildRequires:    R-CRAN-tibble >= 3.0.6
BuildRequires:    R-CRAN-httr >= 1.4.2
BuildRequires:    R-CRAN-readr >= 1.4.0
BuildRequires:    R-CRAN-xml2 >= 1.3.2
BuildRequires:    R-CRAN-tidyr >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.6
BuildRequires:    R-CRAN-circlize >= 0.4.11
BuildRequires:    R-CRAN-base64enc >= 0.1.3
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-curl >= 5.0.2
Requires:         R-CRAN-tibble >= 3.0.6
Requires:         R-CRAN-httr >= 1.4.2
Requires:         R-CRAN-readr >= 1.4.0
Requires:         R-CRAN-xml2 >= 1.3.2
Requires:         R-CRAN-tidyr >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.0.6
Requires:         R-CRAN-circlize >= 0.4.11
Requires:         R-CRAN-base64enc >= 0.1.3
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-R6 

%description
Easy-to-use tools for performing complex queries on 'avidaDB', a semantic
database that stores genomic and transcriptomic data of self-replicating
computer programs (known as digital organisms) that mutate and evolve
within a user-defined computational environment.

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
