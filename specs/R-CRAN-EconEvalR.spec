%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EconEvalR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Economic Evaluation Methods for Cost-Benefit, Partial Budgeting, and Cost-Effectiveness Analyses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.2
BuildRequires:    R-CRAN-mgcv 
Requires:         R-CRAN-cli >= 3.6.2
Requires:         R-CRAN-mgcv 

%description
Provides functions for economic evaluation, including Cost-Benefit
Analysis, Benefit-Cost Ratio, Net Present Value, Internal Rate of Return,
Partial Budgeting, Budget Impact Analysis, Cost-Effectiveness Analysis,
Decision Tree Analysis, One-Way, Two-Way, Multi-Way, and Probabilistic
Sensitivity Analyses, Expected Value of Perfect Information, and Expected
Value of Partial Perfect Information. The implemented methods are based on
established approaches in economic evaluation and decision analysis; see
Drummond et al. (2015, ISBN:9780199665884), Briggs et al. (2006,
ISBN:9780198526629), Boardman et al. (2018, ISBN:9781108415996), and van
Hout et al. (1994) <doi:10.1002/hec.4730030505>. The package produces
summaries, graphical displays, and reproducible workflows for applications
in veterinary science, agriculture, public health, epidemiology, health
economics, and related fields.

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
