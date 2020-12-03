%global packname  CPBayes
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Meta Analysis for Studying Cross-Phenotype Genetic Associations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-forestplot 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-forestplot 
Requires:         R-grDevices 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-mvtnorm 

%description
A Bayesian meta-analysis method for studying cross-phenotype genetic
associations. It uses summary-level data across multiple phenotypes to
simultaneously measure the evidence of aggregate-level pleiotropic
association and estimate an optimal subset of traits associated with the
risk locus. CPBayes is based on a spike and slab prior. The methodology is
available from: A Majumdar, T Haldar, S Bhattacharya, JS Witte (2018)
<doi:10.1371/journal.pgen.1007139>.

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
