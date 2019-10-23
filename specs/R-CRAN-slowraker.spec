%global packname  slowraker
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          A Slow Version of the Rapid Automatic Keyword Extraction (RAKE)Algorithm

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-CRAN-openNLP 
BuildRequires:    R-utils 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-NLP 
Requires:         R-CRAN-openNLP 
Requires:         R-utils 

%description
A mostly pure-R implementation of the RAKE algorithm (Rose, S., Engel, D.,
Cramer, N. and Cowley, W. (2010) <doi:10.1002/9780470689646.ch1>), which
can be used to extract keywords from documents without any training data.

%prep
%setup -q -c -n %{packname}


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
