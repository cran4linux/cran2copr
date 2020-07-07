%global packname  CoClust
%global packver   0.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}
Summary:          Copula Based Cluster Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-gtools 
Requires:         R-methods 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-gtools 

%description
A copula based clustering algorithm that finds clusters according to the
complex multivariate dependence structure of the data generating process.
The updated version of the algorithm is described in Di Lascio, F.M.L. and
Giannerini, S. (2016). "Clustering dependent observations with copula
functions". Statistical Papers, p.1-17. <doi:10.1007/s00362-016-0822-3>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
