%global __brp_check_rpaths %{nil}
%global packname  PhaseTypeR
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          General-Purpose Phase-Type Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-igraph 
Requires:         R-methods 

%description
General implementation of core function from phase-type theory.
'PhaseTypeR' can be used to model continuous and discrete phase-type
distributions, both univariate and multivariate. The package includes
functions for outputting the mean and (co)variance of phase-type
distributions; their density, probability and quantile functions;
functions for random draws; functions for reward-transformation; and
functions for plotting the distributions as networks. For more information
on these functions please refer to Bladt and Nielsen (2017, ISBN:
978-1-4939-8377-3) and Campillo Navarro (2019)
<https://orbit.dtu.dk/en/publications/order-statistics-and-multivariate-discrete-phase-type-distributio>.

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
