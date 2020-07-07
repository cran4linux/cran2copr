%global packname  baguette
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}
Summary:          Efficient Model Functions for Bagging

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-parsnip >= 0.1.0
BuildRequires:    R-CRAN-hardhat 
BuildRequires:    R-CRAN-butcher 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-C50 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-dials 
Requires:         R-CRAN-parsnip >= 0.1.0
Requires:         R-CRAN-hardhat 
Requires:         R-CRAN-butcher 
Requires:         R-rpart 
Requires:         R-CRAN-C50 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-dials 

%description
Tree- and rule-based models can be bagged using this package and their
predictions equations are stored in an efficient format to reduce the
model objects size and speed.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
