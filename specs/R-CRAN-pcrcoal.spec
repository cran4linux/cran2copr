%global packname  pcrcoal
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Implementing the Coalescent Approach to PCR Simulation Developedby Weiss and Von Haeseler (NAR, 1997)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.11.1
Requires:         R-core >= 2.11.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 2.3
BuildRequires:    R-methods >= 2.11.1
BuildRequires:    R-CRAN-ggplot2 >= 0.8.8
BuildRequires:    R-CRAN-phylosim >= 0.12
Requires:         R-CRAN-ape >= 2.3
Requires:         R-methods >= 2.11.1
Requires:         R-CRAN-ggplot2 >= 0.8.8
Requires:         R-CRAN-phylosim >= 0.12

%description
Implementing the Coalescent Approach to PCR Simulation.

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
%{rlibdir}/%{packname}/INDEX
