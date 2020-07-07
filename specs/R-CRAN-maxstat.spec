%global packname  maxstat
%global packver   0.7-25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.25
Release:          3%{?dist}
Summary:          Maximally Selected Rank Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.7.0
Requires:         R-core >= 1.7.0
BuildRequires:    R-CRAN-exactRankTests >= 0.8.23
BuildRequires:    R-CRAN-mvtnorm >= 0.5.10
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-exactRankTests >= 0.8.23
Requires:         R-CRAN-mvtnorm >= 0.5.10
Requires:         R-stats 
Requires:         R-graphics 

%description
Maximally selected rank statistics with several p-value approximations.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/results
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
