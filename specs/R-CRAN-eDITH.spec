%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eDITH
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Model Transport of Environmental DNA in River Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-OCNet >= 1.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-rivnet >= 0.3.1
BuildRequires:    R-CRAN-BayesianTools 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-DHARMa 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-OCNet >= 1.1.0
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-rivnet >= 0.3.1
Requires:         R-CRAN-BayesianTools 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-DHARMa 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-fields 

%description
Runs the eDITH (environmental DNA Integrating Transport and Hydrology)
model, which implements a mass balance of environmental DNA (eDNA)
transport at a river network scale coupled with a species distribution
model to obtain maps of species distribution. eDITH can work with both
eDNA concentration (e.g., obtained via quantitative polymerase chain
reaction) or metabarcoding (read count) data. Parameter estimation can be
performed via Bayesian techniques (via the 'BayesianTools' package) or
optimization algorithms. An interface to the 'DHARMa' package for
posterior predictive checks is provided. See Carraro et al. (2018)
<doi:10.1073/pnas.1813843115> and Carraro et al. (2020)
<doi:10.1038/s41467-020-17337-8> for methodological details.

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
