%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bidser
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Work with 'BIDS' (Brain Imaging Data Structure) Projects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-neuroim2 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rio 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-neuroim2 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rio 

%description
Tools for working with 'BIDS' (Brain Imaging Data Structure) formatted
neuroimaging datasets. The package provides functionality for reading and
querying 'BIDS'-compliant projects, creating mock 'BIDS' datasets for
testing, and extracting preprocessed data from 'fMRIPrep' derivatives. It
supports searching and filtering 'BIDS' files by various entities such as
subject, session, task, and run to streamline neuroimaging data workflows.
See Gorgolewski et al. (2016) <doi:10.1038/sdata.2016.44> for the 'BIDS'
specification.

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
