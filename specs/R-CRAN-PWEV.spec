%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PWEV
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          PSO Based Weighted Ensemble Algorithm for Volatility Modelling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-rumidas 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-CRAN-WeightedEnsemble 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-zoo 
Requires:         R-stats 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-rumidas 
Requires:         R-CRAN-rugarch 
Requires:         R-CRAN-WeightedEnsemble 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-zoo 

%description
Price volatility refers to the degree of variation in series over a
certain period of time. This volatility is especially noticeable in
agricultural commodities, adding uncertainty for farmers, traders, and
others in the agricultural supply chain. Commonly and popularly used four
volatility models viz, GARCH, Glosten Jagannatan Runkle-GARCH (GJR-GARCH)
model, exponentially weighted moving average (EWMA) model and
Multiplicative Error Model (MEM) are selected and implemented. PWAVE,
weighted ensemble model based on particle swarm optimization (PSO) is
proposed to combine the forecast obtained from all the candidate models.
This package has been developed using algorithm of Paul et al.
<doi:10.1007/s40009-023-01218-x> and Yeasin and Paul (2024)
<doi:10.1007/s11227-023-05542-3>.

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
