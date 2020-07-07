%global packname  expp
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          3%{?dist}
Summary:          Spatial Analysis of Extra-Pair Paternity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-CRAN-spatstat 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-deldir 
Requires:         R-CRAN-spatstat 

%description
Tools and data to accompany Schlicht, L., Valcu, M., & Kempenaers, B.
(2015) <doi:10.1111/1365-2656.12293>. Spatial patterns of extra-pair
paternity: beyond paternity gains and losses. Journal of Animal Ecology,
84(2), 518-531.

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
