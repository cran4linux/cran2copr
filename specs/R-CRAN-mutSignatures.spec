%global packname  mutSignatures
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Decipher Mutational Signatures from Somatic Mutational Catalogs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-methods 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-proxy 
Requires:         R-methods 

%description
Cancer cells accumulate DNA mutations as result of DNA damage and DNA
repair processes. This computational framework is aimed at deciphering DNA
mutational signatures operating in cancer. The framework includes modules
that support raw data import and processing, mutational signature
extraction, and results interpretation and visualization. The framework
accepts widely used file formats storing information about DNA variants,
such as Variant Call Format files. The framework performs Non-Negative
Matrix Factorization to extract mutational signatures explaining the
observed set of DNA mutations. Bootstrapping is performed as part of the
analysis. The framework supports parallelization and is optimized for use
on multi-core systems. The software was described by Fantini D et al
(2020) <doi:10.1038/s41598-020-75062-0> and is based on a custom R-based
implementation of the original MATLAB WTSI framework by Alexandrov LB et
al (2013) <doi:10.1016/j.celrep.2012.12.008>.

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
