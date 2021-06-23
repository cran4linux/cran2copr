%global __brp_check_rpaths %{nil}
%global packname  iCluster
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Integrative clustering of multiple genomic data types

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-parallel 
Requires:         R-lattice 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-gplots 
Requires:         R-parallel 

%description
Integrative clustering of multiple genomic data types using a joint latent
variable model.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
