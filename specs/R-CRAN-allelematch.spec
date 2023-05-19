%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  allelematch
%global packver   2.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Identifying Unique Multilocus Genotypes where Genotyping Error and Missing Data may be Present

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dynamicTreeCut 
Requires:         R-CRAN-dynamicTreeCut 

%description
Tools for the identification of unique of multilocus genotypes when both
genotyping error and missing data may be present; targeted for use with
large datasets and databases containing multiple samples of each
individual (a common situation in conservation genetics, particularly in
non-invasive wildlife sampling applications). Functions explicitly
incorporate missing data and can tolerate allele mismatches created by
genotyping error. If you use this package, please cite the original
publication in Molecular Ecology Resources (Galpern et al., 2012), the
details for which can be generated using citation('allelematch'). For a
complete vignette, please access via the Data S1 Supplementary
documentation and tutorials (PDF) located at
<doi:10.1111/j.1755-0998.2012.03137.x>.

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
