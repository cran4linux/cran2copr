%global packname  RPS
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Resistant Procrustes Superimposition

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-geomorph 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-Gmedian 
Requires:         R-CRAN-geomorph 
Requires:         R-MASS 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-Gmedian 

%description
Based on RPS tools, a rather complete resistant shape analysis of 2D and
3D datasets based on landmarks can be performed. In addition,
landmark-based resistant shape analysis of individual asymmetry in 2D for
matching or object symmetric structures is also possible.

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
%{rlibdir}/%{packname}/INDEX
