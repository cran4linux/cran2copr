%global packname  PCADSC
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          2%{?dist}
Summary:          Tools for Principal Component Analysis-Based Data StructureComparisons

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-reshape2 
Requires:         R-methods 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-ggplot2 
Requires:         R-Matrix 

%description
A suite of non-parametric, visual tools for assessing differences in data
structures for two datasets that contain different observations of the
same variables. These tools are all based on Principal Component Analysis
(PCA) and thus effectively address differences in the structures of the
covariance matrices of the two datasets. The PCASDC tools consist of
easy-to-use, intuitive plots that each focus on different aspects of the
PCA decompositions. The cumulative eigenvalue (CE) plot describes
differences in the variance components (eigenvalues) of the deconstructed
covariance matrices. The angle plot presents the information loss when
moving from the PCA decomposition of one dataset to the PCA decomposition
of the other. The chroma plot describes the loading patterns of the two
datasets, thereby presenting the relative weighting and importance of the
variables from the original dataset.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
