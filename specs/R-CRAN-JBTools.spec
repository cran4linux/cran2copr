%global packname  JBTools
%global packver   0.7.2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2.9
Release:          1%{?dist}
Summary:          Misc Small Tools and Helper Functions for Other Code of J.Buttlar

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-plotrix 

%description
Collection of several tools and helper functions used across the other
packages of J. Buttlar ('ncdf.tools' and 'spectral.methods').

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
