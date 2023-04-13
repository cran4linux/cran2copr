%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crosshap
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Local Haplotype Clustering and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.00
Requires:         R-core >= 4.00
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-clustree 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggdist 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpp 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-clustree 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggdist 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpp 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
A local haplotyping visualization toolbox to capture major patterns of
co-inheritance between clusters of linked variants, whilst connecting
findings to phenotypic and demographic traits across individuals.
'crosshap' enables users to explore and understand genomic variation
across a trait-associated region. For an example of successful local
haplotype analysis, see Marsh et al. (2022)
<doi:10.1007/s00122-022-04045-8>.

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
