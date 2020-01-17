%global packname  spfrontier
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}
Summary:          Spatial Stochastic Frontier Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-ezsim 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-ezsim 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-numDeriv 

%description
A set of tools for estimation of various spatial specifications of
stochastic frontier models.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
