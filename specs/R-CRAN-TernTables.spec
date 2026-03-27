%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TernTables
%global packver   1.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.4
Release:          1%{?dist}%{?buildtag}
Summary:          Publication-Ready Summary Tables and Statistical Testing for Clinical Research

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-flextable >= 0.9.0
BuildRequires:    R-CRAN-officer >= 0.4.6
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-epitools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-flextable >= 0.9.0
Requires:         R-CRAN-officer >= 0.4.6
Requires:         R-CRAN-cli 
Requires:         R-CRAN-epitools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-writexl 

%description
Generates publication-ready summary tables for clinical research,
supporting descriptive summaries and comparisons across two or three
groups. The package streamlines the analytical workflow by detecting
variable types and applying appropriate statistical tests (Welch t-test,
Wilcoxon rank-sum, Welch ANOVA, Kruskal-Wallis, Chi-squared, or Fisher's
exact test). Results are formatted as 'tibble' objects and can be exported
to 'Word' or 'Excel' using the 'officer', 'flextable', and 'writexl'
packages. Optional pairwise post-hoc testing for three-group comparisons
(Games-Howell and Dunn's test) is available via the 'rstatix' package.
Example data are derived from the landmark adjuvant colon cancer trial
described in Moertel et al. (1990) <doi:10.1056/NEJM199002083220602>.

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
