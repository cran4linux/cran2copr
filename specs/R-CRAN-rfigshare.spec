%global packname  rfigshare
%global packver   0.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          3%{?dist}
Summary:          An R Interface to 'figshare'

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 0.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-httr >= 0.3
Requires:         R-methods 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-XML 

%description
An interface to 'figshare' (http://figshare.com), a scientific repository
to archive and assign 'DOIs' to data, software, figures, and more.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
