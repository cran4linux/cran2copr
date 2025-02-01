%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robomit
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Robustness Checks for Omitted Variable Bias

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-stats 

%description
Robustness checks for omitted variable bias. The package includes
robustness checks proposed by Oster (2019). The 'robomit' package computes
i) the bias-adjusted treatment correlation or effect and ii) the degree of
selection on unobservables relative to observables (with respect to the
treatment variable) that would be necessary to eliminate the result based
on the framework by Oster (2019). The code is based on the 'psacalc'
command in 'Stata'. Additionally, 'robomit' offers a set of sensitivity
analysis and visualization functions. See Oster, E. 2019.
<doi:10.1080/07350015.2016.1227711>. Additionally, see Diegert, P.,
Masten, M. A., & Poirier, A. (2022) for a recent discussion of the topic:
<doi:10.48550/arXiv.2206.02303>.

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
