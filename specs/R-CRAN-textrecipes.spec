%global packname  textrecipes
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Extra 'Recipes' for Text Processing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-recipes >= 0.1.4
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tokenizers 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-stopwords 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-modeldata 
Requires:         R-CRAN-recipes >= 0.1.4
Requires:         R-CRAN-dials 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tokenizers 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-stopwords 
Requires:         R-CRAN-magrittr 
Requires:         R-Matrix 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-modeldata 

%description
Converting text to numerical features requires specifically created
procedures, which are implemented as steps according to the 'recipes'
package. These steps allows for tokenization, filtering, counting (tf and
tfidf) and feature hashing.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
