%global __brp_check_rpaths %{nil}
%global packname  orthoDr
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          3%{?dist}%{?buildtag}
Summary:          Semi-Parametric Dimension Reduction Models Using OrthogonalityConstrained Optimization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-dr 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-survival 
Requires:         R-CRAN-dr 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-rgl 
Requires:         R-MASS 

%description
Utilize an orthogonality constrained optimization algorithm of Wen & Yin
(2013) <DOI:10.1007/s10107-012-0584-1> to solve a variety of dimension
reduction problems in the semiparametric framework, such as Ma & Zhu
(2012) <DOI:10.1080/01621459.2011.646925>, Ma & Zhu (2013)
<DOI:10.1214/12-AOS1072>, Sun, Zhu, Wang & Zeng (2017) <arXiv:1704.05046>
and Zhou & Zhu (2018+) <arXiv:1802.06156>. It also serves as a general
purpose optimization solver for problems with orthogonality constraints.
Parallel computing for approximating the gradient is enabled through
`OpenMP'.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
