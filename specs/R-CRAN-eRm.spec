%global packname  eRm
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Extended Rasch Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-splines 
BuildRequires:    R-Matrix 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-psych 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-splines 
Requires:         R-Matrix 
Requires:         R-lattice 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-psych 

%description
Fits Rasch models (RM), linear logistic test models (LLTM), rating scale
model (RSM), linear rating scale models (LRSM), partial credit models
(PCM), and linear partial credit models (LPCM).  Missing values are
allowed in the data matrix.  Additional features are the ML estimation of
the person parameters, Andersen's LR-test, item-specific Wald test,
Martin-Loef-Test, nonparametric Monte-Carlo Tests, itemfit and personfit
statistics including infit and outfit measures, ICC and other plots,
automated stepwise item elimination, simulation module for various binary
data matrices.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.pdf
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/NEWSRd2txt.R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
