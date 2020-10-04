%global packname  rbefdata
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          3%{?dist}%{?buildtag}
Summary:          BEFdata R package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-rtematres 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-rtematres 
Requires:         R-CRAN-RColorBrewer 

%description
Basic R package to access data structures offered by any BEFdata portal
instance.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/fixtures
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
