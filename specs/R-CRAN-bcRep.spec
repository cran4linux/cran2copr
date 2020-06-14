%global packname  bcRep
%global packver   1.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.6
Release:          2%{?dist}
Summary:          Advanced Analysis of B Cell Receptor Repertoire Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-ineq 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-CRAN-vegan 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-ineq 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-plotrix 

%description
Methods for advanced analysis of B cell receptor repertoire data, like
gene usage, mutations, clones, diversity, distance measures and
multidimensional scaling and their visualisation.

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
%doc %{rlibdir}/%{packname}/NEWS.pdf
%doc %{rlibdir}/%{packname}/NEWS.Rmd
%{rlibdir}/%{packname}/INDEX
