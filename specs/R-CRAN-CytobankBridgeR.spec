%global __brp_check_rpaths %{nil}
%global packname  CytobankBridgeR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Bridging and Extending the CytobankAPI Package in R to theCytobank Web Application

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CytobankAPI >= 1.0.0
BuildRequires:    R-stats 
Requires:         R-CRAN-CytobankAPI >= 1.0.0
Requires:         R-stats 

%description
A collection of tools that leverage the CytobankAPI R package
<https://cran.r-project.org/web/packages/CytobankAPI/vignettes/cytobank-quickstart.html>
to complete more complex workflows, and add/extend various Cytobank
features.

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
%doc %{rlibdir}/%{packname}/cluster_gates_templates
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
