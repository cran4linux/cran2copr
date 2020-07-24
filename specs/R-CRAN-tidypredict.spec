%global packname  tidypredict
%global packver   0.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          1%{?dist}
Summary:          Run Predictions Inside the Database

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-tibble 

%description
It parses a fitted 'R' model object, and returns a formula in 'Tidy Eval'
code that calculates the predictions. It works with several databases
back-ends because it leverages 'dplyr' and 'dbplyr' for the final 'SQL'
translation of the algorithm. It currently supports lm(), glm(),
randomForest(), ranger(), earth(), xgb.Booster.complete(), cubist(), and
ctree() models.

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
