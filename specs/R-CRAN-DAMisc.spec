%global packname  DAMisc
%global packver   1.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          1%{?dist}
Summary:          Dave Armstrong's Miscellaneous Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-effects 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
BuildRequires:    R-nnet 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-optiscale 
BuildRequires:    R-CRAN-fANCOVA 
BuildRequires:    R-CRAN-AICcmodavg 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-clarkeTest 
Requires:         R-lattice 
Requires:         R-grid 
Requires:         R-CRAN-car 
Requires:         R-CRAN-effects 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-nnet 
Requires:         R-splines 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-VGAM 
Requires:         R-boot 
Requires:         R-CRAN-optiscale 
Requires:         R-CRAN-fANCOVA 
Requires:         R-CRAN-AICcmodavg 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-clarkeTest 

%description
Miscellaneous set of functions I use in my teaching either at the
University of Western Ontario or the Inter-university Consortium for
Political and Social Research (ICPSR) Summer Program in Quantitative
Methods.  Broadly, the functions help with presentation and interpretation
of LMs and GLMs, but also implement some new tools like Alternating Least
Squares Optimal Scaling for dependent variables, a Bayesian analog to the
ALSOS algorithm.  There are also tools to help understand interactions in
both LMs and binary GLMs.

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
%{rlibdir}/%{packname}/INDEX
