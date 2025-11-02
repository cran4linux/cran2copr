%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  factorH
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multifactor Nonparametric Rank-Based ANOVA with Post Hoc Tests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rcompanion 
BuildRequires:    R-CRAN-FSA 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-rcompanion 
Requires:         R-CRAN-FSA 
Requires:         R-CRAN-car 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rlang 

%description
Multifactor nonparametric analysis of variance based on ranks. Builds on
the Kruskal-Wallis H test and its 2x2 Scheirer-Ray-Hare extension to
handle any factorial designs. Provides effect sizes, Dunn-Bonferroni
pairwise-comparison matrices, and simple-effects analyses. Tailored for
psychology and the social sciences, with beginner-friendly R syntax and
outputs that can be dropped into journal reports. Includes helpers to
export tab-separated results and compact tables of descriptive statistics
(to APA-style reports).

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
