%global __brp_check_rpaths %{nil}
%global packname  PoA
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Finds the Price of Anarchy for Routing Games

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-nloptr 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-nloptr 

%description
Computes the optimal flow, Nash flow and the Price of Anarchy for any
routing game defined within the game theoretical framework. The input is a
routing game in the form of it’s cost and flow functions. Then transforms
this into an optimisation problem, allowing both Nash and Optimal flows to
be solved by nonlinear optimisation. See
<https://en.wikipedia.org/wiki/Congestion_game> and Knight and Harper
(2013) <doi:10.1016/j.ejor.2013.04.003> for more information.

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
