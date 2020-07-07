%global packname  recipes
%global packver   0.1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.13
Release:          2%{?dist}
Summary:          Preprocessing Tools to Create Design Matrices

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-tidyselect >= 0.2.5
BuildRequires:    R-CRAN-purrr >= 0.2.3
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-gower 
BuildRequires:    R-CRAN-ipred 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-tidyselect >= 0.2.5
Requires:         R-CRAN-purrr >= 0.2.3
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-gower 
Requires:         R-CRAN-ipred 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-timeDate 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
An extensible framework to create and preprocess design matrices. Recipes
consist of one or more data manipulation and analysis "steps". Statistical
parameters for the steps can be estimated from an initial data set and
then applied to other data sets. The resulting design matrices can then be
used as inputs into statistical or machine learning models.

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

%files
%{rlibdir}/%{packname}
