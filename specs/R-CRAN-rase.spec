%global packname  rase
%global packver   0.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Range Ancestral State Estimation for Phylogeography andComparative Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 3.1
BuildRequires:    R-CRAN-spatstat >= 1.36.0
BuildRequires:    R-CRAN-mvtnorm >= 1.0.0
BuildRequires:    R-CRAN-polyCub >= 0.5.0
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-ape >= 3.1
Requires:         R-CRAN-spatstat >= 1.36.0
Requires:         R-CRAN-mvtnorm >= 1.0.0
Requires:         R-CRAN-polyCub >= 0.5.0
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-sm 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Implements the Range Ancestral State Estimation for phylogeography
described in Quintero, I., Keil, P., Jetz, W., & Crawford, F. W. (2015)
<DOI:10.1093/sysbio/syv057>. It also includes Bayesian inference of
ancestral states under a Brownian Motion model of character evolution and
Maximum Likelihood estimation of rase for n-dimensional data. Visualizing
functions in 3D are implemented using the rgl package.

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
