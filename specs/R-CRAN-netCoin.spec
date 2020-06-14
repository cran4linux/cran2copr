%global packname  netCoin
%global packver   1.1.25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.25
Release:          2%{?dist}
Summary:          Interactive Analytic Networks

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-Matrix >= 1.2.4
BuildRequires:    R-CRAN-haven >= 1.1.0
BuildRequires:    R-CRAN-igraph >= 1.0.1
Requires:         R-Matrix >= 1.2.4
Requires:         R-CRAN-haven >= 1.1.0
Requires:         R-CRAN-igraph >= 1.0.1

%description
Create interactive analytic networks. It joins the data analysis power of
R to obtain coincidences, co-occurrences and correlations, and the
visualization libraries of 'JavaScript' in one package. The methods are
described in Escobar and Martinez-Uribe (2020)
<doi:10.18637/jss.v093.i11>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
