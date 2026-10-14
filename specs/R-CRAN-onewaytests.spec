%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  onewaytests
%global packver   3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2
Release:          1%{?dist}%{?buildtag}
Summary:          One-Way Tests in Independent Groups Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-wesanderson 
Requires:         R-stats 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-car 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-nortest 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-wesanderson 

%description
Performs one-way tests for independent groups designs under
homoscedasticity and heteroscedasticity. The tests described by Dag et al.
(2018) <doi:10.32614/RJ-2018-022> include one-way analysis of variance
(ANOVA), Welch's heteroscedastic F test, Welch's heteroscedastic F test
with trimmed means and Winsorized variances, Brown-Forsythe test,
Alexander-Govern test, James second-order test, and Kruskal-Wallis test.
Additional tests described by Kasikci et al. (2026)
<doi:10.32614/RJ-2026-014> include Scott-Smith test, Box F test, Johansen
F test, generalized tests equivalent to parametric bootstrap and fiducial
tests, Alvandi's F test, Alvandi's generalized p-value, approximate F
test, B square test, Cochran test, Weerahandi's generalized F test,
modified Brown-Forsythe test, adjusted Welch's heteroscedastic F test,
Welch-Aspin test, and permutation F test. The package also provides
pairwise comparisons and graphical methods, as well as Student's t test,
Welch's t test, and Mann-Whitney U test for two independent samples. It
assesses variance homogeneity and within-group normality using tests and
plots.

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
