%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tdarec
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A 'recipes' Extension for Persistent Homology and Its Vectorizations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-vctrs >= 0.5.0
BuildRequires:    R-CRAN-recipes >= 0.1.17
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-vctrs >= 0.5.0
Requires:         R-CRAN-recipes >= 0.1.17
Requires:         R-CRAN-dials 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 

%description
Topological data analytic methods in machine learning rely on
vectorizations of the persistence diagrams that encode persistent
homology, as surveyed by Ali &al (2000) <doi:10.48550/arXiv.2212.09703>.
Persistent homology can be computed using 'TDA' and 'ripserr' and
vectorized using 'TDAvec'.  The Tidymodels package collection modularizes
machine learning in R for straightforward extensibility; see Kuhn & Silge
(2022, ISBN:978-1-4920-9644-3).  These 'recipe' steps and 'dials' tuners
make efficient algorithms for computing and vectorizing persistence
diagrams available for Tidymodels workflows.

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
