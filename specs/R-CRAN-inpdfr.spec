%global packname  inpdfr
%global packver   0.1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.11
Release:          1%{?dist}
Summary:          Analyse Text Documents Using Ecological Tools

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         xpdf
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.1.3
BuildRequires:    R-CRAN-wordcloud >= 2.5
BuildRequires:    R-CRAN-R.devices >= 2.14.0
BuildRequires:    R-cluster >= 2.0.1
BuildRequires:    R-CRAN-metacom >= 1.4.4
BuildRequires:    R-CRAN-entropart >= 1.4.1
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-stringi >= 1.0.1
BuildRequires:    R-CRAN-tm >= 0.6.2
BuildRequires:    R-CRAN-ca >= 0.58
BuildRequires:    R-CRAN-SnowballC >= 0.5.1
Requires:         R-parallel >= 3.1.3
Requires:         R-CRAN-wordcloud >= 2.5
Requires:         R-CRAN-R.devices >= 2.14.0
Requires:         R-cluster >= 2.0.1
Requires:         R-CRAN-metacom >= 1.4.4
Requires:         R-CRAN-entropart >= 1.4.1
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-stringi >= 1.0.1
Requires:         R-CRAN-tm >= 0.6.2
Requires:         R-CRAN-ca >= 0.58
Requires:         R-CRAN-SnowballC >= 0.5.1

%description
A set of functions to analyse and compare texts, using classical text
mining functions, as well as those from theoretical ecology.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
