%global packname  RAEN
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Random Approximate Elastic Net (RAEN) Variable Selection Method

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-fastcmprsk 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-fastcmprsk 

%description
The Proportional Subdistribution Hazard (PSH) model has been popular for
estimating the effects of the covariates on the cause of interest in
Competing Risks analysis. The fast accumulation of large scale datasets
has posed a challenge to classical statistical methods. Current penalized
variable selection methods show unsatisfactory performance in ultra-high
dimensional data. We propose a novel method, the Random Approximate
Elastic Net (RAEN), with a robust and generalized solution to the variable
selection problem for the PSH model. Our method shows improved sensitivity
for variable selection compared with current methods.

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
