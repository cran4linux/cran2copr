%global packname  LMERConvenienceFunctions
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model Selection and Post-Hoc Analysis for (G)LMER Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-LCFdata 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-LCFdata 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-mgcv 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-graphics 

%description
The main function of the package is to perform backward selection of fixed
effects, forward fitting of the random effects, and post-hoc analysis
using parallel capabilities. Other functionality includes the computation
of ANOVAs with upper- or lower-bound p-values and R-squared values for
each model term, model criticism plots, data trimming on model residuals,
and data visualization. The data to run examples is contained in package
LCF_data.

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
