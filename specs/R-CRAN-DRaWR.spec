%global packname  DRaWR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Discriminative Random Walk with Restart

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-ROCR 
Requires:         R-Matrix 
Requires:         R-CRAN-ROCR 

%description
We present DRaWR, a network-based method for ranking genes or properties
related to a given gene set. Such related genes or properties are
identified from among the nodes of a large, heterogeneous network of
biological information. Our method involves a random walk with restarts,
performed on an initial network with multiple node and edge types,
preserving more of the original, specific property information than
current methods that operate on homogeneous networks. In this first stage
of our algorithm, we find the properties that are the most relevant to the
given gene set and extract a subnetwork of the original network,
comprising only the relevant properties. We then rerank genes by their
similarity to the given gene set, based on a second random walk with
restarts, performed on the above subnetwork.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
