%global packname  Ryacas0
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          3%{?dist}
Summary:          Legacy 'Ryacas' (Interface to 'Yacas' Computer Algebra System)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-settings 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-settings 
Requires:         R-CRAN-xml2 

%description
A legacy version of 'Ryacas', an interface to the 'yacas' computer algebra
system (<http://www.yacas.org/>).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/THANKS
%doc %{rlibdir}/%{packname}/WISHLIST
%doc %{rlibdir}/%{packname}/yacas
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
