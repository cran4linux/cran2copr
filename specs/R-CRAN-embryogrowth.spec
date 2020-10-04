%global packname  embryogrowth
%global packver   7.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.6
Release:          3%{?dist}%{?buildtag}
Summary:          Tools to Analyze the Thermal Reaction Norm of Embryo Growth

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-HelpersMG >= 3.6
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-parallel 
Requires:         R-CRAN-HelpersMG >= 3.6
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-numDeriv 
Requires:         R-parallel 

%description
Tools to analyze the embryo growth and the sexualisation thermal reaction
norms.

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
