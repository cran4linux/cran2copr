%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BLMEngineInR
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Biotic Ligand Model Engine

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-methods 
Requires:         R-CRAN-openxlsx 
Requires:         R-utils 

%description
A chemical speciation and toxicity prediction model for the toxicity of
metals to aquatic organisms. The Biotic Ligand Model (BLM) engine was
originally programmed in 'PowerBasic' by Robert Santore and others. The
main way the BLM can be used is to predict the toxicity of a metal to an
organism with a known sensitivity (i.e., it is known how much of that
metal must accumulate on that organism's biotic ligand to cause a
physiological effect in a certain percentage of the population, such as a
20%% loss in reproduction or a 50%% mortality rate). The second way the BLM
can be used is to estimate the chemical speciation of the metal and other
constituents in water, including estimating the amount of metal
accumulated to an organism's biotic ligand during a toxicity test. In the
first application of the BLM, the amount of metal associated with a
toxicity endpoint, or regulatory limit will be predicted, while in the
second application, the amount of metal is known and the portions of that
metal that exist in various forms will be determined. This version of the
engine has been re-structured to perform the calculations in a different
way that will make it more efficient in R, while also making it more
flexible and easier to maintain in the future. Because of this, it does
not currently match the desktop model exactly, but we hope to improve this
comparability in the future.

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
