%global packname  SimSeq
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Nonparametric Simulation of RNA-Seq Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fdrtool 
Requires:         R-CRAN-fdrtool 

%description
RNA sequencing analysis methods are often derived by relying on
hypothetical parametric models for read counts that are not likely to be
precisely satisfied in practice. Methods are often tested by analyzing
data that have been simulated according to the assumed model. This testing
strategy can result in an overly optimistic view of the performance of an
RNA-seq analysis method. We develop a data-based simulation algorithm for
RNA-seq data. The vector of read counts simulated for a given experimental
unit has a joint distribution that closely matches the distribution of a
source RNA-seq dataset provided by the user. Users control the proportion
of genes simulated to be differentially expressed (DE) and can provide a
vector of weights to control the distribution of effect sizes. The
algorithm requires a matrix of RNA-seq read counts with large sample sizes
in at least two treatment groups. Many datasets are available that fit
this standard.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
