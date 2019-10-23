%global packname  genvar
%global packver   0.0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.4
Release:          1%{?dist}
Summary:          An Imperative Library for Data Manipulation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.1.0
Requires:         R-core >= 3.5.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-readstata13 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-clubSandwich 
Requires:         R-CRAN-Formula 
Requires:         R-foreign 
Requires:         R-CRAN-readstata13 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-clubSandwich 

%description
Implements tools for manipulating data sets and performing regressions in
a way that is familiar to users of a popular, but proprietary, statistical
package commonly used in the social sciences. Loads a single dataset into
memory and implements a set of imperative commands to modify that data and
perform regressions and other analysis on the dataset. Offers an
alternative to standard R's function-based approach to data manipulation.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
