%global __brp_check_rpaths %{nil}
%global packname  bnpsd
%global packver   1.3.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.13
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Genotypes from the BN-PSD Admixture Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-nnls 
Requires:         R-stats 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-nnls 

%description
The Pritchard-Stephens-Donnelly (PSD) admixture model has k intermediate
subpopulations from which n individuals draw their alleles dictated by
their individual-specific admixture proportions.  The BN-PSD model
additionally imposes the Balding-Nichols (BN) allele frequency model to
the intermediate populations, which therefore evolved independently from a
common ancestral population T with subpopulation-specific FST (Wright's
fixation index) parameters.  The BN-PSD model can be used to yield complex
population structures.  This simulation approach is now extended to
subpopulations related by a tree.  Method described in Ochoa and Storey
(2021) <doi:10.1371/journal.pgen.1009241>.

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
