%global __brp_check_rpaths %{nil}
%global packname  AquaBPsim
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Aquaculture Breeding Program Simulation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-matlib 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pedigree 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-stats 
Requires:         R-CRAN-matlib 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pedigree 
Requires:         R-CRAN-readxl 
Requires:         R-stats 

%description
Breeding programs can be simulated with this package. The functions are
written to simulate production and reproduction systems encountered in
aquaculture and are easy to combine with custom functions. Simulating
breeding programs is useful to predict the expected genetic gain, rate of
inbreeding and the effect of changes in the breeding program. AquaBPsim
does not simulate genome wide-markers and QTLs, but it simulates estimated
breeding values as values correlated to the true breeding values. The
correlation equals the accuracy, which can be provided or calculated using
deterministic formulas. For genomic selection, the accuracy can be
calculate using the formula of Deatwyler et al. (2010)
<doi:10.1534/genetics.110.116855>. Without genomic selection, accuracy can
be calculated with the selection index method (Mrode, 2014.
ISBN:978-1-84593-981-6).

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
