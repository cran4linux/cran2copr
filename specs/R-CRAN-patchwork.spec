%global packname  patchwork
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          The Composer of Plots

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-gtable 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-graphics 

%description
The 'ggplot2' package provides a strong API for sequentially building up a
plot, but does not concern itself with composition of multiple plots.
'patchwork' is a package that expands the API to allow for arbitrarily
complex composition of plots by, among others, providing mathematical
operators for combining multiple plots. Other packages that try to address
this need (but with a different approach) are 'gridExtra' and 'cowplot'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
