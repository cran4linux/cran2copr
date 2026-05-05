%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cosmic
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Ordinal Stereotype Model for Incident-Level Comparison

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-posterior 
Requires:         R-stats 

%description
Implements the Conditional Ordinal Stereotype Model for Incident-Level
Comparison (COSMIC), a method for analyzing ordinal outcomes observed
across multiple actors within shared events. The model uses a conditional
likelihood to remove event-level confounding and estimate actor-specific
propensities relative to their peers. Efficient computation is achieved
via a dynamic programming algorithm for the Poisson-multinomial
normalization term, enabling scalable estimation with Markov chain Monte
Carlo. The package provides tools for data preparation, model fitting
using Stan, and extraction of posterior summaries for comparative
inference. Estimation of police officer propensity to escalate force is
the primary motivation for the model. For more details see Ridgeway (2026)
"A Conditional Ordinal Stereotype Model to Estimate Police Officers’
Propensity to Escalate Force" <doi:10.1080/01621459.2025.2597050>.

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
