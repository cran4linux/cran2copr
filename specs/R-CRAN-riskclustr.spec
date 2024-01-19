%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  riskclustr
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Study Etiologic Heterogeneity

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mlogit 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-mlogit 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-Matrix 

%description
A collection of functions related to the study of etiologic heterogeneity
both across disease subtypes and across individual disease markers. The
included functions allow one to quantify the extent of etiologic
heterogeneity in the context of a case-control study, and provide p-values
to test for etiologic heterogeneity across individual risk factors. Begg
CB, Zabor EC, Bernstein JL, Bernstein L, Press MF, Seshan VE (2013)
<doi:10.1002/sim.5902>.

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
