%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MLMusingR
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Practical Multilevel Modeling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-performance 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-WeMix 
Requires:         R-CRAN-lme4 
Requires:         R-stats 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-performance 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-WeMix 

%description
Convenience functions and datasets to be used with Practical Multilevel
Modeling using R. The package includes functions for calculating group
means, group mean centered variables, and displaying some basic missing
data information. A function for computing robust standard errors for
linear mixed models based on Liang and Zeger (1986)
<doi:10.1093/biomet/73.1.13> and Bell and 'McCaffrey' (2002)
<https://www150.statcan.gc.ca/n1/en/pub/12-001-x/2002002/article/9058-eng.pdf?st=NxMjN1YZ>
is included as well as a function for checking for level-one
homoskedasticity (Raudenbush & Bryk, 2002, ISBN:076191904X).

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
