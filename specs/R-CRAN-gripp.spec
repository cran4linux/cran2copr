%global packname  gripp
%global packver   0.2.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.20
Release:          1%{?dist}
Summary:          General Inverse Problem Platform

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-GA 
Requires:         R-utils 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-GA 

%description
Set of functions designed to solve inverse problems. The direct problem is
used to calculate a cost function to be minimized. Here are listed some
papers using Inverse Problems solvers and sensitivity analysis: (Jader
Lugon Jr.; Antonio J. Silva Neto 2011)
<doi:10.1590/S1678-58782011000400003>. (Jader Lugon Jr.; Antonio J. Silva
Neto; Pedro P.G.W. Rodrigues 2008) <doi:10.1080/17415970802082864>. (Jader
Lugon Jr.; Antonio J. Silva Neto; Cesar C. Santana 2008)
<doi:10.1080/17415970802082922>.

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
%doc %{rlibdir}/%{packname}/alvo.dat
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/f1.R
%{rlibdir}/%{packname}/INDEX
