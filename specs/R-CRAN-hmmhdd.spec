%global packname  hmmhdd
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Hidden Markov Models for High Dimensional Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gmfd 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-roahd 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-gmfd 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-roahd 

%description
Some algorithms for the study of Hidden Markov Models for two different
types of data. For the study of univariate and multivariate data in a
finite framework, we provide some methods based on the definition of a
Gaussian copula function to define the dependence between data (for
further details, see Martino A., Guatteri, G. and Paganoni A. M. (2018)
<https://mox.polimi.it/publication-results/?id=776&tipo=add_qmox>). For
the study of functional data, we define an objective function based on
distances between random curves to define the emission functions of the
HMM (for further details, see Martino A., Guatteri, G. and Paganoni A. M.
(2019) <https://mox.polimi.it/publication-results/?id=805&tipo=add_qmox>).

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
%{rlibdir}/%{packname}/INDEX
