%global packname  broom
%global packver   0.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.6
Release:          3%{?dist}
Summary:          Convert Statistical Analysis Objects into Tidy Tibbles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-generics >= 0.0.2
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-generics >= 0.0.2
Requires:         R-CRAN-backports 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-nlme 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 

%description
Summarizes key information about statistical objects in tidy tibbles. This
makes it easy to report results, create plots and consistently work with
large numbers of models at once. Broom provides three verbs that each
provide different types of information about a model. tidy() summarizes
information about model components such as coefficients of a regression.
glance() reports information about an entire model, such as goodness of
fit measures like AIC and BIC. augment() adds information about individual
observations to a dataset, such as fitted values or influence measures.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
