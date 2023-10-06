%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jmv
%global packver   2.4.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.9
Release:          1%{?dist}%{?buildtag}
Summary:          The 'jamovi' Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-car >= 3.0.0
BuildRequires:    R-CRAN-jmvcore >= 2.4.2
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-psych >= 1.7.5
BuildRequires:    R-CRAN-emmeans >= 1.4.2
BuildRequires:    R-CRAN-afex >= 0.28.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-PMCMR 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-CRAN-vcdExtra 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-mvnormtest 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-car >= 3.0.0
Requires:         R-CRAN-jmvcore >= 2.4.2
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-psych >= 1.7.5
Requires:         R-CRAN-emmeans >= 1.4.2
Requires:         R-CRAN-afex >= 0.28.0
Requires:         R-CRAN-R6 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-PMCMR 
Requires:         R-CRAN-vcd 
Requires:         R-CRAN-vcdExtra 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-mvnormtest 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 

%description
A suite of common statistical methods such as descriptives, t-tests,
ANOVAs, regression, correlation matrices, proportion tests, contingency
tables, and factor analysis. This package is also useable from the
'jamovi' statistical spreadsheet (see <https://www.jamovi.org> for more
information).

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
