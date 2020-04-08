%global packname  idefix
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}
Summary:          Efficient Designs for Discrete Choice Experiments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mlogit 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-dplyr 
Requires:         R-MASS 
Requires:         R-CRAN-mlogit 
Requires:         R-parallel 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-utils 

%description
Generates efficient designs for discrete choice experiments based on the
multinomial logit model, and individually adapted designs for the mixed
multinomial logit model. The generated designs can be presented on screen
and choice data can be gathered using a shiny application. Crabbe M, Akinc
D and Vandebroek M (2014) <doi:10.1016/j.trb.2013.11.008>.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
