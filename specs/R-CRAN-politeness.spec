%global packname  politeness
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          2%{?dist}
Summary:          Detecting Politeness Features in Text

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-spacyr 
BuildRequires:    R-CRAN-textir 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-textclean 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-ggplot2 
Requires:         R-parallel 
Requires:         R-CRAN-spacyr 
Requires:         R-CRAN-textir 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-textclean 

%description
Detecting markers of politeness in English natural language. This package
allows researchers to easily visualize and quantify politeness between
groups of documents. This package combines prior research on the
linguistic markers of politeness (Brown & Levinson, 1987
<http://psycnet.apa.org/record/1987-97641-000>; Danescu-Niculescu-Mizil et
al., 2013 <arXiv:1306.6078>; Voigt et al., 2017
<doi:10.1073/pnas.1702413114>). We thank the Spencer Foundation, the
Hewlett Foundation, and Harvard's Institute for Quantitative Social
Science for support.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
