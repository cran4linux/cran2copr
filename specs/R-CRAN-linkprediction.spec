%global packname  linkprediction
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Link Prediction Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-intergraph 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-intergraph 

%description
Implementations of most of the existing proximity-based methods of link
prediction in graphs. Among the 20 implemented methods are e.g.: Adamic L.
and Adar E. (2003) <doi:10.1016/S0378-8733(03)00009-1>, Leicht E., Holme
P., Newman M. (2006) <doi:10.1103/PhysRevE.73.026120>, Zhou T. and Zhang Y
(2009) <doi:10.1140/epjb/e2009-00335-8>, and Fouss F., Pirotte A., Renders
J., and Saerens M. (2007) <doi:10.1109/TKDE.2007.46>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
