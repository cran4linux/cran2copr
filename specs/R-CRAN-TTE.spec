%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TTE
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Design and Analysis Tools for Target Trial Emulation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-utils 

%description
Design and analysis tools for target trial emulation using longitudinal
observational data. Functions are provided for checking person-period
data, expanding longitudinal data into sequentially nested trials,
estimating inverse probability weights for intention-to-treat and
per-protocol analyses, and assessing weight distributions and covariate
balance. Additional functions fit weighted pooled discrete-time outcome
models, obtain standardized risks and treatment contrasts, and estimate
weighted Kaplan-Meier and Aalen-Johansen curves. Two worked examples based
on fully synthetic data illustrate an active-comparator new-user study
comparing sodium-glucose cotransporter 2 inhibitors with dipeptidyl
peptidase-4 inhibitors and an analysis of sequentially nested trials
comparing angiotensin receptor blocker and calcium channel blocker
strategies.

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
