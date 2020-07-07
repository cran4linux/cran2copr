%global packname  smnet
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          3%{?dist}
Summary:          Smoothing for Stream Network Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-SSN 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-SSN 
Requires:         R-CRAN-spam 
Requires:         R-splines 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-DBI 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 

%description
Fits flexible additive models to data on stream networks, taking account
of flow-connectivity of the network.  Models are fitted using penalised
least squares.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
