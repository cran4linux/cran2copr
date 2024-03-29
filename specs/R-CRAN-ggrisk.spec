%global __brp_check_rpaths %{nil}
%global packname  ggrisk
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Risk Score Plot for Cox Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-egg 
BuildRequires:    R-CRAN-do 
BuildRequires:    R-CRAN-set 
BuildRequires:    R-CRAN-cutoff 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-nomogramFormula 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-egg 
Requires:         R-CRAN-do 
Requires:         R-CRAN-set 
Requires:         R-CRAN-cutoff 
Requires:         R-grid 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-nomogramFormula 
Requires:         R-CRAN-reshape2 

%description
The risk plot may be one of the most commonly used figures in tumor
genetic data analysis. We can conclude the following two points: Comparing
the prediction results of the model with the real survival situation to
see whether the survival rate of the high-risk group is lower than that of
the low-level group, and whether the survival time of the high-risk group
is shorter than that of the low-risk group. The other is to compare the
heat map and scatter plot to see the correlation between the predictors
and the outcome.

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
