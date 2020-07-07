%global packname  RKEA
%global packver   0.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          3%{?dist}
Summary:          R/KEA Interface

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RKEAjars >= 5.0.1
BuildRequires:    R-CRAN-rJava >= 0.6.3
BuildRequires:    R-CRAN-tm 
Requires:         R-CRAN-RKEAjars >= 5.0.1
Requires:         R-CRAN-rJava >= 0.6.3
Requires:         R-CRAN-tm 

%description
An R interface to KEA (Version 5.0). KEA (for Keyphrase Extraction
Algorithm) allows for extracting keyphrases from text documents. It can be
either used for free indexing or for indexing with a controlled
vocabulary. For more information see <http://www.nzdl.org/Kea/>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
