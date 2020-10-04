%global packname  micEconAids
%global packver   0.6-18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.18
Release:          3%{?dist}%{?buildtag}
Summary:          Demand Analysis with the Almost Ideal Demand System (AIDS)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-systemfit >= 1.1.12
BuildRequires:    R-CRAN-micEcon >= 0.6.0
BuildRequires:    R-CRAN-miscTools >= 0.6.0
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-stats 
Requires:         R-CRAN-systemfit >= 1.1.12
Requires:         R-CRAN-micEcon >= 0.6.0
Requires:         R-CRAN-miscTools >= 0.6.0
Requires:         R-CRAN-lmtest 
Requires:         R-stats 

%description
Functions and tools for analysing consumer demand with the Almost Ideal
Demand System (AIDS) suggested by Deaton and Muellbauer (1980).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
