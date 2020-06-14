%global packname  diffdepprop
%global packver   0.1-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          2%{?dist}
Summary:          Calculates Confidence Intervals for two Dependent Proportions

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gee 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-PropCIs 
Requires:         R-CRAN-gee 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-PropCIs 

%description
The package includes functions to calculate confidence intervals for the
difference of dependent proportions. There are two functions implemented
to edit the data (dichotomising with the help of cutpoints, counting
accordance and discordance of two tests or situations). For the
calculation of the confidence intervals entries of the fourfold table are
needed.

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
