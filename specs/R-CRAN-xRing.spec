%global packname  xRing
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Visualization and Correction of X-Ray Micro-Density Profiles

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-dplR 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-tkRplotR 
Requires:         R-CRAN-dplR 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-tkRplotR 

%description
Contains functions to identify tree-ring borders based on X-ray
micro-density profiles and a Graphical User Interface to visualize density
profiles and correct tree-ring borders.

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
%doc %{rlibdir}/%{packname}/img
%{rlibdir}/%{packname}/INDEX
