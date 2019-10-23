%global packname  sglasso
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}
Summary:          Lasso Method for RCON(V,E) Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
RCON(V, E) models are a kind of restriction of the Gaussian Graphical
Models defined by a set of equality constraints on the entries of the
concentration matrix. 'sglasso' package implements the structured
graphical lasso (sglasso) estimator proposed in Abbruzzo et al. (2014) for
the weighted l1-penalized RCON(V, E) model. Two cyclic coordinate
algorithms are implemented to compute the sglasso estimator, i.e. a cyclic
coordinate minimization (CCM) and a cyclic coordinate descent (CCD)
algorithm.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
