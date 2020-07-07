%global packname  icesSAG
%global packver   1.3-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.6
Release:          3%{?dist}
Summary:          Stock Assessment Graphs Database Web Services

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-icesVocab 
Requires:         R-CRAN-png 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-icesVocab 

%description
R interface to access the web services of the ICES Stock Assessment Graphs
database <http://sg.ices.dk>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
