%global packname  solitude
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          An Implementation of Isolation Forest

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.0
BuildRequires:    R-CRAN-igraph >= 1.2.2
BuildRequires:    R-CRAN-data.table >= 1.11.4
BuildRequires:    R-CRAN-future.apply >= 0.2.0
BuildRequires:    R-CRAN-ranger >= 0.10.0
Requires:         R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-igraph >= 1.2.2
Requires:         R-CRAN-data.table >= 1.11.4
Requires:         R-CRAN-future.apply >= 0.2.0
Requires:         R-CRAN-ranger >= 0.10.0

%description
Isolation forest is anomaly detection method introduced by the paper
Isolation based Anomaly Detection (Liu, Ting and Zhou
<doi:10.1145/2133360.2133363>).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
