%global packname  rIP
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}
Summary:          Detects Fraud in Online Surveys by Tracing, Scoring, andVisualizing IP Addresses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-iptools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-amerika 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-utils 
Requires:         R-CRAN-iptools 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-amerika 
Requires:         R-CRAN-jsonlite 

%description
Takes an array of IPs and the keys for the services the user wishes to use
(IP Hub, IP Intel, and Proxycheck), and passes these to all respective
APIs. Returns a dataframe with the IP addresses (used for merging),
country, ISP, labels for non-US IP Addresses, VPS use, and recommendations
for blocking. The package also provides optional visualization tools for
checking the distributions. Additional functions are provided to call each
discrete API endpoint. The package and methods are detailed in the recent
paper Waggoner, Kennedy, and Clifford (2019) <doi:10.21105/joss.01285>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
