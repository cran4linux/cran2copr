%global packname  ddalpha
%global packver   1.3.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.11
Release:          2%{?dist}
Summary:          Depth-Based Classification and Calculation of Data Depth

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-MASS 
BuildRequires:    R-class 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-MASS 
Requires:         R-class 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-geometry 

%description
Contains procedures for depth-based supervised learning, which are
entirely non-parametric, in particular the DDalpha-procedure (Lange,
Mosler and Mozharovskyi, 2014 <doi:10.1007/s00362-012-0488-4>). The
training data sample is transformed by a statistical depth function to a
compact low-dimensional space, where the final classification is done. It
also offers an extension to functional data and routines for calculating
certain notions of statistical depth functions. 50 multivariate and 5
functional classification problems are included. (Pokotylo, Mozharovskyi
and Dyckerhoff, 2019 <doi:10.18637/jss.v091.i05>).

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
