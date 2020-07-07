%global packname  PairwiseD
%global packver   0.9.62
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.62
Release:          3%{?dist}
Summary:          Pairing Up Units and Vectors in Panel Data Setting

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-utils 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-openxlsx 
Requires:         R-utils 

%description
Pairing observations according to a chosen formula and facilitates
bilateral analysis of the panel data. Paring is possible for observations,
as well as for vectors of observations ordered with respect to time.

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
