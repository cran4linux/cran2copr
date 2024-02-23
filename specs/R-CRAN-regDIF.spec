%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  regDIF
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Regularized Differential Item Functioning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats > 3.0.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-stats > 3.0.0
Requires:         R-utils 
Requires:         R-CRAN-statmod 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 

%description
Performs regularization of differential item functioning (DIF) parameters
in item response theory (IRT) models (Belzak & Bauer, 2020)
<https://pubmed.ncbi.nlm.nih.gov/31916799/> using a penalized
expectation-maximization algorithm.

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
