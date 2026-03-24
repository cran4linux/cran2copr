%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wcvpmatch
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Taxonomic Name Reconciliation Against the 'WCVP' Backbone

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fozziejoin 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fozziejoin 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Standardizes and reconciles scientific plant names against a World
Checklist of Vascular Plants ('WCVP')-style taxonomic backbone. The
package parses names into taxonomic components and applies staged exact
and fuzzy matching for binomial and trinomial inputs, including
infraspecific rank-aware checks. It also returns accepted-name context and
row-level matching flags to support reproducible, auditable preprocessing
for downstream biodiversity, spatial, and trait analyses. A user-supplied
backbone can be passed through 'target_df'; when the optional companion
package 'wcvpdata' is installed, its default checklist can also be used.

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
