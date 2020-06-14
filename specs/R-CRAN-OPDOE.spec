%global packname  OPDOE
%global packver   1.0-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          2%{?dist}
Summary:          Optimal Design of Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-orthopolynom 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-crossdes 
BuildRequires:    R-CRAN-polynom 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-orthopolynom 
Requires:         R-nlme 
Requires:         R-CRAN-crossdes 
Requires:         R-CRAN-polynom 

%description
Several function related to Experimental Design are implemented here, see
"Optimal Experimental Design with R" by Rasch D. et. al (ISBN
9781439816974).

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
