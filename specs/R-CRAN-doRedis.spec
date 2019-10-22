%global packname  doRedis
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Foreach parallel adapter for the rredis package

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5
Requires:         R-core >= 2.5
BuildRequires:    R-CRAN-rredis >= 1.6.8
BuildRequires:    R-CRAN-foreach >= 1.3.0
BuildRequires:    R-CRAN-iterators >= 1.0.0
BuildRequires:    R-utils 
Requires:         R-CRAN-rredis >= 1.6.8
Requires:         R-CRAN-foreach >= 1.3.0
Requires:         R-CRAN-iterators >= 1.0.0
Requires:         R-utils 

%description
A Redis parallel backend for the %dopar% function

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/ec2-redis-worker-installer.sh
%doc %{rlibdir}/%{packname}/redis-worker-installer.sh
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
