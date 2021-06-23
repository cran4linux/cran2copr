%global __brp_check_rpaths %{nil}
%global packname  RxnSim
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Functions to Compute Chemical Reaction Similarity

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rcdk >= 3.4.3
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-fingerprint 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-rcdk >= 3.4.3
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-fingerprint 
Requires:         R-CRAN-data.table 

%description
Methods to compute chemical similarity between two or more reactions and
molecules. Allows masking of chemical substructures for weighted
similarity computations. Uses packages 'rCDK' and 'fingerprint' for
cheminformatics functionality.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/DB
%{rlibdir}/%{packname}/INDEX
