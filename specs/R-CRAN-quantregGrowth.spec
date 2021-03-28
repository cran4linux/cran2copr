%global packname  quantregGrowth
%global packver   1.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Growth Charts via Smooth Regression Quantiles with Automatic Smoothness Estimation and Additive Terms

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-splines 
Requires:         R-CRAN-quantreg 
Requires:         R-splines 

%description
Fits non-crossing regression quantiles as a function of linear covariates
and multiple smooth terms via B-splines with L1-norm difference penalties.
The smoothing parameters are estimated as part of the model fitting.
Monotonicity and concavity constraints on the fitted curves are allowed.
See Muggeo, Sciandra, Tomasello and Calvo (2013)
<doi:10.1007/s10651-012-0232-1> and <doi:10.13140/RG.2.2.12924.85122> for
some code examples. Smoothing parameter selection with additive terms is
discussed in Muggeo and others (2020) <doi:10.1177/1471082X20929802>.

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
