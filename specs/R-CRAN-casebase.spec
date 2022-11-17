%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  casebase
%global packver   0.10.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.3
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Flexible Smooth-in-Time Hazards and Risk Functions via Logistic and Multinomial Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-VGAM 

%description
Fit flexible and fully parametric hazard regression models to survival
data with single event type or multiple competing causes via logistic and
multinomial regression. Our formulation allows for arbitrary functional
forms of time and its interactions with other predictors for
time-dependent hazards and hazard ratios. From the fitted hazard model, we
provide functions to readily calculate and plot cumulative incidence and
survival curves for a given covariate profile. This approach accommodates
any log-linear hazard function of prognostic time, treatment, and
covariates, and readily allows for non-proportionality. We also provide a
plot method for visualizing incidence density via population time plots.
Based on the case-base sampling approach of Hanley and Miettinen (2009)
<DOI:10.2202/1557-4679.1125>, Saarela and Arjas (2015)
<DOI:10.1111/sjos.12125>, and Saarela (2015)
<DOI:10.1007/s10985-015-9352-x>.

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
