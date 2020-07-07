%global packname  zyp
%global packver   0.10-1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.1.1
Release:          3%{?dist}
Summary:          Zhang + Yue-Pilon Trends Package

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Kendall 
Requires:         R-CRAN-Kendall 

%description
Contains an efficient implementation of Sen's slope method (Sen, 1968)
plus implementation of Xuebin Zhang's (Zhang, 1999) and Yue-Pilon's (Yue,
2002) prewhitening approaches to determining trends in climate data.

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
