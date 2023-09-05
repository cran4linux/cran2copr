%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AteMeVs
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Average Treatment Effects with Measurement Error and Variable Selection for Confounders

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ncvreg 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ncvreg 

%description
A recent method proposed by Yi and Chen (2023)
<doi:10.1177/09622802221146308> is used to estimate the average treatment
effects using noisy data containing both measurement error and spurious
variables. The package 'AteMeVs' contains a set of functions that provide
a step-by-step estimation procedure, including the correction of the
measurement error effects, variable selection for building the model used
to estimate the propensity scores, and estimation of the average treatment
effects. The functions contain multiple options for users to implement,
including different ways to correct for the measurement error effects,
distinct choices of penalty functions to do variable selection, and
various regression models to characterize propensity scores.

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
