%global packname  fragilityindex
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Fragility Index

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-stringr 
Requires:         R-base 
Requires:         R-stats 
Requires:         R-CRAN-pbapply 
Requires:         R-survival 
Requires:         R-CRAN-stringr 

%description
Implements and extends the fragility index calculation for dichotomous
results as described in Walsh, Srinathan, McAuley, Mrkobrada, Levine,
Ribic, Molnar, Dattani, Burke, Guyatt, Thabane, Walter, Pogue, and
Devereaux (2014) <DOI:10.1016/j.jclinepi.2013.10.019>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
