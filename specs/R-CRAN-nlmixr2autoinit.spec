%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nlmixr2autoinit
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Generation of Initial Estimates for Population Pharmacokinetic Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nlmixr2data 
BuildRequires:    R-CRAN-nlmixr2 
BuildRequires:    R-CRAN-nlmixr2est 
BuildRequires:    R-CRAN-rxode2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-vpc 
Requires:         R-CRAN-nlmixr2data 
Requires:         R-CRAN-nlmixr2 
Requires:         R-CRAN-nlmixr2est 
Requires:         R-CRAN-rxode2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-vpc 

%description
Provides automated methods for generating initial parameter estimates in
population pharmacokinetic modeling. The pipeline integrates adaptive
single-point methods, naive pooled graphic approaches, noncompartmental
analysis methods, and parameter sweeping across pharmacokinetic models. It
estimates residual unexplained variability using either data-driven or
fixed-fraction approaches and assigns pragmatic initial values for
inter-individual variability. These strategies are designed to improve
model robustness and convergence in 'nlmixr2' workflows. For more details
see Huang Z, Fidler M, Lan M, Cheng IL, Kloprogge F, Standing JF (2025)
<doi:10.1007/s10928-025-10000-z>.

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
