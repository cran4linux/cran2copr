%global packname  splithalfr
%global packver   1.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          2%{?dist}
Summary:          Extensible Bootstrapped Split-Half Reliabilities

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-rlang >= 0.3.4
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-rlang >= 0.3.4

%description
Calculates scores and estimates bootstrapped split-half reliabilities for
reaction time tasks and questionnaires. The 'splithalfr' can be extended
with custom scoring algorithms for user-provided datasets. For more
information, see Parsons, Kruijt, & Fox (2018)
<doi:10.31234/osf.io/6ka9z>.

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
