%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  causalMed
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric G-Formula for Longitudinal Mediation and Total Effects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.1
Requires:         R-core >= 3.5.1
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progressr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progressr 

%description
Causal mediation analysis for longitudinal data with time-varying
exposures, mediators and confounders, covering both interventional (Lin et
al. (2017) <doi:10.1002/sim.7426>) and natural (Zheng and van der Laan
(2017) <doi:10.1515/jci-2016-0006>) direct and indirect effects.
Estimation uses the parametric g-formula (Robins (1986)
<doi:10.1016/0270-0255(86)90088-6>), which is also exposed directly so
that counterfactual means or risks can be estimated under static, dynamic
or time-varying hypothetical interventions.

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
