%global packname  plink
%global packver   1.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          2%{?dist}
Summary:          IRT Separate Calibration Linking Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.3
Requires:         R-core >= 3.3.3
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-lattice 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-statmod 
Requires:         R-methods 
Requires:         R-lattice 
Requires:         R-MASS 
Requires:         R-CRAN-statmod 

%description
Item response theory based methods are used to compute linking constants
and conduct chain linking of unidimensional or multidimensional tests for
multiple groups under a common item design.  The unidimensional methods
include the Mean/Mean, Mean/Sigma, Haebara, and Stocking-Lord methods for
dichotomous (1PL, 2PL and 3PL) and/or polytomous (graded response, partial
credit/generalized partial credit, nominal, and multiple-choice model)
items.  The multidimensional methods include the least squares method and
extensions of the Haebara and Stocking-Lord method using single or
multiple dilation parameters for multidimensional extensions of all the
unidimensional dichotomous and polytomous item response models.  The
package also includes functions for importing item and/or ability
parameters from common IRT software, conducting IRT true score and
observed score equating, and plotting item response curves/surfaces,
vector plots, information plots, and comparison plots for examining
parameter drift.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
