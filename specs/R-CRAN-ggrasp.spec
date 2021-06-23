%global __brp_check_rpaths %{nil}
%global packname  ggrasp
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Gaussian-Based Genome Representative Selector withPrioritization

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-bgmm 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mixtools 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-bgmm 
Requires:         R-CRAN-colorspace 
Requires:         R-methods 

%description
Given a group of genomes and their relationship with each other, the
package clusters the genomes and selects the most representative members
of each cluster. Additional data can be provided to the prioritize certain
genomes. The results can be printed out as a list or a new phylogeny with
graphs of the trees and distance distributions also available. For
detailed introduction see: Thomas H Clarke, Lauren M Brinkac, Granger
Sutton, and Derrick E Fouts (2018), GGRaSP: a R-package for selecting
representative genomes using Gaussian mixture models, Bioinformatics,
bty300, <doi:10.1093/bioinformatics/bty300>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
