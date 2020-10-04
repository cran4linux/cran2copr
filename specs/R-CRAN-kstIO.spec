%global packname  kstIO
%global packver   0.3-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Knowledge Space Theory Input/Output

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pks >= 0.4.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sets 
BuildRequires:    R-CRAN-relations 
BuildRequires:    R-CRAN-kstMatrix 
Requires:         R-CRAN-pks >= 0.4.0
Requires:         R-MASS 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sets 
Requires:         R-CRAN-relations 
Requires:         R-CRAN-kstMatrix 

%description
Knowledge space theory by Doignon and Falmagne (1999)
<doi:10.1007/978-3-642-58625-5> is a set- and order-theoretical framework
which proposes mathematical formalisms to operationalize knowledge
structures in a particular domain.  The 'kstIO' package provides basic
functionalities to read and write KST data from/to files to be used
together with the 'kst', 'kstMatrix', 'pks' or 'DAKS' packages.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
