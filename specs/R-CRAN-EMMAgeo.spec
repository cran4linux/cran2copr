%global packname  EMMAgeo
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          2%{?dist}
Summary:          End-Member Modelling of Grain-Size Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-matrixStats 

%description
End-member modelling analysis of grain-size data is an approach to unmix a
data set's underlying distributions and their contribution to the data
set. EMMAgeo provides deterministic and robust protocols for that purpose.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
