%global __brp_check_rpaths %{nil}
%global packname  powerpkg
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Power Analyses for the Affected Sib Pair and the TDT Design

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-tcltk 
Requires:         R-tcltk 

%description
There are two main functions: (1) To estimate the power of testing for
linkage using an affected sib pair design, as a function of the recurrence
risk ratios. We will use analytical power formulae as implemented in R.
These are based on a Mathematica notebook created by Martin Farrall. (2)
To examine how the power of the transmission disequilibrium test (TDT)
depends on the disease allele frequency, the marker allele frequency, the
strength of the linkage disequilibrium, and the magnitude of the genetic
effect. We will use an R program that implements the power formulae of
Abel and Muller-Myhsok (1998). These formulae allow one to quickly compute
power of the TDT approach under a variety of different conditions. This R
program was modeled on Martin Farrall's Mathematica notebook.

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
