%global packname  simIReff
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Stochastic Simulation for Information Retrieval Evaluation:Effectiveness Scores

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-rvinecopulib >= 0.2.8.1.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-bde 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-extraDistr 
Requires:         R-CRAN-rvinecopulib >= 0.2.8.1.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-bde 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-np 
Requires:         R-CRAN-extraDistr 

%description
Provides tools for the stochastic simulation of effectiveness scores to
mitigate data-related limitations of Information Retrieval evaluation
research, as described in Urbano and Nagler (2018)
<doi:10.1145/3209978.3210043>. These tools include: fitting, selection and
plotting distributions to model system effectiveness, transformation
towards a prespecified expected value, proxy to fitting of copula models
based on these distributions, and simulation of new evaluation data from
these distributions and copula models.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
