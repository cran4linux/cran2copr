%global packname  JointNets
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}
Summary:          End-to-End Sparse Gaussian Graphical Model Simulation,Estimation, Visualization, Evaluation and Application

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.4
Requires:         R-core >= 3.4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-JGL 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-brainR 
BuildRequires:    R-CRAN-misc3d 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-methods 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-CRAN-JGL 
Requires:         R-MASS 
Requires:         R-CRAN-brainR 
Requires:         R-CRAN-misc3d 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rgl 
Requires:         R-methods 

%description
An end-to-end package for learning multiple sparse Gaussian graphical
models and nonparanormal models from Heterogeneous Data with Additional
Knowledge. It is able to simulate multiple related graphs as well as
produce samples drawn from them. Multiple state-of-the-art sparse Gaussian
graphical model estimators are included to both multiple and difference
estimation. Graph visualization is available in 2D as well as 3D, designed
specifically for brain. Moreover, a set of evaluation metrics are
integrated for easy exploration with model validity. Finally,
classification using graphical model is achieved with Quadratic
Discriminant Analysis. The package comes with multiple demos with datasets
from various fields. Methods references: SIMULE (Wang B et al. (2017)
<doi:10.1007/s10994-017-5635-7>), WSIMULE (Singh C et al. (2017)
<arXiv:1709.04090v2>), DIFFEE (Wang B et al. (2018) <arXiv:1710.11223>),
JEEK (Wang B et al. (2018) <arXiv:1806.00548>), JGL(Danaher P et al.
(2012) <arXiv:1111.0324>) and kdiffnet (Sekhon A et al, preprint for
publication).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
