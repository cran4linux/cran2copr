%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SIP
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Single-Iteration Permutation for Large-Scale Biobank Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 

%description
A single, phenome-wide permutation of large-scale biobank data. When a
large number of phenotypes are analyzed in parallel, a single permutation
across all phenotypes followed by genetic association analyses of the
permuted data enables estimation of false discovery rates (FDRs) across
the phenome. These FDR estimates provide a significance criterion for
interpreting genetic associations in a biobank context. For the basic
permutation of unrelated samples, this package takes a sample-by-variable
file with ID, genotypic covariates, phenotypic covariates, and phenotypes
as input. For data with related samples, it also takes a file with sample
pair-wise identity-by-descent information. The function outputs a permuted
sample-by-variable file ready for genome-wide association analysis. See
Annis et al. (2021) <doi:10.21203/rs.3.rs-873449/v1> for details.

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
