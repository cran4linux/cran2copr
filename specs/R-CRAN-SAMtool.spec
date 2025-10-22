%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SAMtool
%global packver   1.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stock Assessment Methods Toolkit

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-MSEtool >= 3.0.0
BuildRequires:    R-CRAN-TMB >= 1.9.0
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-MSEtool >= 3.0.0
Requires:         R-CRAN-TMB >= 1.9.0
Requires:         R-CRAN-abind 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gplots 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-snowfall 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-vars 

%description
Simulation tools for closed-loop simulation are provided for the 'MSEtool'
operating model to inform data-rich fisheries. 'SAMtool' provides a
conditioning model, assessment models of varying complexity with
standardized reporting, model-based management procedures, and diagnostic
tools for evaluating assessments inside closed-loop simulation.

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
