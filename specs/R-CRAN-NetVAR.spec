%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NetVAR
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Network Structures in VAR Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-fGarch 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-fGarch 

%description
Vector AutoRegressive (VAR) type models with tailored regularisation
structures are provided to uncover network type structures in the data,
such as influential time series (influencers). Currently the package
implements the LISAR model from Zhang and Trimborn (2023)
<doi:10.2139/ssrn.4619531>. The package automatically derives the required
regularisation sequences and refines it during the estimation to provide
the optimal model. The package allows for model optimisation under various
loss functions such as Mean Squared Forecasting Error (MSFE), Akaike
Information Criterion (AIC), and Bayesian Information Criterion (BIC). It
provides a dedicated class, allowing for summary prints of the optimal
model and a plotting function to conveniently analyse the optimal model
via heatmaps.

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
