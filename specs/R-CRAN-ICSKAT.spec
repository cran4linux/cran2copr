%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ICSKAT
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interval-Censored Sequence Kernel Association Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rje 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rje 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-zoo 

%description
Implements the Interval-Censored Sequence Kernel Association (ICSKAT) test
for testing the association between interval-censored time-to-event
outcomes and groups of single nucleotide polymorphisms (SNPs).
Interval-censored time-to-event data occur when the event time is not
known exactly but can be deduced to fall within a given interval. For
example, some medical conditions like bone mineral density deficiency are
generally only diagnosed at clinical visits. If a patient goes for
clinical checkups yearly and is diagnosed at, say, age 30, then the onset
of the deficiency is only known to fall between the date of their age 29
checkup and the date of the age 30 checkup. Interval-censored data include
right- and left-censored data as special cases. This package also
implements the interval-censored Burden test and the ICSKATO test, which
is the optimal combination of the ICSKAT and Burden tests. Please see the
vignette for a quickstart guide. The paper describing these methods is "
Inference for Set-Based Effects in Genetic Association Studies with
Interval-Censored Outcomes" by Sun R, Zhu L, Li Y, Yasui Y, & Robison L
(Biometrics 2023, <doi:10.1111/biom.13636>).

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
