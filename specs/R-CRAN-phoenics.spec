%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phoenics
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Pathways Longitudinal and Differential Analysis in Metabolomics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-blme 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-blme 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 

%description
Perform a differential analysis at pathway level based on metabolite
quantifications and information on pathway metabolite composition. The
method is based on a Principal Component Analysis step and on a linear
mixed model. Automatic query of metabolic pathways is also implemented.

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
