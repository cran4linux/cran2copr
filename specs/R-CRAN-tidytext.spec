%global packname  tidytext
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          3%{?dist}
Summary:          Text Mining using 'dplyr', 'ggplot2', and Other Tidy Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr >= 0.1.1
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-hunspell 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-tokenizers 
BuildRequires:    R-CRAN-janeaustenr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stopwords 
Requires:         R-CRAN-purrr >= 0.1.1
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-hunspell 
Requires:         R-CRAN-generics 
Requires:         R-Matrix 
Requires:         R-CRAN-tokenizers 
Requires:         R-CRAN-janeaustenr 
Requires:         R-methods 
Requires:         R-CRAN-stopwords 

%description
Text mining for word processing and sentiment analysis using 'dplyr',
'ggplot2', and other tidy tools.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
