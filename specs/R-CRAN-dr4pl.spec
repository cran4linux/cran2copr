%global __brp_check_rpaths %{nil}
%global packname  dr4pl
%global packver   1.1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.11
Release:          3%{?dist}%{?buildtag}
Summary:          Dose Response Data Analysis using the 4 Parameter Logistic (4pl)Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-tensor 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-ggplot2 
Requires:         R-Matrix 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-tensor 
Requires:         R-CRAN-Rdpack 

%description
Models the relationship between dose levels and responses in a
pharmacological experiment using the 4 Parameter Logistic model.
Traditional packages on dose-response modelling such as 'drc' and 'nplr'
often draw errors due to convergence failure especially when data have
outliers or non-logistic shapes. This package provides robust estimation
methods that are less affected by outliers and other initialization
methods that work well for data lacking logistic shapes. We provide the
bounds on the parameters of the 4PL model that prevent parameter estimates
from diverging or converging to zero and base their justification in a
statistical principle. These methods are used as remedies to convergence
failure problems.  Gadagkar, S. R. and Call, G. B. (2015)
<doi:10.1016/j.vascn.2014.08.006> Ritz, C. and Baty, F. and Streibig, J.
C. and Gerhard, D. (2015) <doi:10.1371/journal.pone.0146021>.

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
%doc %{rlibdir}/%{packname}/image
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
