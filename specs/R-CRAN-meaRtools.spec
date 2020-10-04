%global packname  meaRtools
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Micro-Electro Array (MEA) Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-lattice 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-emdist 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-lattice 
Requires:         R-tcltk 
Requires:         R-CRAN-emdist 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-gtools 

%description
Core algorithms for MEA spike train analysis, feature extraction,
statistical analysis and plotting of multiple MEA recordings with multiple
genotypes and treatments, published by Gelfman et al (2017) at
<https://github.com/igm-team/meaRtools/>.

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
%doc %{rlibdir}/%{packname}/demas-test.R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/publications.md
%doc %{rlibdir}/%{packname}/sje1.R
%doc %{rlibdir}/%{packname}/wong-test.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
