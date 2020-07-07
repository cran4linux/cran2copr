%global packname  soilphysics
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          3%{?dist}
Summary:          Soil Physical Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-CRAN-rpanel 
BuildRequires:    R-MASS 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-boot 
BuildRequires:    R-grDevices 
BuildRequires:    R-datasets 
Requires:         R-CRAN-rpanel 
Requires:         R-MASS 
Requires:         R-tcltk 
Requires:         R-CRAN-tkrplot 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-boot 
Requires:         R-grDevices 
Requires:         R-datasets 

%description
Basic and model-based soil physical analyses.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
