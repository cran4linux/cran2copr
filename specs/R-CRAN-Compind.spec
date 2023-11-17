%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Compind
%global packver   2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Composite Indicators Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Benchmarking 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-nonparaeff 
BuildRequires:    R-CRAN-smaa 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-FactoMineR 
Requires:         R-CRAN-Benchmarking 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-nonparaeff 
Requires:         R-CRAN-smaa 
Requires:         R-CRAN-np 
Requires:         R-CRAN-FactoMineR 

%description
A collection of functions to calculate Composite Indicators methods,
focusing, in particular, on the normalisation and weighting-aggregation
steps, as described in OECD Handbook on constructing composite indicators:
methodology and user guide
<https://www.oecd-ilibrary.org/economics/handbook-on-constructing-composite-indicators-methodology-and-user-guide_9789264043466-en>,
'Vidoli' and 'Fusco' and 'Mazziotta' <doi:10.1007/s11205-014-0710-y>,
'Mazziotta' and 'Pareto' (2016) <doi:10.1007/s11205-015-0998-2>, 'Van
Puyenbroeck and 'Rogge' <doi:10.1016/j.ejor.2016.07.038> and other
authors.

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
