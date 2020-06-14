%global packname  DeducerText
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Deducer GUI for Text Data

License:          LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-wordcloud >= 2.1
BuildRequires:    R-CRAN-Deducer >= 0.7.0
BuildRequires:    R-CRAN-tm >= 0.6
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-SnowballC 
Requires:         R-CRAN-wordcloud >= 2.1
Requires:         R-CRAN-Deducer >= 0.7.0
Requires:         R-CRAN-tm >= 0.6
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-SnowballC 

%description
A GUI for text mining

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
