%global __brp_check_rpaths %{nil}
%global packname  DoubleExpSeq
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Differential Exon Usage Test for RNA-Seq Data via EmpiricalBayes Shrinkage of the Dispersion Parameter

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-datasets 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-numDeriv 
Requires:         R-datasets 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Differential exon usage test for RNA-Seq data via an empirical Bayes
shrinkage method for the dispersion parameter the utilizes
inclusion-exclusion data to analyze the propensity to skip an exon across
groups. The input data consists of two matrices where each row represents
an exon and the columns represent the biological samples. The first matrix
is the count of the number of reads expressing the exon for each sample.
The second matrix is the count of the number of reads that either express
the exon or explicitly skip the exon across the samples, a.k.a. the total
count matrix. Dividing the two matrices yields proportions representing
the propensity to express the exon versus skipping the exon for each
sample.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
