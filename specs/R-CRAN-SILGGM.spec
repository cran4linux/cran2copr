%global __brp_check_rpaths %{nil}
%global packname  SILGGM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Inference of Large-Scale Gaussian Graphical Model inGene Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-glasso 
Requires:         R-MASS 
Requires:         R-CRAN-reshape 
Requires:         R-utils 

%description
Provides a general framework to perform statistical inference of each gene
pair and global inference of whole-scale gene pairs in gene networks using
the well known Gaussian graphical model (GGM) in a time-efficient manner.
We focus on the high-dimensional settings where p (the number of genes) is
allowed to be far larger than n (the number of subjects). Four main
approaches are supported in this package: (1) the bivariate nodewise
scaled Lasso (Ren et al (2015) <doi:10.1214/14-AOS1286>) (2) the
de-sparsified nodewise scaled Lasso (Jankova and van de Geer (2017)
<doi:10.1007/s11749-016-0503-5>) (3) the de-sparsified graphical Lasso
(Jankova and van de Geer (2015) <doi:10.1214/15-EJS1031>) (4) the GGM
estimation with false discovery rate control (FDR) using scaled Lasso or
Lasso (Liu (2013) <doi:10.1214/13-AOS1169>). Windows users should install
'Rtools' before the installation of this package.

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
