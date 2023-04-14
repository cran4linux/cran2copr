%global __brp_check_rpaths %{nil}
%global packname  nJira
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          SQL Like Query Interface for 'Jira'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-plyr 

%description
SQL like query interface to fetch data from any 'Jira' installation. The
data is fetched using 'Jira' REST API, which can be found at the following
URL: <https://developer.atlassian.com/cloud/jira/platform/rest/v2>.

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
%{rlibdir}/%{packname}
