%global packname  fastnet
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}
Summary:          Large-Scale Social Network Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach >= 1.4.0
BuildRequires:    R-CRAN-igraph >= 1.2.0
BuildRequires:    R-CRAN-tidygraph >= 1.1.0
BuildRequires:    R-CRAN-doParallel >= 1.0.0
Requires:         R-CRAN-foreach >= 1.4.0
Requires:         R-CRAN-igraph >= 1.2.0
Requires:         R-CRAN-tidygraph >= 1.1.0
Requires:         R-CRAN-doParallel >= 1.0.0

%description
We present an implementation of the algorithms required to simulate
large-scale social networks and retrieve their most relevant metrics.

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
