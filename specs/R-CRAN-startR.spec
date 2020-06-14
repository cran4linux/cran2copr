%global packname  startR
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}
Summary:          Automatically Retrieve Multidimensional Distributed Data Sets

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-parallel 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-future 
Requires:         R-parallel 

%description
Tool to automatically fetch, transform and arrange subsets of
multidimensional data sets (collections of files) stored in local and/or
remote file systems or servers, using multicore capabilities where
possible. The tool provides an interface to perceive a collection of data
sets as a single large multidimensional data array, and enables the user
to request for automatic retrieval, processing and arrangement of subsets
of the large array. Wrapper functions to add support for custom file
formats can be plugged in/out, making the tool suitable for any research
field where large multidimensional data sets are involved.

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
