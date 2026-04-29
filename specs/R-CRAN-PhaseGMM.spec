%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PhaseGMM
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Phase-Function Based Estimation and Inference for Linear Errors-in-Variables (EIV) Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-nleqslv 
Requires:         R-CRAN-nleqslv 

%description
Estimation and inference for coefficients of linear EIV models with
symmetric measurement errors. The measurement errors can be homoscedastic
or heteroscedastic, for the latter, replication for at least some
observations needs to be available. The estimation method and asymptotic
inference are based on a generalised method of moments framework, where
the estimating equations are formed from (1) minimising the distance
between the empirical phase function (normalised characteristic function)
of the response and that of the linear combination of all the covariates
at the estimates, and (2) minimising a corrected least-square discrepancy
function. Specifically, for a linear EIV model with p error-prone and q
error-free covariates, if replicates are available, the GMM approach is
based on a 2(p+q) estimating equations if some replicates are available
and based on p+2q estimating equations if no replicate is available. The
details of the method are described in Nghiem and Potgieter (2020)
<doi:10.1093/biomet/asaa025> and Nghiem and Potgieter (2025)
<doi:10.5705/ss.202022.0331>.

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
