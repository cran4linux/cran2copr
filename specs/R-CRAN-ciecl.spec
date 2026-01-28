%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ciecl
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          International Classification of Diseases 'ICD-10'/'ICD-11' for Chile

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-comorbidity 
BuildRequires:    R-CRAN-gt 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-comorbidity 
Requires:         R-CRAN-gt 

%description
Tools for working with the International Classification of Diseases
('ICD-10' Chile official 'MINSAL'/'DEIS' v2018). Includes optimized 'SQL'
search with 'SQLite', fuzzy matching of medical terms (Jaro-Winkler),
Charlson and Elixhauser comorbidity calculation, 'WHO' 'ICD-11' 'API'
integration, and hierarchical code validation. Data from Centro FIC Chile
'DEIS' <https://deis.minsal.cl/centrofic/>.

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
