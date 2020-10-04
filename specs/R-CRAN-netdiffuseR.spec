%global packname  netdiffuseR
%global packver   1.22.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.22.0
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Diffusion and Contagion Processes on Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-networkDynamic 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-CRAN-sna 
Requires:         R-CRAN-network 
Requires:         R-CRAN-networkDynamic 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-MatchIt 
Requires:         R-CRAN-SparseM 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-boot 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-viridisLite 

%description
Empirical statistical analysis, visualization and simulation of diffusion
and contagion processes on networks. The package implements algorithms for
calculating network diffusion statistics such as transmission rate, hazard
rates, exposure models, network threshold levels, infectiousness
(contagion), and susceptibility. The package is inspired by work published
in Valente, et al., (2015) <DOI:10.1016/j.socscimed.2015.10.001>; Valente
(1995) <ISBN: 9781881303213>, Myers (2000) <DOI:10.1086/303110>, Iyengar
and others (2011) <DOI:10.1287/mksc.1100.0566>, Burt (1987)
<DOI:10.1086/228667>; among others.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
