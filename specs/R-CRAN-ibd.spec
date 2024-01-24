%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ibd
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Incomplete Block Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-multcomp 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-car 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-multcomp 

%description
A collection of several utility functions related to binary incomplete
block designs. Contains function to generate A- and D-efficient binary
incomplete block designs with given numbers of treatments, number of
blocks and block size. Contains function to generate an incomplete block
design with specified concurrence matrix. There are functions to generate
balanced treatment incomplete block designs and incomplete block designs
for test versus control treatments comparisons with specified concurrence
matrix. Allows performing analysis of variance of data and computing
estimated marginal means of factors from experiments using a connected
incomplete block design. Tests of hypothesis of treatment contrasts in
incomplete block design set up is supported.

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
