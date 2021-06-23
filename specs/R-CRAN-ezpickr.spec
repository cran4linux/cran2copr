%global __brp_check_rpaths %{nil}
%global packname  ezpickr
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Data Import Using GUI File Picker

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-textreadr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-mboxr 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-textreadr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-mboxr 
Requires:         R-CRAN-vroom 
Requires:         R-CRAN-rmarkdown 
Requires:         R-utils 
Requires:         R-CRAN-tidyr 

%description
Choosing any rectangular data file using interactive GUI dialog box, and
seamlessly manipulating tidy data between an 'Excel' window and R session.

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
