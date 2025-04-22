%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sicure
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Single-Index Mixture Cure Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-npcure 
BuildRequires:    R-CRAN-StatMatch 
BuildRequires:    R-stats 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-npcure 
Requires:         R-CRAN-StatMatch 
Requires:         R-stats 

%description
Single-index mixture cure models allow estimating the probability of cure
and the latency depending on a vector (or functional) covariate, avoiding
the curse of dimensionality. The vector of parameters that defines the
model can be estimated by maximum likelihood. A nonparametric estimator
for the conditional density of the susceptible population is provided. For
more details, see Piñeiro-Lamas (2024)
(<https://ruc.udc.es/dspace/handle/2183/37035>). Funding: This work,
integrated into the framework of PERTE for Vanguard Health, has been
co-financed by the Spanish Ministry of Science, Innovation and
Universities with funds from the European Union NextGenerationEU, from the
Recovery, Transformation and Resilience Plan (PRTR-C17.I1) and from the
Autonomous Community of Galicia within the framework of the Biotechnology
Plan Applied to Health.

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
