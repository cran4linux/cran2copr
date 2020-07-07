%global packname  effectR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          Predicts Oomycete Effectors

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-seqinr >= 3.3.6
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-seqinr >= 3.3.6
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-reshape2 
Requires:         R-utils 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-viridis 

%description
Predicts cytoplasmic effector proteins using genomic data by searching for
motifs of interest using regular expression searches and hidden Markov
models (HMM) based in Haas et al. (2009) <doi:10.1038/nature08358>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
