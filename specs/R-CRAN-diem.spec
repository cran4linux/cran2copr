%global packname  diem
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Debris-Containing Droplet Identification using EM

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-Matrix 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-igraph 
Requires:         R-utils 
Requires:         R-stats 

%description
Identification of debris-containing droplets from a droplet-based single
cell/nucleus RNA-seq. 'diem' uses the expression profile of background RNA
droplets, followed by expectation maximization (EM), to assign candidates
as debris or nuclei. See Alvarez M, Rahmani E, et al (2019)
<doi:10.1101/786285> for details.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
