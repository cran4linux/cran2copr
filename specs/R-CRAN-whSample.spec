%global packname  whSample
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for Sampling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-tools 
Requires:         R-utils 

%description
Interactive tools for generating random samples. Users select an .xlsx or
.csv file with population data and are walked through selecting the sample
type (Simple Random Sample or Stratified), the number of backups desired,
and a "stratify_on" value (if desired). The sample size is determined
using a normal approximation to the hypergeometric distribution based on
Nicholson (1956) <doi:10.1214/aoms/1177728270>. An .xlsx file is created
with the sample and key metadata for reference. It is menu-driven and lets
users pick an output directory. See vignettes for a detailed walk-through.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
