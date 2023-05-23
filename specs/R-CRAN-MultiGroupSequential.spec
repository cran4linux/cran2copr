%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultiGroupSequential
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Group-Sequential Procedures with Multiple Hypotheses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-OpenMx 
BuildRequires:    R-CRAN-hommel 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-OpenMx 
Requires:         R-CRAN-hommel 

%description
It is often challenging to strongly control the family-wise type-1 error
rate in the group-sequential trials with multiple endpoints (hypotheses).
The inflation of type-1 error rate comes from two sources (S1) repeated
testing individual hypothesis and (S2) simultaneous testing multiple
hypotheses. The 'MultiGroupSequential' package is intended to help
researchers to tackle this challenge. The procedures provided include the
sequential procedures described in Luo and Quan (2023)
<doi:10.1080/19466315.2023.2191989> and the graphical procedure proposed
by Maurer and Bretz (2013) <doi:10.1080/19466315.2013.807748>. Luo and
Quan (2013) describes three procedure and the functions to implement these
procedures are (1) seqgspgx() implements a sequential graphical procedure
based on the group-sequential p-values; (2) seqgsphh() implements a
sequential Hochberg/Hommel procedure based on the group-sequential
p-values; and (3) seqqvalhh() implements a sequential Hochberg/Hommel
procedure based on the q-values. In addition, seqmbgx() implements the
sequential graphical procedure described in Maurer and Bretz (2013).

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
