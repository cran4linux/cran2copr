%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  canaper
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Categorical Analysis of Neo- And Paleo-Endemism

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-assertr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-phyloregion 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-assertr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-phyloregion 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-vegan 

%description
Provides functions to analyze the spatial distribution of biodiversity, in
particular categorical analysis of neo- and paleo-endemism (CANAPE) as
described in Mishler et al (2014) <doi:10.1038/ncomms5473>. 'canaper'
conducts statistical tests to determine the types of endemism that occur
in a study area while accounting for the evolutionary relationships of
species.

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
