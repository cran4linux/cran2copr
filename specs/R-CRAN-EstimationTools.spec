%global __brp_check_rpaths %{nil}
%global packname  EstimationTools
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum Likelihood Estimation for Probability Functions from Data Sets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-autoimage 
BuildRequires:    R-graphics 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-Rdpack 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-autoimage 
Requires:         R-graphics 

%description
Routines for parameter estimation for any probability density or mass
function implemented in R via maximum likelihood (ML) given a data set.
The main routines 'maxlogL' and 'maxlogLreg' are wrapper functions
specifically developed for ML estimation. There are included optimization
procedures such as 'nlminb' and 'optim' from base package, and 'DEoptim'
Mullen (2011) <doi: 10.18637/jss.v040.i06>. Standard errors are estimated
with 'numDeriv' Gilbert (2011)
<https://CRAN.R-project.org/package=numDeriv> or the option 'Hessian =
TRUE' of 'optim' function.

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
