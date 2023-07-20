%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  signatureSurvival
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Signature Survival Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forestplot 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forestplot 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-ggplot2 

%description
When multiple Cox proportional hazard models are performed on clinical
data (month or year and status) and a set of differential expressions of
genes, the results (Hazard risks, z-scores and p-values) can be used to
create gene-expression signatures. Weights are calculated using the
survival p-values of genes and are utilized to calculate expression values
of the signature across the selected genes in all patients in a cohort. A
Single or multiple univariate or multivariate Cox proportional hazard
survival analyses of the patients in one cohort can be performed by using
the gene-expression signature and visualized using our survival plots.

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
