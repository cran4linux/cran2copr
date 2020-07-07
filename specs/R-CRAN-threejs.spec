%global packname  threejs
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          3%{?dist}
Summary:          Interactive 3D Scatter Plots, Networks and Globes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 1.0.0
BuildRequires:    R-CRAN-htmlwidgets >= 0.3.2
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-crosstalk 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-igraph >= 1.0.0
Requires:         R-CRAN-htmlwidgets >= 0.3.2
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-crosstalk 
Requires:         R-methods 
Requires:         R-stats 

%description
Create interactive 3D scatter plots, network plots, and globes using the
'three.js' visualization library (<https://threejs.org>).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/INDEX
