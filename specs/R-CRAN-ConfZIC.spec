%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ConfZIC
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Confidence Envelopes for Model Selection Criteria Based on Minimum ZIC

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cmna 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ltsa 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidytable 
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-cmna 
Requires:         R-stats 
Requires:         R-CRAN-ltsa 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-mvtnorm 
Requires:         R-utils 
Requires:         R-CRAN-tidytable 
Requires:         R-CRAN-psych 

%description
Narrow down the number of models to look at in model selection using the
confidence envelopes based on the minimum ZIC (Generalized Information
Criteria) values for regression and time series data. Functions involve
the computation of multivariate normal-probabilities with covariance
matrices based on minimum ZIC inverting the CDF of the minimum ZIC. It
involves both the computation of singular and non-singular probabilities
as described in Genz (1992)
<[https:doi.org/10.2307/1390838]https:doi.org/10.2307/1390838>.

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
