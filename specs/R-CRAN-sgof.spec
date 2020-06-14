%global packname  sgof
%global packver   2.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.2
Release:          2%{?dist}
Summary:          Multiple Hypothesis Testing

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-poibin 
Requires:         R-stats 
Requires:         R-CRAN-poibin 

%description
Seven different methods for multiple testing problems. The SGoF-type
methods (see for example, Carvajal Rodríguez et al., 2009
<doi:10.1186/1471-2105-10-209>; de Uña Álvarez, 2012
<doi:10.1515/1544-6115.1812>; Castro Conde et al., 2015
<doi:10.1177/0962280215597580>) and the BH and BY false discovery rate
controlling procedures.

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
%{rlibdir}/%{packname}/INDEX
