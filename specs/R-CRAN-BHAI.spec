%global packname  BHAI
%global packver   0.99.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.2
Release:          3%{?dist}%{?buildtag}
Summary:          Estimate the Burden of Healthcare-Associated Infections

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-prevtoinc 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-prevtoinc 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-plotrix 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-methods 

%description
Provides an approach which is based on the methodology of the Burden of
Communicable Diseases in Europe (BCoDE) and can be used for large and
small samples such as individual countries. The Burden of
Healthcare-Associated Infections (BHAI) is estimated in
disability-adjusted life years, number of infections as well as number of
deaths per year. Results can be visualized with various plotting functions
and exported into tables.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
