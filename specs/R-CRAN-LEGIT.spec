%global __brp_check_rpaths %{nil}
%global packname  LEGIT
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Latent Environmental & Genetic InTeraction (LEGIT) Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-lme4 
Requires:         R-CRAN-formula.tools 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-snow 
Requires:         R-CRAN-doSNOW 
Requires:         R-utils 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-Hmisc 
Requires:         R-grDevices 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-lme4 

%description
Constructs genotype x environment interaction (GxE) models where G is a
weighted sum of genetic variants (genetic score) and E is a weighted sum
of environments (environmental score) using the alternating optimization
algorithm by Jolicoeur-Martineau et al. (2017) <arXiv:1703.08111>. This
approach has greatly enhanced predictive power over traditional GxE models
which include only a single genetic variant and a single environmental
exposure. Although this approach was originally made for GxE modelling, it
is flexible and does not require the use of genetic and environmental
variables. It can also handle more than 2 latent variables (rather than
just G and E) and 3-way interactions or more. The LEGIT model produces
highly interpretable results and is very parameter-efficient thus it can
even be used with small sample sizes (n < 250). Tools to determine the
type of interaction (vantage sensitivity, diathesis-stress or differential
susceptibility), with any number of genetic variants or environments, are
available <arXiv:1712.04058>. The software can now produce mixed-effects
LEGIT models through the lme4 package.

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
