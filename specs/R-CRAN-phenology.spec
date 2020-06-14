%global packname  phenology
%global packver   7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.3
Release:          2%{?dist}
Summary:          Tools to Manage a Parametric Function that Describes Phenology

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-HelpersMG >= 3.2
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-lmf 
Requires:         R-CRAN-HelpersMG >= 3.2
Requires:         R-CRAN-numDeriv 
Requires:         R-parallel 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-lmf 

%description
Functions used to fit and test the phenology of species based on counts.

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
