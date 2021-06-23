%global __brp_check_rpaths %{nil}
%global packname  MPGE
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Two-Step Approach to Testing Overall Effect of Gene-Environment Interaction for Multiple Phenotypes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-car 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-utils 

%description
Interaction between a genetic variant (e.g., a single nucleotide
polymorphism) and an environmental variable (e.g., physical activity) can
have a shared effect on multiple phenotypes (e.g., blood lipids). We
implement a two-step method to test for an overall interaction effect on
multiple phenotypes. In first step, the method tests for an overall
marginal genetic association between the genetic variant and the
multivariate phenotype. The genetic variants which show an evidence of
marginal overall genetic effect in the first step are prioritized while
testing for an overall gene-environment interaction effect in the second
step. Methodology is available from: A Majumdar, KS Burch, S Sankararaman,
B Pasaniuc, WJ Gauderman, JS Witte (2020) <doi:10.1101/2020.07.06.190256>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
