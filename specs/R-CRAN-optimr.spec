%global packname  optimr
%global packver   2016-8.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2016.8.16
Release:          1%{?dist}
Summary:          A Replacement and Extension of the 'optim' Function

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-optextras 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-setRNG 
BuildRequires:    R-CRAN-Rvmmin 
BuildRequires:    R-CRAN-Rcgmin 
Requires:         R-CRAN-optextras 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-setRNG 
Requires:         R-CRAN-Rvmmin 
Requires:         R-CRAN-Rcgmin 

%description
Provides a test of replacement and extension of the optim() function to
unify and streamline optimization capabilities in R for smooth, possibly
box constrained functions of several or many parameters. This version has
a reduced set of methods and is intended to be on CRAN.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/developmentnotes
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
