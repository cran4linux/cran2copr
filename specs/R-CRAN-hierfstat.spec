%global packname  hierfstat
%global packver   0.04-22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.04.22
Release:          3%{?dist}
Summary:          Estimation and Tests of Hierarchical F-Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-adegenet 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-adegenet 

%description
Allows the estimation of hierarchical F-statistics from haploid or diploid
genetic data with any numbers of levels in the hierarchy, following the
algorithm of Yang (Evolution, 1998, 52(4):950-956; <DOI:10.2307/2411227>.
Functions are also given to test via randomisations the significance of
each F and variance components, using the likelihood-ratio statistics G.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
