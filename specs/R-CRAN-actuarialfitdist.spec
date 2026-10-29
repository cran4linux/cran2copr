%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  actuarialfitdist
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Actuarial Severity Fitting with Limits and Deductibles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits actuarial claim severity distributions to ground-up loss data while
accounting for deductible truncation, policy-limit censoring, observation
weights, optional severity scaling variables, and fixed parameters.
Supports single-family and spliced body-tail models, candidate-model
comparison, limited expected values, loss elimination ratios, increased
limits factors, deductible and limit rating factors, valuation or
depreciation adjustments, simulation, diagnostics, and uncertainty
estimation. The package is designed for property and casualty actuarial
applications in which analysts fit ground-up severity and translate the
fitted distribution into pricing factors for limits, deductibles, and
valuation provisions. For background on statistical severity modeling, see
Klugman, Panjer, and Willmot (2019, ISBN:9781119523789), "Loss Models:
From Data to Decisions", 5th edition.

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
