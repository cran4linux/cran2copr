%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mintyr
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          High-Performance Phenotypic Data Pipelines for Breeding

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-data.table 
Requires:         R-parallel 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rsample 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-writexl 

%description
A streamlined toolkit specifically designed for genomic selection and
quantitative genetics in animal breeding. It provides high-performance
data manipulation backed by 'data.table', focusing on multi-breed and
multi-trait nested grouping operations. Features include zero-copy data
importing, automated cross-validation splitting, and robust tools to
generate and batch-export formatted phenotypic files required by various
breeding software (e.g., 'ASReml-R', 'HIBLUP', 'DMU'), heavily optimizing
iterative variance component analysis and large-scale evaluation
pipelines.

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
