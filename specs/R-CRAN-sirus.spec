%global packname  sirus
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Stable and Interpretable RUle Set

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-Matrix 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 

%description
A regression and classification algorithm based on random forests, which
takes the form of a short list of rules. SIRUS combines the simplicity of
decision trees with the predictivity of random forests for problems with
low order interactions. The core aggregation principle of random forests
is kept, but instead of aggregating predictions, SIRUS selects the most
frequent nodes of the forest to form a stable rule ensemble model. The
algorithm is fully described in the following article: Benard C., Biau G.,
da Veiga S., Scornet E. (2019) <arXiv:1908.06852>. This R package is a
fork from the project ranger (<https://github.com/imbs-hl/ranger>).

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
