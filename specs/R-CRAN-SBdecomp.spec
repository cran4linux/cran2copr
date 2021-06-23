%global __brp_check_rpaths %{nil}
%global packname  SBdecomp
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of the Proportion of SB Explained by Confounders

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-twang 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-survey 
Requires:         R-stats 
Requires:         R-CRAN-twang 
Requires:         R-graphics 
Requires:         R-CRAN-survey 

%description
Uses parametric and nonparametric methods to quantify the proportion of
the estimated selection bias (SB) explained by each observed confounder
when estimating propensity score weighted treatment effects. Parast, L and
Griffin, BA (2020). "Quantifying the Bias due to Observed Individual
Confounders in Causal Treatment Effect Estimates". Statistics in Medicine,
39(18): 2447- 2476 <doi: 10.1002/sim.8549>.

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
