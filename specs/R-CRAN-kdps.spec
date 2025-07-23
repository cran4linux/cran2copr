%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kdps
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Kinship Decouple and Phenotype Selection (KDPS)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-tibble 

%description
A phenotype-aware algorithm for resolving cryptic relatedness in genetic
studies. It removes related individuals based on kinship or
identity-by-descent (IBD) scores while prioritizing subjects with
phenotypes of interest. This approach helps maximize the retention of
informative subjects, particularly for rare or valuable traits, and
improves statistical power in genetic and epidemiological studies. KDPS
supports both categorical and quantitative phenotypes, composite scoring,
and customizable pruning strategies using a fuzziness parameter. Benchmark
results show improved phenotype retention and high computational
efficiency on large-scale datasets like the UK Biobank. Methods used
include Manichaikul et al. (2010) <doi:10.1093/bioinformatics/btq559> for
kinship estimation, Purcell et al. (2007) <doi:10.1086/519795> for IBD
estimation, and Bycroft et al. (2018) <doi:10.1038/s41586-018-0579-z> for
UK Biobank data reference.

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
