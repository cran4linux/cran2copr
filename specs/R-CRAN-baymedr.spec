%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  baymedr
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of Bayes Factors for Common Biomedical Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-rms 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survival 

%description
BAYesian inference for MEDical designs in R. Functions for the computation
of Bayes factors for common biomedical research designs. Implemented are
functions to test the equivalence (equiv_bf), non-inferiority (infer_bf),
and superiority (super_bf) of an experimental group compared to a control
group on a continuous outcome measure, as well as functions for simulating
survival data and calculating a Bayes factor for Cox proportional hazards
models. Bayes factors for these tests can be computed based on raw data or
summary statistics.

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
