%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  naniar
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Structures, Summaries, and Visualisations for Missing Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-norm 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-visdat 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-UpSetR 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-norm 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-visdat 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-UpSetR 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-lifecycle 

%description
Missing values are ubiquitous in data and need to be explored and handled
in the initial stages of analysis. 'naniar' provides data structures and
functions that facilitate the plotting of missing values and examination
of imputations. This allows missing data dependencies to be explored with
minimal deviation from the common work patterns of 'ggplot2' and tidy
data. The work is fully discussed at Tierney & Cook (2023)
<doi:10.18637/jss.v105.i07>.

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
