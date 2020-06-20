%global packname  doc2concrete
%global packver   0.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          1%{?dist}
Summary:          Measuring Concreteness in Natural Language

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-english 
BuildRequires:    R-CRAN-textstem 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-textclean 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-ggplot2 
Requires:         R-parallel 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-english 
Requires:         R-CRAN-textstem 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-textclean 

%description
Models for detecting concreteness in natural language. This package is
built in support of Yeomans (2020) <doi:10.17605/OSF.IO/DYZN6>, which
reviews linguistic models of concreteness in several domains. Here, we
provide an implementation of the best-performing domain-general model
(from Brysbaert et al., (2014) <doi:10.3758/s13428-013-0403-5>) as well as
two pre-trained models for the feedback and plan-making domains.

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
