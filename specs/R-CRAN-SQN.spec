%global packname  SQN
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          3%{?dist}
Summary:          subset quantile normalization

License:          LGPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust >= 3.2
BuildRequires:    R-CRAN-nor1mix >= 1.0.7
Requires:         R-CRAN-mclust >= 3.2
Requires:         R-CRAN-nor1mix >= 1.0.7

%description
Normalization based a subset of negative control probes as described in
'Subset quantile normalization using negative control features'. Wu Z,
Aryee MJ, J Comput Biol. 2010 Oct;17(10):1385-95 [PMID 20976876].

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
