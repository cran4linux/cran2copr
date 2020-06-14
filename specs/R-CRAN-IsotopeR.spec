%global packname  IsotopeR
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          2%{?dist}
Summary:          Stable Isotope Mixing Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fgui 
BuildRequires:    R-CRAN-runjags 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-CRAN-fgui 
Requires:         R-CRAN-runjags 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-plotrix 

%description
Estimates diet contributions from isotopic sources using JAGS. Includes
estimation of concentration dependence and measurement error.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
