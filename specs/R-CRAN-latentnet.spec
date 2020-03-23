%global packname  latentnet
%global packver   2.10.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.10.5
Release:          1%{?dist}
Summary:          Latent Position and Cluster Models for Statistical Networks

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildRequires:    R-CRAN-statnet.common >= 4.1.0
BuildRequires:    R-CRAN-ergm >= 3.9.0
BuildRequires:    R-CRAN-coda >= 0.17.1
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-tools 
BuildRequires:    R-MASS 
Requires:         R-CRAN-statnet.common >= 4.1.0
Requires:         R-CRAN-ergm >= 3.9.0
Requires:         R-CRAN-coda >= 0.17.1
Requires:         R-CRAN-network 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-abind 
Requires:         R-tools 
Requires:         R-MASS 

%description
Fit and simulate latent position and cluster models for statistical
networks. See Krivitsky and Handcock (2008) <10.18637/jss.v024.i05> and
Krivitsky, Handcock, Raftery, and Hoff (2009)
<10.1016/j.socnet.2009.04.001>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
