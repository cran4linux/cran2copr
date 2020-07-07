%global packname  d3Network
%global packver   0.5.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2.1
Release:          3%{?dist}
Summary:          Tools for creating D3 JavaScript network, tree, dendrogram, andSankey graphs from R

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-whisker 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-whisker 

%description
This packages is intended to make it easy to create D3 JavaScript network,
tree, dendrogram, and Sankey graphs from R using data frames. !!! NOTE:
Active development has moved to the networkD3 package. !!!

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
