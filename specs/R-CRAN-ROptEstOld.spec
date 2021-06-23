%global __brp_check_rpaths %{nil}
%global packname  ROptEstOld
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Optimally Robust Estimation - Old Version

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-distr >= 2.8.0
BuildRequires:    R-CRAN-distrEx >= 2.8.0
BuildRequires:    R-CRAN-RandVar >= 1.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-evd 
Requires:         R-CRAN-distr >= 2.8.0
Requires:         R-CRAN-distrEx >= 2.8.0
Requires:         R-CRAN-RandVar >= 1.2.0
Requires:         R-methods 
Requires:         R-CRAN-evd 

%description
Optimally robust estimation using S4 classes and methods. Old version
still needed for current versions of ROptRegTS and RobRex.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/TOBEDONE
%{rlibdir}/%{packname}/INDEX
