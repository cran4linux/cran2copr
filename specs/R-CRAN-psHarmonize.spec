%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psHarmonize
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Creates a Harmonized Dataset Based on a Set of Instructions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 

%description
Functions which facilitate harmonization of data from multiple different
datasets. Data harmonization involves taking data sources with differing
values, creating coding instructions to create a harmonized set of values,
then making those data modifications. 'psHarmonize' will assist with data
modification once the harmonization instructions are written. Coding
instructions are written by the user to create a "harmonization sheet".
This sheet catalogs variable names, domains (e.g. clinical, behavioral,
outcomes), provides R code instructions for mapping or conversion of data,
specifies the variable name in the harmonized data set, and tracks notes.
The package will then harmonize the source datasets according to the
harmonization sheet to create a harmonized dataset. Once harmonization is
finished, the package also has functions that will create descriptive
statistics using 'RMarkdown'. Data Harmonization guidelines have been
described by Fortier I, Raina P, Van den Heuvel ER, et al. (2017)
<doi:10.1093/ije/dyw075>. Additional details of our R package have been
described by Stephen JJ, Carolan P, Krefman AE, et al. (2024)
<doi:10.1016/j.patter.2024.101003>.

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
