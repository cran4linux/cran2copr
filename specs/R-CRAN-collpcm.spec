%global packname  collpcm
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Collapsed Latent Position Cluster Model for Social Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-latentnet 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-network 
Requires:         R-CRAN-latentnet 

%description
Markov chain Monte Carlo based inference routines for collapsed latent
position cluster models or social networks, which includes searches over
the model space (number of clusters in the latent position cluster model).
The label switching algorithm used is that of Nobile and Fearnside (2007)
<doi:10.1007/s11222-006-9014-7> which relies on the algorithm of Carpaneto
and Toth (1980) <doi:10.1145/355873.355883>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
