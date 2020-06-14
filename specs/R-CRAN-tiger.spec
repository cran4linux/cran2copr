%global packname  tiger
%global packver   0.2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3.1
Release:          2%{?dist}
Summary:          TIme series of Grouped ERrors

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-CRAN-qualV 
BuildRequires:    R-CRAN-klaR 
BuildRequires:    R-CRAN-som 
BuildRequires:    R-lattice 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-hexbin 
Requires:         R-CRAN-qualV 
Requires:         R-CRAN-klaR 
Requires:         R-CRAN-som 
Requires:         R-lattice 

%description
Temporally resolved groups of typical differences (errors) between two
time series are determined and visualized

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
